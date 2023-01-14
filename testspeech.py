from speechkit import Session, SpeechSynthesis
import pyaudio

oauth_token = "y0_AgAAAABiCOIiAATuwQAAAADZXWDaEUtZKrmuTmWJprgtgu64L7GW_YE"
catalog_id = "b1glrooambngcj9rtk38"

session = Session.from_yandex_passport_oauth_token(oauth_token, catalog_id)
synthesizeAudio = SpeechSynthesis(session)

synthesizeAudio.synthesize(
    'out.mp3', text='Пошел нахуй! Ебло пасатижное!',
    voice='oksana', format='mp3', sampleRateHertz='16000'
)

# audio_data = synthesizeAudio.synthesize_stream(
# 		text='Пошел нахуй! Ебло пасатижное!',
#     voice='jane', emotion='neutral', format='lpcm', sampleRateHertz='16000'
# )

def pyaudio_play_audio_function(audio_data, num_channels=1, 
                                sample_rate=16000, chunk_size=4000) -> None:
    """
    Воспроизводит бинарный объект с аудио данными в формате lpcm (WAV)
    
    :param bytes audio_data: данные сгенерированные спичкитом
    :param integer num_channels: количество каналов, спичкит генерирует 
        моно дорожку, поэтому стоит оставить значение `1`
    :param integer sample_rate: частота дискретизации, такая же 
        какую вы указали в параметре sampleRateHertz
    :param integer chunk_size: размер семпла воспроизведения, 
        можно отрегулировать если появится потрескивание
    """
    p = pyaudio.PyAudio()
    stream = p.open(
        format=pyaudio.paInt16,
        channels=num_channels,
        rate=sample_rate,
        output=True,
        frames_per_buffer=chunk_size
    )

    try:
        for i in range(0, len(audio_data), chunk_size):
            stream.write(audio_data[i:i + chunk_size])
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

sample_rate = 16000 # частота дискретизации должна 
                    # совпадать при синтезе и воспроизведении
# audio_data = synthesizeAudio.synthesize_stream(
#     text='Привет мир, снова и снова!',
#     voice='oksana', format='lpcm', sampleRateHertz=sample_rate
# )
# Воспроизводим синтезированный файл
pyaudio_play_audio_function(audio_data, sample_rate=sample_rate)
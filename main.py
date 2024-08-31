import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from moviepy.editor import AudioFileClip
from moviepy.video.VideoClip import ImageClip

directory_images_path = Path('images')
images = sorted([file.name for file in directory_images_path.iterdir() if file.name.split('.')[0].strip().isdigit()], key=lambda i: int(i.split('.')[0]))

directory_audio_path = Path('audio')
audio = sorted([file.name for file in directory_audio_path.iterdir() if file.name.split('.')[0].strip().isdigit()], key=lambda i: int(i.split('.')[0]))


def create_video(i):
    audio_clip = AudioFileClip(f'audio/{audio[i]}')

    image_clip = ImageClip(f'images/{images[i]}', duration=audio_clip.duration)

    image_clip = image_clip.set_audio(audio_clip)

    filename = f"{''.join(images[i].split('.')[0])}_{''.join(audio[i].split('.')[0])}.mp4"
    image_clip.write_videofile(f'videos/{filename}', logger=None, fps=60)
    print(f"Створено відео: {filename}")


if __name__ == '__main__':
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=None) as executor:
        for i in range(min(len(images), len(audio))):
            executor.submit(create_video, i)

    print(f"Час виконання скрипта: {time.time() - start_time} секунд")

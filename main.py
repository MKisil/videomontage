from pathlib import Path
from moviepy.editor import AudioFileClip
from moviepy.video.VideoClip import ImageClip


def main():
    directory_images_path = Path('images')
    images = [file.name for file in directory_images_path.iterdir() if file.name != '.gitkeep']

    directory_audio_path = Path('audio')
    audio = [file.name for file in directory_audio_path.iterdir() if file.name != '.gitkeep']

    for i in range(min(len(images), len(audio))):
        audio_clip = AudioFileClip(f'audio/{audio[i]}')

        image_clip = ImageClip(f'images/{images[i]}', duration=audio_clip.duration)

        image_clip = image_clip.set_audio(audio_clip)

        image_clip.write_videofile(
            f'videos/{''.join(images[i].split('.')[:-1])}_{''.join(audio[i].split('.')[:-1])}.mp4', fps=70)


if __name__ == '__main__':
    main()

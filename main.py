import asyncio
import logging
import time
from asyncio import Task
from pathlib import Path
from typing import Final

from PIL import Image, ImageFilter

logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

START: Final[float] = time.perf_counter()

IMG_FILEPATH: Final[Path] = Path(
    r'D:\OneDrive\Taken Photos\Fujifilm X-T2\All at once\DSCF0346.JPG'
)


def ts() -> str:
    return f'{time.perf_counter() - START:6.3f}s'


def log(message: str) -> None:
    logger.info('%s | %s', ts(), message)


def process_image_sync(path: Path) -> None:
    """Heavy CPU-bound Pillow work."""
    log('Image processing started')

    with Image.open(path) as img:
        for i in range(3):
            log(f'Blur iteration {i + 1}')

            img = img.filter(ImageFilter.GaussianBlur(radius=8))
            img = img.resize((img.width // 2, img.height // 2))
            img = img.resize((img.width * 2, img.height * 2))

    log('Image processing finished')


async def ticker(name: str, count: int = 20, delay: float = 0.2) -> None:
    """Should tick every 200 ms if the event loop isn't blocked."""
    for i in range(count):
        await asyncio.sleep(delay)
        log(f'{name}: tick {i + 1}')

    log(f'{name}: finished')


async def main_threaded() -> None:
    log('=== Async version ===')

    tasks: list[Task] = [
        asyncio.create_task(ticker('A')),
        asyncio.create_task(ticker('B')),
        asyncio.create_task(asyncio.to_thread(process_image_sync, IMG_FILEPATH)),
        asyncio.create_task(asyncio.to_thread(process_image_sync, IMG_FILEPATH)),
    ]

    await asyncio.gather(*tasks)

    log('Async version finished')


def main() -> None:
    asyncio.run(main_threaded())


if __name__ == '__main__':
    main()

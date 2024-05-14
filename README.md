# signature-detection-verification-system

Проект Андрея Алибекова с кейс-чемпионата Газпромбанка май 2024.
Данная система предназначена для сверки подписи на документе с эталонной подписью для подтверждения авторства.
Система состоит из 3 моделей:
- Распознавание подписи на документе с помощью дообученной модели Yolov8
- Очистка картинки с подписью от лишних элементов таких как печатный текст и прямые линии. Для этого была дообучена модель cycleGAN
- Сравнение двух подписей на схожесть. Для этого была использована VGG16

Модели очистки и сравнения основаны на следующей [статье](https://arxiv.org/pdf/2004.12104)

## Распознавание подписи
[Yolov8](https://github.com/ultralytics/ultralytics) -- это SOTA модель для работы с изображениями в задачах классификации, распознавания, сегментации и слежения. Данная модель была дообучена на датасете [SingverOD](https://www.kaggle.com/datasets/victordibia/signverod) с 2700 размеченными документами с подписями.

## Очистка картинки с подписью
[cycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)

Артефакты, полученные при обучении модели на [wandb](https://api.wandb.ai/links/alibekovand_org/2a9cmgb6)

## Сравнение двух подписей
Для получения модели сравнения подписей использована техника transfer learning. Изначально VGG16 обучена как классификатор подписей по принадлежности одному из 50 человек из датасета. Полученный в такой нейросети предпоследний слой хранит в себе фичи(признаки). Данные вектора можно сравнить между собой, в системе для этого выбран косинус угла между этими векторами. Чем картинки более схожи, тем ближе к 1 будет значение косинуса.
 

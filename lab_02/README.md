# Замечания к ЛР№2 по компьютерной графике

**Задание**: нарисовать рисунок (по варианту) и масштабировать/поворачивать/переносить его согласно входным данным от пользователя (смещение, коэффициенты масштабирования, угол поворота, центр масштабирования/поворота). Нужно реализовать еще откат на одно действие назад.

- Внимательно смотрите на выданный рисунок: если нарисован прямоугольничек, то это не экран, а реально прямоугольник, который нужно отрисовать вместе с фигурой. Казалось бы и так логично, но я на этом попался и чуть не улетел, пришлось срочно допиливать прямоугольник (из-за этого код довольно говнокодский, с большим повторением функций для эпициклоиды и прямоугольника).
- На защите в основном спрашивает по коммутативности операций преобразования.
- Еще Куров вводит входные данные и спрашивает, что сейчас получится (удалится/приблизится к центру масштабирования, отразится, увеличится, уменьшится, сожмется и все такое)
- Пока допиливал прямоугольник, не привязал его размеры к эпициклоиде (у которой можно менять размер и кол-во лепестков), поэтому эпициклоида немного вышла за рамки прямоугольника - нехорошо (по рисунку она у меня должна быть полностью внутри).
- Даже если у вас экранные координаты, координаты на входе пользователь может задавать отрицательные, дробные и какие угодно вещественные, и за пределами экрана тоже.

За работу получил в итоге 6/7 (не совсем точно ответил про коммутативность операций масштабирования и поворота - слушайте на лекциях внимательно).
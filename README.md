# cat-compression
Репозиторий с решением лабы по сжиманию котика

![permalink setting demo](https://i.imgur.com/J006WPv.gif)

сжимал двигая пиксели в соответствии с диффуром, если попробовать другой диффур или другие картинки то получится тоже прикольно
для сжатия x'=-x, y'=y, для вращения x'=y, y'=-x


![permalink setting demo](https://i.imgur.com/0yYsEyy.gif)

разные котики лежат в папке cats, диффуры апроксимировались методом эйлера, параметр scale_factor отвечает за размер одного пикселя картинке на холсте (если запустить с >1 там видно что пиксели ездят отдельно друг от друга и не по сетке)
ускорение начиная с какого-то из шагов достигается благодаря мемоизации на методе вычисления следующей точки (встроеная в питон)

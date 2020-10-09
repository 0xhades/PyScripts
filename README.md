# PyScripts
mini python scripts

# listmaker
make all the possibilities of chars with a specify length
```
python3 listmaker.py (chars) (length)
example:
python3 listmaker.py 1234567890 3
```

# changecolor
change color (RGB) to another (RGB) color

*Require PIL (pip3 install pillow)*
```
python3 changecolor.py (image path) (target color 255,255,255) (change to 255,255,255) (noice rate)
example (change white to black):
python3 changecolor.py ~/blackline.png 255,255,255 0,0,0 100
```

# getrandomline
get random lines of a big list
```
python3 getrandomline.py (file) (how many loops) (min) (max) (if line contain this, don't print)
example:
python3 getrandomline.py ~/database.txt 10 100 4000000 error 
```

# choas
randomize an enitre list, even if u want to random every x lines
```
python3 choas.py (file) [x]
example:
python3 choas.py ~/database.txt [3]
```



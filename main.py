
s = '|Model architecture | Optimizer | Train batch / steps | Train images | Stop epoch | Test accuracy |\n\
|2 x inception(w dr) 2 x (conv(144ft)+maxpool) flt 2 x dense (w dr) act \[w batch normalization\]|Adam(0.001)|64/300|Normalized color + augmentation|41|86.47 %\n\
|2 x inception(w dr) (conv(144ft)+maxpool) (conv(288ft)+maxpool) flt 2 x dense (w dr) \[w batch normalization\]|Adam(0.001)|64/300|Normalized color + augmentation|65|86.37 %'

out = '{|class="wikitable\n'

for line_nr, line in enumerate(s.splitlines()):
    for word in line.split('|'):
        word = word.strip()
        if len(word)<1:
            continue
        #header
        if line_nr == 0:
            out += '!'+word+'\n'
        else:
            out += '|'+word+'\n'
    out += '|-\n'

out += '|}'

print(out)

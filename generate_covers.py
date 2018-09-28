with open('covers.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

covers = set()
end = []
for line in lines.split('\n'):
    if not line.startswith('#xmenu'):
        if line:
            end.append(line)
        continue

    covers.add(line)

with open('Covers2.css', 'w', encoding='utf-8') as f:
    f.write('\n'.join(covers))
    f.write('\n')
    f.write('\n'.join(end))

print('Now paste the contents of Covers2 to Covers to complete the process')
convert jpeg to jpg
```
for fil in *.jpeg; do git mv -- "$fil" ${fil%.jpeg}.jpg; done
```

to list all file extensions
```
find . -type f -name '*.*' | sed 's|.*\.||' | sort -u
```


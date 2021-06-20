convert jpeg to jpg
```
for fil in *.jpeg; do git mv -- "$fil" ${fil%.jpeg}.jpg; done
```


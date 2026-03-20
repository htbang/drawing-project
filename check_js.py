import js2py, codecs
text = codecs.open('index.html', 'r', 'utf-8').read()
start = text.find('<script>') + 8
end = text.find('</script>', start)
js = text[start:end]
try:
    js2py.eval_js('function __validate(){' + js + '\n}')
    print('OK')
except Exception as e:
    print('ERR', e)

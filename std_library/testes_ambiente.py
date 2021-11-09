# os.environ, os.getenv, os.putenv
import os

for k,v in os.environ.items():
    print(f'{k}={v}')
print('--- fim teste ---')

print(os.environ['HOME'])
print(os.getenv('HOME'))
print('--- fim teste ---')

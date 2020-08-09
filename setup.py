from distutils.core import setup
setup(
  name = 'sunnyside',        
  packages = ['sunnyside'],   
  version = '0.1',     
  license='MIT',        
  description = 'Python wrapper for OpenWeather API',   # Give a short description about your library
  author = 'Jun Qi Li',                   
  author_email = 'JunQi.Li63@myhunter.cuny.edu',      
  url = '',   
  download_url = 'https://github.com/junqili259/Sunnyside/archive/v0.1.tar.gz',   
  keywords = ['OpenWeather'],   # Keywords that define your package best
  install_requires=[            
          'requests'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
  python_requires='>=3.6',
)
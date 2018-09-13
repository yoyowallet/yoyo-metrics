from setuptools import setup

setup(
    name='yoyo_metrics',
    version='1.0',
    description='Library to send metrics using different backends.',
    url='http://github.com/yoyowallet/yoyo-metrics',
    author='',
    author_email='dev@yoyowallet.com',
    license='MIT',
    packages=['yoyo_metrics'],
    zip_safe=False,
    install_requires=[
        'datadog==0.22.0',
    ]
)

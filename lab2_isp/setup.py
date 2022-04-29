from setuptools import setup

setup(
    name='serializer',
    version='1.0.0',
    description='Lab2_isp_bsuir',
    packages=['serializer',
              'serializer/ser_factory',
              'serializer/json_serializer',
              'serializer/toml_serializer',
              'serializer/yaml_serializer',
              'serializer/pack_recover'],
    author='lLeshii',
    install_requires=['PyYaml == 5.3.1',
                      'pytoml == 0.1.21'],
    entry_points={
        'console_scripts': [
            'ser_cons = serializer.serializer_cons:main'
        ]}
    )
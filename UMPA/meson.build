# Locate python
py = import('python').find_installation(pure: false)
dep_py = py.dependency()
omp = dependency('openmp')

# Locate numpy
incdir_numpy = run_command(py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy)  

# Install UMPA cython model library
py.extension_module(
    'model',
    'model.pyx',
    dependencies : [dep_py, omp], 
    override_options : ['cython_language=cpp'],
    install: true,
    include_directories: [inc_np],
    subdir: 'UMPA'
)

# Define UMPA native python sources
python_sources = [
    '__init__.py',
    'align.py',
    'speckle_matching.py',
    'utils.py',
]

# Install source files
py.install_sources(
  python_sources,
  pure: false,
  subdir: 'UMPA',
)
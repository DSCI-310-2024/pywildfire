import pytest
import shutil

# The following code removes any files or directories created during the tests that 
# require deletion at the end of the session.

@pytest.fixture(autouse = True, scope = 'session')
def cleanup_directories_after_session():
    yield
    for dir in ['tests/test_zip_data1', 'tests/test_zip_data2']:
        try:
            shutil.rmtree(dir)
        except FileNotFoundError:
            pass 
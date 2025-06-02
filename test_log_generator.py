import builtins
from unittest.mock import patch, mock_open
import log_generator

def test_write_random_log_entry():
    # Patch 'random.choice' to control output
    with patch('random.choice', side_effect=["ERROR", "File not found"]):
        # Patch open to mock file writing
        m = mock_open()
        with patch('builtins.open', m):
            log_generator.write_random_log_entry()
        
        # Check if the file was opened correctly
        m.assert_called_once_with(log_generator.log_file, 'a')
        
        # Check if the correct log line was written
        handle = m()
        handle.write.assert_called_once_with("ERROR: File not found\n")


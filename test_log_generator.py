from log_generator import write_log

def test_write_log(tmp_path):
    test_log = tmp_path / "sample.log"
    write_log("INFO", "Hello test!", file_path=test_log)

    with open(test_log) as f:
        content = f.read()
        assert "INFO: Hello test!" in content


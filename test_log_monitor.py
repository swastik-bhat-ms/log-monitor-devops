# test_log_monitor.py

from log_monitor import process_log_lines

def test_process_log_lines():
    log_content = [
        "This is a normal log line\n",
        "Critical failure occurred\n",
        "All operations succeeded\n",
        "Error: unable to connect\n"
    ]

    alerts = process_log_lines(log_content)

    # There should be 2 alerts: critical and error
    assert len(alerts) == 2
    assert "critical failure occurred" in alerts[0].lower()
    assert "error: unable to connect" in alerts[1].lower()


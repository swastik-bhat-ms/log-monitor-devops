from log_monitor import process_log_lines

def test_process_log_lines():
    # Prepare mock log lines
    log_content = [
        "This is a normal log line\n",
        "Critical failure occurred\n",
        "All operations succeeded\n",
        "Error: unable to connect\n"
    ]

    alerts = process_log_lines(log_content)

    # There should be 2 alerts for "Critical" and "Error"
    assert len(alerts) == 2
    assert "[ALERT] Keyword 'critical' found:" in alerts[0]
    assert "critical failure occurred" in alerts[0].lower()  # case insensitive check



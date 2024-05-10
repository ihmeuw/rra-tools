def test_rra_tools() -> None:
    from rra_tools import (
        cli_tools,
        jobmon,
        logging,
        parallel,
        shell_tools,
        translate,
    )

    assert cli_tools
    assert logging
    assert jobmon
    assert parallel
    assert shell_tools
    assert translate

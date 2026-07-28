from ffbinaries import FFBinariesAPIClientError


def test_base_exception() -> None:
    assert issubclass(FFBinariesAPIClientError, Exception)

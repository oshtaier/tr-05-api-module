import pytest
from mock import MagicMock

from threatresponse.api.enrich.deliberate import DeliberateAPI


def test_observables_succeeds():
    response = MagicMock()

    request = MagicMock()
    request.post.return_value = response

    payload = [{'foo': 'bar'}]

    api = DeliberateAPI(request)
    api.observables(payload)

    request.post.assert_called_once_with(
        '/iroh/iroh-enrich/deliberate/observables',
        json=payload,
    )

    response.json.assert_called_once_with()


def test_observables_fails():
    class TestError(Exception):
        pass

    response = MagicMock()
    response.raise_for_status.side_effect = TestError('Oops!')

    request = MagicMock()
    request.post.return_value = response

    payload = [{'foo': 'bar'}]

    api = DeliberateAPI(request)
    with pytest.raises(TestError):
        api.observables(payload)

    request.post.assert_called_once_with(
        '/iroh/iroh-enrich/deliberate/observables',
        json=payload,
    )

    response.raise_for_status.assert_called_once_with()

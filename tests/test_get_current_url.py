import pytest
import threading
from .util import run_test, destroy_window


def get_current_url():
    import webview

    def _get_current_url(webview):
        print("get_current_url")
        webview.get_current_url()
        print("get_current_url done")

    t = threading.Thread(target=_get_current_url, args=(webview,))
    t.start()
    destroy_window(webview, 5)
    print("create_window")
    webview.create_window('Get current url test', 'https://www.example.org')


def test_get_current_url():
    run_test(get_current_url)

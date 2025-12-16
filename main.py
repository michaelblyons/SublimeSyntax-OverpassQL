import sublime
import sublime_plugin

from webbrowser import open_new_tab
from urllib.parse import quote, urlencode


class OpenOverpassTurboCommand(sublime_plugin.WindowCommand):
    # https://wiki.openstreetmap.org/wiki/Overpass_turbo/URL_Parameters
    URL = 'https://overpass-turbo.eu/?'

    def run(self, **args):
        view = self.window.active_view()

        region = view.sel()[0]
        if not len(region):
            region = sublime.Region(0, view.size())

        query_text = view.substr(region)

        open_new_tab(self.URL + urlencode({
            'Q': query_text,
        }, quote_via=quote))

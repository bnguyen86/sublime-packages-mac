import sublime, sublime_plugin

class MinifyAndDeployCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command("save");
        self.view.run_command("minify");
        self.view.window().run_command("deploy_resource_bundle");

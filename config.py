import os
from appium.options.android import UiAutomator2Options
from pydantic import BaseModel
from utils import file


class Config(BaseModel):
    context: str
    remote_url: str = os.getenv("REMOTE_URL")
    device_name: str = os.getenv("DEVICE_NAME")
    appWaitActivity: str = os.getenv("APP_WAIT_ACTIVITY")
    app: str = os.getenv("app")
    platformName: str = os.getenv("platformName")
    platformVersion: str = os.getenv("platformVersion")
    userName: str = os.getenv("USER_NAME")
    accessKey: str = os.getenv("ACCESS_KEY")

    def to_driver_options(self, context):

        options = UiAutomator2Options()

        print(self.context, self.device_name, self.app)

        if context == "local_real":
            options.set_capability("platformName", self.platformName)
            options.set_capability("remote_url", self.remote_url)
            options.set_capability("app", file.abs_path_from_project(self.app))
            options.set_capability("appWaitActivity", self.appWaitActivity)

        if context == "local_emulator":
            options.set_capability("platformName", self.platformName)
            options.set_capability("remote_url", self.remote_url)
            options.set_capability("app", file.abs_path_from_project(self.app))
            options.set_capability("appWaitActivity", self.appWaitActivity)

        if context == "bstack":
            options.set_capability("remote_url", self.remote_url)
            options.set_capability("deviceName", self.device_name)
            options.set_capability("platformName", self.platformName)
            options.set_capability("platformVersion", self.platformVersion)
            options.set_capability("appWaitActivity", self.appWaitActivity)
            options.set_capability("app", self.app)
            options.set_capability(
                "bstack:options", {
                    "projectName": "First Python project",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": self.userName,
                    "accessKey": self.accessKey,
                },
            )

        return options


config = Config(context="local_emulator")

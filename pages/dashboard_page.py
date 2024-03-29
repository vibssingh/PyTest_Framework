from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DashboardPage(BasePage):
    heading = (By.XPATH, "//*[@class='oxd-topbar-header-breadcrumb']/h6")
    assign_leave_option = (By.XPATH, "//*[@title='Assign Leave']")
    time_at_work_option = (By.XPATH, "//*[@title='Time at Work']")

    def actual_heading(self):
        log = self.get_logger()
        dashboard_heading = self.find(self.heading).text
        log.info("Heading is " + dashboard_heading)
        return dashboard_heading

    def assign_leave_displayed(self):
        log = self.get_logger()
        assign_leave = self.find(self.assign_leave_option).is_displayed()
        log.info("Assign Leave Option is displayed " + assign_leave)
        return assign_leave

    def time_at_work_displayed(self):
        log = self.get_logger()
        time_at_work = self.find(self.assign_leave_option).is_displayed()
        log.info(f"Time At Work Option is displayed  {time_at_work}")
        return time_at_work

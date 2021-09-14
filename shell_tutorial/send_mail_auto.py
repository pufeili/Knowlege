#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 @FileName  :main.py
 @Time      :2021/9/14 10:03
 @Author    :LPF
"""
import yagmail
import time


class Mail:
    """
    邮件相关类
    """
    def sendmail(self, msg, title, receivers, attachment=None):
        """
        发送邮件
        Arguments:
            msg {str} -- 邮件正文
            title {str} -- 邮件标题
            receivers {list} -- 邮件接收者，数组
            attachment {list} -- 附件，数组
        """
        yag = yagmail.SMTP(
            host='smtp.qq.com',
            user='xxxxx@qq.com',    # 发送者邮箱
            password='xxxx',   # 授权码，无空格
            smtp_ssl=True
        )

        try:
            yag.send(to=receivers, subject=title, contents=msg, attachments=attachment)
            self.log("Mail sent successfully")
            yag.close()     # 关闭链接

        except BaseException as e:
            print(e)
            # print("Error: 无法发送邮件")
            self.log("Mail sending failed")
            yag.close()     # 关闭链接

    def log(self, content):
        now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'{now_time}: {content}')


if __name__ == "__main__":
    auto_send = Mail()
    # auto_send.sendmail("测试邮件正文", "测试邮件标题", ['xxxxx@qq.com'])
    auto_send.sendmail(receivers=['xxxxx@qq.com'],
                       title='测试邮件',
                       msg='详细见附件',
                       attachment=['./实验室硬件配置表.xlsx', './2021.png'])
    run_code = 0

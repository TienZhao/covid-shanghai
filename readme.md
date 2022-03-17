# COVID-Shanghai

- 受到GitHub异常影响，代码更新无法被部署到页面上，可能会导致2022-03-17数据更新延迟。
  Due to some incident with GitHub, the page update can not be deployed now. This may cause delay in the update of 2022-03-17 data.

  - https://github.com/actions/deploy-pages/issues/22
  
- Demo link: [https://tienzhao.github.io/covid-shanghai/demo.html](https://tienzhao.github.io/covid-shanghai/demo.html)

  - **This demo stopped working** because Baidu Map recognize the rapidly increasing traffic as attack and blocked my developer account.

- New demo link: [https://tienzhao.github.io/covid-shanghai/shanghai.html](https://tienzhao.github.io/covid-shanghai/demo.html)

  - Click the left-top button, and see the COVID case addresses in Shanghai.

- Data updated on March 16, 2022

- Workflow:
  - Manually download announcement text from [Shanghai Municipal Health Commission](https://wsjkw.sh.gov.cn/xwzx/)
  - Parse addresses from texts
  - Plot it on map

- **This gadget is totally open-source, and the developer hopes it will improve technology democracy among all of us facing the pandemic.**

- Todos (Get your hand on it!):
  - Write a crawler to download gazette
  - Update file loop methods: try to read past 14 day data regardless of months.

- Support ￥10, and let's get rid of COVID!

  ![](images/donation.jpg)


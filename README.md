# pulumi_examples_gcp_py
此處使用 Google 雲端平台(Google Cloud Platform, GCP)，並以 Python 作為開發的程式語言。

# 前置作業
## 開發環境準備
安裝以下工具：
- [Python 3.6+](https://www.python.org/downloads/)
- Pulumi
    ```bash
    # Linux
    $ curl -fsSL https://get.pulumi.com | sh

    # macOS
    $ brew install pulumi
    ```
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
    ```bash
    # 下載 Google Cloud SDK

    # 安裝 Google Cloud SDK
    $ ./google-cloud-sdk/install.sh

    # 初始化 Google Cloud SDK
    $ gcloud init
    ...
    Pick cloud project to use:
     [1] Create a new project
    Please enter numeric choice or text value (must exactly match list
    item):  <your-gcp-project-name>
    ...

    # 由於 Pulumi 需要與我們的 Google 資源互動，所以要設定授權
    $ gcloud auth application-default login
    ```

    若尚未將 GCP 的專案綁定帳戶資訊，請記得設定專案的帳戶資訊：
    1. 登入 Google Cloud 介面
    2. 選擇剛所建立的 GCP 專案
    3. 點選左上角的`導覽選單(Navigation Menu)`，並選擇`帳單(Billing)`
    4. 連結你的帳單帳戶

## 註冊 Pulumi 帳號和建立 Access Token
1. 到 [Pulumi 官網](https://app.pulumi.com/signup) 註冊帳號
   > Pulumi 個人使用是免費的(基礎功能)，若為多人以上共同開發或需要進階功能，則須依層級付費。
2. 登入 [Pulumi 控制台](https://app.pulumi.com/)
3. 點選用戶頭像 > Settings > Access Tokens
4. 建立一組 Access Token
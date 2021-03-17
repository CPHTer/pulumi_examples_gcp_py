### 注意事項
* 範例皆以乾淨的環境運行，因此會在步驟中重新建立堆疊。若您的堆疊已含有其它資源，部署的結果可能會與範例結果有所差異，請先[刪除資源](#刪除資源)再開始我們的範例。

# 目標
* 初始化 Pulumi 專案

# 步驟
1. 準備運行環境 `venv`
    ```bash
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
2. 建立 `dev` 堆疊
    ```bash
    $ pulumi stack init dev
    ....
    Created stack 'dev'

    $ pulumi stack ls
    NAME  LAST UPDATE  RESOURCE COUNT  URL
    dev*  n/a          n/a             https://app.pulumi.com/<username>/minimal-py/dev
    ```

3. 設定 GCP 專案
    ```bash
    $ pulumi config set gcp:project <your-gcp-project-name>
    ```
4. 執行部署
    ```bash
    $ pulumi up
    Previewing update (dev)

    ...

        Type                 Name            Plan
    +   pulumi:pulumi:Stack  minimal-py-dev  create

    Resources:
        + 1 to create

    Do you want to perform this update? yes
    Updating (dev)

    ...

        Type                 Name            Status
    +   pulumi:pulumi:Stack  minimal-py-dev  created

    Resources:
        + 1 created

    Duration: 16s
    ```

# 刪除資源
1. 刪除資源
    ```bash
    $ pulumi destroy
    ```
2. 刪除 `dev` 堆疊
    ```bash
    $ pulumi stack rm dev
    ```

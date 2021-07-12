# tron-airdrop

一个 Tron 网络空投工具。手续费由用户承担，~~适合奸商~~。

## 开始

请先在你的机器上安装 ` Python 3`，`pymysql`，`tronpy`，安装方法自行谷歌。  

然后，装上 `MySQL` 并执行
```
CREATE TABLE `your_database_name`.`address` ( `tron_address` LONGTEXT NOT NULL ) ENGINE = InnoDB;
```

下载 tron-airdrop.py，并按下图所示修改。

[![2Vnk0f.png](https://z3.ax1x.com/2021/05/30/2Vnk0f.png)](https://imgtu.com/i/2Vnk0f)
![image](https://user-images.githubusercontent.com/53929319/120092844-af6e9c80-c148-11eb-99e7-e795e9f09956.png)

最后，设置个定时任务自动执行就可以了。

## 注意事项
**1. 只支持 TRC20 合约。**  
**2. 请确保你的账户 TRX 余额大于 15。**  
**3. 建议不要用创建合约的账户，新开个账户，避免安全问题导致私钥泄露。**

## 捐赠
USDT-TRC20(TRX): `TGJo5uGVGXywskuM22sZcNGAxWK6ah538h`  
Monero(XMR): `49XZKKiXRXLDM8BGr4U3vyKpXVwZYsnqpawiV5TuHZ416topqimNc77SubKABHyrAGeRJfQ8oFE7GH57ZFrDgspgNv2f6Tw`

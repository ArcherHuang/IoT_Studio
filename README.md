# NEXCOM 物聯雲 IoT Studio

## 【 Overview 】
* 實作架構 
   
## 【 File 】
      
| 編號 | 資料夾 |  檔案名稱 | 說明  |
|---|---|---|---|
|1| /Arduino  |  |   |
|2| /Python  | sensingDataToAllIoTCloudHTTPSend.py |   |
|3| /Python  | sensingDataToAllIoTCloudWebSocketReceive.py |   |
|4| /Python  | sensingDataToAllIoTCloudWebSocketSend.py |   |

## 【 Board and Sensor 】

* [LinkIt Smart 7688 Duo](https://www.seeedstudio.com/LinkIt-Smart-7688-Duo-p-2574.html)
* [Arduino Breakout for LinkIt Smart 7688 Duo](https://www.seeedstudio.com/Arduino-Breakout-for-LinkIt-Smart-7688-Duo-p-2576.html)
* [Grove - Temperature & Humidity Sensor](http://www.alliotcloud.com/market/singl.php?PID=56)
* [Raspberry Pi 3 Model B](http://www.alliotcloud.com/market/singl.php?PID=40)

## 【 Integrated Development Environment - IDE 】
 
 * Arduino
   *  [Arduino IDE v1.6.4](https://www.arduino.cc/en/Main/OldSoftwareReleases)
 * Python
   * [Sublime Text](https://www.sublimetext.com/)
   * [Visual Studio Code](https://code.visualstudio.com/b?utm_expid=101350005-27.GqBWbOBuSRqlazQC_nNSRg.1&utm_referrer=https%3A%2F%2Fwww.google.com.tw%2F)
   * [Jupyter](http://jupyter.org/)
     * Command: ipython notebook

## 【 Firmware 】
* [Download](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/downloads)

## 【 Library 】

* DHT ( DHT sensor library by Adafruit Version: 1.2.3 )
   *  在 Arduino Sketch 中點選```草稿碼``` ➙ ```匯入程式庫``` ➙ ```管理程式庫``` ➙ 右上角搜尋欄位輸入 ```DHT``` ➙ 選擇 ```DHT sensor library by Adafruit Version: 1.2.3```

## 【 Tools 】
 * Windows 作業系統
   *  登入
      * Windows 端
        * [使用 Putty](https://the.earth.li/~sgtatham/putty/latest/x86/putty.exe)
   *  傳送檔案 
      * Windows 端
        * [使用 FileZilla Client](https://filezilla-project.org/)

 * macOS 作業系統
   *  登入（本地端到 Raspberry Pi 端）- 終端機
      * 登入（在本地端電腦的終端機執行） ➙ ```ssh root@Raspberry Pi 的IP```
   *  傳送檔案（本地端到 Raspberry Pi 端）- 終端機
      * 傳送檔案（在本地端電腦的終端機執行） ➙ ```scp 在電腦中的檔案位置 root@Raspberry Pi 的IP:要傳送到 Raspberry Pi 中的位置```
      
## 【 Execute 】

 * 執行 Python Code
```bash
$ python Python-Name-Here.py
```

## 【 JSON Tools 】
 * [JSON Lint](http://jsonlint.com/)
 * [JSON Editor Online](http://www.jsoneditoronline.org/)

## 【 Reference 】

* [Get Started with the LinkIt Smart 7688](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-development-board)
* [Get Started with the LinkIt Smart 7688 Duo](https://docs.labs.mediatek.com/resource/linkit-smart-7688/en/get-started/get-started-with-the-linkit-smart-7688-duo-development-board)
* [LinkIt Smart 7688 Developer’s Guide](https://labs.mediatek.com/en/download/ih80Qtjo)
* [All IoT Cloud](http://www.alliotcloud.com/media/index1.php)

## 【 Blog 】
* [Archer @ 部落格](https://github.com/ArcherHuang/MyBlog/blob/master/README.md)

## 【 License 】

The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

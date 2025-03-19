# Getting started with Python

Before starting building the projects, you need to make some preparation first. Do not skip this step as it provides crucial information for installing.

### 1.Installing Thonny (Important)：

Thonny is a free, open-source software platform with compact size, simple interface, simple operation and rich functions, making it a Python IDE for beginners. In this tutorial, we use this IDE to develop ESP32 during the whole process.

Thonny supports various operating system, including Windows、Mac OS、Linux.

#### **(1) Downloading Thonny：**

①Enter the official website of Thonny: [<span class="underline">https://thonny.org</span>](https://thonny.org) and download the latest version of Thonny.

②Open-source code repositories of Thonny: [<span class="underline">https://github.com/thonny/thonny</span>](https://github.com/thonny/thonny)

Follow the instruction of official website to install Thonny or click the links below to download and install. (Select the appropriate one based on your operating system.)

| Operating System | Download links/methods                                       |
| :--------------: | ------------------------------------------------------------ |
|     MAC OS：     | [https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg](https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg) |
|    Windows：     | [https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe]( https:/github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe) |
|     Linux：      | **The latest version:**<br />**Binary bundle for PC (Thonny+Python):** bash <(wget -O - https://thonny.org/installer-for-linux)<br />**With pip:** pip3 install thonny<br /><br />**Distro packages (may not be the latest version):**<br />**Debian, Rasbian, Ubuntu, Mint and others:** sudo apt install thonny<br />**Fedora:** sudo dnf install thonny |


![](media/bd5823ede2c01d1fa4696438c62aec51.png)

#### **(2) Install Thonny on Windows：**

The icon of Thonny after downloading is as below.

![](media/d3caa98d406fa06a124d5c98195b90db.png)

1.  Double click“thonny-3.3.13.exe”，the following dialog box will appear. I choose“![](media/11fb59a50abe0bf54df7e4cb891ad2c0.png)”to operate, you can also select“![](media/37be3f3bcc9aa0eb48c8b844eb46a71c.png)” to operate.
    
    ![](media/4c044b255da8b14fe674eb9cce01627d.png)
    
2.  If you’re not familiar with computer software installation, you can simply keep clicking “**Next**” until the installation completes.
    

![](media/995b36640124b6a9b23f10473ff8a38a.png)

![](media/8bcc17840b9fc15d76f79fee8a0168ee.png)

3. If you want to change Thonny’s installation path, you can click “**Browse...**” to modify it. After selecting installation path, click “**OK**”. If you do not want to change it, just click “**Next**”.

![](media/df6f63b42ebb1676b22c26b25dc9c7aa.png)

![](media/f5cd6d619b4645601c5b098ffdbec12a.png)

4.  Check “**Create desktop icon**” and then it will generate a shortcut on your desktop to facilitate you to open Thonny later.

![](media/a30c89dde3de81ad00aced30510071be.png)

5.  Click “**Install**” to install the software.
    
    ![](media/6ace65142291e5e8af5f81e4a6b2f180.png)

6.  During the installation, you only need to wait for completion, and you should not click "**Cancel**", otherwise Thonny will fail to be installed.
    

![](media/a504b3a3ab16b4d91040cd5878acea0c.png)

7. Once you see the interface as below, Thonny has been installed successfully. Click “**Finish**”.

![](media/a1fb6027e54a975de1c0aa1e1a0d6a29.png)

8. If you’ve check“**Create desktop icon**”during the installation process, you can see the below icon on your desktop.

![](media/80f35044d91d66f734e36059db35f273.png)



### 2. Basic Configuration of Thonny：

1.  Click the desktop icon of Thonny and you can see the interface of it as follows, and we can also choose the language and initial settings.  Once set, click "**Let's Go\!**"
    
    ![](media/ee240978a4f844184f1ea9f5a21d0395.png)
    
    ![](media/619a856895d95e00beed748b1438072d.png)
    
    ![](media/bcf6c31e4f69c904a7a0c0e9df7e8d7d.png)
    
2.  Select“**View**”→“**Files**”and“**Shell**”.
    
    ![image-20231110120459662](./media/image-20231110120459662.png)
    
    ![image-20231110120507683](./media/image-20231110120507683.png)
    
    ![image-20231110120513761](./media/image-20231110120513761.png)



### 3.Installing CP2102 driver：

ESP32 uses CP2102 to download codes. So before using it, we need to install CP2102 driver in our computers.

#### **Windows System**

Check whether CP2102 has been installed

(1). Connect your computer and ESP32 with a USB cable.

![](./media/image-20231110120529164.png)

(2). Turn to the main interface of your computer, select “**This PC**” and right-click to select “**Manage**”.

![](media/84bc1f7d3169cad24b23d2ac620bc111.png)

(3). Click “**Device Manager**”, your computer has installed CP2102 driver，you can see “Silicon Labs CP210x USB to UART Bridge (COMx)”

![](media/a320816d8aed54304018d8380b5b6b3d.png)

Installing CP2102 driver

(1) If you have not yet installed the CP2102 driver, you’ll see the following interface.

![](media/776adb879fe6e299e3610cc92cfaf70b.png)

(2) Click “CP2102USB to UART Bridge Controller”, and right-click to select “Update driver”.

![](media/7b342fbd38b03cba4dfce2045f4fe17b.png)

(3) Click “Browse my computer for drivers ”.

![](media/1cb9eaea189e4766d17a0a5977c23a74.png)

(4) Click “Browse...” select CP210x\_6.7.4 (Driver path：2. Windows System\\1. Python\_Tutorial\\1. Preparation for Python(Windows)\\CP2102 Driver File-Windows), Click “Next”.


![](media/7e93cd82c70973203ea88aa433a32462.png)

(5) Wait for the CP2102 driver installation to be finished. When you see the following interface, which indicates that the CP2102 driver has been installed to your computer. You can close the interface.

![](media/b99fbcb61c133392d1b94b65f51fc2c7.png)

(6) When ESP32 is connected to computer, the interface appears as follows.


![](media/da0dffd89b5f385612c3230422ee732f.png)

#### **MAC System**

You can refer to the link：[https://docs.keyestudio.com/projects/KS5010/en/latest/docs/3.1Get-started-with-Arduino.html#how-to-install-the-cp2102-driver](https://docs.keyestudio.com/projects/KS5010/en/latest/docs/3.1Get-started-with-Arduino.html#how-to-install-the-cp2102-driver)

### 4.Burning Micropython Firmware (Important)

To run Python programs on ESP32, we need to burn a firmware to ESP32 first.

#### (1) Downloading Micropython firmware

Official website of microPython：<http://micropython.org/>

Webpage listing firmware of microPython for ESP32：[<span class="underline">https://micropython.org/download/esp32/</span>](https://micropython.org/download/esp32/)

![](media/c706d3cd6862323dcfccfd11ec7d1da3.png)

Firmware used in this tutorial is **esp32-20210902-v1.17.bin**

Click the following link to download directly：[Python_Firmware](Python_Firmware.zip)


#### (2) Burning a Micropython Firmware

Connect your computer and ESP32 with a USB cable.

![image-20230426151320377](media/image-20230426151320377.png)

Make sure that the driver has been installed successfully and that it can recognize COM port correctly. Open device manager and expand “**Ports(COM\&LPT)**”.

![](media/d154c68ab7e252cf013b374069a2c6c0.png)

Note: COM ports may be different on different computers

A. Open Thonny，click “**Run**” and select “**Select interpreter...**”.

![](media/bda2bfc9d4576aef0b63e1f6373bf5a7.png)

B. Select “**Micropython (ESP32)**”, select “**Silicon Labs CP210x USB to UART Bridge(COM3**)”, and then click “**Install or update firmware**”. 

![](media/adfa634e977c803db209b18418f1df76.png)

C. The following dialog box pops up, Select “**Silicon Labs CP210x USB to UART Bridge(COM3)**” for “**Port**”, and then click “**Browse...**”. Select the previous prepared microPython firmware “**esp32-20210902-v1.17.bin”**. Check “**Erase flash before installing**” and “**Flash mode**”, then click “**Install**” to wait for the prompt of finishing installation.

（Note: If you fail to install the firmware, press the Boot on the ESP32 mainboard and click “Install” again.）

![](media/8b746aeb78c731ab638141c8c197437b.png)

![Img](./media/img-20250313163721.png)

![](media/5813b136c67bf0fe3de66db589f9e9bf.png)

D. Wait for the installation to be done, then click“**Close**”and“**OK**”.

![](media/f706c7f121e659e206fd9727665f1af2.png)

![](media/1d3975349fa695b6d07378e83a49ec31.png)

![](media/7fc6ac0c25d55775ef60449f497c6f2f.png)

E. Close all dialog boxes, turn to main interface and click![](media/a807dd85c760f2bda89025b9fd70156e.png)“**STOP**”. As shown in the illustration below:

![](media/e9d1c2d43c22cf13ada2bdf4808aacb9.png)

F. So far, all the preparations have been made.

### 5.Test Code：

Testing the Shell commander

Enter “**print('hello world')**” in “**Shell**” and press Enter.

![](media/0dd4176ed13f85a7c96c14b4e20e6166.png)

Running Online(Important)

ESP32 needs to be connected to a computer when it is run online. Users can use Thonny to writer and debug programs.

1.  Open Thonny and click “**Open…**”.
    

![](media/7fded176b193d1ac598571f7d16599f7.png)

2.  Click “**This computer**”on the newly pop-up window.
    

![](media/101bf94e8e29ce5bc4a948f15b5dbe51.png)

3.  In the new dialog box, select “**Project\_01\_HelloWorld.py**” in “...\2. Python Projects\\Project 01：Hello World” folder.

![Img](./media/img-20250313163857.png)


4.  Click![](media/31511be865975be04b53f27aa45c60a7.png)“Run current script”to execute the program and “**Hello World**” will be printed in“**Shell**”.
    

![](media/d15552e75ae0a9b2184e75b173f271b8.png)

**Note**：When running online, if you press the Reset button of ESP32, user’s code will not be executed again. If you wish to run the code automatically after resetting the code, please refer to the following Running Offline.

Running Offline(Important)

After ESP32 is reset, it runs the file boot\.py in root directory first and then runs your code file, and finally it enters “**Shell**”. Therefore, to make ESP32 execute user’s programs after resetting, we need to add a guiding program in boot\.py to execute user’s code.

1.  Move the program folder “2. Windows System\\1. Python\_Tutorial\\2. Python Projects” to disk(D) in advance with the path of “D:/2. Python Projects”. Open “**Thonny**”.


![](media/000a950d20ba8d5cb478cbeb33dd238c.png)

2.  Expand “**Project 00: Boot**” in the “**2. Python Projects**” in the directory of disk(D), and double-click ”**boot\.py**”, which is provided by us to enable programs in“**MicroPython device**” to run offline.


![](media/da4d70e3edebeaba6bb5fa6247a777b9.png)

3. If you want your written programs to run offline, you need to upload “**boot\.py”** we provided and all your codes to “MicroPython device” and press ESP32’s Reset button. Here we use programs **Project 00** and **Project 01** as examples. Select “**boot\.py**”, right-click to select “**Upload to /**”.

![](media/4322dafa440f20bea8bca8b5f0437b17.png)

4. Similarly, upload“**Project\_01\_HelloWorld.py**” to“**MicroPython device**”.

![](media/5734425738777d7a79a7e0abc4d65106.png)

5. Press ESP32’s Reset button and in the box of the “**Shell**” below, you can see the code is executed.

![](media/40e0e288b6b228b8a906054d8b602869.png)

### 6.Thonny Common operations：

Upload the code to ESP32

For convenience, let's take the opertation on “**boot\.py**” as an example. 

If we add “**boot\.py**” to each code directory, every time when ESP32 restarts, if there is a “**boot\.py**” in the root directory, it will execute this code first.

![](media/2a33e5afa8793c96d69255afb9067f15.png)

Select “**boot\.py**” in “**Project 03：LED Flashing**”, right-click your mouse and select “**Upload to /**” to upload code to ESP32’s root directory, select to click “**OK**”.

![](media/f3bca24026e4beda4f05ccd89cbeea14.png)

![](media/14a519166b9f9e7b3420812fb4295210.png)

Downloading Code to Computer

Select “**boot\.py**” in “**MicroPython device**”, right-click to select “**Download to ...**” to download the code to your computer.

![](media/cf9de37f4565f94e386542c777403dc3.png)

Delete files from ESP32 Root Directory

Select “**boot\.py**” in “**MicroPython device**”, right-click it and select “**Delete**” to delete “**boot\.py**” from ESP32’s root directory.

![](media/70e75f7f9f40b454dd3a3b580b736b2f.png)

Select “**boot\.py**” in “**Project 03：LED Flashing**”, right-click it and select “**Move to Recycle Bin**” to delete it from “**Project 03：LED Flashing**”.

![](media/646bb65f65361eb2c70b4abf40fc74ea.png)

Creating and Saving the code

Click “**File**” → “**New**” to create and write codes.

![](media/1d71df4720f9455dcaf17a72ec38bb1b.png)

Enter codes in the newly opened file. Here we use codes of “**Project\_03\_LED\_Flashing.py**” as an example.

![](media/e80d2f6ce955d013a708fd7134d6e64a.png)

Click![](media/40348c4ef49beb5e90593df6050c1d62.png)“**Save**”on the menu bar, you can save the codes either to your computer or to ESP32.

![](media/0f184894cef3d5d00a216dc2161d05d0.png)

Select “**MicroPython device**”, enter “**main\.py**” in the newly pop-up window and click “**OK**”.

![](media/895a782664e10406ce2ab9ba18507d19.png)

You can see that the code has been uploaded to ESP32.

![](media/cec982987cf6b8cc24d5830e7777ac63.png)

Disconnect and reconnect USB cable, and then you can see that LED is on for 0.5 s and then off for 0.5s.

![image-20230522090300281](media/image-20230522090300281.png)

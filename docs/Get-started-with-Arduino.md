# Getting started with Arduino

## Windows System：

![](media/6cf6312dc7c7db27794b54d58a8bf80c.png)


### 1.1.Download and install Arduino software：

（1）First, enter arduino's official website:[<span class="underline">https://www.arduino.cc/</span>](https://www.arduino.cc/), and click “SOFTWARE”to enter the download page. As shown in the figure below：

![](media/bfe8c9e405c71123dee7921eddff86d3.png)

![](media/7250961db41ba42e4b881d77bd76a319.png)

（2）Then, select and download the corresponding installer for your operating system. If you are a Windows user, please select “Windows Installer” to download to install the driver correctly.

![](media/894116c5cf0023dd9720946cfb441790.png)

Choose to click the **Windows Win7 and newer** to download Arduino 1.8.16 version installer, which requires manual installation. But when click the **Windows ZIP File**, the Arduino 1.8.16 zip file will be downloaded directly, just unzip it to complete the installation.

![](media/a983a2f2eceb968afbff8ba0f0376240.png)

In general, you can click **JUST DOWNLOAD** to download it, although if you like, you can choose a small sponsorship to help the great Arduino open source cause.

（3）After the Arduino IDE is downloaded, continue the installation. When you receive the warning from the operating system, please allow the driver installation by clicking **I Agree** first, and then click **Next** after selecting the components to install.

![](media/00e334d3c756a2495da6f0d1b2db680a.png)

![](media/de541d90a1cda992ad8e3f0cbaf95f94.png)

（4）Select the installation directory (we recommend keeping the default directory), and then click **Install**.

![](media/7da9aca1e8432c59372e7c7ab2574bd9.png)

（5）Select Install if the following screen appears.

![](media/85b29de2aa791ecc77280ccde91e53c5.png)

This process extracts and installs all the necessary files to properly execute the Arduino software (IDE).

![](media/739c41701fbcab202f0e587f534bad30.png)

After installation is complete, an Arduino Software shortcut will be generated in the desktop.

![](media/d28223c55a30f949760779720fe4ec24.png)

### 1.2.Install a driver on Windows：

（Note：If you have installed the driver, just skip it）

Before using the ESP32 board, you must install a driver, otherwise it will not communicate with computer. Unlike the USB series chip(ATMEGA8U2) of the Arduino UNO R3, the ESP32 board is used the CP2102 chip USB series chip and USB type C interface.

The driver of the CP2102 chip is included in 1.8.0 version and newer version of Arduino IDE. Usually, you connect the board to the computer and wait for Windows to begin its driver installation process. After a few moments, the process will succeed.

**Note:**

1\. Please make sure that your IDE is updated to 1.8.0 or newer version

2\. If the version of Arduino IDE you download is below 1.8, you should download the driver of CP2102 and install it manually.

Link to download the driver of CP2102:[Download CP2102 Driver](CP2102-Driver-File-Windows.zip)

If the driver installation process fail, you need to install the driver manually. Open device Manager for your computer and right-click “the computer”→click“Properties”→Click“Device Manager”. Look under Ports (COM & LPT) or other device, a yellow exclamation mark means that the CP2102 driver installation failed.

![](media/9af2e34bf9bdd6675bdf5fa8cd291971.png)

It shows that the driver for CP2102 was not installed sucessfully with a yellow mark. Double-click![](media/a2455b26773cb8d6cb3fccc605ea4dd7.png), and then click “**Update drive...**” to update the driver.

![](media/a122cd6fef74eb5c0c7fe16fac2fed59.png)

Click “**Browse my computer for drivers**”，and find the Arduino software we installed or downloaded.

![](media/a02d3e643231cfe267d4debf0ef258c4.png)

There is a **drivers** folder in Arduino software installed package（![](media/aae89b3213589edf1c320d5502489820.png)), open driver folder and you can see the driver of CP210X series chips.

Click“**Browse...**”, then find the drivers folder, or you could enter“driver”to search in rectangular box, then click“**Next**”.

![](media/eb6ca318005b5c570ad4fbef73024351.png)

After a while, the driver is installed successfully.

![](media/4f2af46602a5ef73985914170911c519.png)

Open the computer device Manager again, you can see that the CP2102 driver has been successfully installed, and find the yellow exclamation mark disappear.

![](media/af2324b73308f1796b8b7c9dc14878e7.png)

### 1.3. Install the ESP32 on Arduino IDE：

The installation process for ESP32 is almost the same as that for ESP8266. To install ESP32 on an Arduino IDE, follow these steps：  Note：you need to download Arduino IDE 1.8.5 or advanced version to install the ESP32.

(1) Click the icon![](media/4f2de68a91c7f59024aa87a522e36ab3.png)to open the Arduino IDE.

![](media/8aca9b5378e794375f2c15d3b4e238ba.png)

（2）Click“**File**” →**“Preferences”**，copy the website address：https://dl.espressif.com/dl/package_esp32_index.json in the “**Additional Boards Manager URLs:**”，and then click“**OK**” to save the address.

![](media/a8febbd62268514a30cec4e183b1eaed.png)

![](media/ea68c66041f48b44b4682eb3a0e11e79.png)

（3）First click “**Tools**”→“**Board:**”，and click“**Boards Manager...**”to enter“**Boards Manager**”, enter “**ESP32**” in the box after“**ALL**”, then select the latest version to Install, the installation package is not large, click “**Install**” to Install the plug-in, as shown in the figure below.

![](media/a710d2a8166e3e62d9b48d9b7386e9e4.png)

![](media/9824059733dcbbfb3dff58736923a4a9.png)

After successful installation, click “**Close**” to Close the page。

### 1.4. Arduino IDE Setting:

（1）Click the icon![](media/4f2de68a91c7f59024aa87a522e36ab3.png) to open the Arduino IDE.

![](media/8aca9b5378e794375f2c15d3b4e238ba.png)

（2）When downloading the code to the board, you must select the correct name of Arduino board that matches the board connected to your computer,click“**Tools**”→“**Board:**”. As shown below ;

(Note: we use the ESP32 board in this tutorial; therefore, we select ESP32 Arduino**)**

![](media/78695faae974868fb29c972e89a9d917.png)

![](media/3a3bbc0ce1845aceb35af40aea7c84ca.png)

Set the board type as follows:

![](media/43b6c4d7f639f1e4b7adb017db805ea1.png)

Then select the correct COM port (the corresponding COM port can be seen after the driver is installed successfully).

![](media/94587092f31929ebb9cdbcc5fe1718de.png)

![](media/97ab2e53b87bd0812b2b064405f86196.png)

Before a code was uploaded to the ESP32 mainboard, we have to demonstrate the functionality of each symbol that appeared in the Arduino IDE toolbar.

![](media/1235ef274c17d00db74fca324072ff84.png)

A- Used to verify whether there is any compiling mistakes or not.

B- Used to upload the sketch to your Arduino board.

C- Used to create shortcut window of a new sketch.

D- Used to directly open an example sketch.

E- Used to save the sketch.

F- Used to send the serial data received from board to the serial monitor.

## Mac System:

![](media/a6fc83596009c574d8e29ef383748549.png)

### 2.1.Download and install the Arduino IDE:

![](media/5d58d3cf67b308423ddb9f286f6cb697.png)

### 2.2.How to install the CP2102 driver：

（**Note：** If you have installed the driver, just skip it）

（1）Connect the ESP32 mainboard to your MacOS computer using a USB cable and open Arduino IDE.

![image-20231108104251634](./media/image-20231108104251634.png)

Click “**Tools”**→”**Board: ESP32 Dev Module** ”and **“/dev/cu.usbserial-0001”**.

![](media/00d823dbf27e569a2ba23277b1e15a41.jpeg)

Click ![](media/9c9158a5d49baa740ea2f0048f655017.png) to upload code.

**Note:** If code is uploaded unsuccessfully, you need to install driver of CP2102, please continue to follow the instructions as below:

（2）Download the driver of CP2102：[Download CP2102 Driver](CP2102-Driver-File-MAC.zip)

（3）Click to download the MacOS version, as shown below.

![](media/c09e7c279a858574756d1192b3a995aa.png)

（4）Unzip the downloaded package.

![](media/6870a714ddd11015dc43b1d5743e0666.jpeg)

（5）Open folder and double-click“**SiLabsUSBDriverDisk.dmg**” file.

![](media/61ae3e706a1c4afa7948d5fb2e797a6d.png)

You will view the following files as follows:

![](media/3f1afe9499f6d852492cfb9d6b11e9ab.jpeg)

（6）Double-click**“Install CP210x VCP Driver”,** check“**Don’t warn me when opening application on this disk image**”and click“**Open**”.

![](media/14f6ebb088e654abc2f0149645e34ed1.png)

（7）Click“**Continue**”.

![](media/b1cb125dccf6470ebe255f8f65b902eb.jpeg)

（8）Click "**Agree**" and then click "**Continue**".

![](media/865dcc76cb7f58854b56f1020233f05e.jpeg)

（9）Click “**Continue**” and enter your user password.

![](media/1ef6d65b61ad7c6e0a3989ba59de74d5.jpeg)

![](media/29bbca3360d806164717733460574356.png)

10. Select “**Open Security Preferences**”.

![](media/ca6bc6e536202f07a53c09201a0996ff.png)

（11）Click the lock to unlock security & privacy preference, enter your user password to authorize, and then click“**unlock**”.

![](media/cb6be428257143635fc4f729487549c5.jpeg)

![](media/e8f637a3a9510aa8f90c65820d4d1cd8.jpeg)

（12）See the lock has been opened, click“**Allow**”.

![](media/250a1cbb7f93fc2a572944bea9fe5494.jpeg)

（13）Back to installation page, and wait to install.

![](media/0da6d0d4296d6e3de0b30dfd3c615265.jpeg)

（14）Successfully installed.

![](media/7cca827fe946096f228797dadce10661.jpeg)

（15）Open arduinoIDE，click“**Tools**”, select Board“**ESP32 Dev Module**” and port“**/dev/cu.usbserial-0001**”.

![](media/00d823dbf27e569a2ba23277b1e15a41.jpeg)

（16）Click![](media/b7c913eaa4dcea1bc326dd7a7b5a2af6.png) to upload code and show **Done uploading**”.

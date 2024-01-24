---
title: Using the Windows App Certification Kit
description: To give your desktop app the best chance of getting certified, validate and test it on your computer before you submit it for certification and listing in the Windows Store.
ms.assetid: 8B460B84-0997-4987-9B66-90F9C6D88D83
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Using the Windows App Certification Kit

To give your desktop app the best chance of getting certified, validate and test it on your computer before you submit it for certification and listing in the Windows Store. To certify your app, you need to install and run the [Windows App Certification Kit](/previous-versions//mt637081(v=vs.85)). For details on specific tests within the kit, refer to [Windows App Certification Kit tests](windows-app-certification-kit-tests.md).

For a high level look at the certification process, and where the use of this tool fits in, see [Certify your desktop app](windows-certification-portal.md).

The current release of Windows ACK is available in 14 languages (Czech, English, French, German, Italian, Japanese, Korean, Polish, Portuguese (Brazil), Russian, Simplified Chinese, Spanish, Traditional Chinese, and Turkish).

## Prerequisites

Before you install the Windows ACK, you need to install and run the operating system.

1. Install and run the operating system you're developing apps for.

-   If you're developing apps for Windows 7, you can install and run Windows 7, Windows 8, or Windows 8.1.
-   If you're developing a Windows 8 desktop app or Windows 8 desktop device app, you can install and run Windows 8 or Windows 8.1.
-   If you're developing a Windows 8.1 desktop app or Windows 8 desktop device app, install Windows 8.1.

2. Install the [Windows App Certification Kit 3.3](/previous-versions//mt637081(v=vs.85)), which is included in the Windows Software Development Kit (SDK) for Windows 8.1.

**Note:** When you install Windows App Certification Kit 3.3 or higher on your PC, you replace any previously installed version of the kit.

## Instructions to run Windows App Certification Kit 3.3

**Validate your desktop app by using the Windows App Certification Kit 3.3 interactively**

1.  From the Start menu, search for Windows App Cert Kit.
2.  From the Windows App Certification Kit, click the test validation category you want to run. If you’re validating a desktop app, select **Validate Desktop app**.
3.  In the next screen, browse to the setup file of the desktop app you want to validate.
    -   **Note:** You can use the [command line steps](#commandlinesteps) to include options or an installation switch, if necessary.
4.  Indicate the app usage type, and then click **Next**. The Windows App Certification Kit starts installing the desktop app using the setup files so it can validate the installation.
5.  If you're asked to reboot the system to complete setup, choose **No**. If your app needs to install several components or external dependencies, carefully select the name for your app. The name you choose here is the name your app is given if it gets listed in the Windows Store. When validation is complete, save the report with the name you gave your app in Step 6. The Windows App Certification Kit creates an XML report file and saves it.
6.  Navigate to the folder where you saved the report and open it to view the results of the test. If your test failed and you’re eligible for a waiver, the info you need to submit is listed here. You must submit a detailed description for each possible waiver request.

**Validate your Windows desktop app by using the Windows App Certification Kit 3.3 from a command line**

1.  Navigate to the folder where you saved the report and open it to view the results of the test. Failed tests with a possible waiver request are listed here. You must submit a detailed description for each possible waiver request.
2.  From the folder that contains the Windows App Certification Kit, enter these commands in this order:

    -   <span id="commandLineSteps"></span><span id="commandlinesteps"></span><span id="COMMANDLINESTEPS"></span>`appcert.exe reset`
    -   `appcert test -apptype desktop -setuppath d:\cdrom\setup.exe  -appusage peruser -reportoutputpath [report file name]`

    where: `[report file name]`is the fully qualified file name of the XML file that the kit will create to contain the test report.

3.  After the test completes, open the report file named \[report file name\] and view the test results.

    **Note:** For more information about the Windows App Certification Kit command line, enter the command appcert.exe /?

    The Windows App Certification Kit must be run in the context of an active user session but you can't launch apps in a non-interactive session. The way the kit handles tokens for running tests with or without administrative privileges depends on this user session context as well. The kit can be run from a service, but the service must be able to spawn the kit process in an active user session.

**Use the Windows App Certification Kit to validate your Windows 7 apps**

-   The Windows App Certification Kit replaced the Windows Software Logo Kit. If you want the Windows 7 logo for your app, use the Windows App Certification Kit for your validation testing and report. The kit can detect which operating system it's running on and automatically launches for Windows 7 apps. Follow the same process for validating Windows 7 apps.

**Submit for certification**

-   After your app is validated, you're ready to submit it for certification [through the portal submission process](https://www.microsoft.com/?ref=go).

## Reference Documents

-   [Certification requirements for Windows desktop apps](/windows/desktop/win_cert/certification-requirements-for-windows-desktop-apps)
-   [Windows Store onboarding for desktop apps](/previous-versions//dn322034(v=vs.85))
-   [Windows 7 desktop app certification requirements](https://techcommunity.microsoft.com/t5/windows-hardware-certification/bg-p/WindowsHardwareCertification)

## Windows App Certification Kit tests

We’ve changed the kit to make the [Windows ACK tests](windows-app-certification-kit-tests.md) easier to use. The kit now has:

-   A new simplified user interface
-   Improved multi-user test, which no longer requires that you set up a second user account

 

 

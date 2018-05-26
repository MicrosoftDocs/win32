---
title: How to Configure Security Settings
description: You will need to configure the security settings for Windows Image Acquisition (WIA) before you can successfully create a DeviceManager object on an Active Server Pages (ASP) page.
ms.assetid: fc7b3413-cbb4-4b9b-9935-181ea890c413
keywords:
- Windows Image Acquisition (WIA),security settings
- WIA (Windows Image Acquisition),security settings
- Windows Image Acquisition Automation Layer,security settings
- WIA Automation Layer,security settings
- Image Acquisition Automation Layer,security settings
- Windows Image Acquisition (WIA),Microsoft Management Console (MMC)
- WIA (Windows Image Acquisition),Microsoft Management Console (MMC)
- Windows Image Acquisition Automation Layer,Microsoft Management Console (MMC)
- WIA Automation Layer,Microsoft Management Console (MMC)
- Image Acquisition Automation Layer,Microsoft Management Console (MMC)
- Windows Image Acquisition (WIA),Component Services snap-in
- WIA (Windows Image Acquisition),Component Services snap-in
- Windows Image Acquisition Automation Layer,Component Services snap-in
- WIA Automation Layer,Component Services snap-in
- Image Acquisition Automation Layer,Component Services snap-in
- Windows Image Acquisition (WIA),WIA Device Manager
- WIA (Windows Image Acquisition),WIA Device Manager
- Windows Image Acquisition Automation Layer,WIA Device Manager
- WIA Automation Layer,WIA Device Manager
- Image Acquisition Automation Layer,WIA Device Manager
- Windows Image Acquisition (WIA),WIA Logger
- WIA (Windows Image Acquisition),WIA Logger
- Windows Image Acquisition Automation Layer,WIA Logger
- WIA Automation Layer,WIA Logger
- Image Acquisition Automation Layer,WIA Logger
- WIA Device Manager
- WIA Logger
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# How to Configure Security Settings

You will need to configure the security settings for Windows Image Acquisition (WIA) before you can successfully create a [**DeviceManager**](-wiaaut-devicemanager.md) object on an Active Server Pages (ASP) page. This configuration is necessary because the script in an ASP page runs in the context of the IUSR\_MACHINENAME or IWAM\_MACHINENAME account (where MACHINENAME is the uppercase computer name).

This topic outlines the necessary steps to configure WIA security settings.

-   [Run the Microsoft Management Console](#run-the-microsoft-management-console)
-   [Add the Component Services Snap-in](#add-the-component-services-snap-in)
-   [Adjust Security Settings for WIA Device Manager](#adjust-security-settings-for-wia-device-manager)
-   [Adjust Security Settings for WIA Logger](#adjust-security-settings-for-wia-logger)
-   [Reboot](#reboot)

## Run the Microsoft Management Console

Click **Run** on the **Start menu**, type `mmc` and click **OK**.

![run dialog box](images/ss-wiaaut-s01.gif)

## Add the Component Services Snap-in

Perform the following steps to add the **Component Services Snap-in**.

1.  From the **File** menu, select **Add/Remove Snap-in**.

    ![add/remove snap](images/ss-wiaaut-s02.gif)

2.  On the **Standalone** tab, click **Add**.

    ![add/remove snap-in dialog box](images/ss-wiaaut-s03.gif)

3.  Select **Component Services**, click **Add**, click **Close**, and then click **OK**.

    ![add standalone snap-in dialog box](images/ss-wiaaut-s04.gif)

## Adjust Security Settings for WIA Device Manager

1.  In the tree-view control, select **Console Root**, click **Component Services**, click **Computers**, click **My Computer**, and then click **DCOM Config**. Right-click on the **WIA Device Manager** icon and select **Properties**.

    ![dcom config](images/ss-wiaaut-s05.gif)

2.  Add Launch Permissions for the IUSR\_WIAAUT and IWAM\_WIAAUT accounts as follows: On the **Security** tab in the **Launch Permissions** section, click **Customize** and click **Edit**.

    ![wia device manager properties](images/ss-wiaaut-s07.gif)

    1.  Add the IUSR\_WIAAUT account (if it is not already present) and select **Allow** next to **Launch Permission**.

        ![allow launch permission for iusr\-wiaaut](images/ss-wiaaut-s09.gif)

    2.  Add the IWAM\_WIAAUT account (if it is not already present) and select **Allow** next to **Launch Permission**.

        ![allow launch permission for iwam\-wiaaut](images/ss-wiaaut-s10.gif)

3.  Add Access Permissions for the previous two accounts as follows: On the **Security** tab, in the **Access Permissions** section, click **Customize** and click **Edit**.

    ![customize access permissions](images/ss-wiaaut-s08.gif)

    1.  Add the IUSR\_WIAAUT account (if it is not already present) and select **Allow** next to **Access Permission**.

        ![allow access permission for iusr\-wiaaut](images/ss-wiaaut-s11.gif)

    2.  Add the IWAM\_WIAAUT account (if it is not already present) and select **Allow** next to **Access Permission**.

        ![allow access permission for iwam\-wiaaut](images/ss-wiaaut-s12.gif)

## Adjust Security Settings for WIA Logger

Repeat the previous steps for the WIA Logger component and add the IUSR\_WIAAUT and IWAM\_WIAAUT accounts for both launch and access permissions.

![wia logger dcom config](images/ss-wiaaut-s06.gif)

## Reboot

Restart your computer. If you know how to restart the WIA Device Manager service, you could do that instead.

 

 





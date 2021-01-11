---
description: Contains information on the programming interface for the Wireless Zero Configuration service on Windows XP and Windows Server 2003.
ms.assetid: cd9e8fc0-0a65-4654-95aa-201751183521
title: Wireless Zero Configuration Reference
ms.topic: article
ms.date: 05/31/2018
---

# Wireless Zero Configuration Reference

\[The Wireless Zero Configuration programming interface is no longer supported as of Windows Vista and Windows Server 2008. Instead, use the [Native Wifi API](native-wifi-reference.md), which provides similar functionality. For more information, see [About the Native Wifi API](about-the-native-wifi-api.md).\]

This section contains information on the programming interface for the Wireless Zero Configuration service on Windows XP and Windows Server 2003. The topics include:

-   [Wireless Zero Configuration Functions](wireless-zero-configuration-functions.md)
-   [Wireless Zero Configuration Structures](wireless-zero-configuration-structures.md)

Wireless Zero Configuration is a Windows service on Windows XP and Windows Server 2003 that is used to configure and manage wireless network connections on a wireless adapter. The service name for Wireless Zero Configuration is WZCSVC. On Windows XP, the display name for the WZCSVC service is Wireless Zero Configuration. On Windows Server 2003, the display name for the WZCSVC service is Wireless Configuration.

The Wireless Zero Configuration service is normally started at boot time. The programming interface for the Wireless Zero Configuration service can be used only if the Wireless Zero Configuration service has been started. If the Wireless Zero Configuration service is not started, then the Wireless Zero Configuration functions will return an error.

To enable the Wireless Zero Configuration service so it starts up automatically, go to the **Start** button. Select the **Settings** option and then select **Control Panel**. If you are using the Windows XP view, select the **Performance and Maintenance** category and then select **Administrative Tools**. If you are using the Classic View, then select **Administrative Tools**. Click the **Services** icon in the left pane. Click the Wireless Zero Configuration icon in the right pane and change the **Startup Type** dropbox to **Automatic**. This setting will set the service to start automatically at boot time. Then click the **Start** button to start the Wireless Zero Wireless Zero Configuration service and click the **OK** button.

The Wireless Zero Configuration can also be started and stopped from a command prompt. To start the Wireless Zero Configuration, run the following command:

**net start wzcsvc**

To stop the Wireless Zero Configuration, run the following command:

**net stop wzcsvc**

 

 




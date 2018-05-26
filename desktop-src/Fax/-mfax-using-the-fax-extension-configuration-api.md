---
Description: The Fax Service Extension Configuration API provides persistent, secure storage for fax extension configuration data.
ms.assetid: dff22593-6909-40a3-995a-4c4582c11ce1
title: Using the Fax Extension Configuration API
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using the Fax Extension Configuration API

The Fax Service Extension Configuration API provides persistent, secure storage for fax extension configuration data. Using the configuration persistence mechanism, fax extension DLLs such as fax service providers (FSPs) and routing extensions can retrieve and set fax device configuration data in a location-independent manner, and can register for and receive notifications from the fax service about changes in device configuration data.

The ability to persistently store configuration data in a location-independent manner solves problems that can arise in many situations. For example, if a Microsoft Management Console (MMC) snap-in executes remotely, it cannot configure properties for the fax extension because the snap-in does not have access to the configuration data that resides on the remote server. An example of a future problem could be if the storage location of configuration data changes. Fax service extensions that rely on a static storage location, such as the system registry, would no longer function.

When you use the configuration persistence mechanism, your configuration data has the same security as the fax server's own configuration data. This ensures that only users who have permission to configure the server will be able to modify the extension's configuration data.

If you plan to implement this feature, you must export the [**FaxExtInitializeConfig**](/windows/previous-versions/FaxExt/nf-faxext-faxextinitializeconfig?branch=master) function. When you export **FaxExtInitializeConfig**, the fax service calls the function during service startup, when the service loads the fax extension DLL. Except in the case of a virtual FSP, the fax service calls **FaxExtInitializeConfig** before it calls any other fax extension initialization function. In the case of a virtual FSP, the fax service calls [**FaxDevVirtualDeviceCreation**](/windows/previous-versions/FaxDev/nf-faxdev-faxdevvirtualdevicecreation?branch=master) before it calls **FaxExtInitializeConfig**. The fax service passes the pointers to five fax server callback functions as parameters to **FaxExtInitializeConfig**.

This section includes the following topics.

-   [Associating Data with a Fax Device](-mfax-associating-data-with-a-fax-device.md)
-   [Fax Service and Configuration Extension Interaction](-mfax-fax-service-and-configuration-extension-interaction.md)
-   [Device Identifier Types](-mfax-device-identifier-types.md)
-   [Storing Global Configuration Data](-mfax-storing-global-configuration-data.md)
-   [Accessing Extension Configuration Data](-mfax-accessing-extension-configuration-data.md)

 

 




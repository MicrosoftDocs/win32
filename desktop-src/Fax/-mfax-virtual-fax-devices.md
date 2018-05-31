---
Description: A virtual fax device is one that appears to exist to a user, but in fact has no corresponding Telephony Application Programming Interface (TAPI) line device associated with it on a fax server.
ms.assetid: 873481e5-abf3-401d-9d45-5ee04eabe4ac
title: Virtual Fax Devices
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Virtual Fax Devices

A virtual fax device is one that appears to exist to a user, but in fact has no corresponding Telephony Application Programming Interface (TAPI) line device associated with it on a fax server. A fax service provider (FSP) that supports fax transmissions over the Internet is an example of a provider that uses a virtual fax device. In this example, a physical fax device does not exist, only a connection to the Internet.

An FSP can present multiple virtual fax devices to the fax service if the provider exports the [**FaxDevVirtualDeviceCreation**](-mfax-faxdevvirtualdevicecreation.md) function. The fax service checks the FSP DLL during initialization for **FaxDevVirtualDeviceCreation**. If the function is present, the fax service allows the user to send and receive faxes using the virtual device. For more information, see [Using a Virtual Device to Transmit a Fax](-mfax-using-a-virtual-device-to-transmit-a-fax.md).

 

 




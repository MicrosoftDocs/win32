---
Description: MTP/Bluetooth Connection Interfaces
ms.assetid: 7bbd5fe3-85f1-4f0a-9d3e-22746bd23aae
title: MTP/Bluetooth Connection Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MTP/Bluetooth Connection Interfaces

The following interfaces allow applications to enumerate and connect only to devices that support the Media Transfer Protocol (MTP) over Bluetooth (MTP/Bluetooth). The WPD driver-, collection-, and client-interfaces are not restricted to the MTP/ Bluetooth protocol.



| Interface                                                              | Description                                                                                                         |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**IConnectionRequestCallback**](iconnectionrequestcallback.md)       | Defines a single callback method that applications use to receive notification of completed and cancelled requests. |
| [**IEnumPortableDeviceConnectors**](ienumportabledeviceconnectors.md) | Enumerates **IPortableDeviceConnector** interfaces.                                                                 |
| [**IPortableDeviceConnector**](/windows/win32/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector?branch=master)           | Supports methods that applications call to establish connections to MTP Bluetooth devices.                          |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




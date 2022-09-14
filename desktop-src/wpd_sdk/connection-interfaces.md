---
description: MTP/Bluetooth Connection Interfaces
ms.assetid: 7bbd5fe3-85f1-4f0a-9d3e-22746bd23aae
title: MTP/Bluetooth Connection Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# MTP/Bluetooth Connection Interfaces

The following interfaces allow applications to enumerate and connect only to devices that support the Media Transfer Protocol (MTP) over Bluetooth (MTP/Bluetooth). The WPD driver-, collection-, and client-interfaces are not restricted to the MTP/ Bluetooth protocol.



| Interface                                                              | Description                                                                                                         |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [**IConnectionRequestCallback**](iconnectionrequestcallback.md)       | Defines a single callback method that applications use to receive notification of completed and cancelled requests. |
| [**IEnumPortableDeviceConnectors**](ienumportabledeviceconnectors.md) | Enumerates **IPortableDeviceConnector** interfaces.                                                                 |
| [**IPortableDeviceConnector**](/windows/desktop/api/portabledeviceconnectapi/nn-portabledeviceconnectapi-iportabledeviceconnector)           | Supports methods that applications call to establish connections to MTP Bluetooth devices.                          |



 

## Related topics

<dl> <dt>

[**Programming Reference**](programming-reference.md)
</dt> </dl>

 

 




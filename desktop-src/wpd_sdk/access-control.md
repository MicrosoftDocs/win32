---
description: Access Control
ms.assetid: d17137f9-b206-4ced-82e5-96a7d927c89b
title: Access Control (WPD API)
ms.topic: article
ms.date: 05/31/2018
---

# Access Control (WPD API)

The Windows Driver Model (WDM) supports restricting device access via Access Control Lists (ACLs) on the Plug and Play (PnP) Device Nodes. This means that vendors and network administrators can restrict access to any device type. When an application opens a handle to a driver by calling [**IPortableDevice::Open**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-open), the driver's I/O Manager verifies whether the given user has the required access, and similarly does access checks when IOCTLs are sent to the driver from that handle.

For example, a network administrator could restrict Guest users to read-only access for portable devices, while they could grant Authenticated users read/write access. In this case, it implies that if a Guest issued a WPD command that required read/write access (such as Delete Object); it would fail with Access Denied, whereas if an Authenticated user issued the same command, it would succeed.

The Group Policy entries for controlling access to removable storage and portable devices is actually nothing more than an easy way for Administrators to apply PnP device node ACLs to a whole class of devices at a time (for example, applying the "Deny Write Access to Portable Devices" Group Policy would adjust the ACLs of all WPD devices to deny write access).

## I/O Control Codes in WPD

WPD applications communicate with drivers by opening device handles and sending I/O Control Codes (IOCTLs). These IOCTLs consist of four sections:

1.  Device Type
2.  Function Code
3.  Buffer Method
4.  Access Type

The fourth section, the Access Type, specifies the specific access requirement for the given command. The driver's I/O manager uses this data to perform the Access Control List (ACL) check.

So if an IOCTL were defined as:


```C++
    #define MY_READ_IOCTL CTL_CODE(FILE_DEVICE_X, CONTROL_FUNCTION_Y, METHOD_BUFFERED, FILE_READ_ACCESS)
```



The driver's I/O manager would check that the owner of the device handle has read access to the device when this message is sent.

And, if an IOCTL were defined as:


```C++
    #define MY_READWRITE_IOCTL CTL_CODE(FILE_DEVICE_X, CONTROL_FUNCTION_Z, METHOD_BUFFERED, (FILE_READ_ACCESS | FILE_WRITE_ACCESS))
```



The driver's I/O manager would check that the owner of the device handle has read/write access to the device when this message is sent.

## Related topics

<dl> <dt>

[**Application Overview**](application-overview.md)
</dt> <dt>

[**IPortableDevice::Open**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-open)
</dt> <dt>

[**IPortableDevice::SendCommand**](/windows/desktop/api/PortableDeviceApi/nf-portabledeviceapi-iportabledevice-sendcommand)
</dt> </dl>

 

 




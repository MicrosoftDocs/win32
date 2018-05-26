---
title: RedirectDeviceType enumeration
description: Used to specify the type of a device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B6356217-814E-462F-9DBC-F6D3C0CE129F
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- RedirectDeviceType enumeration Remote Desktop Services
topic_type:
- apiref
api_name:
- RedirectDeviceType
api_location:
- MsTscAx.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
---

# RedirectDeviceType enumeration

Used to specify the type of a device.

## Syntax


```C++
typedef enum  { 
  UsbDevice  = 0
} RedirectDeviceType;
```



## Constants

<dl> <dt>

<span id="UsbDevice"></span><span id="usbdevice"></span><span id="USBDEVICE"></span>**UsbDevice**
</dt> <dd>

A USB device.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**AddDeviceByInstanceId**](imsrdpdevicecollection2-adddevicebyinstanceid.md)
</dt> <dt>

[**RedirectNow**](imsrdpdevicecollection2-redirectnow.md)
</dt> </dl>

 

 






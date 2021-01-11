---
description: Retrieves the type of Windows Image Acquisition (WIA) hardware device.
ms.assetid: 5f10bcd1-03a0-4cd9-8886-e1f957312c3b
title: DeviceInfo.Type property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DeviceInfo.Type
api_type: 
- COM
api_location: 
- Wiascr.dll
---

# DeviceInfo.Type property

Retrieves the type of Windows Image Acquisition (WIA) hardware device. Possible values are:

-   DigitalCamera
-   Scanner
-   StreamingVideo
-   Default

This property is read-only.

## Syntax


```JScript
propVal = DeviceInfo.Type
```



## Property value

String that receives the device.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Wiascr.dll (version 4.90 or later)</dt> </dl> |



 

 





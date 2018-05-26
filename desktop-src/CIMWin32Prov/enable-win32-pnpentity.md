---
Description: Enables this Plug and Play device.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8f2096c4-03b4-4005-9b97-0086f2b41080
ms.prod: windows-server-dev
ms.technology:
- cimwin32
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Enable method of the Win32\_PnPEntity class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Enable method of the Win32\_PnPEntity class

Enables this Plug and Play device.

## Syntax


```mof
Uint32 Enable(
  [out] boolean rebootNeeded
);
```



## Parameters

<dl> <dt>

*rebootNeeded* \[out\]
</dt> <dd>

Whether a reboot is needed.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Cimwin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_PnPEntity**](win32-pnpentity.md)
</dt> </dl>

 

 





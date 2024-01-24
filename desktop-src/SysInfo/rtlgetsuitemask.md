---
description: Retrieves a bit mask that identifies the product suites available on the system. If this function is called in an application that runs in the context of a server silo, the suite mask for the server silo is retrieved instead.
ms.assetid: 1D6434FD-D7BD-45F9-B7C3-238890AF9928
title: RtlGetSuiteMask function (Ntddk.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtlGetSuiteMask
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# RtlGetSuiteMask function

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Retrieves a bit mask that identifies the product suites available on the system. If this function is called in an application that runs in the context of a server silo, the suite mask for the server silo is retrieved instead.

## Syntax


```C++
ULONG NTAPI RtlGetSuiteMask(void);
```



## Parameters

This function has no parameters.

## Return value

A bit mask that identifies the product suites available on the system. The bit mask can include the following values.



| Return value                                                                          | Description                                                                                                                                                                                                                                             |
|---------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x00000001</dt> </dl> | Microsoft Small Business Server was once installed on the system, but may have been upgraded to another version of Windows. Refer to the Remarks section for more information about this bit flag.<br/>                                           |
| <dl> <dt>0x00000002</dt> </dl> | Windows 10 Enterprise, Windows 8.1 Enterprise, Windows Server 2008 Enterprise, Windows Server 2003, Enterprise Edition, or Windows 2000 Advanced Server is installed. Refer to the Remarks section for more information about this bit flag.<br/> |
| <dl> <dt>0x00000004</dt> </dl> | Microsoft BackOffice components are installed.<br/>                                                                                                                                                                                               |
| <dl> <dt>0x00000008</dt> </dl> | Communications Server 2003, Communications Server 2005, Communications Server 2007, or Communications Server 2007 R2 is installed.<br/>                                                                                                           |
| <dl> <dt>0x00000010</dt> </dl> | Terminal Services is installed. This value is always set.<br/> If **TerminalServer** is set but **SingleUserTS** is not set, the system is running in application server mode.<br/>                                                         |
| <dl> <dt>0x00000020</dt> </dl> | Microsoft Small Business Server is installed with the restrictive client license in force. Refer to the Remarks section for more information about this bit flag.<br/>                                                                            |
| <dl> <dt>0x00000040</dt> </dl> | Windows XP Embedded is installed.<br/>                                                                                                                                                                                                            |
| <dl> <dt>0x00000080</dt> </dl> | Windows Server 2008 Datacenter, Windows Server 2003, Datacenter Edition, or Windows 2000 Datacenter Server is installed.<br/>                                                                                                                     |
| <dl> <dt>0x00000100</dt> </dl> | Remote Desktop is supported, but only one interactive session is supported. This value is set unless the system is running in application server mode.<br/>                                                                                       |
| <dl> <dt>0x00000200</dt> </dl> | Windows Vista Home Premium, Windows Vista Home Basic, or Windows XP Home Edition is installed.<br/>                                                                                                                                               |
| <dl> <dt>0x00000400</dt> </dl> | Windows Server 2003, Web Edition is installed.<br/>                                                                                                                                                                                               |
| <dl> <dt>0x00002000</dt> </dl> | Windows Storage Server 2003 R2 or Windows Storage Server 2003 is installed.<br/>                                                                                                                                                                  |
| <dl> <dt>0x00004000</dt> </dl> | Windows Server 2003, Compute Cluster Edition is installed.<br/>                                                                                                                                                                                   |
| <dl> <dt>0x00008000</dt> </dl> | Windows Home Server is installed.<br/>                                                                                                                                                                                                            |



 

## Remarks

You should not rely upon only the 0x00000001 flag to determine whether Small Business Server has been installed on the system, as both this flag and the 0x00000020 flag are set when this product suite is installed. If you upgrade this installation to Windows Server, Standard Edition, the 0x00000020 flag will be cleared however, the 0x00000001 flag will remain set. In this case, this indicates that Small Business Server was once installed on this system. If this installation is further upgraded to Windows Server, Enterprise Edition, the 0x00000001 flag will remain set.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Ntddk.h</dt> </dl>   |
| Library<br/>                  | <dl> <dt>Ntdll.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 





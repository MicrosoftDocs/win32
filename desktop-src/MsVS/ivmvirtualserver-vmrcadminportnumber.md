---
title: IVMVirtualServer VMRCAdminPortNumber property
description: The VMRCAdminPortNumber property contains the VMRC administration port number.
ms.assetid: 00dcdd1c-13e8-4427-a180-be62037e2d4d
keywords:
- VMRCAdminPortNumber property Virtual Server
- VMRCAdminPortNumber property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCAdminPortNumber property
- VMRCAdminPortNumber property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCAdminPortNumber property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCAdminPortNumber
- IVMVirtualServer.get_VMRCAdminPortNumber
- IVMVirtualServer.put_VMRCAdminPortNumber
- VMVirtualServer.VMRCAdminPortNumber
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMVirtualServer::VMRCAdminPortNumber property

The **VMRCAdminPortNumber** property contains the VMRC administration port number.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCAdminPortNumber(
  [in]  long vmrcAdminPortNumber
);

HRESULT get_VMRCAdminPortNumber(
  [out] long *vmrcAdminPortNumber
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMVirtualServer.VMRCAdminPortNumber( _
  ByRef vmrcAdminPortNumber, _
  ByVal vmrcAdminPortNumber _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The TCP/IP port number for VMRC administration. The value must be within the range of 1 and 65535.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                         |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                        |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *vmrcAdminPortNumber* parameter is **NULL**.<br/>     |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *vmrcAdminPortNumber* parameter is out of range.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                        |



## Examples

The following example displays the **VMRCAdminPortNumber** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC admin port number: " & objVS.VMRCAdminPortNumber
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 






---
title: IVMHostInfo HostDrives property
description: The HostDrives property contains an array of host hard disk drive names.
ms.assetid: b8a2cbbf-5569-4f15-adbe-ce77051f10f1
keywords:
- HostDrives property Virtual Server
- HostDrives property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , HostDrives property
- HostDrives property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , HostDrives property
topic_type:
- apiref
api_name:
- IVMHostInfo.HostDrives
- IVMHostInfo.get_HostDrives
- VMHostInfo.HostDrives
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

# IVMHostInfo::HostDrives property

The **HostDrives** property contains an array of host hard disk drive names.

This property is read-only.

## Syntax


```C++
HRESULT get_HostDrives(
  [out] VARIANT *hostDrives
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
<td><pre><code>VMHostInfo.HostDrives( _
  ByRef hostDrives _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains an array of host drive names which can be passed to [**VMVirtualServer.CreateHostDriveVirtualHardDisk**](ivmvirtualserver-createhostdrivevirtualharddisk.md).

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 






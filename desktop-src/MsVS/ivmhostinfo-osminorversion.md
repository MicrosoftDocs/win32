---
title: IVMHostInfo OSMinorVersion property
description: The OSMinorVersion property contains the minor operating system release version currently running on the host machine.
ms.assetid: ce1a5d92-a007-4ffe-907a-c8ab548a75c4
keywords:
- OSMinorVersion property Virtual Server
- OSMinorVersion property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , OSMinorVersion property
- OSMinorVersion property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , OSMinorVersion property
topic_type:
- apiref
api_name:
- IVMHostInfo.OSMinorVersion
- IVMHostInfo.get_OSMinorVersion
- VMHostInfo.OSMinorVersion
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMHostInfo::OSMinorVersion property

The **OSMinorVersion** property contains the minor operating system release version currently running on the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_OSMinorVersion(
  [out] long *osMinorVersion
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
<td><pre><code>VMHostInfo.OSMinorVersion( _
  ByRef osMinorVersion _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The minor operating system release version currently running on the host machine.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
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

 

 






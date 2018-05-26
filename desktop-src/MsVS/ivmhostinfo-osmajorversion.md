---
title: IVMHostInfo OSMajorVersion property
description: The OSMajorVersion property contains the major operating system release version currently running on the host machine.
ms.assetid: f11c91f9-fa71-40b3-9c7a-bd9b96f052eb
keywords:
- OSMajorVersion property Virtual Server
- OSMajorVersion property Virtual Server , IVMHostInfo interface
- IVMHostInfo interface Virtual Server , OSMajorVersion property
- OSMajorVersion property Virtual Server , VMHostInfo interface
- VMHostInfo interface Virtual Server , OSMajorVersion property
topic_type:
- apiref
api_name:
- IVMHostInfo.OSMajorVersion
- IVMHostInfo.get_OSMajorVersion
- VMHostInfo.OSMajorVersion
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

# IVMHostInfo::OSMajorVersion property

The **OSMajorVersion** property contains the major operating system release version currently running on the host machine.

This property is read-only.

## Syntax


```C++
HRESULT get_OSMajorVersion(
  [out] long *osMajorVersion
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
<td><pre><code>VMHostInfo.OSMajorVersion( _
  ByRef osMajorVersion _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The major operating system release version currently running on the host machine.

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

 

 






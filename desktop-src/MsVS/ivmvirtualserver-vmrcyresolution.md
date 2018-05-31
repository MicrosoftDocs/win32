---
title: IVMVirtualServer VMRCYResolution property
description: The VMRCYResolution property contains the vertical resolution used for server administration.
ms.assetid: 1c7282a4-cce7-4844-a013-1c43d74d4ced
keywords:
- VMRCYResolution property Virtual Server
- VMRCYResolution property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VMRCYResolution property
- VMRCYResolution property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VMRCYResolution property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VMRCYResolution
- IVMVirtualServer.get_VMRCYResolution
- IVMVirtualServer.put_VMRCYResolution
- VMVirtualServer.VMRCYResolution
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

# IVMVirtualServer::VMRCYResolution property

The **VMRCYResolution** property contains the vertical resolution used for server administration.

This property is read/write.

## Syntax


```C++
HRESULT put_VMRCYResolution(
  [in]  long vmrcYResolution
);

HRESULT get_VMRCYResolution(
  [out] long *vmrcYResolution
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
<td><pre><code>VMVirtualServer.VMRCYResolution( _
  ByRef vmrcYResolution, _
  ByVal vmrcYResolution _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The vertical resolution used for server administration.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                 |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *vmrcYResolution* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                |



## Examples

The following example displays the **VMRCYResolution** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Wscript.Echo "VMRC Y-Resolution: " & objVS.VMRCYResolution
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

 

 






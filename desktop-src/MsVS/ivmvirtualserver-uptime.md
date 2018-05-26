---
title: IVMVirtualServer UpTime property
description: The UpTime property contains the number of seconds the Virtual Server application has been running.
ms.assetid: a4824b93-02cb-4e3a-8b51-d3e6de942b1e
keywords:
- UpTime property Virtual Server
- UpTime property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , UpTime property
- UpTime property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , UpTime property
topic_type:
- apiref
api_name:
- IVMVirtualServer.UpTime
- IVMVirtualServer.get_UpTime
- VMVirtualServer.UpTime
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

# IVMVirtualServer::UpTime property

The **UpTime** property contains the number of seconds the Virtual Server application has been running.

This property is read-only.

## Syntax


```C++
HRESULT get_UpTime(
  [out] long *secondsAlive
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
<td><pre><code>VMVirtualServer.UpTime( _
  ByRef secondsAlive _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of seconds the Virtual Server application has been running.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *secondsAlive* is **NULL**.<br/>   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example displays the **UpTime** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Uptime: " & objVS.Uptime
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

 

 






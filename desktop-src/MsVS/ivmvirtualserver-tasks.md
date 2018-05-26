---
title: IVMVirtualServer Tasks property
description: The Tasks property contains a collection of tasks.
ms.assetid: fb6ec307-2721-4934-bfdc-06dc648132e0
keywords:
- Tasks property Virtual Server
- Tasks property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , Tasks property
- Tasks property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , Tasks property
topic_type:
- apiref
api_name:
- IVMVirtualServer.Tasks
- IVMVirtualServer.get_Tasks
- VMVirtualServer.Tasks
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

# IVMVirtualServer::Tasks property

The **Tasks** property contains a collection of tasks.

This property is read-only.

## Syntax


```C++
HRESULT get_Tasks(
  [out] IVMTaskCollection **taskCollection
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
<td><pre><code>VMVirtualServer.Tasks( _
  ByRef taskCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMTaskCollection**](ivmtaskcollection.md) object associated with Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *taskCollection* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>               |



## Examples

The following example displays properties of the **Tasks** object associated with the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Set objTColl = objVS.Tasks
If objTColl.Count = 0 Then
  Wscript.Echo "Current tasks: [none]"
Else
  Wscript.Echo "Current tasks: "
  For Each objT in objTColl
    Wscript.Echo "    Task: " & objT.ID & ":" & objT.Description
  Next
End If
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

 

 






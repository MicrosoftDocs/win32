---
title: IVMVirtualServer VirtualNetworks property
description: The VirtualNetworks property contains a collection of IVMVirtualNetwork objects.
ms.assetid: facaf325-7588-40b1-b35b-f52e0f9a12c0
keywords:
- VirtualNetworks property Virtual Server
- VirtualNetworks property Virtual Server , IVMVirtualServer interface
- IVMVirtualServer interface Virtual Server , VirtualNetworks property
- VirtualNetworks property Virtual Server , VMVirtualServer class
- VMVirtualServer class Virtual Server , VirtualNetworks property
topic_type:
- apiref
api_name:
- IVMVirtualServer.VirtualNetworks
- IVMVirtualServer.get_VirtualNetworks
- VMVirtualServer.VirtualNetworks
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

# IVMVirtualServer::VirtualNetworks property

The **VirtualNetworks** property contains a collection of [**IVMVirtualNetwork**](ivmvirtualnetwork.md) objects.

This property is read-only.

## Syntax


```C++
HRESULT get_VirtualNetworks(
  [out] IVMVirtualNetworkCollection **virtualNetworkCollection
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
<td><pre><code>VMVirtualServer.VirtualNetworks( _
  ByRef virtualNetworkCollection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md) object associated with Virtual Server.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                            |
|-----------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>           |
| <dl> <dt>E\_POINTER</dt> </dl>         | *virtualNetworkCollection* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>           |



## Examples

The following example displays properties of the [**VMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md) object in the **VirtualNetworks** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")
Wscript.Echo "Name: " & objVS.Name

Set objVNColl = objVS.VirtualNetworks
If objVNColl.Count = 0 Then
  Wscript.Echo "Virtual networks: [none]"
Else
  Wscript.Echo "Virtual networks: " & objVNColl.Count
  For Each objVN in objVNColl
    Wscript.Echo "    Name: " & objVN.Name
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

 

 






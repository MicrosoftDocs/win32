---
title: IVMVirtualServer MaximumNumberOfIDEBuses property
description: The MaximumNumberOfIDEBuses property contains the maximum number of buses allowed for IDE.
ms.assetid: '02a680f6-ce3f-44a4-ab5d-05fc3865a3bb'
keywords: ["MaximumNumberOfIDEBuses property Virtual Server", "MaximumNumberOfIDEBuses property Virtual Server , IVMVirtualServer interface", "IVMVirtualServer interface Virtual Server , MaximumNumberOfIDEBuses property", "MaximumNumberOfIDEBuses property Virtual Server , VMVirtualServer class", "VMVirtualServer class Virtual Server , MaximumNumberOfIDEBuses property"]
topic_type:
- apiref
api_name:
- IVMVirtualServer.MaximumNumberOfIDEBuses
- IVMVirtualServer.get_MaximumNumberOfIDEBuses
- VMVirtualServer.MaximumNumberOfIDEBuses
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualServer::MaximumNumberOfIDEBuses property

The **MaximumNumberOfIDEBuses** property contains the maximum number of buses allowed for IDE.

This property is read-only.

## Syntax


```C++
HRESULT get_MaximumNumberOfIDEBuses(
  [out] long *maxNumBuses
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
<td><pre><code>VMVirtualServer.MaximumNumberOfIDEBuses( _
  ByRef maxNumBuses _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The maximum number of buses allowed for IDE.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | *maxNumBuses* is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Examples

The following example displays the **MaximumNumberOfIDEBuses** property value of the [**VMVirtualServer**](ivmvirtualserver.md) object.


```VB
Set objVS = CreateObject("VirtualServer.Application")

Wscript.Echo "Name: " & objVS.Name
Wscript.Echo "Maximum number of IDE buses: " & objVS.MaximumNumberOfIDEBuses
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualServer**](ivmvirtualserver.md)
</dt> </dl>

 

 






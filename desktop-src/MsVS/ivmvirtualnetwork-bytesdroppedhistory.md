---
title: IVMVirtualNetwork BytesDroppedHistory property
description: The BytesDroppedHistory property contains the recent number of bytes dropped by this virtual network (as an array of number of bytes).
ms.assetid: 4c673f8d-26b8-420f-b1dd-6348b9c903ec
keywords:
- BytesDroppedHistory property Virtual Server
- BytesDroppedHistory property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , BytesDroppedHistory property
- BytesDroppedHistory property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , BytesDroppedHistory property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.BytesDroppedHistory
- IVMVirtualNetwork.get_BytesDroppedHistory
- VMVirtualNetwork.BytesDroppedHistory
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

# IVMVirtualNetwork::BytesDroppedHistory property

The **BytesDroppedHistory** property contains the recent number of bytes dropped by this virtual network (as an array of number of bytes).

This property is read-only.

## Syntax


```C++
HRESULT get_BytesDroppedHistory(
  [out] VARIANT *bytesDropped
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
<td><pre><code>VMVirtualNetwork.BytesDroppedHistory( _
  ByRef bytesDropped _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The recent number of bytes dropped by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of bytes dropped at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                              |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>             |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *bytesDropped* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>             |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 






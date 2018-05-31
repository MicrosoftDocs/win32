---
title: IVMVirtualNetwork BytesSentHistory property
description: The BytesSentHistory property contains the recent number of bytes sent per second by this virtual network (as an array of number of bytes).
ms.assetid: 69319f54-e3e7-4c0a-a65c-b6f68fec53f4
keywords:
- BytesSentHistory property Virtual Server
- BytesSentHistory property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , BytesSentHistory property
- BytesSentHistory property Virtual Server , VMVirtualNetwork interface
- VMVirtualNetwork interface Virtual Server , BytesSentHistory property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.BytesSentHistory
- IVMVirtualNetwork.get_BytesSentHistory
- VMVirtualNetwork.BytesSentHistory
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

# IVMVirtualNetwork::BytesSentHistory property

The **BytesSentHistory** property contains the recent number of bytes sent per second by this virtual network (as an array of number of bytes).

This property is read-only.

## Syntax


```C++
HRESULT get_BytesSentHistory(
  [out] VARIANT *bytesSent
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
<td><pre><code>VMVirtualNetwork.BytesSentHistory( _
  ByRef bytesSent _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of bytes sent per second by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of bytes sent at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *bytesSent* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>          |



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

 

 






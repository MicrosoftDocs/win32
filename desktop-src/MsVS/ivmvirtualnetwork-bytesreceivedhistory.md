---
title: IVMVirtualNetwork BytesReceivedHistory property
description: The BytesReceivedHistory property contains the recent number of bytes received per second by this virtual network (as an array of number of bytes).
ms.assetid: '216641dc-ec9b-41d7-a80a-7bb42cf8a9ee'
keywords: ["BytesReceivedHistory property Virtual Server", "BytesReceivedHistory property Virtual Server , IVMVirtualNetwork interface", "IVMVirtualNetwork interface Virtual Server , BytesReceivedHistory property", "BytesReceivedHistory property Virtual Server , VMVirtualNetwork interface", "VMVirtualNetwork interface Virtual Server , BytesReceivedHistory property"]
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.BytesReceivedHistory
- IVMVirtualNetwork.get_BytesReceivedHistory
- VMVirtualNetwork.BytesReceivedHistory
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualNetwork::BytesReceivedHistory property

The **BytesReceivedHistory** property contains the recent number of bytes received per second by this virtual network (as an array of number of bytes).

This property is read-only.

## Syntax


```C++
HRESULT get_BytesReceivedHistory(
  [out] VARIANT *bytesReceived
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
<td><pre><code>VMVirtualNetwork.BytesReceivedHistory( _
  ByRef bytesReceived _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of bytes received per second by this virtual network as an unsigned **Integer** array of 60 elements, representing the number of bytes received at each second over the past minute.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                               |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>              |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *bytesReceived* parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>              |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 






---
title: IVMVirtualNetwork BytesReceived property
description: The BytesReceived property contains the current number of bytes received per second by this virtual network.
ms.assetid: 'e36038dc-ad14-4242-bf3b-cdc75b1f5043'
keywords: ["BytesReceived property Virtual Server", "BytesReceived property Virtual Server , IVMVirtualNetwork interface", "IVMVirtualNetwork interface Virtual Server , BytesReceived property", "BytesReceived property Virtual Server , VMVirtualNetwork class", "VMVirtualNetwork class Virtual Server , BytesReceived property"]
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.BytesReceived
- IVMVirtualNetwork.get_BytesReceived
- VMVirtualNetwork.BytesReceived
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMVirtualNetwork::BytesReceived property

The **BytesReceived** property contains the current number of bytes received per second by this virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_BytesReceived(
  [out] long *bytesReceived
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
<td><pre><code>VMVirtualNetwork.BytesReceived( _
  ByRef bytesReceived _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The current number of bytes received per second by this virtual network.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                               |
|------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>              |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *bytesReceived* parameter is **NULL**.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>              |



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

 

 






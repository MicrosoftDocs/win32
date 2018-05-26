---
title: IVMVirtualNetwork Notes property
description: The Notes property contains the notes for this virtual network.
ms.assetid: d872f624-885e-4aae-a0ed-211bcf61c34a
keywords:
- Notes property Virtual Server
- Notes property Virtual Server , IVMVirtualNetwork interface
- IVMVirtualNetwork interface Virtual Server , Notes property
- Notes property Virtual Server , VMVirtualNetwork class
- VMVirtualNetwork class Virtual Server , Notes property
topic_type:
- apiref
api_name:
- IVMVirtualNetwork.Notes
- IVMVirtualNetwork.get_Notes
- IVMVirtualNetwork.put_Notes
- VMVirtualNetwork.Notes
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

# IVMVirtualNetwork::Notes property

The **Notes** property contains the notes for this virtual network.

This property is read/write.

## Syntax


```C++
HRESULT put_Notes(
  [in]  BSTR virtualNetworkNotes
);

HRESULT get_Notes(
  [out] BSTR *virtualNetworkNotes
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
<td><pre><code>VMVirtualNetwork.Notes( _
  ByRef virtualNetworkNotes, _
  ByVal virtualNetworkNotes _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The notes for the virtual network.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                          |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *virtualNetworkName* parameter is **NULL**.<br/>        |
| <dl> <dt> E\_INVALIDARG</dt> </dl>     | The *virtualNetworkName* parameter is an empty string.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                      |



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

 

 






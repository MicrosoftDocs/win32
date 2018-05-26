---
title: IVMVirtualNetworkCollection Item property
description: The Item property contains the IVMVirtualNetwork object at a given index (1-based index).
ms.assetid: 7886217d-dedb-4c89-9822-3e1fe2e6bdd6
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMVirtualNetworkCollection interface
- IVMVirtualNetworkCollection interface Virtual Server , Item property
- Item property Virtual Server , VMVirtualNetworkCollection interface
- VMVirtualNetworkCollection interface Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMVirtualNetworkCollection.Item
- IVMVirtualNetworkCollection.get_Item
- VMVirtualNetworkCollection.Item
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

# IVMVirtualNetworkCollection::Item property

The **Item** property contains the [**IVMVirtualNetwork**](ivmvirtualnetwork.md) object at a given index (1-based index).

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long              index,
        Long              index,
  [out] IVMVirtualNetwork **virtualNetwork
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
<td><pre><code>VMVirtualNetworkCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef virtualNetwork _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMVirtualNetwork**](ivmvirtualnetwork.md) object at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *virtualNetwork* parameter is **NULL**.<br/>                                        |
| <dl> <dt>S\_FALSE</dt> </dl>           | The *index* parameter does not reference a virtual network.<br/>                        |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>  | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetworkCollection**](ivmvirtualnetworkcollection.md)
</dt> </dl>

 

 






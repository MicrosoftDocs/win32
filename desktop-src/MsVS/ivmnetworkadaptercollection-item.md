---
title: IVMNetworkAdapterCollection Item property
description: The Item property contains the IVMNetworkAdapter object that corresponds to the given index in this collection.
ms.assetid: aa6599cb-4290-4613-b022-29293e951e5e
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMNetworkAdapterCollection interface
- IVMNetworkAdapterCollection interface Virtual Server , Item property
- Item property Virtual Server , VMNetworkAdapterCollection interface
- VMNetworkAdapterCollection interface Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMNetworkAdapterCollection.Item
- IVMNetworkAdapterCollection.get_Item
- VMNetworkAdapterCollection.Item
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

# IVMNetworkAdapterCollection::Item property

The **Item** property contains the [**IVMNetworkAdapter**](ivmnetworkadapter.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long              index,
        Long              index,
  [out] IVMNetworkAdapter **networkInterface
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
<td><pre><code>VMNetworkAdapterCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef networkInterface _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMNetworkAdapter**](ivmnetworkadapter.md) object at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *networkInterface* parameter is **NULL**.<br/>                                      |
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

[**IVMNetworkAdapterCollection**](ivmnetworkadaptercollection.md)
</dt> </dl>

 

 






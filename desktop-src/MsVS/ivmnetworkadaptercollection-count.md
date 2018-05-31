---
title: IVMNetworkAdapterCollection Count property
description: The Count property contains the number of network interfaces in the collection.
ms.assetid: 28979b5a-5d55-4370-84ee-d64374d32eac
keywords:
- Count property Virtual Server
- Count property Virtual Server , IVMNetworkAdapterCollection interface
- IVMNetworkAdapterCollection interface Virtual Server , Count property
- Count property Virtual Server , IVMNetworkAdapterCollection interface
- IVMNetworkAdapterCollection interface Virtual Server , Count property
topic_type:
- apiref
api_name:
- IVMNetworkAdapterCollection.Count
- IVMNetworkAdapterCollection.get_Count
- IVMNetworkAdapterCollection.Count
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

# IVMNetworkAdapterCollection::Count property

The **Count** property contains the number of network interfaces in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out] long *count
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
<td><pre><code>IVMNetworkAdapterCollection.Count( _
  ByRef count _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of network interfaces in this collection.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>      |
| <dl> <dt> E\_POINTER</dt> </dl>        | The parameter *count* is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>  |



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

 

 






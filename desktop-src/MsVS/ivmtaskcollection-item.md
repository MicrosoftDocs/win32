---
title: IVMTaskCollection Item property
description: The Item property contains the IVMTask object that corresponds to the given index in this collection.
ms.assetid: fff76714-7a2a-42fd-b43f-0d38687af51c
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMTaskCollection interface
- IVMTaskCollection interface Virtual Server , Item property
- Item property Virtual Server , VMTaskCollection class
- VMTaskCollection class Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMTaskCollection.Item
- IVMTaskCollection.get_Item
- VMTaskCollection.Item
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

# IVMTaskCollection::Item property

The **Item** property contains the [**IVMTask**](ivmtask.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long    index,
        Long    index,
  [out] IVMTask **task
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
<td><pre><code>VMTaskCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef task _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMTask**](ivmtask.md) object found at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                           |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *task* parameter is **NULL**.<br/>                       |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>  | The given index is invalid or the task no longer exists<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                           |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMTaskCollection**](ivmtaskcollection.md)
</dt> </dl>

 

 






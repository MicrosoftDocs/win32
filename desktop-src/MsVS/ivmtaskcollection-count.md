---
title: IVMTaskCollection Count property
description: The Count property contains the number of tasks defined in this collection.
ms.assetid: b8b03f8c-0008-4a76-b93d-484ee14f71d9
keywords:
- Count property Virtual Server
- Count property Virtual Server , IVMTaskCollection interface
- IVMTaskCollection interface Virtual Server , Count property
- Count property Virtual Server , IVMTaskCollection class
- IVMTaskCollection class Virtual Server , Count property
topic_type:
- apiref
api_name:
- IVMTaskCollection.Count
- IVMTaskCollection.get_Count
- IVMTaskCollection.Count
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

# IVMTaskCollection::Count property

The **Count** property contains the number of tasks defined in this collection.

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
<td><pre><code>IVMTaskCollection.Count( _
  ByRef count _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of tasks defined in this collection.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                  |
|-----------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter is **NULL**.<br/>    |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



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

 

 






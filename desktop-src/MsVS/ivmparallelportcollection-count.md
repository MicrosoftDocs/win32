---
title: IVMParallelPortCollection Count property
description: The Count property contains the number of parallel ports defined in this collection.
ms.assetid: 8796a2c3-4e00-4ebe-93a6-6a3e47f371b9
keywords:
- Count property Virtual Server
- Count property Virtual Server , IVMParallelPortCollection interface
- IVMParallelPortCollection interface Virtual Server , Count property
- Count property Virtual Server , VMParallelPortCollection interface
- VMParallelPortCollection interface Virtual Server , Count property
topic_type:
- apiref
api_name:
- IVMParallelPortCollection.Count
- IVMParallelPortCollection.get_Count
- VMParallelPortCollection.Count
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

# IVMParallelPortCollection::Count property

The **Count** property contains the number of parallel ports defined in this collection.

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
<td><pre><code>VMParallelPortCollection.Count( _
  ByRef count _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of parallel ports defined in this collection.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *count* parameter is **NULL**.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMParallelPortCollection**](ivmparallelportcollection.md)
</dt> </dl>

 

 






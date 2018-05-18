---
title: IVMAccessRightsCollection Count property
description: The Count property retrieves the number of access control entries contained in this collection.
ms.assetid: '29b00a9e-9ccd-4afd-8d93-341f943a74c9'
keywords: ["Count property Virtual Server", "Count property Virtual Server , IVMAccessRightsCollection interface", "IVMAccessRightsCollection interface Virtual Server , Count property", "Count property Virtual Server , IVMAccessRightsCollection interface", "IVMAccessRightsCollection interface Virtual Server , Count property"]
topic_type:
- apiref
api_name:
- IVMAccessRightsCollection.Count
- IVMAccessRightsCollection.get_Count
- IVMAccessRightsCollection.Count
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccessRightsCollection::Count property

The **Count** property retrieves the number of access control entries contained in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out] long *count
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
<td><pre><code>IVMAccessRightsCollection.Count( _
  ByRef count _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                  |
|------------------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/> |
| <dl> <dt> E\_POINTER</dt> </dl>         | *count* is **NULL**.<br/>          |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/> |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRightsCollection**](ivmaccessrightscollection.md)
</dt> </dl>

 

 






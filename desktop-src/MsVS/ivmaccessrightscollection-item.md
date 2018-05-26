---
title: IVMAccessRightsCollection Item property
description: The Item property retrieves the IVMAccessRights object that corresponds to the given index in this collection.
ms.assetid: e355b598-d1aa-4358-b723-a7cf56161fcf
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMAccessRightsCollection interface
- IVMAccessRightsCollection interface Virtual Server , Item property
- Item property Virtual Server , IVMAccessRightsCollection interface
- IVMAccessRightsCollection interface Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMAccessRightsCollection.Item
- IVMAccessRightsCollection.get_Item
- IVMAccessRightsCollection.Item
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

# IVMAccessRightsCollection::Item property

The **Item** property retrieves the **IVMAccessRights** object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long            index,
        Long            index,
  [out] IVMAccessRights **accessControlEntry
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
<td><pre><code>IVMAccessRightsCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef accessControlEntry _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMAccessRights**](ivmaccessrights.md) object at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *outAccessControlEntry* parameter is **NULL**.<br/>                                 |
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

[**IVMAccessRightsCollection**](ivmaccessrightscollection.md)
</dt> </dl>

 

 






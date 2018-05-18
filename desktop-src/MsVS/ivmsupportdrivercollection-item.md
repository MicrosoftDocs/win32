---
title: IVMSupportDriverCollection Item property
description: The Item property contains the IVMSupportDriver object that corresponds to the given index in this collection.
ms.assetid: '614fd817-ee3a-405d-a0ff-3946dfab5f47'
keywords: ["Item property Virtual Server", "Item property Virtual Server , IVMSupportDriverCollection interface", "IVMSupportDriverCollection interface Virtual Server , Item property", "Item property Virtual Server , VMSupportDriverCollection interface", "VMSupportDriverCollection interface Virtual Server , Item property"]
topic_type:
- apiref
api_name:
- IVMSupportDriverCollection.Item
- IVMSupportDriverCollection.get_Item
- VMSupportDriverCollection.Item
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSupportDriverCollection::Item property

The **Item** property contains the [**IVMSupportDriver**](ivmsupportdriver.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long             index,
        Long             index,
  [out] IVMSupportDriver **supportDriver
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
<td><pre><code>VMSupportDriverCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef supportDriver _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains the [**VMSupportDriver**](ivmsupportdriver.md) object at the given index.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                                       |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *supportDriver* parameter is **NULL**.<br/>                                         |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>  | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSupportDriverCollection**](ivmsupportdrivercollection.md)
</dt> </dl>

 

 






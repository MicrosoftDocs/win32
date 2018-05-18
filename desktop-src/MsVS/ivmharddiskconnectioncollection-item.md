---
title: IVMHardDiskConnectionCollection Item property
description: The Item property contains the IVMHardDiskConnection object that corresponds to the given index in this collection.
ms.assetid: '9fd293c1-0b58-4bd3-91cf-9850d94c6031'
keywords: ["Item property Virtual Server", "Item property Virtual Server , IVMHardDiskConnectionCollection interface", "IVMHardDiskConnectionCollection interface Virtual Server , Item property", "Item property Virtual Server , VMHardDiskConnectionCollection interface", "VMHardDiskConnectionCollection interface Virtual Server , Item property"]
topic_type:
- apiref
api_name:
- IVMHardDiskConnectionCollection.Item
- IVMHardDiskConnectionCollection.get_Item
- VMHardDiskConnectionCollection.Item
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHardDiskConnectionCollection::Item property

The **Item** property contains the [**IVMHardDiskConnection**](ivmharddiskconnection.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long                  index,
  [out] IVMHardDiskConnection **hardDiskConnection
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
<td><pre><code>VMHardDiskConnectionCollection.Item( _
  ByVal index, _
  ByRef hardDiskConnection _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMHardDiskConnection**](ivmharddiskconnection.md) object found at the given index.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                                                       |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *hardDiskConnection* parameter is **NULL**.<br/>                                    |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>   | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDiskConnectionCollection**](ivmharddiskconnectioncollection.md)
</dt> </dl>

 

 






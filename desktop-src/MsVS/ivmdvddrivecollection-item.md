---
title: IVMDVDDriveCollection Item property
description: The Item property contains the IVMDVDDrive object that corresponds to the given index in this collection.
ms.assetid: 073ab928-60c1-4d21-acd8-5673f5569817
keywords:
- Item property Virtual Server
- Item property Virtual Server , IVMDVDDriveCollection interface
- IVMDVDDriveCollection interface Virtual Server , Item property
- Item property Virtual Server , VMDVDDriveCollection interface
- VMDVDDriveCollection interface Virtual Server , Item property
topic_type:
- apiref
api_name:
- IVMDVDDriveCollection.Item
- IVMDVDDriveCollection.get_Item
- VMDVDDriveCollection.Item
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

# IVMDVDDriveCollection::Item property

The **Item** property contains the [**IVMDVDDrive**](ivmdvddrive.md) object that corresponds to the given index in this collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Item(
  [in]  long        index,
        Long        index,
  [out] IVMDVDDrive **dvdDrive
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
<td><pre><code>VMDVDDriveCollection.Item( _
  ByVal index, _
  ByVal index, _
  ByRef dvdDrive _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMDVDDrive**](ivmdvddrive.md) object found at the given index.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                                                       |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                                      |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *dvdDrive* parameter is **NULL**.<br/>                                              |
| <dl> <dt>DISP\_E\_BADINDEX</dt> </dl>   | The index of the requested item does not correspond to an item in this collection.<br/> |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>                                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                                      |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDriveCollection**](ivmdvddrivecollection.md)
</dt> </dl>

 

 






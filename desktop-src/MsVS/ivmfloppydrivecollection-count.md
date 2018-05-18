---
title: IVMFloppyDriveCollection Count property
description: The Count property contains the number of floppy drives defined in this collection.
ms.assetid: '682c0734-d102-49b3-8900-6e17d978e1bc'
keywords: ["Count property Virtual Server", "Count property Virtual Server , IVMFloppyDriveCollection interface", "IVMFloppyDriveCollection interface Virtual Server , Count property", "Count property Virtual Server , IVMFloppyDriveCollection interface", "IVMFloppyDriveCollection interface Virtual Server , Count property"]
topic_type:
- apiref
api_name:
- IVMFloppyDriveCollection.Count
- IVMFloppyDriveCollection.get_Count
- IVMFloppyDriveCollection.Count
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMFloppyDriveCollection::Count property

The **Count** property contains the number of floppy drives defined in this collection.

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
<td><pre><code>IVMFloppyDriveCollection.Count( _
  ByRef count _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The number of floppy drives defined in this collection.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                                              |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                             |
| <dl> <dt>E\_POINTER</dt> </dl>          | The parameter is **NULL**.<br/>                                                |
| <dl> <dt> VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration for this virtual machine is invalid or cannot be found.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>  | An unexpected error occurred.<br/>                                             |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMFloppyDriveCollection**](ivmfloppydrivecollection.md)
</dt> </dl>

 

 






---
title: IVMHostInfo FloppyDrives property
description: The FloppyDrives property contains an array of drive letters associated with host floppy drives.
ms.assetid: '24a23c66-910c-4e8f-9539-097ea2de717a'
keywords: ["FloppyDrives property Virtual Server", "FloppyDrives property Virtual Server , IVMHostInfo interface", "IVMHostInfo interface Virtual Server , FloppyDrives property", "FloppyDrives property Virtual Server , VMHostInfo interface", "VMHostInfo interface Virtual Server , FloppyDrives property"]
topic_type:
- apiref
api_name:
- IVMHostInfo.FloppyDrives
- IVMHostInfo.get_FloppyDrives
- VMHostInfo.FloppyDrives
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMHostInfo::FloppyDrives property

The **FloppyDrives** property contains an array of drive letters associated with host floppy drives.

This property is read-only.

## Syntax


```C++
HRESULT get_FloppyDrives(
  [out] VARIANT *floppyDrives
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
<td><pre><code>VMHostInfo.FloppyDrives( _
  ByRef floppyDrives _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains an array of drive letters associated with host floppy drives.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                        |
|-----------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>       |
| <dl> <dt>E\_POINTER</dt> </dl>         | The outgoing parameter is **NULL**.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>       |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHostInfo**](ivmhostinfo.md)
</dt> </dl>

 

 






---
title: IVMDVDDrive ImageFile property
description: The ImageFile property contains the full path of the image file captured by this DVD drive.
ms.assetid: 'fa835c1d-cc46-4ce0-8985-308e98515b7e'
keywords: ["ImageFile property Virtual Server", "ImageFile property Virtual Server , IVMDVDDrive interface", "IVMDVDDrive interface Virtual Server , ImageFile property", "ImageFile property Virtual Server , VMDVDDrive interface", "VMDVDDrive interface Virtual Server , ImageFile property"]
topic_type:
- apiref
api_name:
- IVMDVDDrive.ImageFile
- IVMDVDDrive.get_ImageFile
- VMDVDDrive.ImageFile
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMDVDDrive::ImageFile property

The **ImageFile** property contains the full path of the image file captured by this DVD drive.

This property is read-only.

## Syntax


```C++
HRESULT get_ImageFile(
  [out] BSTR *imagePath
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
<td><pre><code>VMDVDDrive.ImageFile( _
  ByRef imagePath _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The full path to the image file captured by this DVD drive.

This property value is read-only.

## Error codes



| Name                                                                                                 | Meaning                                                                   |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                     | The operation was successful.<br/>                                  |
| <dl> <dt>E\_POINTER</dt> </dl>                | The parameter is **NULL**.<br/>                                     |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>        | The virtual machine could not be found.<br/>                        |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl>     | The bus location for this drive is invalid.<br/>                    |
| <dl> <dt>VM\_E\_MEDIA\_WRONG\_TYPE</dt> </dl> | The media captured by this DVD drive is not an ISO image file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>        | An unexpected error occurred.<br/>                                  |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> </dl>

 

 






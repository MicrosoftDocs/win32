---
error-parsing-yaml: 
---

# IVMDVDDrive::Attachment property

The **Attachment** property retrieves an enumerated value representing the type of media attached to the DVD drive within the virtual machine.

This property is read-only.

## Syntax


```C++
HRESULT get_Attachment(
  [out] VMDVDDriveAttachmentType *driveAttachment
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
<td><pre><code>VMDVDDrive.Attachment( _
  ByRef driveAttachment _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The attached media type.

This property value is read-only.

## Error codes



| Name                                                                                             | Meaning                                                |
|--------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                 | The operation was successful.<br/>               |
| <dl> <dt>E\_POINTER</dt> </dl>            | The parameter is **NULL**.<br/>                  |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>    | The virtual machine could not be found.<br/>     |
| <dl> <dt>VM\_E\_DRIVE\_INVALID</dt> </dl> | The bus location for this drive is invalid.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>    | An unexpected error occurred.<br/>               |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMDVDDrive**](ivmdvddrive.md)
</dt> <dt>

[**VMDVDDriveAttachmentType**](vmdvddriveattachmenttype.md)
</dt> </dl>

 

 






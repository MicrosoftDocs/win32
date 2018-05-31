---
error-parsing-yaml: 
---

# IVMHardDisk::Parent property

The **Parent** property contains the [**IVMHardDisk**](ivmharddisk.md) object associated with the parent hard disk image.

This property is read/write.

## Syntax


```C++
HRESULT put_Parent(
  [in]  IVMHardDisk *parent
);

HRESULT get_Parent(
  [out] IVMHardDisk **parent
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
<td><pre><code>VMHardDisk.Parent( _
  ByRef parent, _
  ByVal parent _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMHardDisk**](ivmharddisk.md) object associated with the parent hard disk image.

This property value is read/write.

## Error codes



| Name                                                                                                          | Meaning                                                                                                                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                              | The operation was successful.<br/>                                                                                                                                                                                                                                |
| <dl> <dt>E\_POINTER</dt> </dl>                         | The *parent* parameter is **NULL**.<br/>                                                                                                                                                                                                                          |
| <dl> <dt>S\_FALSE</dt> </dl>                           | This is not a differencing hard disk, so it has no parent.<br/>                                                                                                                                                                                                   |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl>                | The system could not find the parent virtual hard disk file.<br/>                                                                                                                                                                                                 |
| <dl> <dt>E\_PATH\_NOT\_FOUND</dt> </dl>                | The system could not find the path to the parent virtual hard disk file.<br/>                                                                                                                                                                                     |
| <dl> <dt>VM\_E\_PREF\_READ\_ERROR</dt> </dl>           | The preferences for the current hard disk image could not be read.<br/>                                                                                                                                                                                           |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> </dl>       | An error occurred while attempting to open the current hard disk image file.<br/>                                                                                                                                                                                 |
| <dl> <dt>VM\_E\_HD\_IMAGE\_ACCESS</dt> </dl>           | An error occurred while attempting to access the current hard disk image file.<br/>                                                                                                                                                                               |
| <dl> <dt>VM\_E\_PARENT\_CHILD\_ID\_MISMATCH</dt> </dl> | The virtual hard disk image located by the parameter *parent* does not have the same ID as the child disk image. Make sure the parent virtual hard disk image located by *parent* is the same image used to create the differencing virtual hard disk image.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>                 | An unexpected error occurred.<br/>                                                                                                                                                                                                                                |



## Remarks

This property is only valid with differencing hard disk images.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMHardDisk**](ivmharddisk.md)
</dt> </dl>

 

 






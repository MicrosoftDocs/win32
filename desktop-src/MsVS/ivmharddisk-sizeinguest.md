---
error-parsing-yaml: 
---

# IVMHardDisk::SizeInGuest property

The **SizeInGuest** property contains the size, in bytes, of the hard disk image, as represented in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_SizeInGuest(
  [out] VARIANT *fileSize
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
<td><pre><code>VMHardDisk.SizeInGuest( _
  ByRef fileSize _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The size, in bytes, of the hard disk image, as represented in the guest operating system. This number is returned as a **Decimal** value.

This property value is read-only.

## Error codes



| Name                                                                                                    | Meaning                                                                                   |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                        | The operation was successful.<br/>                                                  |
| <dl> <dt>E\_POINTER</dt> </dl>                   | The parameter is **NULL**.<br/>                                                     |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl>          | The current virtual hard disk file could not be found.<br/>                         |
| <dl> <dt>VM\_E\_HD\_IMAGE\_OPEN\_FAIL</dt> </dl> | An error occurred while attempting to open the current hard disk image file.<br/>   |
| <dl> <dt>VM\_E\_HD\_IMAGE\_ACCESS</dt> </dl>     | An error occurred while attempting to access the current hard disk image file.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>           | An unexpected error occurred.<br/>                                                  |



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

 

 






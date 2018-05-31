---
error-parsing-yaml: 
---

# IVMHardDisk::Security property

The [**IVMSecurity**](ivmsecurity.md) object associated with the current hard disk image file.

This property is read-only.

## Syntax


```C++
HRESULT get_Security(
  [out] IVMSecurity **security
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
<td><pre><code>VMHardDisk.Security( _
  ByRef security _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains a [**VMSecurity**](ivmsecurity.md) instance that represents the security attributes of the current hard disk image file.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                                                            |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>                                           |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *security* parameter is **NULL**.<br/>                                   |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>      | Could not allocate memory for the security descriptor.<br/>                  |
| <dl> <dt>E\_FILE\_NOT\_FOUND</dt> </dl> | The hard disk image file associated with this COM object was not found.<br/> |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                                       |



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

 

 






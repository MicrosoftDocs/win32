---
error-parsing-yaml: 
---

# IVMGuestOS::AdditionsVersion property

The **AdditionsVersion** property contains the version of the Additions installed in the guest operating system.

This property is read-only.

## Syntax


```C++
HRESULT get_AdditionsVersion(
  [out] BSTR *additionsVersion
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
<td><pre><code>VMGuestOS.AdditionsVersion( _
  ByRef additionsVersion _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The version of the Additions installed in the guest operating system.

This property value is read-only.

## Error codes



| Name                                                                                                     | Meaning                                                                                                        |
|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                         | The operation was successful.<br/>                                                                       |
| <dl> <dt>E\_POINTER</dt> </dl>                    | *additionsVersion* is **NULL**.<br/>                                                                     |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl>            | The virtual machine could not be found.<br/>                                                             |
| <dl> <dt> VM\_E\_ADDITIONS\_NOT\_AVAIL</dt> </dl> | Additions are not installed in this virtual machine, or the virtual machine has never been started.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl>            | An unexpected error occurred.<br/>                                                                       |



## Remarks

If the virtual machine is not running when this method is invoked, the method will attempt to read the Additions version that was cached in the configuration file the last time the virtual machine was run.

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMGuestOS**](ivmguestos.md)
</dt> </dl>

 

 






---
error-parsing-yaml: 
---

# IVMGuestOS::IsHostTimeSyncEnabled property

The **IsHostTimeSyncEnabled** property contains **TRUE** if the Additions in this virtual machine should synchronize the guest's clock with the host's clock.

This property is read/write.

## Syntax


```C++
HRESULT put_IsHostTimeSyncEnabled(
  [in]  VARIANT_BOOL shouldEnable
);

HRESULT get_IsHostTimeSyncEnabled(
  [out] VARIANT_BOOL *isEnabled
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
<td><pre><code>VMGuestOS.IsHostTimeSyncEnabled( _
  ByVal shouldEnable, _
  ByRef isEnabled _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the Additions in this virtual machine should synchronize the guest's clock with the host's clock.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>  |
| <dl> <dt> E\_POINTER</dt> </dl>        | *isEnabled* was not specified.<br/> |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The configuration is unknown.<br/>  |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/> |



## Remarks

You cannot change this setting while the virtual machine is active (that is, running or in saved state).

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

 

 






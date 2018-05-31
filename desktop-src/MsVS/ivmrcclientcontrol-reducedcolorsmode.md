---
error-parsing-yaml: 
---

# IVMRCClientControl::ReducedColorsMode property

The **ReducedColorsMode** property indicates whether the client's reduced-colors mode is enabled.

This property is read/write.

## Syntax


```C++
HRESULT put_ReducedColorsMode(
  [in]  VARIANT_BOOL reducedColorsMode
);

HRESULT get_ReducedColorsMode(
  [out] VARIANT_BOOL *reducedColorsMode
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
<td><pre><code>VMRCClientControl.ReducedColorsMode( _
  ByRef reducedColorsMode, _
  ByVal reducedColorsMode _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the client's reduced-colors mode is enabled.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                    |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                   |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/>   |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *reducedColorsMode* parameter was **NULL**.<br/> |



## Remarks

When the client's reduced-colors mode is enabled, the virtual machine screen displays are drawn with a limited color palette. This reduces the amount of data sent from the VMRC server to the client, allowing faster updates to occur over slow network connections.

> [!Note]  
> Enabling this feature takes affect when a new connection is made. It cannot be changed for an already established connection.

 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 






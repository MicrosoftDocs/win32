---
error-parsing-yaml: 
---

# IVMRCClientControl::ServerDisplayName property

The **ServerDisplayName** property contains the name of the virtual machine to be displayed.

This property is read/write.

## Syntax


```C++
HRESULT put_ServerDisplayName(
  [in]  BSTR serverDisplayName
);

HRESULT get_ServerDisplayName(
  [out] BSTR *serverDisplayName
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
<td><pre><code>VMRCClientControl.ServerDisplayName( _
  ByRef serverDisplayName, _
  ByVal serverDisplayName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The name of the virtual machine to be displayed.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                    |
|------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                   |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/>   |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *serverDisplayName* parameter was **NULL**.<br/> |



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

 

 






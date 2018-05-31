---
error-parsing-yaml: 
---

# IVMRCClientControl::ReadyState property

The **ReadyState** property contains the control's current readiness state.

This property is read/write.

## Syntax


```C++
HRESULT put_ReadyState(
  [in]  long readyState
);

HRESULT get_ReadyState(
  [out] long *readyState
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
<td><pre><code>VMRCClientControl.ReadyState( _
  ByRef readyState, _
  ByVal readyState _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The control's current readiness value.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                            |
|------------------------------------------------------------------------------------------|----------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>           |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *readyState* parameter was **NULL**<br/> |



## Remarks

The *readyState* values are the same as for other ActiveX control state values.

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

 

 






---
error-parsing-yaml: 
---

# IVMRCClientControl::ServerDisplayWidth property

The **ServerDisplayWidth** property contains the width of the video display area in pixels.

This property is read-only.

## Syntax


```C++
HRESULT get_ServerDisplayWidth(
  [out] long *displayWidth
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
<td><pre><code>VMRCClientControl.ServerDisplayWidth( _
  ByRef displayWidth _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The width of the video display area in pixels.

This property value is read-only.

## Error codes



| Name                                                                                     | Meaning                                               |
|------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>              |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *displayWidth* parameter was **NULL**.<br/> |



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

 

 






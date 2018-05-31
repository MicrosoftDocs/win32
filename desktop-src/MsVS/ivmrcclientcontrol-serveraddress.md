---
error-parsing-yaml: 
---

# IVMRCClientControl::ServerAddress property

The **ServerAddress** property contains the network address of the VMRC server.

This property is read/write.

## Syntax


```C++
HRESULT put_ServerAddress(
  [in]  BSTR serverAddress
);

HRESULT get_ServerAddress(
  [out] BSTR *serverAddress
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
<td><pre><code>VMRCClientControl.ServerAddress( _
  ByRef serverAddress, _
  ByVal serverAddress _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The network address of the VMRC server.

This property value is read/write.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *serverAddress* parameter was **NULL**.<br/>   |



## Remarks

The server address may be specified either by its DNS name or by a dotted-decimal TCP/IP address.

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

 

 






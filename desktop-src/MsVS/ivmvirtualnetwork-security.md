---
error-parsing-yaml: 
---

# IVMVirtualNetwork::Security property

The **Security** property contains the [**IVMSecurity**](ivmsecurity.md) object associated with the virtual network.

This property is read-only.

## Syntax


```C++
HRESULT get_Security(
  [out] IVMSecurity **outSecurity
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
<td><pre><code>VMVirtualNetwork.Security( _
  ByRef outSecurity _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMSecurity**](ivmsecurity.md) object which defines the security attributes of the virtual network.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                           |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The parameter *outSecurity* is **NULL**.<br/>               |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>     | Could not allocate memory for the security descriptor.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error occurred.<br/>                          |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMVirtualNetwork**](ivmvirtualnetwork.md)
</dt> </dl>

 

 






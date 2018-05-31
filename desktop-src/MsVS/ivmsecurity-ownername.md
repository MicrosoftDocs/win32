---
error-parsing-yaml: 
---

# IVMSecurity::OwnerName property

The **OwnerName** property contains the account name of the owner.

This property is read/write.

## Syntax


```C++
HRESULT put_OwnerName(
  [in]  BSTR inOwnerName
);

HRESULT get_OwnerName(
  [out] BSTR *outOwnerName
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
<td><pre><code>VMSecurity.OwnerName( _
  ByRef outOwnerName, _
  ByVal inOwnerName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The account name of the owner. This may be a SID string if the account name cannot be resolved.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *outOwnerName* parameter was **NULL**.<br/>                                             |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *inOwnerName* parameter was invalid or empty.<br/>                                      |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> </dl>

 

 






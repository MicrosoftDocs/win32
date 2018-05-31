---
error-parsing-yaml: 
---

# IVMRCClientControl::UserName property

The **UserName** property contains the network user account name to use for validating credentials with the VMRC server.

This property is write-only.

## Syntax


```C++
HRESULT put_UserName(
  [in] BSTR userName
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
<td><pre><code>VMRCClientControl.UserName( _
  ByVal userName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Sets the network user account to use for validating credentials with the VMRC server.

This property value is write-only.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *userName* parameter was **NULL**.<br/>        |



## Remarks

This property is used in conjunction with the [**IVMRCClientControl::UserDomain**](ivmrcclientcontrol-userdomain.md) and [**IVMRCClientControl::UserPassword**](ivmrcclientcontrol-userpassword.md) properties to set the credentials used when validating credentials with the VMRC server. If all three of these properties are set to a zero-length string, the current default user credentials are used for authentication.

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

 

 






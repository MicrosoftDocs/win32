---
error-parsing-yaml: 
---

# IVMSecurity::GroupName property

The **GroupName** property retrieves the account name of the group.

This property is read/write.

## Syntax


```C++
HRESULT put_GroupName(
  [in]  BSTR groupName
);

HRESULT get_GroupName(
  [out] BSTR *groupName
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
<td><pre><code>VMSecurity.GroupName( _
  ByRef groupName, _
  ByVal groupName _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The account name of the group. This may be a SID string if the name cannot be resolved.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                    |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>                   |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *groupName* parameter was **NULL**.<br/>         |
| <dl> <dt> E\_INVALIDARG</dt> </dl>     | The *groupName* parameter was invalid or empty.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                  |



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

 

 






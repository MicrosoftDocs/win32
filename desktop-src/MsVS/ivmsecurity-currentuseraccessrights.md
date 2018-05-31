---
error-parsing-yaml: 
---

# IVMSecurity::CurrentUserAccessRights property

The **CurrentUserAccessRights** property represents the access rights for the caller of the COM interface.

This property is read-only.

## Syntax


```C++
HRESULT get_CurrentUserAccessRights(
  [out] IVMAccessRights **accessRights
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
<td><pre><code>VMSecurity.CurrentUserAccessRights( _
  ByRef accessRights _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**VMAccessRights**](ivmaccessrights.md) object which represents the discretionary access control list for the caller of the COM interface.

This property value is read-only.

## Error codes



| Name                                                                                           | Meaning                                   |
|------------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>               | The operation was successful.<br/>  |
| <dl> <dt> E\_POINTER</dt> </dl>         | *accessRights* was **NULL**.<br/>   |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/> |



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

 

 






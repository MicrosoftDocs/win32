---
error-parsing-yaml: 
---

# IVMAccessRights::ReadPermissions property

The **ReadPermissions** property determines whether this entry controls the ability to read permissions.

This property is read/write.

## Syntax


```C++
HRESULT put_ReadPermissions(
  [in]  VARIANT_BOOL readPermissions
);

HRESULT get_ReadPermissions(
  [out] VARIANT_BOOL *readPermissions
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
<td><pre><code>VMAccessRights.ReadPermissions( _
  ByVal readPermissions, _
  ByRef readPermissions _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to read permissions of the protected object.

This property value is read/write.

## Error codes



| Name                                                                                  | Meaning                                    |
|---------------------------------------------------------------------------------------|--------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>     | The operation was successful.<br/>   |
| <dl> <dt>E\_POINTER</dt> </dl> | *readPermissions* was **NULL**.<br/> |



## Examples

The following example prints the **ReadPermissions** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


```VB
Dim vsApp
Dim vsSecurity
Dim vsAccessRights
Dim arProperty

Set vsApp = WScript.CreateObject("VirtualServer.Application")
Set vsSecurity = vsApp.Security
Set vsAccessRights = vsSecurity.AccessRights

For Each arProperty In vsAccessRights
    Wscript.Echo "Name: " & arProperty.Name
    Wscript.Echo "Read permissions: " & arProperty.ReadPermissions
    Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRights**](ivmaccessrights.md)
</dt> </dl>

 

 






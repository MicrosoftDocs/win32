---
title: IVMAccessRights ChangePermissions property
description: The ChangePermissions property determines whether this entry controls the ability to change permissions.
ms.assetid: '9c33ea28-a9ee-4983-aab5-eb634a331ad9'
keywords: ["ChangePermissions property Virtual Server", "ChangePermissions property Virtual Server , IVMAccessRights interface", "IVMAccessRights interface Virtual Server , ChangePermissions property", "ChangePermissions property Virtual Server , VMAccessRights interface", "VMAccessRights interface Virtual Server , ChangePermissions property"]
topic_type:
- apiref
api_name:
- IVMAccessRights.ChangePermissions
- IVMAccessRights.get_ChangePermissions
- IVMAccessRights.put_ChangePermissions
- VMAccessRights.ChangePermissions
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccessRights::ChangePermissions property

The **ChangePermissions** property determines whether this entry controls the ability to change permissions.

This property is read/write.

## Syntax


```C++
HRESULT put_ChangePermissions(
  [in]  VARIANT_BOOL changePermissions
);

HRESULT get_ChangePermissions(
  [out] VARIANT_BOOL *changePermissions
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
<td><pre><code>VMAccessRights.ChangePermissions( _
  ByVal changePermissions, _
  ByRef changePermissions _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to change permissions of the protected object.

This property value is read/write.

## Error codes



| Name                                                                                  | Meaning                                      |
|---------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>      | The operation was successful.<br/>     |
| <dl> <dt>E\_POINTER</dt> </dl> | *changePermissions* was **NULL**.<br/> |



## Examples

The following example prints the **ChangePermissions** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Change permissions: " & arProperty.ChangePermissions
    Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRights**](ivmaccessrights.md)
</dt> </dl>

 

 






---
title: IVMAccessRights ReadAccess property
description: The ReadAccess property determines whether this entry controls read access.
ms.assetid: 'ac9ad224-5056-466e-b3de-3906e4303921'
keywords: ["ReadAccess property Virtual Server", "ReadAccess property Virtual Server , IVMAccessRights interface", "IVMAccessRights interface Virtual Server , ReadAccess property", "ReadAccess property Virtual Server , VMAccessRights interface", "VMAccessRights interface Virtual Server , ReadAccess property"]
topic_type:
- apiref
api_name:
- IVMAccessRights.ReadAccess
- IVMAccessRights.get_ReadAccess
- IVMAccessRights.put_ReadAccess
- VMAccessRights.ReadAccess
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccessRights::ReadAccess property

The **ReadAccess** property determines whether this entry controls read access.

This property is read/write.

## Syntax


```C++
HRESULT put_ReadAccess(
  [in]  VARIANT_BOOL readAccess
);

HRESULT get_ReadAccess(
  [out] VARIANT_BOOL *readAccess
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
<td><pre><code>VMAccessRights.ReadAccess( _
  ByVal readAccess, _
  ByRef readAccess _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to read from the protected object.

This property value is read/write.

## Error codes



| Name                                                                                  | Meaning                                  |
|---------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>      | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl> | *readAccess* was **NULL**.<br/>    |



## Examples

The following example prints the **ReadAccess** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Read access: " & arProperty.ReadAccess
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

 

 






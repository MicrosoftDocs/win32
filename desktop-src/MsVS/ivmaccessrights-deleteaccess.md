---
title: IVMAccessRights DeleteAccess property
description: The DeleteAccess property determines whether this entry controls delete access.
ms.assetid: c209e07a-d387-4787-aa0a-db6822abc89b
keywords:
- DeleteAccess property Virtual Server
- DeleteAccess property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , DeleteAccess property
- DeleteAccess property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , DeleteAccess property
topic_type:
- apiref
api_name:
- IVMAccessRights.DeleteAccess
- IVMAccessRights.get_DeleteAccess
- IVMAccessRights.put_DeleteAccess
- VMAccessRights.DeleteAccess
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMAccessRights::DeleteAccess property

The **DeleteAccess** property determines whether this entry controls delete access.

This property is read/write.

## Syntax


```C++
HRESULT put_DeleteAccess(
  [in]  VARIANT_BOOL deleteAccess
);

HRESULT get_DeleteAccess(
  [out] VARIANT_BOOL *deleteAccess
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
<td><pre><code>VMAccessRights.DeleteAccess( _
  ByVal deleteAccess, _
  ByRef deleteAccess _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to delete the protected object.

This property value is read/write.

## Error codes



| Name                                                                                  | Meaning                                  |
|---------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>     | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl> | *deleteAccess* was **NULL**.<br/>  |



## Examples

The following example prints the **DeleteAccess** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Delete access: " & arProperty.DeleteAccess
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

 

 






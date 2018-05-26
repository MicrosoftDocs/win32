---
title: IVMAccessRights ExecuteAccess property
description: The ExecuteAccess property determines whether this entry controls execute access.
ms.assetid: 866f11af-d6c5-4dba-a6f2-d0137968b3b4
keywords:
- ExecuteAccess property Virtual Server
- ExecuteAccess property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , ExecuteAccess property
- ExecuteAccess property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , ExecuteAccess property
topic_type:
- apiref
api_name:
- IVMAccessRights.ExecuteAccess
- IVMAccessRights.get_ExecuteAccess
- IVMAccessRights.put_ExecuteAccess
- VMAccessRights.ExecuteAccess
api_location:
- VsComInterfaces.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IVMAccessRights::ExecuteAccess property

The **ExecuteAccess** property determines whether this entry controls execute access.

This property is read/write.

## Syntax


```C++
HRESULT put_ExecuteAccess(
  [in]  VARIANT_BOOL executeAccess
);

HRESULT get_ExecuteAccess(
  [out] VARIANT_BOOL *executeAccess
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
<td><pre><code>VMAccessRights.ExecuteAccess( _
  ByVal executeAccess, _
  ByRef executeAccess _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to execute the protected object.

This property value is read/write.

## Error codes



| Name                                                                                   | Meaning                                  |
|----------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>       | The operation was successful.<br/> |
| <dl> <dt> E\_POINTER</dt> </dl> | *executeAccess* was **NULL**.<br/> |



## Examples

The following example prints the **ExecuteAccess** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Execute access: " & arProperty.ExecuteAccess
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

 

 






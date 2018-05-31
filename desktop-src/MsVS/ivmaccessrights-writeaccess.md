---
title: IVMAccessRights WriteAccess property
description: The WriteAccess property determines whether this entry controls write access.
ms.assetid: d06f5902-9a5e-40bc-80e7-c579ec5edb08
keywords:
- WriteAccess property Virtual Server
- WriteAccess property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , WriteAccess property
- WriteAccess property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , WriteAccess property
topic_type:
- apiref
api_name:
- IVMAccessRights.WriteAccess
- IVMAccessRights.get_WriteAccess
- IVMAccessRights.put_WriteAccess
- VMAccessRights.WriteAccess
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

# IVMAccessRights::WriteAccess property

The **WriteAccess** property determines whether this entry controls write access.

This property is read/write.

## Syntax


```C++
HRESULT put_WriteAccess(
  [in]  VARIANT_BOOL writeAccess
);

HRESULT get_WriteAccess(
  [out] VARIANT_BOOL *writeAccess
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
<td><pre><code>VMAccessRights.WriteAccess( _
  ByVal writeAccess, _
  ByRef writeAccess _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the entry controls the ability to write to the protected object.

This property value is read/write.

## Error codes



| Name                                                                                  | Meaning                                  |
|---------------------------------------------------------------------------------------|------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>      | The operation was successful.<br/> |
| <dl> <dt>E\_POINTER</dt> </dl> | *writeAccess* was **NULL**.<br/>   |



## Examples

The following example prints the **WriteAccess** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Write access: " & arProperty.WriteAccess
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

 

 






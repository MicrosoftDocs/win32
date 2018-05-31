---
title: IVMAccessRights Sid property
description: The Sid property retrieves the SID string of the user or group.
ms.assetid: 2ff87160-0fb1-491c-91c5-98683dcd5ec4
keywords:
- Sid property Virtual Server
- Sid property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , Sid property
- Sid property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , Sid property
topic_type:
- apiref
api_name:
- IVMAccessRights.Sid
- IVMAccessRights.get_Sid
- IVMAccessRights.put_Sid
- VMAccessRights.Sid
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

# IVMAccessRights::Sid property

The **Sid** property retrieves the SID string of the user or group.

This property is read/write.

## Syntax


```C++
HRESULT put_Sid(
  [in]  BSTR sid
);

HRESULT get_Sid(
  [out] BSTR *sid
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
<td><pre><code>VMAccessRights.Sid( _
  ByVal sid, _
  ByRef sid _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The SID string of the owner.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                                                           |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *sid* parameter is **NULL**.<br/>                                                       |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | The *sid* parameter is not valid or an empty string.<br/>                                   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



## Examples

The following example prints the **Sid** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "SID: " & arProperty.SID
    Wscript.Echo
Next
```



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMAccessRights**](ivmaccessrights.md)
</dt> </dl>

 

 






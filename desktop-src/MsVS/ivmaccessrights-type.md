---
title: IVMAccessRights Type property
description: The Type property retrieves the type of access control entry.
ms.assetid: fe1959b7-1cef-42eb-a68e-da31eb09f988
keywords:
- Type property Virtual Server
- Type property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , Type property
- Type property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , Type property
topic_type:
- apiref
api_name:
- IVMAccessRights.Type
- IVMAccessRights.get_Type
- IVMAccessRights.put_Type
- VMAccessRights.Type
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

# IVMAccessRights::Type property

The **Type** property retrieves the type of access control entry.

This property is read/write.

## Syntax


```C++
HRESULT put_Type(
  [in]  VMAccessRightsType type
);

HRESULT get_Type(
  [out] VMAccessRightsType *type
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
<td><pre><code>VMAccessRights.Type( _
  ByVal type, _
  ByRef type _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Determines whether the entry allows or denies the specific access rights.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                            |
|-----------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                           |
| <dl> <dt> E\_POINTER</dt> </dl>        | The *type* parameter is **NULL**.<br/>                       |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | An invalid value was specified in the *type* parameter.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                          |



## Examples

The following example prints the **Type** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Type: " & arProperty.Type
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
</dt> <dt>

[**VMAccessRightsType**](vmaccessrightstype.md)
</dt> </dl>

 

 






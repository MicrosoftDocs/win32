---
title: IVMAccessRights Flags property
description: The Flags property contains the inheritance flags of the access control entry.
ms.assetid: 06d414d0-8e74-415c-b296-f48ed4043175
keywords:
- Flags property Virtual Server
- Flags property Virtual Server , IVMAccessRights interface
- IVMAccessRights interface Virtual Server , Flags property
- Flags property Virtual Server , VMAccessRights interface
- VMAccessRights interface Virtual Server , Flags property
topic_type:
- apiref
api_name:
- IVMAccessRights.Flags
- IVMAccessRights.get_Flags
- IVMAccessRights.put_Flags
- VMAccessRights.Flags
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

# IVMAccessRights::Flags property

The **Flags** property contains the inheritance flags of the access control entry.

This property is read/write.

## Syntax


```C++
HRESULT put_Flags(
  [in]  byte flags
);

HRESULT get_Flags(
  [out] byte *flags
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
<td><pre><code>VMAccessRights.Flags( _
  ByRef flags, _
  ByVal flags _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Retrieves the flags which determine how the access control entry is inherited by child containers and objects.

This property value is read/write.

## Error codes



| Name                                                                                          | Meaning                                                             |
|-----------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                            |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *flags* parameter is **NULL**.<br/>                       |
| <dl> <dt>E\_INVALIDARG</dt> </dl>      | An invalid value was specified in the *flags* parameter.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/>                           |



## Examples

The following example prints the **Flags** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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
    Wscript.Echo "Flags: " & arProperty.Flags
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

 

 






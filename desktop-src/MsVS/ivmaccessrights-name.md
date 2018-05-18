---
title: IVMAccessRights Name property
description: The Name property retrieves the account name of the user or group.
ms.assetid: 'a4bb0fdb-94a6-4fd0-af5a-46c6489a6ffc'
keywords: ["Name property Virtual Server", "Name property Virtual Server , IVMAccessRights interface", "IVMAccessRights interface Virtual Server , Name property", "Name property Virtual Server , VMAccessRights interface", "VMAccessRights interface Virtual Server , Name property"]
topic_type:
- apiref
api_name:
- IVMAccessRights.Name
- IVMAccessRights.get_Name
- IVMAccessRights.put_Name
- VMAccessRights.Name
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMAccessRights::Name property

The **Name** property retrieves the account name of the user or group.

This property is read/write.

## Syntax


```C++
HRESULT put_Name(
  [in]  BSTR name
);

HRESULT get_Name(
  [out] BSTR *name
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
<td><pre><code>VMAccessRights.Name( _
  ByRef name, _
  ByVal name _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The account name of the user or group. This may be a SID string if the name cannot be resolved.

This property value is read/write.

## Error codes



| Name                                                                                           | Meaning                                                                                           |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>E\_POINTER</dt> </dl>          | The *name* parameter is **NULL**.<br/>                                                      |
| <dl> <dt>E\_INVALIDARG</dt> </dl>       | The *name* parameter is not valid or is an empty string.<br/>                               |
| <dl> <dt> DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred. Other **HRESULT** error values may be returned as well.<br/> |



## Examples

The following example prints the account **Name** property of the access control entries from the security object protecting access to the COM interfaces and global settings.


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

 

 






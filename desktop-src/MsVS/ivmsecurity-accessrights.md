---
title: IVMSecurity AccessRights property
description: The AccessRights property represents the discretionary access control list.
ms.assetid: 'a23a73dd-ba47-49ab-9e55-325fbfb3154e'
keywords: ["AccessRights property Virtual Server", "AccessRights property Virtual Server , IVMSecurity interface", "IVMSecurity interface Virtual Server , AccessRights property", "AccessRights property Virtual Server , VMSecurity interface", "VMSecurity interface Virtual Server , AccessRights property"]
topic_type:
- apiref
api_name:
- IVMSecurity.AccessRights
- IVMSecurity.get_AccessRights
- VMSecurity.AccessRights
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSecurity::AccessRights property

The **AccessRights** property represents the discretionary access control list.

This property is read-only.

## Syntax


```C++
HRESULT get_AccessRights(
  [out] IVMAccessRightsCollection **accessRights
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
<td><pre><code>VMSecurity.AccessRights( _
  ByRef accessRights _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The [**IVMAccessRightsCollection**](ivmaccessrightscollection.md) object representing the discretionary access control list.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                   |
|-----------------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt> S\_OK</dt> </dl>             | The operation was successful.<br/>  |
| <dl> <dt>E\_POINTER</dt> </dl>         | *accessRights* was **NULL**.<br/>   |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unknown error has occurred.<br/> |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSecurity**](ivmsecurity.md)
</dt> </dl>

 

 






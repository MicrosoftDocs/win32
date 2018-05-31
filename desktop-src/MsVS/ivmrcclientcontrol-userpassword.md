---
title: IVMRCClientControl UserPassword property
description: The UserPassword property contains the network user account password to use for validating credentials with the VMRC server.
ms.assetid: 73692ed1-3ed6-478b-bc3b-20783de74ec0
keywords:
- UserPassword property Virtual Server
- UserPassword property Virtual Server , IVMRCClientControl interface
- IVMRCClientControl interface Virtual Server , UserPassword property
- UserPassword property Virtual Server , VMRCClientControl interface
- VMRCClientControl interface Virtual Server , UserPassword property
topic_type:
- apiref
api_name:
- IVMRCClientControl.UserPassword
- IVMRCClientControl.put_UserPassword
- VMRCClientControl.UserPassword
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IVMRCClientControl::UserPassword property

The **UserPassword** property contains the network user account password to use for validating credentials with the VMRC server.

This property is write-only.

## Syntax


```C++
HRESULT put_UserPassword(
  [in] BSTR userPassword
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
<td><pre><code>VMRCClientControl.UserPassword( _
  ByVal userPassword _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Sets the network user account password to use for validating credentials with the VMRC server.

This property value is write-only.

## Error codes



| Name                                                                                     | Meaning                                                  |
|------------------------------------------------------------------------------------------|----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>         | The operation was successful.<br/>                 |
| <dl> <dt>S\_FALSE</dt> </dl>      | This property cannot be changed at this time.<br/> |
| <dl> <dt>E\_INVALIDARG</dt> </dl> | The *userPassword* parameter was **NULL**.<br/>    |



## Remarks

This property is used in conjunction with the [**IVMRCClientControl::UserDomain**](ivmrcclientcontrol-userdomain.md) and [**IVMRCClientControl::UserName**](ivmrcclientcontrol-username.md) properties to set the credentials used when validating credentials with the VMRC server. If all three of these properties are set to a zero-length string, the current default user credentials are used for authentication.

> [!Note]  
> The user password is specified with an unencrypted string.

 

## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VMRCClientControl.h</dt> </dl>    |
| Library<br/>  | <dl> <dt>VMRCClientControl.lib</dt> </dl>  |



## See also

<dl> <dt>

[**IVMRCClientControl**](ivmrcclientcontrol.md)
</dt> </dl>

 

 






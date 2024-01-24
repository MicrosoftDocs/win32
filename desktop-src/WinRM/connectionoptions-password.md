---
title: ConnectionOptions.Password property (WSManDisp.h)
description: Sets the password of a local or a domain account on the remote computer. This property determines the password for authentication.
ms.assetid: 61ba54b6-7da0-423e-b5b2-c4dd8aacd042
ms.tgt_platform: multiple
keywords:
- Password property Windows Remote Management
- Password property Windows Remote Management , ConnectionOptions object
- ConnectionOptions object Windows Remote Management , Password property
topic_type:
- apiref
api_name:
- ConnectionOptions.Password
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ConnectionOptions.Password property

Sets the password of a local or a domain account on the remote computer. This property determines the password for authentication. For more information, see [Authentication for Remote Connections](authentication-for-remote-connections.md).

This property is read/write.

## Syntax


```VB
ConnectionOptions.Password As String
```



## Property value

String that contains the password of a local or a domain account on the remote computer.

If no value is supplied and the **WSManFlagCredUsernamePassword** flag is not set, the password of the account that is running the script is used.

If no value is supplied and the **WSManFlagCredUsernamePassword** flag is set, the script prompts the user to enter the password (and the user name, if this is not supplied). If a valid user name and password are not entered, then an access denied error is returned.

## Remarks

Be aware that you cannot retrieve the password. The password can only be set with this property.

If you create a [**ConnectionOptions**](connectionoptions.md) object and use a user name and password to connect to Windows Remote Management, then the **WSManFlagCredUserNamePassword** flag should be set on the call to [**WSMan.CreateSession**](wsman-createsession.md).

For more information about setting passwords, see the Remarks section in [**ConnectionOptions**](connectionoptions.md).

## Examples

The following code example creates a [**ConnectionOptions**](connectionoptions.md) object and sets the **Password**.


```VB
' Create a WSMan object. 
Set objWsman = CreateObject( "WSMAN.Automation" )
' Create a ConnectionOptions object
Set objOptions = objWSMan.CreateConnectionOptions
objOptions.Password = "<password>"
```



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**ConnectionOptions**](connectionoptions.md)
</dt> </dl>

 

 






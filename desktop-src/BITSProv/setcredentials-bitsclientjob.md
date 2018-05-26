---
title: SetCredentials method of the BitsClientJob class
description: The SetCredentials method identifies the Target parameter, the authentication scheme, and the user credentials to use for user authentication requests.
ms.assetid: 69ae8c36-11e6-4030-9b38-006c4a5bfc07
keywords:
- SetCredentials method
- SetCredentials method, BitsClientJob class
- BitsClientJob class, SetCredentials method
topic_type:
- apiref
api_name:
- BitsClientJob.SetCredentials
api_location:
- Root\microsoft\bits
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SetCredentials method of the BitsClientJob class

The **SetCredentials** method identifies the *Target* parameter, the authentication scheme, and the user credentials to use for user authentication requests.

## Syntax


```mof
uint32 SetCredentials(
  [in] Uint16 Target,
  [in] Uint16 Scheme,
  [in] string UserName,
  [in] string Password
);
```



## Parameters

<dl> <dt>

*Target* \[in\]
</dt> <dd>

Specifies whether the destination is either a server or a proxy. The *Target* parameter can be set to the following values:



| Value                                                                        | Meaning           |
|------------------------------------------------------------------------------|-------------------|
| <dl> <dt>0</dt> </dl> | Server<br/> |
| <dl> <dt>1</dt> </dl> | Proxy<br/>  |



 

</dd> <dt>

*Scheme* \[in\]
</dt> <dd>

Specifies the authentication scheme to use. The *Scheme* parameter can be set to one of the following values:



| Scheme                                                                       | Meaning                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Basic is a scheme in which the username and password are sent in clear text to the server or proxy.<br/>                                                                                                                                         |
| <dl> <dt>1</dt> </dl> | Digest is a challenge-response scheme that uses a server-specified data string for the challenge.<br/>                                                                                                                                           |
| <dl> <dt>2</dt> </dl> | NTLM is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.<br/>                                                                                                        |
| <dl> <dt>3</dt> </dl> | Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine the scheme to use for authentication. For example, this value allows negotiation to determine whether the Kerberos protocol or NTLM is used.<br/> |
| <dl> <dt>4</dt> </dl> | Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.<br/>                                                                                                                         |



 

</dd> <dt>

*UserName* \[in\]
</dt> <dd>

A **null**-terminated string that contains the user name to authenticate.

</dd> <dt>

*Password* \[in\]
</dt> <dd>

A **null**-terminated string that contains the password in clear text. The *password* parameter can be empty. This parameter should be set to **NULL** if the *UserName* parameter is **NULL**.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 






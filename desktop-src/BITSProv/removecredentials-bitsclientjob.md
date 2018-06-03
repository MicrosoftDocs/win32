---
title: RemoveCredentials method of the BitsClientJob class
description: The RemoveCredentials method removes the credentials from the Target parameter.
ms.assetid: 202f40f7-1663-4a67-b71d-f57b3c181852
keywords:
- RemoveCredentials method
- RemoveCredentials method, BitsClientJob class
- BitsClientJob class, RemoveCredentials method
topic_type:
- apiref
api_name:
- BitsClientJob.RemoveCredentials
api_location:
- bits1_5.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveCredentials method of the BitsClientJob class

The **RemoveCredentials** method removes the credentials from the *Target* parameter.

## Syntax


```mof
uint32 RemoveCredentials(
  [in] Uint16 Target,
  [in] Uint16 Scheme
);
```



## Parameters

<dl> <dt>

*Target* \[in\]
</dt> <dd>

Specifies destination where the credentials will be removed. The *Target* parameter can be set to the following values:



| Value                                                                        | Meaning           |
|------------------------------------------------------------------------------|-------------------|
| <dl> <dt>0</dt> </dl> | Server<br/> |
| <dl> <dt>1</dt> </dl> | Proxy<br/>  |



 

</dd> <dt>

*Scheme* \[in\]
</dt> <dd>

Specifies the authentication scheme to remove. The *Scheme* parameter can be set to one of the following values:



| Scheme                                                                       | Meaning                                                                                                                                                                                                                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | Basic is a scheme in which the user name and password are sent in clear text to the server or proxy.<br/>                                                                                                                                        |
| <dl> <dt>1</dt> </dl> | Digest is a challenge-response scheme that uses a server-specified data string for the challenge.<br/>                                                                                                                                           |
| <dl> <dt>2</dt> </dl> | NTLM is a challenge-response scheme that uses the credentials of the user for authentication in a Windows-based network environment.<br/>                                                                                                        |
| <dl> <dt>3</dt> </dl> | Negotiate is a challenge-response scheme that negotiates with the server or proxy to determine the scheme to use for authentication. For example, this value allows negotiation to determine whether the Kerberos protocol or NTLM is used.<br/> |
| <dl> <dt>4</dt> </dl> | Passport is a centralized authentication service provided by Microsoft that offers a single logon for member sites.<br/>                                                                                                                         |



 

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                           |
| Redistributable<br/>          | Windows Management Framework on Windows Server 2008 with SP2<br/>                     |
| Namespace<br/>                | Root\\microsoft\\bits<br/>                                                            |
| Header<br/>                   | <dl> <dt>Bits1\_5.h</dt> </dl>       |
| MOF<br/>                      | <dl> <dt>BitsProvider.mof</dt> </dl> |



## See also

<dl> <dt>

[**BitsClientJob**](bitsclientjob.md)
</dt> </dl>

 

 






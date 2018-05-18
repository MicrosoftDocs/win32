---
title: ProtectedFileInputStream.create synchronous method
description: Synchronously creates a ProtectedFileInputStream object from an existing protected file.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '1BAB8D06-5F26-4549-BC54-7A7C121E3A59'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedFileInputStream.create synchronous method"]
topic_type:
- apiref
api_name:
- ProtectedFileInputStream.create synchronous method
api_type:
- NA
---

# ProtectedFileInputStream.create synchronous method

Synchronously creates a [**ProtectedFileInputStream**](protectedfileinputstream-class-java.md) object from an existing protected file.

## Signature

``` syntax
public static ProtectedFileInputStream create(InputStream inputStream,
                                       String userId,
                                       AuthenticationRequestCallback authenticationContext,
                                       ConsentCallback consentCallback,
                                       int policyAcquisitionFlags,
                                       Context applicationContext)
            throws ProtectionException
```

## Parameters



| Name                                | Datatype                                                                                         | Notes                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *inputStream*<br/>            | **InputStream**<br/>                                                                       | input stream with the protected content<br/>                                                                                                                                                                                                                                                                                                                                                  |
| *userId*<br/>                 | **String**<br/>                                                                            | Optional.<br/> A *userId* is used for caching a user policy for offline usage. For multiple user scenarios, caller must supply a *userId*.<br/> If *userId* is null, then the user policy is cached without *userId* and is retrievable with null *userId* as well. A null *userId* also retrieves any matching offline user policy cached without *userId* or any *userId*.<br/> |
| *authenticationContext*<br/>  | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/> |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *consentCallback*<br/>        | [**ConsentCallback**](https://msdn.microsoft.com/library/windows/desktop/dn833503)<br/>                     |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *policyAcquisitionFlags*<br/> | **int**<br/>                                                                               | See [**PolicyAcquisitionFlags**](policyacquisitionflags-class-java.md)s for more information.<br/>                                                                                                                                                                                                                                                                                           |
| *applicationContext*<br/>     | **Context**<br/>                                                                           |                                                                                                                                                                                                                                                                                                                                                                                                     |



 

## Returns

[**ProtectedFileInputStream**](protectedfileinputstream-class-java.md)

## Throws

[**ProtectionException**](protectionexception-class-java.md)

## Defined in

ProtectedFileInputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 






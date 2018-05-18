---
title: ProtectedFileInputStream.create asynchronous method
description: Asynchronously implements a wrapper of the input stream allowing reading of an RMS protected input stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '6C144D28-638C-466F-B55A-5ADFBA2D571C'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectedFileInputStream.create asynchronous method"]
topic_type:
- apiref
api_name:
- ProtectedFileInputStream.create asynchronous method
api_type:
- NA
---

# ProtectedFileInputStream.create asynchronous method

Asynchronously implements a wrapper of the input stream allowing reading of an RMS protected input stream.

## Signature

``` syntax
public static IAsyncControl create(InputStream inputStream,
                                   String userId,
                                   AuthenticationRequestCallback authenticationContext,
                                   ConsentCallback consentCallback,
                                   int policyAcquisitionFlags,
                                   CreationCallback<ProtectedFileInputStream> callback) 
        throws InvalidParameterException
```

## Parameters



| Name                                | Datatype                                                                                                       | Notes                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *inputStream*<br/>            | **InputStream**<br/>                                                                                     | input stream with the protected content<br/>                                                                                                                                                                                                                                                                                                                                                  |
| *userId*<br/>                 | **String**<br/>                                                                                          | Optional.<br/> A *userId* is used for caching a user policy for offline usage. For multiple user scenarios, caller must supply a *userId*.<br/> If *userId* is null, then the user policy is cached without *userId* and is retrievable with null *userId* as well. A null *userId* also retrieves any matching offline user policy cached without *userId* or any *userId*.<br/> |
| *authenticationContext*<br/>  | [**AuthenticationRequestCallback**](authenticationrequestcallback-interface-java.md)<br/>               |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *consentCallback*<br/>        | [**ConsentCallback**](https://msdn.microsoft.com/library/windows/desktop/dn833503)<br/>                                   |                                                                                                                                                                                                                                                                                                                                                                                                     |
| *policyAcquisitionFlags*<br/> | **int**<br/>                                                                                             | See [**PolicyAcquisitionFlags**](policyacquisitionflags-class-java.md)s for more information.<br/>                                                                                                                                                                                                                                                                                           |
| *callback*<br/>               | **CreationCallback**&lt;[**ProtectedFileInputStream**](protectedfileinputstream-class-java.md)&gt;<br/> | The created item<br/>                                                                                                                                                                                                                                                                                                                                                                         |



 

## Returns

An [**IAsyncControl**](iasynccontrol-interface.md) if an asynchronous operation is in progress else null is returned

## Throws

Throws exception if no callback is available that [**onFailure**](authenticationcompletioncallback-onfailure-method-java.md) can be called.

## Defined in

ProtectedFileInputStream.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

 

 






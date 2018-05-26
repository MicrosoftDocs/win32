---
title: ProtectedFileStream.AcquireAsync method
description: Creates a ProtectedFileStream object from a backing stream.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.ProtectedFileStream.AcquireAsync(Microsoft.RightsManagement.ProtectionPolicy,Windows.Storage.Streams.IRandomAccessStream,System.String,Microsoft.RightsManagement.ProtectionOperationOptions)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AcquireAsync method
- AcquireAsync method, ProtectedFileStream class
- ProtectedFileStream class, AcquireAsync method
topic_type:
- apiref
api_name:
- Microsoft.Protection.ProtectedFileStream.AcquireAsync
api_location:
- Microsoft.Protection.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ProtectedFileStream.AcquireAsync method

Creates a [**ProtectedFileStream**](protectedfilestream.md) object from a backing stream. This method is used to open a protected file. The protected file is loaded from the specified backing stream. After [**ProtectedFileStream**](protectedfilestream.md) object is created, apps can use [**ProtectedFileStream::Policy**](protectedfilestream-policy.md) property to get the [**UserPolicy**](userpolicy.md) object that defines the policy used to protect the protected file. The resulting **ProtectedFileStream** can be used to read the contents of the protected file (as a regular IRandomAccessStream).

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

> \[!Warning\]  
> This method must be called on a UI thread. Calling it on a worker thread may result in an unexpected behavior.

 

## Syntax


```C++
public:
static 
      IAsyncOperation<GetProtectedFileStreamResult> AcquireAsync(
  IRandomAccessStream^ stream, 
  
      String
      userId, 
  IAuthenticationCallback^ authenticationCallback, 
  IConsentCallback^ consentCallback, 
  PolicyAcquisitionOptions options
)
```



## Parameters

<dl> <dt>

*stream* 
</dt> <dd>

Type: [IRandomAccessStream](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.irandomaccessstream)

The backing stream where the protected file is loaded from.

</dd> <dt>

*userId* 
</dt> <dd>

Type: **String**

The email address of the user that is trying to consume the protected content.

This email address will be used to determine which policy object to use from the offline cache.

If a policy object for this user is not found in the offline cache then this API will go online (if allowed) to get the policy object.

If null is passed, the first policy object found in the offline cache will be used. And again if there is no policy object found for this content in the offline cache, this API will go online to get the policy object.

This parameter is also used as a hint for [**userId**](authenticationparameters-userid.md) for user authentication, i.e., it will be passed to the [**IAuthenticationCallback.GetTokenAsync**](iauthenticationcallback-gettokenasync.md) in the [**AuthenticationParameters**](authenticationparameters.md) structure.

</dd> <dt>

*authenticationCallback* 
</dt> <dd>

Type: [**IAuthenticationCallback**](iauthenticationcallback.md)

Authentication callback to be used for auth

</dd> <dt>

*consentCallback* 
</dt> <dd>

Type: [**IConsentCallback**](iconsentcallback.md)

Consent callback user for user consent process

</dd> <dt>

*options* 
</dt> <dd>

Type: [**PolicyAcquisitionOptions**](policyacquisitionoptions.md)

Possible offline flag.

</dd> </dl>

## Return value

Type: **IAsyncOperation(GetProtectedFileStreamResult)**

The asynchronous operation. Upon completion, **IAsyncOperation.GetResults** returns a [**ProtectedFileStream**](protectedfilestream.md) object that can be used to write content to the protected file.

## Remarks

> \[!Warning\]  
> To avoid data loss and/or corruption, [**FlushAsync**](protectedfilestream-flushasync.md) must be called if you modify the created stream or before object disposal.

 

> \[!Warning\]  
> This method must be called on a UI thread. Calling it on a worker thread may result in an unexpected behavior.

 

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::Protection<br/>                                                                            |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**ProtectedFileStream**](protectedfilestream.md)
</dt> </dl>

 

 






---
title: UserPolicy.AcquireAsync method
description: Acquire a policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.UserPolicy.AcquireAsync(Windows.Storage.Streams.IBuffer,System.String,Microsoft.RightsManagement.IAuthenticationCallback,Microsoft.RightsManagement.PolicyAcquisitionOptions)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- AcquireAsync method
- AcquireAsync method, UserPolicy class
- UserPolicy class, AcquireAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.AcquireAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.AcquireAsync method

Acquire a policy.

## Syntax


```C++
public:
static IAsyncOperation<GetUserPolicyResult>^ AcquireAsync(
  IBuffer^ serializedPolicy, 
  String^ userId, 
  IAuthenticationCallback^ authenticationCallback, 
  IConsentCallback^ consentCallback, 
  PolicyAcquisitionOptions options
)
```



## Parameters

<dl> <dt>

*serializedPolicy* 
</dt> <dd>

Type: [IBuffer](https://msdn.microsoft.com/library/windows/apps/windows.storage.streams.iinputstream.aspx)

the PL to be consumed

</dd> <dt>

*userId* 
</dt> <dd>

Type: [String](https://msdn.microsoft.com/library/system.string.aspx)

The email address of the user that is trying to consume the protected content.

This email address will be used to determine which policy object to use from the offline cache.

If a policy object for this user is not found in the offline cache then this API will go online (if allowed) to get the policy object.

If null is passed, the first policy object found in the offline cache will be used. And again if there is no policy object found for this content in the offline cache, this API will go online to get the policy object.

This parameter is also used as a hint for [**userId**](authenticationparameters-userid.md) for user authentication, i.e., it will be passed to the [**IAuthenticationCallback.GetTokenAsync()**](iauthenticationcallback-gettokenasync.md) in the [**AuthenticationParameters**](authenticationparameters.md) structure.

</dd> <dt>

*authenticationCallback* 
</dt> <dd>

Type: [**IAuthenticationCallback**](iauthenticationcallback.md)

Authentication callback to be used for authentication process.

</dd> <dt>

*consentCallback* 
</dt> <dd>

Type: [**IConsentCallback**](iconsentcallback.md)

Consent callback user for user consent process

</dd> <dt>

*options* 
</dt> <dd>

Type: [**PolicyAcquisitionOptions**](policyacquisitionoptions.md)

offline flag

</dd> </dl>

## Return value

Type: [**GetUserPolicyResult**](getuserpolicyresult.md)

The asynchronous operation. Upon completion, [IAsyncOperation](https://msdn.microsoft.com/library/windows/apps/br206598.aspx).GetResults returns a [**GetUserPolicyResult**](getuserpolicyresult.md) object.

## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



## See also

<dl> <dt>

[**UserPolicy**](userpolicy.md)
</dt> </dl>

 

 






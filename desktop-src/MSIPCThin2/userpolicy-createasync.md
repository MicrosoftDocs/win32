---
title: UserPolicy.CreateAsync method
description: Create a custom protection policy.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.UserPolicy.CreateAsync(Microsoft.RightsManagement.PolicyDescriptor,System.String,Microsoft.RightsManagement.IAuthenticationCallback,Microsoft.RightsManagement.UserPolicyCreationOptions)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CreateAsync method
- CreateAsync method, UserPolicy class
- UserPolicy class, CreateAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.CreateAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UserPolicy.CreateAsync method

Create a custom protection policy.

## Syntax


```C++
public:
static UserPolicy^ CreateAsync(
  PolicyDescriptor^ policyDescriptor, 
  String^ userId, 
  IAuthenticationCallback^ authenticationCallback, 
  UserPolicyCreationOptions options
)
```



## Parameters

<dl> <dt>

*policyDescriptor* 
</dt> <dd>

Type: [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762)

a [**PolicyDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920762) object which defines the policy.

</dd> <dt>

*userId* 
</dt> <dd>

Type: [String](https://msdn.microsoft.com/library/system.string.aspx)

The email address of the user that is protecting the content.

This email address will be used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using. This parameter is also used as a hint for userId for user authentication, i.e., it will be passed to the [**IAuthenticationCallback.GetTokenAsync**](iauthenticationcallback-gettokenasync.md)() in the [**AuthenticationParameters**](authenticationparameters.md) structure.

</dd> <dt>

*authenticationCallback* 
</dt> <dd>

Type: [**IAuthenticationCallback**](iauthenticationcallback.md)

Authentication callback to be used for authentication.

</dd> <dt>

*options* 
</dt> <dd>

Type: [**UserPolicyCreationOptions**](userpolicycreationoptions.md)

Options for creating protection policy object. For more information, see [**UserPolicyCreationOptions**](userpolicycreationoptions.md).

</dd> </dl>

## Return value

Type: [**UserPolicy**](userpolicy.md)

A [**UserPolicy**](userpolicy.md) object.

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

 

 






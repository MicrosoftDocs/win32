---
title: UserPolicy.CreateFromTemplateDescriptorAsync method
description: Publishing using templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: M:Microsoft.RightsManagement.UserPolicy.CreateFromTemplateDescriptorAsync(Microsoft.RightsManagement.TemplateDescriptor,System.String,Microsoft.RightsManagement.IAuthenticationCallback,Microsoft.RightsManagement.UserPolicyCreationOptions)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CreateFromTemplateDescriptorAsync method
- CreateFromTemplateDescriptorAsync method, UserPolicy class
- UserPolicy class, CreateFromTemplateDescriptorAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.UserPolicy.CreateFromTemplateDescriptorAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UserPolicy.CreateFromTemplateDescriptorAsync method

Publishing using templates

## Syntax


```C++
public:
static IAsyncOperation<UserPolicy>^ CreateFromTemplateDescriptorAsync(
  TemplateDescriptor templateDescriptor, 
  String^ userId, 
  IAuthenticationCallback authenticationCallback, 
  UserPolicyCreationOptions options, 
  IMapView<String^, String^>^                                                 signedAppData
)
```



## Parameters

<dl> <dt>

*templateDescriptor* 
</dt> <dd>

Type: **TemplateDescriptor**

The template from which the policy is being created.

</dd> <dt>

*userId* 
</dt> <dd>

Type: [String](https://msdn.microsoft.com/library/system.string.aspx)

The email address of the user that is protecting the content.

This email address will be used to discover the RMS service instance either ADRMS server or Azure RMS) that the user's organization is using.

This parameter is also used as a hint for userId for user authentication, i.e., it will be passed to the [**IAuthenticationCallback.GetTokenAsync**](iauthenticationcallback-gettokenasync.md) in the [**AuthenticationParameters**](authenticationparameters.md) structure.

</dd> <dt>

*authenticationCallback* 
</dt> <dd>

Type: **IAuthenticationCallback**

Authentication callback to be used for auth

</dd> <dt>

*options* 
</dt> <dd>

Type: [**UserPolicyCreationOptions**](userpolicycreationoptions.md)

Options for creating protection policy object. For more information, see [**UserPolicyCreationOptions**](userpolicycreationoptions.md).

</dd> <dt>

 *signedAppData* 
</dt> <dd>

Type: **IMapView&lt;String^, String^&gt;^**

Singed App data to be stored with this template

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

 

 






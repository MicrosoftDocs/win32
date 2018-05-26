---
title: TemplateDescriptor.GetTemplateListAsync method
description: Get the templates.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.TemplateDescriptor.GetTemplateListAsync(System.String,Microsoft.RightsManagement.IIAuthenticationCallback)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetTemplateListAsync method
- GetTemplateListAsync method, TemplateDescriptor class
- TemplateDescriptor class, GetTemplateListAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.TemplateDescriptor.GetTemplateListAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TemplateDescriptor.GetTemplateListAsync method

Get the templates.

## Syntax


```C++
public:
static IAsyncOperation<IIterable<TemplateDescriptor>>^ GetTemplateListAsync(
  String^ userId, 
  IAuthenticationCallback^ authenticationCallback
)
```



## Parameters

<dl> <dt>

*userId* 
</dt> <dd>

Type: **String**

The email address of the user for whom the templates are being retrieved.

This email address will be used to discover the RMS service instance (either ADRMS server or Azure RMS) that the user's organization is using.

This parameter is also used as a hint for [**userId**](authenticationparameters-userid.md) for user authentication, i.e., it will be passed to the [**IAuthenticationCallback.GetTokenAsync**](iauthenticationcallback-gettokenasync.md) in the [**AuthenticationParameters**](authenticationparameters.md) structure.

</dd> <dt>

*authenticationCallback* 
</dt> <dd>

Type: [**IAuthenticationCallback**](iauthenticationcallback.md)

An authentication callback to be used for authentication process.

</dd> </dl>

## Return value

Type: [**TemplateDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920793)

A list of templates as a collection of [**TemplateDescriptor**](https://msdn.microsoft.com/library/windows/desktop/dn920793) objects.

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

[**TemplateDescriptor**](templatedescriptor.md)
</dt> </dl>

 

 






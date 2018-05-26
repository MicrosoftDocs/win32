---
title: IAuthenticationCallback.GetTokenAsync method
description: Apps must implement this method to authenticate and return an access token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: MMicrosoft.RightsManagement.IAuthenticationCallback.GetTokenAsync(Microsoft.RightsManagement.AuthenticationParameters)
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- GetTokenAsync method
- GetTokenAsync method, IAuthenticationCallback class
- IAuthenticationCallback class, GetTokenAsync method
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IAuthenticationCallback.GetTokenAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IAuthenticationCallback.GetTokenAsync method

Apps must implement this method to authenticate and return an access token.

## Syntax


```C++
public:
IAsyncOperation<String^>^ GetTokenAsync(
  AuthenticationParameters^ authenticationParameters
)
```



## Parameters

<dl> <dt>

*authenticationParameters* 
</dt> <dd>

Type: [**AuthenticationParameters**](authenticationparameters.md)

Information required to authenticate

</dd> </dl>

## Return value

Type: [IAsyncOperation&lt;String^&gt;^](https://msdn.microsoft.com/library/windows/apps/br206598.aspx)

The asynchronous operation. Upon completion, [IAsyncOperation](https://msdn.microsoft.com/library/windows/apps/br206598.aspx).GetResults returns an access token.

## Remarks

This method is modeled after the .NET method [AuthenticationContext.AcquireToken](https://msdn.microsoft.com/library/dn528706.aspx).

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

[**IAuthenticationCallback**](iauthenticationcallback.md)
</dt> </dl>

 

 






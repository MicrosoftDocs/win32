---
title: IAuthenticationCallback interface
description: Interface for getting access token.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: TMicrosoft.RightsManagement.IAuthenticationCallback
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IAuthenticationCallback interface
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IAuthenticationCallback
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IAuthenticationCallback interface

Interface for getting access token. Apps should implement this interface and pass it to the APIs that do authenticated REST calls.

## Syntax


```C++
public interface class IAuthenticationCallback : IInspectable
```



## Members

The **IAuthenticationCallback** interface inherits from [IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821). **IAuthenticationCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAuthenticationCallback** interface has these methods. It also inherits methods from the **Object** class.



| Method                                                         | Description                                                                 |
|:---------------------------------------------------------------|:----------------------------------------------------------------------------|
| [**GetTokenAsync**](iauthenticationcallback-gettokenasync.md) | Apps must implement this method to authenticate and return an access token. |



 

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

[IInspectable](https://msdn.microsoft.com/library/windows/apps/br205821)
</dt> </dl>

 

 






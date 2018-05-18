---
title: IConsentCallback.ConsentAsync method
description: You, the app developer, will implement this method to prompt the user for their consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'M:Microsoft.RightsManagement.IConsentCallback.ConsentAsync'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ConsentAsync method", "ConsentAsync method, IConsentCallback class", "IConsentCallback class, ConsentAsync method"]
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IConsentCallback.ConsentAsync
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
---

# IConsentCallback.ConsentAsync method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

You, the app developer, will implement this method to prompt the user for their consent. This method then returns a collection of [**IConsent**](iconsent.md) objects are used for managing the user consent process.

## Syntax


```C++
public:
IAsyncOperation<IIterable<IConsent^>^ ConsentAsync(
  IIterable<IConsent^>^ consents
)
```



## Parameters

<dl> <dt>

*consents* 
</dt> <dd>

Type: [**IConsent**](iconsent.md)

Collection of [**IConsent**](iconsent.md) objects

</dd> </dl>

## Return value

Type: **IAsyncOperation&lt;IIterable&lt;IConsent^&gt;^**

The asynchronous operation. Upon completion, [IAsyncOperation](https://msdn.microsoft.com/library/windows/apps/br206598.aspx).GetResults returns a collection via [IIterable](https://msdn.microsoft.com/library/br205825.aspx) of [**IConsent**](iconsent.md) objects.

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

[**IConsentCallback**](iconsentcallback.md)
</dt> <dt>

[**IConsent**](iconsent.md)
</dt> </dl>

 

 






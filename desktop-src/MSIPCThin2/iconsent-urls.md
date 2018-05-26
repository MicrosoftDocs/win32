---
title: IConsent.Urls property
description: Gets the list of URLs that need to provide consent.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: PMicrosoft.RightsManagement.IConsent.Urls
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- Urls property
- Urls property, IConsent class
- IConsent class, Urls property
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.IConsent.Urls
- Microsoft.RightsManagement.IConsent.
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IConsent.Urls property

Gets the list of URLs that need to provide consent.

## Syntax


```C++
public:
property IVector<Uri^>^  Urls { 
   IVector<Uri^>^  get();
}
```



## Property value

Type: **IVector&lt;Uri^&gt;^**

List of URLs that need to provide consent.

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

[**IConsent**](iconsent.md)
</dt> </dl>

 

 






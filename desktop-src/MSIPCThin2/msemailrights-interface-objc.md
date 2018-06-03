---
title: MSEmailRights Class
description: Rights that apply to emails.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 2d4fd508-d208-4169-896c-61e6680300cd
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSEmailRights Class
topic_type:
- apiref
api_name:
- MSEmailRights Class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSEmailRights Class

Rights that apply to emails.

## Signature

``` syntax
@interface MSEmailRights : NSObject
```

## Methods



| Name                                 | Description                                                                                                                                                                                                                                                    |
|--------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| +(**NSString**) extract;<br/>  | Specifies a right that allows content to be extracted from a protected email and placed in an unprotected, or a different protected, format. Same value as [**\[MSEditableDocumentRights extract\]**](mseditabledocumentrights-interface-objc.md).<br/> |
| +(**NSString**) forward;<br/>  | Specifies a right that allows a protected email message to be forwarded.<br/>                                                                                                                                                                            |
| +(**NSString**) print;<br/>    | Specifies a right that allows protected email content to be printed. Same value as [**\[MSEditableDocumentRights Print\]**](mseditabledocumentrights-interface-objc.md).<br/>                                                                           |
| +(**NSString**) reply;<br/>    | Specifies a right that allows a protected email message to be replied to with a message that includes a copy of the protected content.<br/>                                                                                                              |
| +(**NSString**) replyAll;<br/> | GSpecifiesets a right that allows reply-all to a protected email message with a message that includes a copy of the protected content.<br/>                                                                                                              |
| +(**NSArray**) all;<br/>       | Specifies a list of all the of rights that apply to emails.<br/>                                                                                                                                                                                         |



 

## Defined in

MSRight.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Remarks

For more information about the built-in rights and the usage restrictions associated with them that apps should observe, see [Built-in Rights Usage Restriction Reference](built-in-rights-usage-restriction-reference.md).

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 






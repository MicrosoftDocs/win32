---
title: MSCommonRights Class
description: Rights that are supported by all apps.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '7f299582-d4e5-4038-b93b-df252a358159'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["MSCommonRights Class"]
topic_type:
- apiref
api_name:
- MSCommonRights Class
api_type:
- NA
---

# MSCommonRights Class

Rights that are supported by all apps.

## Signature

``` syntax
@interface MSCommonRights : NSObject
```

## Methods



| Name                              | Description                                                                                                                |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| +(**NSString**) owner;<br/> | Specifies a right that represents content ownership. This right grants full control over the protected content.<br/> |
| +(**NSString**) view;<br/>  | Specifies a right that allows viewing of protected content.<br/>                                                     |



 

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

 

 






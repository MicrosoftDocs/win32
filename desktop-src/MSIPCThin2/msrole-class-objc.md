---
title: MSRole class
description: Defines the roles supported by the SDK.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 79B032AE-AEF8-49CF-93FC-4926A139DB5D
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSRole class
topic_type:
- apiref
api_name:
- MSRole class
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSRole class

Defines the roles supported by the SDK.

## Signature

``` syntax
@interface MSRole : MSSecureCodableObject
```

## Properties



| Name                                                       | Description                                                               |
|------------------------------------------------------------|---------------------------------------------------------------------------|
| [**viewer**](msrole-viewer-property-objc.md)<br/>   | User will only be able to view the document.<br/>                   |
| [**reviewer**](msrole-reviewer-property.md)<br/>    | User will only be able to view and edit the document.<br/>          |
| [**author**](msrole-author-property.md)<br/>        | User will be able to view, edit, copy, and print the document.<br/> |
| [**coOwner**](msrole-coowner-property-objc.md)<br/> | User will have all permissions; view, edit, copy and print.<br/>    |



 

## Defined in

MSRole.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 






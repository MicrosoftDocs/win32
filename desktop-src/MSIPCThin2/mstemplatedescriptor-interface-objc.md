---
title: MSTemplateDescriptor class
description: Represents a users template.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: C3C26E62-EE99-4C66-A767-FA0A6E6204F5
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSTemplateDescriptor class
topic_type:
- apiref
api_name:
- MSTemplateDescriptor class
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSTemplateDescriptor class

Represents a user's template.

## Signature

``` syntax
@interface MSTemplateDescriptor : NSSecureCodableObject
```

## Methods



| Name                                                                                                                                               | Description                   |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| [**templateListWithUserId**](mstemplatedescriptor-templatelistwithuserid-userid-authenticationcallback-completionblock-method-objc.md)<br/> | Gets the templates<br/> |



 

## Properties



| Name                                                                                     | Description                             |
|------------------------------------------------------------------------------------------|-----------------------------------------|
| [**templateName**](mstemplatedescriptor-name-property-objc.md)<br/>               | Name of this template<br/>        |
| [**templateDescription**](mstemplatedescriptor-description-property-objc.md)<br/> | Description of this template<br/> |
| [**templateId**](mstemplatedescriptor-templateid-property-objc.md)<br/>           | ID of this template<br/>          |



 

## Defined in

MSTemplateDescriptor.h

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.8<br/> |



 

## Thread Safety

Members of this class are not guaranteed to be thread safe.

 

 






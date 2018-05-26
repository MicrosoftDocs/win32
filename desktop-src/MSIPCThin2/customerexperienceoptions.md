---
title: CustomerExperienceOptions enumeration
description: Used to specify a logging option.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: TMicrosoft.RightsManagement.CustomerExperienceOptions
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- CustomerExperienceOptions enumeration
topic_type:
- apiref
api_name:
- Microsoft.RightsManagement.CustomerExperienceOptions
api_location:
- Microsoft.RightsManagement.dll
api_type:
- Assembly
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CustomerExperienceOptions enumeration

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Used to specify a logging option.

## Syntax


```C++
public enum class CustomerExperienceOptions
```



## Members

The **CustomerExperienceOptions** enumeration has these members.



| Member                    | Value                                            | Description                                |
|:--------------------------|:-------------------------------------------------|:-------------------------------------------|
| **LoggingEnabledUnknown** | UploadLoggingConsent::LOGGING\_ENABLED\_UNKNOWN  | logging status is unknown<br/>       |
| **LoggingEnabledNever**   | UploadLoggingConsent::LOGGING\_ENABLED\_NEVER    | logging is disabled permanently<br/> |
| **LoggingEnabledNotNow**  | UploadLoggingConsent::LOGGING\_ENABLED\_NOT\_NOW | logging is disabled temporarily<br/> |
| **LoggingEnabledNow**     | UploadLoggingConsent::LOGGING\_ENABLED\_NOW      | logging is enabled temporarily<br/>  |
| **LoggingEnabledAlways**  | UploadLoggingConsent::LOGGING\_ENABLED\_ALWAYS   | logging is enabled permanently<br/>  |



## Requirements



|                                     |                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                   |
| Minimum supported server<br/> | None supported<br/>                                                                                   |
| Minimum supported phone<br/>  | Windows Phone 8.1<br/>                                                                                |
| Namespace<br/>                | Microsoft::RightsManagement<br/>                                                                      |
| Metadata<br/>                 | <dl> <dt>Microsoft.RightsManagement.winmd</dt> </dl> |



 

 






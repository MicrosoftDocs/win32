---
title: MSMutableProtectedData protectedDataInFile withProtectionPolicy completionBlock method
description: Protects the receiver's data and creates a new MSMutableProtectedData object with the protected data and its metadata.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 82039d03-4dfb-4b90-a862-2c2f7996cdb1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- MSMutableProtectedData protectedDataInFile withProtectionPolicy completionBlock method
topic_type:
- apiref
api_name:
- MSMutableProtectedData protectedDataInFile withProtectionPolicy completionBlock method
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSMutableProtectedData protectedDataInFile:withProtectionPolicy:completionBlock method

Protects the receiver's data and creates a new [**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) object with the protected data and its metadata.

## Signature

``` syntax
- (void)protectedDataInFile:(NSString *)path
      originalFileExtension:(NSString *)originalFileExtension
       withProtectionPolicy:(MSUserPolicy *)userPolicy
            completionBlock:(void(^)(MSMutableProtectedData *data, NSError *error)
              )completionBlock;
```

## Parameters



| Name                               | Datatype                                                                                                                    | Notes                                                                                                                                                                                                                                                                      |
|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *path*<br/>                  | **NSString** \*<br/>                                                                                                  | Required. The path to the protected file.<br/>                                                                                                                                                                                                                       |
| *originalFileExtension*<br/> | **NSString** \*<br/>                                                                                                  | Required. <br/>                                                                                                                                                                                                                                                      |
| *userPolicy*<br/>            | [**MSUserPolicy**](msuserpolicy-interface-objc.md) \*<br/>                                                           | Required. The user policy to be used for protecting the receiver's data.<br/>                                                                                                                                                                                        |
| *completionBlock*<br/>       | [****void(^)(**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md) **\*data, NSError \*error)**<br/> | Required. Called with the following parameters when the method is completed:<br/> *data*   The protected data file object.<br/> *error*   If there is an error creating the data object, contains an **NSError** object that describes the problem.<br/> |



 

## Returns

Nothing.

## Defined in

## Supported Platforms



|                                              |                                  |
|----------------------------------------------|----------------------------------|
| **Minimum supported OS versions**<br/> | iOS 7.0 and OS X 10.7<br/> |



 

## See also

<dl> <dt>

[**MSMutableProtectedData**](msmutableprotecteddata-interface-objc.md)
</dt> </dl>

 

 






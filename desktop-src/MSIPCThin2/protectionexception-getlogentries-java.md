---
title: ProtectionException.getLogEntries method
description: Gets the available log entries and removes them from the internal queue.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: '468E75E1-15E4-4C77-8D81-B3FD4FEAE890'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["ProtectionException.getLogEntries method"]
topic_type:
- apiref
api_name:
- ProtectionException.getLogEntries method
api_type:
- NA
---

# ProtectionException.getLogEntries method

Gets the available log entries and removes them from the internal queue.

Log entries are set under the following conditions:

-   Application has not consented with the SDK to upload logs.
-   The operation is unauthenticated.

Null is returned in rest of the conditions.

## Signature

``` syntax
public String getLogEntries()
```

## Returns

**String**

## Defined in

ProtectionException.java

## Supported Platforms



|                                             |                                         |
|---------------------------------------------|-----------------------------------------|
| **Minimum supported OS version**<br/> | Android 4.0.3 (API level 15)<br/> |



 

## Package

com.microsoft.rightsmanagement.exceptions

 

 






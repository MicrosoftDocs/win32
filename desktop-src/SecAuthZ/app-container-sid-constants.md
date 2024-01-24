---
title: AppContainer SID constants (Winnt.h)
description: These values determine the application package authority.
ms.assetid: 047439EA-789B-41CF-87C2-66CFB3F20908
ms.topic: reference
ms.date: 07/20/2023
---

# App Container SID constants

The AppContainer-specific SID constants determine the application package authority. You *can* use these constants directly, but you likely don't need to define these AppContainer SIDs.

* **SECURITY_APP_PACKAGE_AUTHORITY** ({0,0,0,0,0,15})
* **SECURITY_APP_PACKAGE_BASE_RID** (0x00000002L)
* **SECURITY_BUILTIN_APP_PACKAGE_RID_COUNT** (2L)
* **SECURITY_APP_PACKAGE_RID_COUNT** (8L)
* **SECURITY_CAPABILITY_BASE_RID** (0x00000003L)
* **SECURITY_BUILTIN_CAPABILITY_RID_COUNT** (2L)
* **SECURITY_CAPABILITY_RID_COUNT** (5L)
* **SECURITY_BUILTIN_PACKAGE_ANY_PACKAGE** (0x00000001L) 

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 8 \[desktop apps only\] |
| Minimum supported server | Windows Server 2012 \[desktop apps only\] |
| Header | Winnt.h |

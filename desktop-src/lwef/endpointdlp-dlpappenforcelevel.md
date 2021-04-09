---
description: Specifies the enforcement level of an endpoint Data Loss Prevention (DLP) operation.
title: DlpAppEnforceLevel enumeration (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DlpAppEnforceLevel
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DlpAppEnforceLevel enumeration

Specifies the enforcement level of an endpoint Data Loss Prevention (DLP) operation.

## Syntax


```C++
typedef enum _DlpAppEnforceLevel {
    DlpAppEnforceLevelNone = 0, // No enforcement, DLP enforces operation.
    DlpAppEnforceLevelNotify,   // App send notifications on operation, DLP enforces operation.
    DlpAppEnforceLevelPrevent,  // Currently not supported (App allows or blocks operation, DLP enforces warning, eventing and UI). 
    DlpAppEnforceLevelFull,     // Currently not supported (App handles all enforcement (blocks operation, enforces warning, UI), DLP will only handle auditing.)
    DlpAppEnforceLevelCount,
}DlpAppEnforceLevel;
```


## Constants

<dl> <dt>

*DlpAppEnforceLevelNone* \[in\]
</dt> <dd>

No enforcement by the app. The DLP system will enforce the operation.

</dd> </dl>

<dl> <dt>

*DlpAppEnforceLevelNotify* \[in\]
</dt> <dd>

Tne app will use the DLP APIs to notify the DLP system about the operation. The DLP system will enforce the operation.

</dd> </dl>

<dl> <dt>

*DlpAppEnforceLevelPrevent* \[in\]
</dt> <dd>

Not supported in the current version.

</dd> </dl>

<dl> <dt>

*DlpAppEnforceLevelFull* \[in\]
</dt> <dd>

Not supported in the current version.

</dd> </dl>

<dl> <dt>

*DlpAppEnforceLevelCount* \[in\]
</dt> <dd>

The maximum value of the enumeration.

</dd> </dl>



## Remarks

Values from this enumeration are used by the [DLP_APP_OP_ENLIGHTENED_LEVEL](endpointdlp-dlp_app_op_enlightened_level.md) structure.


## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |


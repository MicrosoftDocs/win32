---
description: Associates an endpoint Data Loss Prevention (DLP) action with an enforcement level.
title: DLP_APP_OP_ENLIGHTENED_LEVEL structure (endpointdlp.h)
ms.topic: reference
ms.date: 03/18/2021
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DLP_APP_OP_ENLIGHTENED_LEVEL
api_type: 
- COM
api_location: 
- endpointdlp.h
---

# DLP_APP_OP_ENLIGHTENED_LEVEL structure

Associates an endpoint Data Loss Prevention (DLP) action with an enforcement level.

## Syntax


```C++
typedef struct _DLP_APP_OP_ENLIGHTENED_LEVEL{
    DlpActionType Operation;
    DlpAppEnforceLevel AppEnforcementLevel;
}DLP_APP_OP_ENLIGHTENED_LEVEL, *PDLP_APP_OP_ENLIGHTENED_LEVEL;
```


## Members

<dl> <dt>

*Operation* \[in\]
</dt> <dd>

A value from the [DlpActionType](endpointdlp-dlpactiontype.md) enumeration specifying the endpoint DLP action type.

</dd> </dl>

<dl> <dt>

*AppEnforcementLevel* \[in\]
</dt> <dd>

A value from the [DlpAppEnforceLevel](endpointdlp-dlpappenforcelevel.md) specifying the level of enforcement for the associated endpoint DLP action type.

</dd> </dl>





## Remarks

Pass an array of these structures into [DlpInitializeEnforcementMode](endpointdlp-dlpinitializeenforcementmode.md) to set the enforcement mode for a set of endpoint DLP operations.

## Requirements



| Requirement          |    Value                   |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1809 (10.0; Build 17763)           |


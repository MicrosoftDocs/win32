---
description: Under WIP policy, represents the enterprise context (such as enterprise IDs) of a process.
title: EDP_CONTEXT structure
ms.topic: reference
ms.date: 01/22/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EDP_CONTEXT
api_type: 
- HeaderDef
api_location: 
- None
---

# EDP_CONTEXT structure

Under WIP policy, represents the enterprise context (such as enterprise IDs) of a process.

## Syntax


```C++
typedef struct
{
    EDP_CONTEXT_STATES contextStates;
    ULONG allowedEnterpriseIdCount;
    PWSTR enterpriseIdForUIEnforcement;
    PWSTR allowedEnterpriseIds[1];
} EDP_CONTEXT;
```

## Members

### contextStates

States (flags) from the [EDP_CONTEXT_STATES](edp_context_states-enum.md) enumeration that apply to the WIP enterprise context.

### allowedEnterpriseIdCount

The number of enterprise IDs in *AllowedEnterpriseIds*.

### enterpriseIdForUIEnforcement

Enterprise ID of the current UI context of the process.

### allowedEnterpriseIds

List of all enterprise IDs the application is allowed to access the enterprise data of.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 





---
description: Specifies flags that apply to the WIP enterprise context of a process.
title: EDP_CONTEXT_STATES enumeration
ms.topic: reference
ms.date: 01/22/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EDP_CONTEXT_STATES
api_type: 
- HeaderDef
api_location: 
- None
---

# EDP_CONTEXT_STATES enumeration

Specifies flags that apply to the WIP enterprise context of a process.

## Syntax


```C++
typedef enum
{
    EDP_CONTEXT_NONE = 0x0,
    EDP_CONTEXT_IS_EXEMPT = 0x1,
    EDP_CONTEXT_IS_ENLIGHTENED = 0x2,
    EDP_CONTEXT_IS_UNENLIGHTENED_ALLOWED = 0x4,
    EDP_CONTEXT_IS_PERMISSIVE = 0x8,
    EDP_CONTEXT_IS_COPY_EXEMPT = 0x10,
    EDP_CONTEXT_IS_DENIED = 0x20,
} EDP_CONTEXT_STATES;

```

## Constants

### EDP_CONTEXT_NONE

WIP context is personal.

### EDP_CONTEXT_IS_EXEMPT

WIP context is exempt, which applies to system apps and processes.

### EDP_CONTEXT_IS_ENLIGHTENED

WIP context is enlightened, which indicates the app can handle both enterprise and personal data.

### EDP_CONTEXT_IS_UNENLIGHTENED_ALLOWED

WIP context is unenlightened allowed, which indicates the app can only handle enterprise data.

### EDP_CONTEXT_IS_PERMISSIVE

Indicates if an enlightened app is allowed to access enterprise network endpoints at all times.

### EDP_CONTEXT_IS_COPY_EXEMPT

Indicates if the app is allowed to perform file copy without protection.

### EDP_CONTEXT_IS_DENIED

WIP context indicates personal app.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 





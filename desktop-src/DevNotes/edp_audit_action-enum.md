---
description: Specifies audit actions for calls to EdpAuditAction.
title: EDP_AUDIT_ACTION enumeration
ms.topic: reference
ms.date: 01/22/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EDP_AUDIT_ACTION
api_type: 
- HeaderDef
api_location: 
- None
---

# EDP_AUDIT_ACTION enumeration

Specifies audit actions for calls to [EdpAuditAction](edpauditaction-function.md).

## Syntax


```C++
typedef enum {
    SystemGenerated = 0,
    FileDecrypt,
    CopyToLocation,
    SendToRecipient,
    Other,
    FileRead,
    NetworkAccess,
} EDP_AUDIT_ACTION;
```

## Constants

### SystemGenerated

Do not use.

### FileDecrypt

A WIP protected file was decrypted.

### CopyToLocation

WIP enterprise data was copied.

### SendToRecipient

WIP enterprise data was sent such as in email.

### FileRead

WIP protected file was read by a personal app or in a personal context.

### NetworkAccess

WIP enterprise network endpoint was accessed in a personal app or in a personal context.

### Other

For other cases.

## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 





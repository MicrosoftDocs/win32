---
description: Under WIP policy, includes a single identity that a file is protected to.
title: ENCRYPTION_PROTECTOR structure
ms.topic: reference
ms.date: 01/22/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ENCRYPTION_PROTECTOR
api_type: 
- HeaderDef
api_location: 
- None
---

# ENCRYPTION_PROTECTOR structure

Under WIP policy, includes a single identity that a file is protected to.

## Syntax


```C++
typedef struct _ENCRYPTION_PROTECTOR {
    DWORD TotalLength;
    SID * UserSid;
    PWSTR ProtectorDescriptor;
} ENCRYPTION_PROTECTOR, *PENCRYPTION_PROTECTOR;
```

## Members

### TotalLength

Total length of the **ENCRYPTION_PROTECTOR** in bytes.

### UserSid

The security identifier (SID) of the user the protector belongs to. For more information, see [SID (winnt.h)](/windows/win32/api/winnt/ns-winnt-sid)

### ProtectorDescriptor

Identity the file is protected to (such as contoso.com) from a WIP policy.


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 





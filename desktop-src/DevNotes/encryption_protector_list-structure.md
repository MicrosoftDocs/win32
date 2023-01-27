---
description: Under WIP policy, includes all the identities a file is protected to.
title: ENCRYPTION_PROTECTOR_LIST structure
ms.topic: reference
ms.date: 01/22/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ENCRYPTION_PROTECTOR_LIST
api_type: 
- HeaderDef
api_location: 
- None
---

# ENCRYPTION_PROTECTOR_LIST structure

Under WIP policy, includes all the identities a file is protected to.

## Syntax


```C++
typedef struct _ENCRYPTION_PROTECTOR_LIST {
    DWORD NumberOfProtectors;
    PENCRYPTION_PROTECTOR *Protectors;
} ENCRYPTION_PROTECTOR_LIST, *PENCRYPTION_PROTECTOR_LIST;
```

## Members

### NumberOfProtectors

Number of protectors in the *Protectors* array.

### Protectors

A pointer to an [ENCRYPTION_PROTECTOR](pencryption_protector-structure.md) structure.


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |




 

 





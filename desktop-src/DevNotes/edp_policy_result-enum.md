---
description: Specifies the result of a call to EdpCheckAccess.
title: EDP_POLICY_RESULT enumeration
ms.topic: reference
ms.date: 01/22/2022
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EDP_POLICY_RESULT
api_type: 
- HeaderDef
api_location: 
- None
---

# EDP_POLICY_RESULT enumeration

Specifies the result of a call to [EdpCheckAccess](edpcheckaccess-function.md).

## Syntax


```C++
typedef enum
{
    EdpPolicyResult_Unknown = 0,
    EdpPolicyResult_Allowed,
    EdpPolicyResult_Blocked,
    EdpPolicyResult_ConsentRequired,
    EdpPolicyResult_ConsentRequired_Add_Encryption,
    EdpPolicyResult_MaxValue
} EDP_POLICY_RESULT;
```

## Constants

### EdpPolicyResult_Unknown

Unused.

### EdpPolicyResult_Allowed

Transfer or sharing of data is allowed.

### EdpPolicyResult_Blocked

Transfer or sharing of data is unconditionally blocked.

### EdpPolicyResult_ConsentRequired

Transfer or sharing of data is allowed if the user consents.

### EdpPolicyResult_ConsentRequired_Add_Encryption

Same as *EdpPolicyResult_ConsentRequired*.

### EdpPolicyResult_MaxValue

Unused.


## Requirements

| Requirement | Value |
|-------------------------------------|-----------------------------------------|
| Minimum supported client | Windows 10                          |
| Minimum supported server | Windows 10                                |
| Header                   | None  |



 

 





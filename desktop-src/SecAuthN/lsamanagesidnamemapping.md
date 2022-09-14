---
UID: 
title: LsaManageSidNameMapping function
description: Adds or removes SID/name mappings from the mapping set registered with the LSA Lookup Service.
old-location: 
ms.assetid: na
ms.date: 04/10/2019
ms.keywords: 
ms.topic: reference
req.header: Ntsecapi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows XP [desktop apps only]
req.target-min-winversvr: Windows Server 2003 [desktop apps only]
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Secur32.lib
req.dll:
- Advapi32.dll
- API-MS-Win-DownLevel-AdvAPI32-l4-1-0.dll
- API-MS-Win-security-lsalookup-l2-1-1.dll
req.irql: 
topic_type:
- APIRef
api_type: 
api_location: 
api_name:
- LsaManageSidNameMapping
targetos: Windows
req.typenames: 
req.redist: 
---

# LsaManageSidNameMapping function

## Description

The **LsaManageSidNameMapping** function adds or removes SID/name mappings from the mapping set registered with the LSA Lookup Service.

```cpp
void WINAPI LsaManageSidNameMapping(
  _In_  LSA_SID_NAME_MAPPING_OPERATION_TYPE    OpType,
  _In_  PLSA_SID_NAME_MAPPING_OPERATION_INPUT  OpInput,
  _Out_ PLSA_SID_NAME_MAPPING_OPERATION_OUTPUT *OpOutput
);
```

## Parameters

### OpType [in]

Indicates if a this function is being called to add or remove an SID/name mapping.

### OpInput [in]

Indicates the domain, account, and SID values to use during this operation. Additional flags can also be set within this structure.

### OpOutput [out]

Contains a value of [LSA_SID_NAME_MAPPING_OPERATION_ERROR](/previous-versions/windows/desktop/legacy/dn280707(v=vs.85)) that indicates operation success or failure.

| Value | Meaning |
|-------|---------|
| **Success** | Operation is complete without error. |
| **NonMappingError** | An error unrelated to SID-name mapping has occurred. |
| **NameCollision** | Operation failure due to name collision. |
| **SidCollision** | Operation failure due to SID collision. |
| **DomainNotFound** | Corresponding domain not found. |
| **DomainSidPrefixMismatch** | Provided SID doesn't have the correct domain prefix. |
| **MappingNotFound** | Mapping not found in the cache. |

## Returns

If the mapping is inserted successfully, the return value is STATUS_SUCCESS.
Otherwise, if the function fails due to SID or name conflicts, STATUS_INVALID_PARAMETER error will be returned.

## Remarks

## See also

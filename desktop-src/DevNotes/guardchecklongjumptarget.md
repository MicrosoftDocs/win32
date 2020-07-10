---
UID: 
title: GuardCheckLongJumpTarget function
description: "Attempts to verify whether the target of a longjmp is valid."
old-location:
ms.assetid: na
ms.date: 04/02/2019
ms.keywords: 
ms.topic: reference
req.header: guardapiset.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
 - APIRef
api_type:
 - DllExport
api_location:
 - api-ms-win-core-guard-l1-1-0.dll
api_name:
 - GuardCheckLongJumpTarget
targetos: Windows
req.typenames: 
req.redist: 
---

# GuardCheckLongJumpTarget function

## Description

Attempts to verify whether the target of a [longjmp](/cpp/c-runtime-library/reference/longjmp) is valid for a process which has [Control Flow Guard (CFG)](../secbp/control-flow-guard.md) enabled.

If the target address corresponds to an image mapping, the valid targets are extracted for the binary.
The function uses those targets to validate the target.
If the binary does not have metadata that describes the set of valid *longjmp* targets, the function returns **TRUE**.

If the target address corresponds to a non-image mapping, as in JIT code, a global read-only policy is consulted to determine whether the jump is allowed.

## Parameters

### TargetAddress [in]

The target address for the jump.

### Flags [in]

Flags describing the operation to be performed on the address.
If you specify **GUARD_CHECK_LONGJUMP_NON_FATAL** (0x1), this function does not terminate the process if the target is invalid.

## Returns

**TRUE** if the target is valid, otherwise **FALSE**.

## Remarks

## See also

---
description: Describes the type of function table which a DYNAMIC_FUNCTION_TABLE represents
title: FUNCTION_TABLE_TYPE enumeration
ms.topic: reference
ms.date: 09/17/2024
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FUNCTION_TABLE_TYPE
api_type: 
- HeaderDef
api_location: 
- None
---

# FUNCTION_TABLE_TYPE enumeration

Describes the type of function table which a [**DYNAMIC\_FUNCTION\_TABLE**](dynamic_function_table_type.md) represents.

## Syntax

```C++
typedef enum _FUNCTION_TABLE_TYPE {
    RF_SORTED,
    RF_UNSORTED,
    RF_CALLBACK,
    RF_KERNEL_DYNAMIC
} FUNCTION_TABLE_TYPE;
```

## Constants

### RF_SORTED

Entries in `FunctionTable` are sorted by their address. These tables were added using [**RtlAddFunctionTable**](/windows/win32/api/winnt/nf-winnt-rtladdfunctiontable).

### RF_UNSORTED

Entries in `FunctionTable` are unsorted. These tables were added using [**RtlAddFunctionTable**](/windows/win32/api/winnt/nf-winnt-rtladdfunctiontable).

### RF_CALLBACK

The `FunctionTable` array is not allocated up front. Instead, values are provided via a callback. These table entries were added to the list using [**RtlInstallFunctionTableCallback**](/windows/desktop/api/WinNT/nf-winnt-rtlinstallfunctiontablecallback).

### RF_KERNEL_DYNAMIC

Entries in `FunctionTable` are sorted by their address and installed by [**RtlAddGrowableFunctionTable**](/windows/desktop/api/WinNT/nf-winnt-rtladdgrowablefunctiontable).

## Remarks

This enum has no associated import library or header file. Additional values may be added in the future without further notice.

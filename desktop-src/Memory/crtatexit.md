---
description: Registers a function to be executed on exit.
title: _crt_atexit
ms.topic: reference
ms.date: 11/21/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- _crt_atexit
api_type:
- DllExport
api_location:
- ucrtbase_enclave.dll
f1_keywords:
- _crt_atexit
helpviewer_keywords:
- _crt_atexit
---

# `_crt_atexit`

Registers a function to be executed on exit.

## Syntax

```cpp
int _crt_atexit(
    _PVFV const function
    )
```

## Parameters

*`function`*\
The function to be executed on exit.

## Returns

Returns 0 if successful, or a nonzero value if an error occurs.

## Remarks

This function modifies the global onexit table.

## Requirements

| Routine | Exported by |
|---|---|
| **`_crt_atexit`** | `<ucrtbase_enclave.dll>` |

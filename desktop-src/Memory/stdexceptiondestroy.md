---
description: Destroys the provided exception object.
title: __std_exception_destroy
ms.topic: reference
ms.date: 11/21/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- __std_exception_destroy
api_type:
- DllExport
api_location:
- ucrtbase_enclave.dll
f1_keywords:
- __std_exception_destroy
helpviewer_keywords:
- __std_exception_destroy
---

# `__std_exception_destroy`

Destroys the provided exception object.

## Syntax

```cpp
void __std_exception_destroy(
    __std_exception_data* const data
    )
```

## Parameters

*`data`*\
The exception to destroy.

## Remarks

## Requirements

| Routine | Exported by |
|---|---|
| **`__std_exception_destroy`** | `<ucrtbase_enclave.dll>` |

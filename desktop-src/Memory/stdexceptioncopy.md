---
description: Provides an exception pointer object that points to a copy of the provided exception.
title: __std_exception_copy
ms.topic: reference
ms.date: 11/21/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- __std_exception_copy
api_type:
- DllExport
api_location:
- ucrtbase_enclave.dll
f1_keywords:
- __std_exception_copy
helpviewer_keywords:
- __std_exception_copy
---

# `__std_exception_copy`

Provides an exception pointer object that points to a copy of the provided exception.

## Syntax

```cpp
void __std_exception_copy(
    __std_exception_data const* const from,
    __std_exception_data*       const to
    )
```

## Parameters

*`from`*\
The exception to copy.

*`to`*\
An exception pointer to a copy of its `from` argument.

## Remarks

In the C++ standard, this function was renamed to [make_exception_ptr](/cpp/parallel/concrt/reference/make-exception-ptr-function).

## Requirements

| Routine | Exported by |
|---|---|
| **`__std_exception_copy`** | `<ucrtbase_enclave.dll>` |

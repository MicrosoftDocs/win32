---
description: Called by the runtime when the program cannot continue.
title: __std_terminate
ms.topic: reference
ms.date: 11/21/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- __std_terminate
api_type:
- DllExport
api_location:
- ucrtbase_enclave.dll
f1_keywords:
- __std_terminate
helpviewer_keywords:
- __std_terminate
---

# `__std_terminate`

Called by the runtime when the program cannot continue. It may also be called directly.

## Syntax

```cpp
void __std_terminate();
```

## Remarks

When called due to a thrown exception, an implicit exception handler is considered active.

## Requirements

| Routine | Exported by |
|---|---|
| **`__std_terminate`** | `<ucrtbase_enclave.dll>` |

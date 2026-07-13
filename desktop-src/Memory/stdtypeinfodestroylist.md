---
description: This function is called during module unload to clean up all of the undecorated name strings that were allocated by calls to name.
title: __std_type_info_destroy_list
ms.topic: reference
ms.date: 11/21/2023
topic_type:
- APIRef
- kbSyntax
api_name:
- __std_type_info_destroy_list
api_type:
- DllExport
api_location:
- ucrtbase_enclave.dll
f1_keywords:
- __std_type_info_destroy_list
helpviewer_keywords:
- __std_type_info_destroy_list
---

# `__std_type_info_destroy_list`

This function is called during module unload to clean up all of the undecorated name strings that were allocated by calls to `name()`.

## Syntax

```cpp
void __std_type_info_destroy_list(
    __type_info_node* const root_node
    )
```

## Parameters

*`root_node`*\
The root node of the list.

## Remarks

## Requirements

| Routine | Exported by |
|---|---|
| **`__std_type_info_destroy_list`** | `<ucrtbase_enclave.dll>` |

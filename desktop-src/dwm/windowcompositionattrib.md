---
description: Specifies options used by the WINDOWCOMPOSITIONATTRIBDATA structure.
title: WINDOWCOMPOSITIONATTRIB structure
ms.topic: reference
ms.date: 02/20/2024
topic_type:
 - APIRef
 - kbSyntax
api_type:
 - HeaderDef
api_location:
 - N/A
api_name:
 - WINDOWCOMPOSITIONATTRIB
---

# WINDOWCOMPOSITIONATTRIB enumeration

Specifies options used by the [WINDOWCOMPOSITIONATTRIBDATA](windowcompositionattribdata.md) structure.

## Syntax

```C++
typedef enum {
    WCA_EXCLUDED_FROM_DDA               = 24
} WINDOWCOMPOSITIONATTRIB;

```

## Fields

`WCA_EXCLUDED_FROM_DDA`

Prevents a window from being captured by the Desktop Duplication API. The pvData member of the [WINDOWCOMPOSITIONATTRIBDATA](/windows/win32/direct3ddxgi/desktop-dup-api) structure points to a value of type BOOL. If the value is TRUE, the window is not captured. Otherwise, the window exhibits normal behavior.\






## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 10 version 1709 (build 16299)] |
| Minimum supported server | None supported |
| Header | N/A |


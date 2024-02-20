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

SPecifies options used by the [WINDOWCOMPOSITIONATTRIBDATA](windowscompositionattribdata.md) structure.

## Syntax

```C++
typedef enum {
    WCA_EXCLUDED_FROM_DDA               = 24
} WINDOWCOMPOSITIONATTRIB;

```

## Fields

`WCA\_EXCLUDED\_FROM\_DDA`

Prevents a window from being captured by the Desktop Duplication API. The pvData member of the [WINDOWCOMPOSITIONATTRIBDATA](/windows/win32/direct3ddxgi/desktop-dup-api) structure points to a value of type BOOL. If the value is TRUE, the window is not captured. Otherwise, the window exhibits normal behavior.\






## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 7 \[desktop apps only\] |
| Minimum supported server | None supported |
| End of client support | Windows 7 |
| Header | N/A |


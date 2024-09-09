---
description: Describes a key/value pair that specifies a window composition attribute and its value.
title: WINDOWCOMPOSITIONATTRIBDATA structure
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
 - WINDOWCOMPOSITIONATTRIBDATA
---

# WINDOWCOMPOSITIONATTRIBDATA structure

Describes a key/value pair that specifies a window composition attribute and its value. This structure is used with the [GetWindowCompositionAttribute](getwindowcompositionattribute.md) and [SetWindowCompositionAttribute](setwindowcompositionattribute.md) functions.

## Syntax

```C++
typedef struct tagWINDOWCOMPOSITIONATTRIBDATA {
    WINDOWCOMPOSITIONATTRIB Attrib;
    void* pvData;
    UINT cbData;
} WINDOWCOMPOSITIONATTRIBDATA;
```

## Fields

`Attrib`

A flag describing which value to get or set, specified as a value of the [WINDOWCOMPOSITIONATTRIB](windowcompositionattrib.md) enumeration. This parameter specifies which attribute to get or set, and the *pvData* member points to an object containing the attribute value.

`pvData`

When used with the **GetWindowCompositionAttribute** function, this member contains a pointer to a variable that will hold the value of the requested attribute when the function returns. When used with the **SetWindowCompositionAttribute** function, it points an object containing the attribute value to set. The type of the value set depends on the value of the Attrib member. For information about what type of value you should pass a pointer to in the *pvData* member, see [WINDOWCOMPOSITIONATTRIB](windowcompositionattrib.md).

`cbData`

The size of the object pointed to by the *pvData* member, in bytes.

## Requirements

| Requirement | Value |
|-|-|
| Minimum supported client | Windows 10 version 1709 (build 16299) |
| Minimum supported server | None supported |
| Header | N/A |


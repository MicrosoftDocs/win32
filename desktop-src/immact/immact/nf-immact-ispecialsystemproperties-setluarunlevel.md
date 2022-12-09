---
title: ISpecialSystemProperties::SetLUARunLevel
description: Sets the LUA run level.
keywords:
- SetLUARunLevel method COM
- SetLUARunLevel method COM , ISpecialSystemProperties interface
- ISpecialSystemProperties interface COM , SetLUARunLevel method
topic_type:
- apiref
api_name:
- ISpecialSystemProperties.SetLUARunLevel
api_location:
- N/A
api_type:
- COM
ms.topic: reference
ms.date: 12/08/2022
---

# ISpecialSystemProperties::SetLUARunLevel method

Sets the LUA run level.

## Syntax

```cpp
HRESULT SetLUARunLevel(
  [in] DWORD dwLUARunLevel,
  [in] ULONG_PTR hwnd
);
```

## Parameters

`dwLUARunLevel`

The LUA run level to set.

`hwnd`

Identifies the object on which to set the LUA run level.

## Return value

A standard **HRESULT** success or error code.

## Remarks

No header file declaring the **ISpecialSystemProperties::SetLUARunLevel** method is included in the Microsoft Windows Software Development Kit (SDK).

## Requirements

| Requirement | Value |
|-|-|
| Header | N/A |
| IDL | N/A |

## See also

* [**ISpecialSystemProperties**](nn-immact-ispecialsystemproperties.md)

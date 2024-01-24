---
title: ISpecialSystemProperties::SetLUARunLevel
description: Passes the requested Windows User Account Controls (UAC) run level (elevation level), and other parameters, through the COM activation pipeline.
keywords:
- SetLUARunLevel method COM
- SetLUARunLevel method COM , ISpecialSystemProperties interface
- ISpecialSystemProperties interface COM , SetLUARunLevel method
topic_type:
- apiref
api_name:
- ISpecialSystemProperties.SetLUARunLevel
api_location:
- ole32.dll
- rpcss.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/19/2023
---

# ISpecialSystemProperties::SetLUARunLevel method

This method is intended for internal Microsoft use; not recommended for use in applications.

Passes the requested Windows User Account Controls (UAC) run level (elevation level), and other parameters, through the COM activation pipeline. UAC was formerly known as Limited User Account (LUA).

## Syntax

```cpp
HRESULT SetLUARunLevel(
  [in] DWORD dwLUARunLevel,
  [in] ULONG_PTR hwnd
);
```

## Parameters

`dwLUARunLevel`

The UAC run level to set. If you define the enumerations shown below, then *dwLUARunLevel* can be either **RUNLEVEL_ADMIN**, **RUNLEVEL_HIGHEST**, or **INVALID_LUA_RUNLEVEL**.

```cpp
typedef enum _RUNLEVEL
{
    RUNLEVEL_LUA = 0,
    RUNLEVEL_HIGHEST,
    RUNLEVEL_ADMIN,
    RUNLEVEL_MAX_NON_UIA,

    RUNLEVEL_LUA_UIA = 16,
    RUNLEVEL_HIGHEST_UIA,
    RUNLEVEL_ADMIN_UIA,
    RUNLEVEL_MAX
}
RUNLEVEL;

typedef enum {  INVALID_LUA_RUNLEVEL = 0xFFFFFFFF } LUARUNLEVEL;
```

`hwnd`

Identifies the object on which to set the UAC run level.

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

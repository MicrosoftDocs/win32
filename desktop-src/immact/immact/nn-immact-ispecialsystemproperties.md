---
title: ISpecialSystemProperties interface
description: Used to pass the requested UAC run level through the COM activation pipeline.
keywords:
- ISpecialSystemProperties interface COM
- ISpecialSystemProperties interface COM , described
topic_type:
- apiref
api_name:
- ISpecialSystemProperties
api_location:
- ole32.dll
- rpcss.dll
api_type:
- COM
ms.topic: reference
ms.date: 01/19/2023
---

# ISpecialSystemProperties interface

This interface is intended for internal Microsoft use; not recommended for use in applications.

Used to pass the requested Windows User Account Controls (UAC) run level (elevation level) through the COM activation pipeline.

## Inheritance

The **ISpecialSystemProperties** interface derives from [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown).

## Methods

The **ISpecialSystemProperties** interface has these methods.

| Method | Description |
|:-|:-|
| [**SetLUARunLevel**](nf-immact-ispecialsystemproperties-setluarunlevel.md) | Passes the requested Windows User Account Controls (UAC) run level (elevation level), and other parameters, through the COM activation pipeline. |

## Remarks

No header file defining the **ISpecialSystemProperties** interface is included in the Microsoft Windows Software Development Kit (SDK).

## Requirements

| Requirement | Value |
|-|-|
| Header | N/A |
| IDL | N/A |

## See also

* [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)

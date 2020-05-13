---
title: IDXCoreAdapterFactory::IsNotificationTypeSupported
description: Determines whether a specified notification type is supported by the operating system (OS).
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::IsNotificationTypeSupported method

Determines whether a specified notification type is supported by the operating system (OS). For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsNotificationTypeSupported(
  DXCoreNotificationType notificationType) = 0;
```

## Parameters

### notificationType

Type: **[DXCoreNotificationType](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype)**

The type of notification that you're querying about support for. See the table in [DXCoreNotificationType](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype) for info about the notification types.

## Returns

Type: **bool**

Returns `true` if the notification type is supported by the system. Otherwise, returns `false`.

## Remarks

You can call **IsNotificationTypeSupported** to determine whether a given notification type is known to this version of the OS. For example, a notification type that's introduced in a particular version of Windows is unknown to previous versions of Windows.

## See also

[IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

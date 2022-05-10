---
title: PFN_DXCORE_NOTIFICATION_CALLBACK
description: A callback function (implemented by your application), which is called by a DXCore object for notification events.
ms.topic: reference
ms.date: 06/20/2019
---

# PFN_DXCORE_NOTIFICATION_CALLBACK callback

A callback function (implemented by your application), which is called by a DXCore object for notification events.

## Syntax

```cpp
typedef void (STDMETHODCALLTYPE *PFN_DXCORE_NOTIFICATION_CALLBACK)(
  DXCoreNotificationType notificationType,
  _In_ IUnknown *object,
  _In_opt_ void *context);
```

## Parameters

### notificationType

Type: **[DXCoreNotificationType](./ne-dxcore_interface-dxcorenotificationtype.md)**

The type of notification representing this invocation. See the table in [DXCoreNotificationType](./ne-dxcore_interface-dxcorenotificationtype.md) for info about what types are valid with which kinds of objects.

### object

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

The [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md) or [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md) object raising the notification.

### context [in]

Type: **void\***

A pointer, which may be `nullptr`, to an object containing context info.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

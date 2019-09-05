---
title: PFN_DXCORE_NOTIFICATION_CALLBACK
description: A callback function (implemented by your application), which is called by a DXCore object for notification events.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# PFN_DXCORE_NOTIFICATION_CALLBACK callback

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

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

Type: **[DXCoreNotificationType](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype)**

The type of notification representing this invocation. See the table in [DXCoreNotificationType](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype) for info about what types are valid with which kinds of objects.

### object

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

The [IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter) or [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) object raising the notification.

### context [in]

Type: **void\***

A pointer, which may be `nullptr`, to an object containing context info.

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

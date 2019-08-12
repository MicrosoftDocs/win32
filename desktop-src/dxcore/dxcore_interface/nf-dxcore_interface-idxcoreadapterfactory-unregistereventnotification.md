---
title: IDXCoreAdapterFactory::UnregisterEventNotification
description: Unregisters from a notification that you previously registered for.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::UnregisterEventNotification method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Unregisters from a notification that you previously registered for. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Parameters

### eventCookie

Type: **uint32_t**

The cookie value (returned when you called [IDXCoreAdapterFactory::RegisterEventNotification](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification)) representing a prior registration that you now wish to unregister for.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_INVALIDARG|The value of *eventCookie* is not a valid cookie representing a prior registration.|

## Remarks

**UnregisterEventNotification** returns only after all pending/in-progress callbacks for this registration have completed. DXCore guarantees that no new callbacks will occur for this registration after **UnregisterEventNotification** has returned. However, to avoid a deadlock, if you call **UnregisterEventNotification** from within your callback, then **UnregisterEventNotification** doesn't wait for the active callback to complete.

> [!IMPORTANT]
> Before you destroy the DXCore object represented by the *dxCoreObject* argument passed to [IDXCoreAdapterFactory::RegisterEventNotification](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification), you must use the cookie value to unregister that object from notifications by calling **UnregisterEventNotification**. If you don't do that, then a fatal exception is raised when the situation is detected.

Once you unregister a cookie value, that value is then eligible for being returned by a subsequent registration

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [IDXCoreAdapterFactory::UnregisterEventNotification](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

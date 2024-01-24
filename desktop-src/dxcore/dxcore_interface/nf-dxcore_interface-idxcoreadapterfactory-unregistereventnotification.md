---
title: IDXCoreAdapterFactory::UnregisterEventNotification
description: Unregisters from a notification that you previously registered for.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::UnregisterEventNotification method

Unregisters from a notification that you previously registered for. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE UnregisterEventNotification(
  uint32_t eventCookie) = 0;
```

## Parameters

### eventCookie

Type: **uint32_t**

The cookie value (returned when you called [IDXCoreAdapterFactory::RegisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md)) representing a prior registration that you now wish to unregister for.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|E_INVALIDARG|The value of *eventCookie* is not a valid cookie representing a prior registration.|

## Remarks

**UnregisterEventNotification** returns only after all pending/in-progress callbacks for this registration have completed. DXCore guarantees that no new callbacks will occur for this registration after **UnregisterEventNotification** has returned. However, to avoid a deadlock, if you call **UnregisterEventNotification** from within your callback, then **UnregisterEventNotification** doesn't wait for the active callback to complete.

> [!IMPORTANT]
> Before you destroy the DXCore object represented by the *dxCoreObject* argument passed to [IDXCoreAdapterFactory::RegisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md), you must use the cookie value to unregister that object from notifications by calling **UnregisterEventNotification**. If you don't do that, then a fatal exception is raised when the situation is detected.

Once you unregister a cookie value, that value is then eligible for being returned by a subsequent registration

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

---
title: IDXCoreAdapterFactory::RegisterEventNotification
description: Registers to receive notifications of specific conditions from a DXCore adapter or adapter list.
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterFactory::RegisterEventNotification method

Registers to receive notifications of specific conditions from a DXCore adapter or adapter list. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE RegisterEventNotification(
  _In_ IUnknown *dxCoreObject,
  DXCoreNotificationType notificationType,
  _In_ PFN_DXCORE_NOTIFICATION_CALLBACK callbackFunction,
  _In_opt_ void *callbackContext,
  _Out_ uint32_t *eventCookie) = 0;
```

## Parameters

### dxCoreObject [in]

Type: **[IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown)\***

The DXCore object ([IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md) or [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md)) whose notifications you're subscribing to.

### notificationType

Type: **[DXCoreNotificationType](./ne-dxcore_interface-dxcorenotificationtype.md)**

The type of notification that you're registering for. See the table in [DXCoreNotificationType](./ne-dxcore_interface-dxcorenotificationtype.md) for info about what types are valid with which kinds of objects.

### callbackFunction [in]

Type: **[PFN_DXCORE_NOTIFICATION_CALLBACK](./nc-dxcore_interface-pfn_dxcore_notification_callback.md)**

A pointer to a callback function (implemented by your application), which is called by the DXCore object for notification events. For the signature of the function, see [PFN_DXCORE_NOTIFICATION_CALLBACK](./nc-dxcore_interface-pfn_dxcore_notification_callback.md).

### callbackContext [in]

Type: **void\***

An optional pointer to an object containing context info. This object is passed to your callback function when the notification is raised.

### eventCookie [out]

Type: **uint32_t\***

A pointer to a **uint32_t** value. If successful, the function dereferences the pointer and sets the value to a non-zero cookie value representing this registration. Use this cookie value to unregister from the notification by calling [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md). See **Remarks**.

If unsuccessful, the function dereferences the pointer and sets the value to zero, which represents an invalid cookie value.

## Returns

Type: **[HRESULT](../../com/structure-of-com-error-codes.md)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](../../com/structure-of-com-error-codes.md) [error code](../../com/com-error-codes-10.md).

|Return value|Description|
|-|-|
|DXGI_ERROR_INVALID_CALL|*notificationType* is unsupported by the operating system (OS).|
|E_INVALIDARG|`nullptr` was provided for *dxCoreObject*, or if an invalid *notificationType* and *dxCoreObject* combination was provided.|
|E_POINTER|`nullptr` was provided for either *callbackFunction* or *eventCookie*.|

## Remarks

You use **RegisterEventNotification** to register for events raised by [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md) and [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md) interfaces. These notification types are supported.

|[DXCoreNotificationType](./ne-dxcore_interface-dxcorenotificationtype.md)|Supported *dxCoreObject*|Notes|
|-|-|-|
|AdapterListStale|**IDXCoreAdapterList**|Indicates that the list of adapters meeting your filter criteria has changed. If the adapter list is stale at the time of registration, then your callback is immediately called. This callback occurs at most one time per registration.|
|AdapterNoLongerValid|**IDXCoreAdapter**|Indicates that the adapter is no longer valid. If the adapter is invalid at registration time, then your callback is immediately called.|
|AdapterBudgetChange|**IDXCoreAdapter**|Indicates that a memory budgeting event has occurred, and that you should call [IDXCoreAdapter::QueryState](./nf-dxcore_interface-idxcoreadapter-querystate.md) (with [DXCoreAdapterState::AdapterMemoryBudget](./ne-dxcore_interface-dxcoreadapterstate.md)) to evaluate the current memory budget state. Upon registration, an initial callback will always occur to allow you to query the initial state.|
|AdapterHardwareContentProtectionTeardown|**IDXCoreAdapter**|Indicates that you should re-evaluate the current crypto session status; for example, by calling [ID3D11VideoContext1::CheckCryptoSessionStatus](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-checkcryptosessionstatus) to determine the impact of the hardware teardown for a specific [ID3D11CryptoSession](/windows/win32/api/d3d11/nn-d3d11-id3d11cryptosession) interface. Upon registration, an initial callback will always occur to allow you to query the initial state.|

A call to the function that you provide in *callbackFunction* is made asynchronously on a background thread by DXCore when the detected event occurs. No guarantee is made as to the ordering or timing of callbacks&mdash;multiple callbacks may occur in any order, or even simultaneously. It's even possible for your callback to be invoked before **RegisterEventNotification** has completed. In that case, DXCore guarantees that your *eventCookie* is set before your callback is called. Multiple callbacks for a specific registration will be serialized in order.

Callbacks may occur at any time until you call [UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md), and it completes. Callbacks occur on their own threads, and you may make calls into the DXCore API on those threads, including **UnregisterEventNotification**. However, you must not release the last reference to the *dxCoreObject* on this thread.

> [!IMPORTANT]
> Before you destroy the DXCore object represented by the *dxCoreObject* argument passed to **RegisterEventNotification**, you must use the cookie value to unregister that object from notifications by calling [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md). If you don't do that, then a fatal exception is raised when the situation is detected.

## See also

[IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

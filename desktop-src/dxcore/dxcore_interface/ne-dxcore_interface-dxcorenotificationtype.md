---
title: DXCoreNotificationType
description: Defines constants that specify types of notifications raised by [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md) or [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md) objects.
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreNotificationType enum

Defines constants that specify types of notifications raised by [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md) or [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md) objects.

You can register and unregister for these notifications by calling [IDXCoreAdapterFactory::RegisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md) and [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md), respectively.

## Syntax

```cpp
enum class DXCoreNotificationType : uint32_t
{
  AdapterListStale = 0,
  AdapterNoLongerValid = 1,
  AdapterBudgetChange = 2,
  AdapterHardwareContentProtectionTeardown = 3
};
```

## Constants

### AdapterListStale

This notification is raised by an <a href="/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist">IDXCoreAdapterList</a> object when the adapter list becomes stale. The fresh-to-stale transition is one-way, and one-time, so this notification is raised at most one time.

### AdapterNoLongerValid

This notification is raised by an <a href="/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object when the adapter becomes no longer valid. The valid-to-invalid transition is one-way, and one-time, so this notification is raised at most one time.

### AdapterBudgetChange

This notification is raised by an <a href="/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object when an adapter budget change occurs. This notification can occur many times. Using this notification is functionally similar to <a href="/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registervideomemorybudgetchangenotificationevent">IDXGIAdapter3::RegisterVideoMemoryBudgetChangeNotificationEvent</a>. In response to this event, you should call [IDXCoreAdapter::QueryState](./nf-dxcore_interface-idxcoreadapter-querystate.md) (with [DXCoreAdapterState::AdapterMemoryBudget](./ne-dxcore_interface-dxcoreadapterstate.md)) to evaluate the current memory budget state.

### AdapterHardwareContentProtectionTeardown

This notification is raised by an <a href="/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object to notify of an adapter's hardware content protection teardown. This notification can occur many times. It is functionally similar to <a href="/windows/win32/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registerhardwarecontentprotectionteardownstatusevent">IDXGIAdapter3::RegisterHardwareContentProtectionTeardownStatusEvent</a>. In response to this event, you should re-evaluate the current crypto session status; for example, by calling [ID3D11VideoContext1::CheckCryptoSessionStatus](/windows/win32/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-checkcryptosessionstatus) to determine the impact of the hardware teardown for a specific [ID3D11CryptoSession](/windows/win32/api/d3d11/nn-d3d11-id3d11cryptosession) interface.

## See also

[IDXCoreAdapterFactory::RegisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-registereventnotification.md), [IDXCoreAdapterFactory::UnregisterEventNotification](./nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification.md), [IDXCoreAdapter](./nn-dxcore_interface-idxcoreadapter.md), [IDXCoreAdapterList](./nn-dxcore_interface-idxcoreadapterlist.md), [DXCore Reference](../dxcore-reference.md), [Using DXCore to enumerate adapters](../dxcore-enum-adapters.md)

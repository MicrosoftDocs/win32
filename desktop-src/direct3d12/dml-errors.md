---
title: Binding in DirectML
description: This topic discusses how to debug DirectML device-removal, and other error conditions.
ms.custom: 19H1
ms.localizationpriority: high
ms.topic: article
ms.date: 03/14/2019
---

# Handling errors and device-removal in DirectML

## Device-removal

If an unrecoverable error occurs, the DirectML device may enter a "device-removed" state. Unrecoverable errors that cause device-removal include invalid API usage (for methods that don't return an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes)), driver error, hardware fault, or out-of-memory (OOM) conditions.

When a DirectML device is removed, all method calls on the device, and every object created by that device, become no-ops. For methods that return an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes), a [**DXGI_ERROR_DEVICE_REMOVED**](/windows/desktop/direct3ddxgi/dxgi-error) error code is returned. You can use the [**IDMLDevice::GetDeviceRemovedReason** method](/windows/desktop/api/directml/nf-directml-idmldevice-getdeviceremovedreason) to check whether the DirectML device has been removed, and to retrieve a more detailed error code.

You can't recover from device-removal except by releasing the affected device and all its children, then re-creating the DirectML device from scratch.

Device-removal of the underlying Direct3D 12 device also causes the DirectML device to be removed. However, the reverse is not true. DirectML device-removal may not necessarily cause the underlying Direct3D 12 device to become removed.

## Debugging DirectML device-removal, and other errors

The most common cause of DirectML errors is invalid API usage. Invalid API usage might result in an **E_INVALIDARG** HRESULT error code, or it might result in device-removal.

We strongly recommend that you enable the [DirectML debug layer](dml-debug-layer.md) during your development, in order to catch and debug such errors. The DirectML debug layer performs extensive validation of method parameters and API usage, and it will emit debug output messages to help you debug.

## See also

* [Using the DirectML debug layer](dml-debug-layer.md)

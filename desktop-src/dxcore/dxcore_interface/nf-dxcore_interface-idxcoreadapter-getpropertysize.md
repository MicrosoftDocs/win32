---
title: IDXCoreAdapter::GetPropertySize
description: For a specified adapter property, retrieves the size of buffer, in bytes, that is required for a call to [GetProperty](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getproperty).
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# IDXCoreAdapter::GetPropertySize method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

For a specified adapter property, retrieves the size of buffer, in bytes, that is required for a call to [GetProperty](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getproperty). Before calling **GetPropertySize** for a property type, call [IsPropertySupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetPropertySize(
  DXCoreAdapterProperty property,
  _Out_ size_t *bufferSize) = 0;
```

## Parameters

### property

Type: **[DXCoreAdapterProperty](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterproperty)**

The type of the property whose size, in bytes, you wish to retrieve.

### bufferSize [out]

Type: **size_t\***

A pointer to a **size_t** value. The function dereferences the pointer and sets the value to the size, in bytes, of the output buffer that you should allocate and pass as the *propertyData* argument in your call to [GetProperty](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getproperty).

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DXGI_ERROR_INVALID_CALL|The property type specified in *property* is not recognized by this operating system (OS). Call [IsPropertySupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The property type specified in *property* is not supported by the adapter. Call [IsPropertySupported](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS).|
|E_POINTER|`nullptr` was provided for *bufferSize*.|

## Remarks

You can call **GetPropertySize** on an adapter that's no longer valid&mdash;the function won't fail.

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

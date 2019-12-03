---
title: IDXCoreAdapterList::GetFactory
description: TBD
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# IDXCoreAdapterList::GetFactory method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Retrieves an [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory) interface pointer to the DXCore adapter factory object. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Syntax

```cpp
virtual HRESULT STDMETHODCALLTYPE GetFactory(
  REFIID riid,
  _COM_Outptr_ void** ppvFactory) = 0;

template <class T>
HRESULT GetFactory(
  _COM_Outptr_ T** ppvFactory);
```

## Parameters

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvFactory*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory).

### ppvFactory [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvFactory* (the dereferenced address) contains a pointer to the existing DXCore adapter factory object. Before returning, the function increments the reference count on the factory object's [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory) interface.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvFactory*.|

## Remarks

For the duration of time that a reference exists on an [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory) interface, an [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) interface, or an [IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter) interface, additional calls to [DXCoreCreateAdapterFactory](/windows/win32/dxcore/dxcore/nf-dxcore-dxcorecreateadapterfactory), [IDXCoreAdapterList::GetFactory](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterlist-getfactory), or [IDXCoreAdapter::GetFactory](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getfactory) will return pointers to the same object, increasing the reference count of the **IDXCoreAdapterFactory** interface.

## See also

[IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

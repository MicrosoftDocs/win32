---
title: DXCoreCreateAdapterFactory
description: Creates a DXCore adapter factory, which you can use to generate further DXCore objects.
ms.localizationpriority: low
ms.topic: reference
ms.date: 06/20/2019
---

# DXCoreCreateAdapterFactory function

## Description

Creates a DXCore adapter factory, which you can use to generate further DXCore objects. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters).

## Parameters

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvFactory*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory).

### ppvFactory [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvFactory* (the dereferenced address) contains a pointer to the DXCore factory created.

## Returns

Type: **[HRESULT](/windows/win32/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/win32/com/structure-of-com-error-codes) [error code](/windows/win32/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvFactory*.|

## Remarks

For the duration of time that a reference exists on an [IDXCoreAdapterFactory](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory) interface, an [IDXCoreAdapterList](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) interface, or an [IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter) interface, additional calls to **DXCoreCreateAdapterFactory**, [IDXCoreAdapterList::GetFactory](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterlist-getfactory), or [IDXCoreAdapter::GetFactory](/windows/win32/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getfactory) will return pointers to the same object, increasing the reference count of the **IDXCoreAdapterFactory** interface.

## See also

[DXCore Reference](/windows/win32/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)
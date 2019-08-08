---
UID: NF:dxcore_interface.IDXCoreAdapter.GetProperty
title: IDXCoreAdapter::GetProperty
description: Retrieves the value of the specified adapter property.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/10/2019
ms.keywords: IDXCoreAdapter interface,GetProperty method, IDXCoreAdapter.GetProperty, IDXCoreAdapter::GetProperty, GetProperty, GetProperty method, GetProperty method,IDXCoreAdapter interface, dxcore/IDXCoreAdapter::GetProperty, dxcore_interface.idxcoreadapterfactory_getproperty
ms.localizationpriority: low
ms.topic: method
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: method
req.ddi-compliance: 
req.dll: dxcore.dll
req.header: dxcore_interface.h
req.idl: 
req.include-header: dxcore.h
req.irql: 
req.kmdf-ver: 
req.lib: dxcore.lib
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: Windows 10 (Build 18936)
req.target-min-winversvr: 
req.target-type: Windows
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
 - kbsyntax
api_type:
 - COM
api_location:
 - dxcore.dll
api_name:
 - IDXCoreAdapter::GetProperty
---

# IDXCoreAdapter::GetProperty method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Retrieves the value of the specified adapter property. Before calling **GetProperty** for a property type, call [IsPropertySupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS). Also before calling **GetProperty**, call [GetPropertySize](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getpropertysize) to determine the necessary size of the buffer in which to receive the property value.

## Parameters

### property

Type: **[DXCoreAdapterProperty](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterproperty)**

The type of the property whose value you wish to retrieve. See the table in [DXCoreAdapterProperty](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterproperty) for more info about each adapter property.

### bufferSize

Type: **size_t**

The size, in bytes, of the output buffer that you allocate and provide in *propertyData*.

### propertyData [out]

Type: **void\***

A pointer to an output buffer that you allocate in your application, and that the function fills in. Call [GetPropertySize](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getpropertysize) to determine the size that the *propertyData* buffer should be for a given adapter property.

## Returns

Type: **[HRESULT](/windows/desktop/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|DXGI_ERROR_INVALID_CALL|The property type specified in *property* is not recognized by this operating system (OS). Call [IsPropertySupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS).|
|DXGI_ERROR_UNSUPPORTED|The property type specified in *property* is not supported by the adapter. Call [IsPropertySupported](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-ispropertysupported) to confirm that the property type is available for this adapter and operating system (OS).|
|E_INVALIDARG|An insufficient buffer size is provided in *propertyData*. Call [GetPropertySize](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-getpropertysize) to determine the size that the *propertyData* buffer should be for a given adapter property.|
|E_POINTER|`nullptr` was provided for *propertyData*.|

## Remarks

You can call **GetProperty** on an adapter that's no longer valid&mdash;the function won't fail as a result of that. This function zeros out the *propertyData* buffer prior to filling it in.

## See also

[IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)

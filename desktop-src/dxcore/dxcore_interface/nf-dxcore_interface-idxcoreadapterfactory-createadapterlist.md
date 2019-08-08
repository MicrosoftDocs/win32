---
UID: NF:dxcore_interface.IDXCoreAdapterFactory.CreateAdapterList
title: IDXCoreAdapterFactory::CreateAdapterList
description: Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/06/2019
ms.keywords: IDXCoreAdapterFactory interface,CreateAdapterList method, IDXCoreAdapterFactory.CreateAdapterList, IDXCoreAdapterFactory::CreateAdapterList, CreateAdapterList, CreateAdapterList method, CreateAdapterList method,IDXCoreAdapterFactory interface, dxcore/IDXCoreAdapterFactory::CreateAdapterList, dxcore_interface.idxcoreadapterfactory_createadapterlist
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
 - IDXCoreAdapterFactory.CreateAdapterList
---

# IDXCoreAdapterFactory::CreateAdapterList method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Generates a list of adapter objects representing the current adapter state of the system, and meeting the criteria specified. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters).

## Parameters

### numAttributes

Type: **uint32_t**

The number of elements in the array pointed to by the *filterAttributes* argument.

### filterAttributes [in]

Type: **const GUID\***

A pointer to an array of adapter attribute GUIDs. For a list of attribute GUIDs, see [DXCore adapter attribute GUIDs](/windows/desktop/dxcore/dxcore-adapter-attribute-guids). At least one GUID must be provided. In the case that more than one GUID is provided in the array, only adapters that meet *all* of the requested attributes will be included in the returned list.

### riid

Type: **REFIID**

A reference to the globally unique identifier (GUID) of the interface that you wish to be returned in *ppvAdapterList*. This is expected to be the interface identifier (IID) of [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist).

### ppvAdapterList [out]

Type: **void\*\***

The address of a pointer to an interface with the IID specified in the *riid* parameter. Upon successful return, *\*ppvAdapterList* (the dereferenced address) contains a pointer to the the adapter list created.

## Returns

Type: **[HRESULT](/windows/desktop/com/structure-of-com-error-codes)**

If the function succeeds, it returns **S_OK**. Otherwise, it returns an [**HRESULT**](/windows/desktop/com/structure-of-com-error-codes) [error code](/windows/desktop/com/com-error-codes-10).

|Return value|Description|
|-|-|
|E_INVALIDARG|`nullptr` was provided for *filterAttributes*, or 0 was provided for *numAttributes*.|
|E_NOINTERFACE|An invalid value was provided for *riid*.|
|E_POINTER|`nullptr` was provided for *ppvAdapterList*.|

## Remarks

Even if no adapters are found, as long as the arguments are valid, **CreateAdapterList** creates a valid [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) object, and returns **S_OK**. Once generated, the adapters in this specific list won't change. But the list will be considered stale if one of the adapters later becomes invalid, or if a new adapter arrives that meets the provided filter criteria. The list returned by **CreateAdapterList** is not ordered in any particular way, and multiple calls to **CreateAdapterList** may produce differently ordered lists.

The resulting list is not ordered in any particular way, but the ordering of a list is consistent across multiple calls, and even across operating system restarts. The ordering may change upon system configuration changes, including the addition or removal of an adapter, or a driver update on an existing adapter.

## See also

[IDXCoreAdapterFactory](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterfactory), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/desktop/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)

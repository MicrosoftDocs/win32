---
UID: NF:dxcore_interface.IDXCoreAdapterList.GetAdapterCount
title: IDXCoreAdapterList::GetAdapterCount
description: Retrieves the number of adapters in a DXCore adapter list object.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/10/2019
ms.keywords: IDXCoreAdapterFactory interface,GetAdapterCount method, IDXCoreAdapterFactory.GetAdapterCount, IDXCoreAdapterFactory::GetAdapterCount, GetAdapterCount, GetAdapterCount method, GetAdapterCount method,IDXCoreAdapterFactory interface, dxcore/IDXCoreAdapterFactory::GetAdapterCount, dxcore_interface.idxcoreadapterfactory_getadaptercount
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
 - IDXCoreAdapterList::GetAdapterCount
---

# IDXCoreAdapterList::GetAdapterCount method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Retrieves the number of adapters in a DXCore adapter list object. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters).

## Returns

Type: **uint32_t**

Returns the number of adapter items in the list.

## See also

[IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)

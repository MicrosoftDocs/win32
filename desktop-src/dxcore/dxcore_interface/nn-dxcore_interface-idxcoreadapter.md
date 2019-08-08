---
UID: NN:dxcore_interface.IDXCoreAdapter
title: IDXCoreAdapter
description: The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/10/2019
ms.keywords: IDXCoreAdapter, IDXCoreAdapter interface, IDXCoreAdapter interface,description, dxcore/IDXCoreAdapter, dxcore.idxcoreadapter
ms.localizationpriority: low
ms.topic: interface
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: interface
req.ddi-compliance: 
req.dll: 
req.header: dxcore_interface.h
req.idl: 
req.include-header: dxcore.h
req.irql: 
req.kmdf-ver: 
req.lib: 
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
 - IDXCoreAdapter
---

# IDXCoreAdapter interface

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

The **IDXCoreAdapter** interface implements methods for retrieving details about an adapter item. **IDXCoreAdapter** inherits from the [IUnknown](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. For programming guidance, and code examples, see [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters).

## Remarks

An adapter's properties are established at the time the adapter starts, and they're immutable for the lifetime of the adapter. This is in contrast to an adapter's state, which can be queried or set, and the values of which can change over time.

## See also

[DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)
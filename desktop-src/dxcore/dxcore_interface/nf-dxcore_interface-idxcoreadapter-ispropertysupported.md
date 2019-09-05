---
title: IDXCoreAdapter::IsPropertySupported
description: Determines whether this DXCore adapter object and the current operating system (OS) support the specified adapter property.
ms.localizationpriority: low
ms.topic: article
ms.date: 06/20/2019
---

# IDXCoreAdapter::IsPropertySupported method

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

Determines whether this DXCore adapter object and the current operating system (OS) support the specified adapter property.

## Syntax

```cpp
virtual bool STDMETHODCALLTYPE IsPropertySupported( 
  DXCoreAdapterProperty property) = 0;
```

## Parameters

### property

Type: **[DXCoreAdapterProperty](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterproperty)**

The type of property that you're querying about support for. See the table in [DXCoreAdapterProperty](/windows/win32/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterproperty) for more info about each adapter property.

## Returns

Type: **bool**

Returns `true` if this DXCore adapter object and the current operating system (OS) support the specified adapter property. Otherwise, returns `false`.

## See also

[IDXCoreAdapter](/windows/win32/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [DXCore Reference](/windows/win32/dxcore/dxcore-reference), [DXCore adapter attribute GUIDs](/windows/win32/dxcore/dxcore-adapter-attribute-guids), [Using DXCore to enumerate adapters](/windows/win32/dxcore/dxcore-enum-adapters)

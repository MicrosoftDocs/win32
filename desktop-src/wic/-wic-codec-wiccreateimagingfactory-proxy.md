---
description: Proxy function for creating the IWICImagingFactory.
ms.assetid: e4f575b0-878f-461e-92e7-9494e505ea6f
title: WICCreateImagingFactory_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WICCreateImagingFactory_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Windowscodecs.lib
---

# WICCreateImagingFactory\_Proxy function

Proxy function for creating the [**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory).

## Syntax

```cpp
HRESULT WICCreateImagingFactory_Proxy(
  _In_  UINT               SDKVersion,
  _Out_ IWICImagingFactory **ppIImagingFactory
);
```

## Parameters

<dl> <dt>

*SDKVersion* \[in\]
</dt> <dd>

Type: **UINT**

</dd> <dt>

*ppIImagingFactory* \[out\]
</dt> <dd>

Type: **[**IWICImagingFactory**](/windows/desktop/api/Wincodec/nn-wincodec-iwicimagingfactory)\*\***

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This function is a helper for creating a WIC factory for explicit DLL linking, which was needed for Windows XP. In normal usage, you would use [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) instead (see [WIC API class factories](./-wic-api.md#class-factories)), since that's always included in all newer versions of Windows.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>windowscodecs.lib</dt> </dl> |



 


---
Description: 'Proxy function for the CreateComponentInfo method.'
ms.assetid: '7d3b791a-d65e-4b90-8050-373a949e6d9c'
title: 'IWICImagingFactory\_CreateComponentInfo\_Proxy function'
---

# IWICImagingFactory\_CreateComponentInfo\_Proxy function

Proxy function for the [**CreateComponentInfo**](-wic-codec-iwicimagingfactory-createcomponentinfo.md) method.

## Syntax


```C++
HRESULT IWICImagingFactory_CreateComponentInfo_Proxy(
  _In_  IWICImagingFactory *pFactory,
  _In_  REFCLSID           clsidComponent,
  _Out_ IWICComponentInfo  **ppIInfo
);
```



## Parameters

<dl> <dt>

*pFactory* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

</dd> <dt>

*clsidComponent* \[in\]
</dt> <dd>

Type: **REFCLSID**

The CLSID for the desired component.

</dd> <dt>

*ppIInfo* \[out\]
</dt> <dd>

Type: **[**IWICComponentInfo**](-wic-codec-iwiccomponentinfo.md)\*\***

A pointer that receives a pointer to a new [**IWICComponentInfo**](-wic-codec-iwiccomponentinfo.md).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



|                                     |                                                                                                                                                                  |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 





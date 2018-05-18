---
Description: 'Proxy function for creating an IWICColorContext.'
ms.assetid: '66348ef2-3056-4ec7-84ad-6e022e320a33'
title: 'WICCreateColorContext\_Proxy function'
---

# WICCreateColorContext\_Proxy function

Proxy function for creating an [**IWICColorContext**](-wic-codec-iwiccolorcontext.md).

## Syntax


```C++
HRESULT WICCreateColorContext_Proxy(
  _In_ IWICImagingFactory *THIS_PTR,
       IWICColorContext   ppIColorContext
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md)\***

Pointer to this [**IWICImagingFactory**](-wic-codec-iwicimagingfactory.md) object.

</dd> <dt>

*ppIColorContext* 
</dt> <dd>

Type: **[**IWICColorContext**](-wic-codec-iwiccolorcontext.md)**

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



 

 





---
Description: 'Proxy function for the GetColorContexts method.'
ms.assetid: '2a6db3bd-d3e1-4e87-a04d-0d1c3ea858fb'
title: 'IWICBitmapDecoder\_GetColorContexts\_Proxy function'
---

# IWICBitmapDecoder\_GetColorContexts\_Proxy function

Proxy function for the [**GetColorContexts**](-wic-codec-iwicbitmapdecoder-getcolorcontexts.md) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetColorContexts_Proxy(
  _In_    IWICBitmapDecoder *THIS_PTR,
  _In_    UINT              cCount,
  _Inout_ IWICColorContext  **ppIColorContexts,
  _Out_   UINT              *pcActualCount
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md)\***

Pointer to this [**IWICBitmapDecoder**](-wic-codec-iwicbitmapdecoder.md) object.

</dd> <dt>

*cCount* \[in\]
</dt> <dd>

Type: **UINT**

The number of color contexts to retrieve.

This value must be the size of, or smaller than, the size available to *ppIColorContexts*.

</dd> <dt>

*ppIColorContexts* \[in, out\]
</dt> <dd>

Type: **[**IWICColorContext**](-wic-codec-iwiccolorcontext.md)\*\***

A pointer that receives a pointer to the [**IWICColorContext**](-wic-codec-iwiccolorcontext.md).

</dd> <dt>

*pcActualCount* \[out\]
</dt> <dd>

Type: **UINT\***

A pointer that receives the number of color contexts contained in the image.

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



 

 





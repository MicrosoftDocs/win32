---
description: Proxy function for the GetDecoderInfo method.
ms.assetid: 4117492e-d652-4c72-9979-cc4e554a6fd8
title: IWICBitmapDecoder_GetDecoderInfo_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICBitmapDecoder_GetDecoderInfo_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICBitmapDecoder\_GetDecoderInfo\_Proxy function

Proxy function for the [**GetDecoderInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapdecoder-getdecoderinfo) method.

## Syntax


```C++
HRESULT IWICBitmapDecoder_GetDecoderInfo_Proxy(
  _In_  IWICBitmapDecoder     *THIS_PTR,
  _Out_ IWICBitmapDecoderInfo **ppIDecoderInfo
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder)\***

Pointer to this [**IWICBitmapDecoder**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoder) object.

</dd> <dt>

*ppIDecoderInfo* \[out\]
</dt> <dd>

Type: **[**IWICBitmapDecoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoderinfo)\*\***

A pointer that receives a pointer to an [**IWICBitmapDecoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapdecoderinfo).

</dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2, Windows Vista \[desktop apps only\]<br/>                                                                                              |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                             |
| DLL<br/>                      | <dl> <dt>Windowscodecs.dll; </dt> <dt>Wincodec.lib</dt> </dl> |



 

 





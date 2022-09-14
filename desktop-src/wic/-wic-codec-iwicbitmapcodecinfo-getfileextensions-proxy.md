---
description: Proxy function for the GetFileExtensions method.
ms.assetid: 1c9232c5-54f3-4186-a1c8-4531e8357d06
title: IWICBitmapCodecInfo_GetFileExtensions_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICBitmapCodecInfo_GetFileExtensions_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICBitmapCodecInfo\_GetFileExtensions\_Proxy function

Proxy function for the [**GetFileExtensions**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapcodecinfo-getfileextensions) method.

## Syntax


```C++
HRESULT IWICBitmapCodecInfo_GetFileExtensions_Proxy(
  _In_    IWICBitmapCodecInfo *THIS_PTR,
  _In_    UINT                cchFileExtensions,
  _Inout_ WCHAR               *wzFileExtensions,
  _Inout_ UINT                *pcchActual
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapCodecInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapcodecinfo)\***

Pointer to this [**IWICBitmapCodecInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapcodecinfo) object.

</dd> <dt>

*cchFileExtensions* \[in\]
</dt> <dd>

Type: **UINT**

The size of the file name extension buffer.

</dd> <dt>

*wzFileExtensions* \[in, out\]
</dt> <dd>

Type: **WCHAR\***

A pointer that receives the file name extensions associated with the codec.

</dd> <dt>

*pcchActual* \[in, out\]
</dt> <dd>

Type: **UINT\***

The actual buffer size needed to retrieve all file name extensions associated with the codec.

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



 

 





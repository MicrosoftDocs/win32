---
description: Proxy function for the GetEncoderInfo method.
ms.assetid: 759965fd-7bc6-4130-b102-b49d1f0d4bf8
title: IWICBitmapEncoder_GetEncoderInfo_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICBitmapEncoder_GetEncoderInfo_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICBitmapEncoder\_GetEncoderInfo\_Proxy function

Proxy function for the [**GetEncoderInfo**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-getencoderinfo) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_GetEncoderInfo_Proxy(
  _In_  IWICBitmapEncoder     *THIS_PTR,
  _Out_ IWICBitmapEncoderInfo **ppIEncoderInfo
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder)\***

Pointer to this [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder) object.

</dd> <dt>

*ppIEncoderInfo* \[out\]
</dt> <dd>

Type: **[**IWICBitmapEncoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapencoderinfo)\*\***

A pointer that receives a pointer to an [**IWICBitmapEncoderInfo**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapencoderinfo).

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



 

 





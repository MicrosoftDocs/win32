---
description: Proxy function for the CreateNewFrame method.
ms.assetid: b23e8689-0fdc-49a7-a004-148b50420127
title: IWICBitmapEncoder_CreateNewFrame_Proxy function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWICBitmapEncoder_CreateNewFrame_Proxy
api_type: 
- DllExport
api_location: 
- Windowscodecs.dll
- Wincodec.lib
---

# IWICBitmapEncoder\_CreateNewFrame\_Proxy function

Proxy function for the [**CreateNewFrame**](/windows/desktop/api/Wincodec/nf-wincodec-iwicbitmapencoder-createnewframe) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_CreateNewFrame_Proxy(
  _In_    IWICBitmapEncoder     *THIS_PTR,
  _Out_   IWICBitmapFrameEncode **ppIFrameEncode,
  _Inout_ IPropertyBag2         **ppIEncoderOptions
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder)\***

Pointer to this [**IWICBitmapEncoder**](/windows/desktop/api/wincodec/nn-wincodec-iwicbitmapencoder) object.

</dd> <dt>

*ppIFrameEncode* \[out\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode)\*\***

A pointer that receives a pointer to the new instance of an [**IWICBitmapFrameEncode**](/windows/desktop/api/Wincodec/nn-wincodec-iwicbitmapframeencode).

</dd> <dt>

*ppIEncoderOptions* \[in, out\]
</dt> <dd>

Type: **[IPropertyBag2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85))\*\***

The named properties to use for frame initialization.

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



 


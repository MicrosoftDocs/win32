---
Description: 'Proxy function for the CreateNewFrame method.'
ms.assetid: 'b23e8689-0fdc-49a7-a004-148b50420127'
title: 'IWICBitmapEncoder\_CreateNewFrame\_Proxy function'
---

# IWICBitmapEncoder\_CreateNewFrame\_Proxy function

Proxy function for the [**CreateNewFrame**](-wic-codec-iwicbitmapencoder-createnewframe.md) method.

## Syntax


```C++
HRESULT IWICBitmapEncoder_CreateNewFrame_Proxy(
  _In_    IWICBitmapEncoder     *THIS_PTR,
  _Out_   IWICBitmapFrameEncode **ppIFrameEncode,
  _Inout_ IPropertyBag2         **ppIEncoderOptions
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md)\***

Pointer to this [**IWICBitmapEncoder**](-wic-codec-iwicbitmapencoder.md) object.

</dd> <dt>

*ppIFrameEncode* \[out\]
</dt> <dd>

Type: **[**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md)\*\***

A pointer that receives a pointer to the new instance of an [**IWICBitmapFrameEncode**](-wic-codec-iwicbitmapframeencode.md).

</dd> <dt>

*ppIEncoderOptions* \[in, out\]
</dt> <dd>

Type: **[IPropertyBag2](http://msdn.microsoft.com/en-us/library/Aa768192(VS.85).aspx)\*\***

The named properties to use for frame initialization.

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



 

 





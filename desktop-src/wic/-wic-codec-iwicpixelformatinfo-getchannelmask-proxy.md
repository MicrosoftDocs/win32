---
Description: 'Proxy function for the GetChannelMask method.'
ms.assetid: 'c96e6078-4648-4333-8a25-bcb03a2cd50b'
title: 'IWICPixelFormatInfo\_GetChannelMask\_Proxy function'
---

# IWICPixelFormatInfo\_GetChannelMask\_Proxy function

Proxy function for the [**GetChannelMask**](-wic-codec-iwicpixelformatinfo-getchannelmask.md) method.

## Syntax


```C++
HRESULT IWICPixelFormatInfo_GetChannelMask_Proxy(
  _In_    IWICPixelFormatInfo *THIS_PTR,
  _In_    UINT                uiChannelIndex,
  _In_    UINT                cbMaskBuffer,
  _Inout_ BYTE                *pbMaskBuffer,
  _Out_   UINT                *pcbActual
);
```



## Parameters

<dl> <dt>

*THIS\_PTR* \[in\]
</dt> <dd>

Type: **[**IWICPixelFormatInfo**](-wic-codec-iwicpixelformatinfo.md)\***

Pointer to this [**IWICPixelFormatInfo**](-wic-codec-iwicpixelformatinfo.md) object.

</dd> <dt>

*uiChannelIndex* \[in\]
</dt> <dd>

Type: **UINT**

The index to the channel mask to retrieve.

</dd> <dt>

*cbMaskBuffer* \[in\]
</dt> <dd>

Type: **UINT**

The size of the *pbMaskBuffer* buffer.

</dd> <dt>

*pbMaskBuffer* \[in, out\]
</dt> <dd>

Type: **BYTE\***

Pointer to the mask buffer.

</dd> <dt>

*pcbActual* \[out\]
</dt> <dd>

Type: **UINT\***

The actual buffer size needed to obtain the channel mask.

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



 

 





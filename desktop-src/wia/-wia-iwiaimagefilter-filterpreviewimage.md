---
description: Filters the preview image.
ms.assetid: 1710211a-a35c-4a51-b3bb-6f03f234f247
title: IWiaImageFilter::FilterPreviewImage method (Wia.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IWiaImageFilter.FilterPreviewImage
api_type: 
- COM
api_location: 
- Wia.h
---

# IWiaImageFilter::FilterPreviewImage method

Filters the preview image.

## Syntax


```C++
HRESULT FilterPreviewImage(
  [in] LONG      lFlags,
  [in] IWiaItem2 *pWiaChildItem2,
  [in] RECT      InputImageExtents,
  [in] IStream   *pInputStream
);
```



## Parameters

<dl> <dt>

*lFlags* \[in\]
</dt> <dd>

Type: **LONG**

Not used. Set to 0.

</dd> <dt>

*pWiaChildItem2* \[in\]
</dt> <dd>

Type: **[**IWiaItem2**](-wia-iwiaitem2.md)\***

The item that is processed.

</dd> <dt>

*InputImageExtents* \[in\]
</dt> <dd>

Type: **RECT**

The coordinates (on the physical acquisition area) of the image that the preview component caches internally.

</dd> <dt>

*pInputStream* \[in\]
</dt> <dd>

Type: **[IStream](/windows/win32/api/objidl/nn-objidl-istream)\***

A pointer to the [IStream](/windows/win32/api/objidl/nn-objidl-istream) interface for the cached image data that is filtered.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Do not call this method directly from your application.

*pWiaChildItem2* must be a child item of the *pWiaItem2* that was passed into [**IWiaImageFilter::InitializeFilter**](-wia-iwiaimagefilter-initializefilter.md).

*InputImageExtents* is needed because the image processing filter is responsible for cutting out the image area that *pWiaChildItem2* represents from the image data passed in through *pInputStream*.

An application must ensure that *pWiaChildItem2* has the same image format (WIA\_IPA\_FORMAT), resolution (WIA\_IPS\_XRES and WIA\_IPS\_YRES) and bit depth (WIA\_IPA\_DEPTH) as *pWiaItem2* had when it was passed into [**GetNewPreview**](-wia-iwiapreview-getnewpreview.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Wia.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Wia.idl</dt> </dl> |



 

 

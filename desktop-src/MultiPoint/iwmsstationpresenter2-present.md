---
title: IWmsStationPresenter2 Present method
description: Displays an updated frame buffer from the input device. This method was inherited from the IWmsStationPresenter interface.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '36CAC6BF-E300-4457-8C5E-BC7335AA6B59'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Present method", "Present method, IWmsStationPresenter2 interface", "IWmsStationPresenter2 interface, Present method"]
topic_type:
- apiref
api_name:
- IWmsStationPresenter2.Present
api_location:
- WmsStationPresenter.idl
api_type:
- COM
---

# IWmsStationPresenter2::Present method

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Displays an updated frame buffer from the input device. This method was inherited from the [**IWmsStationPresenter**](iwmsstationpresenter.md) interface.

## Syntax


```C++
HRESULT Present(
  [in, size_is(cxFrameBuffer * cyFrameBuffer * (cBitsPerPixel / 8)] const BYTE *pbFrameBuffer,
  [in]                                                                    UINT cxFrameBuffer,
  [in]                                                                    UINT cyFrameBuffer,
  [in]                                                                    UINT cBitsPerPixel,
  [in]                                                              const HRGN hRgnDirty
);
```



## Parameters

<dl> <dt>

*pbFrameBuffer* \[in\]
</dt> <dd>

A pointer to the frame buffer to display.

</dd> <dt>

*cxFrameBuffer* \[in\]
</dt> <dd>

The width of the frame buffer, in pixels.

</dd> <dt>

*cyFrameBuffer* \[in\]
</dt> <dd>

The height of the frame buffer, in pixels.

</dd> <dt>

*cBitsPerPixel* \[in\]
</dt> <dd>

The color depth of the bitmap, in bits per pixel.

</dd> <dt>

*hRgnDirty* \[in\]
</dt> <dd>

A handle to the dirty region of the frame buffer. This is the portion of the frame buffer that is to be updated.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| IDL<br/>                      | <dl> <dt>WmsStationPresenter.idl</dt> </dl> |
| IID<br/>                      | IID\_IWmsStationPresenter2 is defined as 5c03282a-b68f-476a-ace8-e0736a9d1260<br/>           |



## See also

<dl> <dt>

[**IWmsStationPresenter2**](iwmsstationpresenter2.md)
</dt> </dl>

 

 






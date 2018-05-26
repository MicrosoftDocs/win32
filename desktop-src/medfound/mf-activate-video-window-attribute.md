---
Description: Handle to the video clipping window.
ms.assetid: 883bc7cf-f52f-4cb5-a942-b42b429b17a9
title: MF\_ACTIVATE\_VIDEO\_WINDOW attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_ACTIVATE\_VIDEO\_WINDOW attribute

Handle to the video clipping window.

## Data type

**UINT64**

Treat as **DWORD\_PTR** (**HWND**).

## Remarks

This attribute applies to the activation object for the enhanced video renderer (EVR). The value is set automatically when you call [**MFCreateVideoRendererActivate**](/windows/win32/mfidl/nf-mfidl-mfcreatevideorendereractivate?branch=master) to create the EVR activation object.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Enhanced Video Renderer Attributes](enhanced-video-renderer-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint64?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT64**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint64?branch=master)
</dt> <dt>

[Activation Objects](activation-objects.md)
</dt> </dl>

 

 





---
Description: Specifies the CLSID of a post-processing plug-in for a video capture device.
ms.assetid: 8F626FAA-C7B8-4DBA-BD65-7CE97CBF3A86
title: MF\_DEVICESTREAM\_EXTENSION\_PLUGIN\_CLSID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_DEVICESTREAM\_EXTENSION\_PLUGIN\_CLSID attribute

Specifies the CLSID of a post-processing plug-in for a video capture device.

## Data type

**GUID**

## Remarks

A post-processing plug-in is an MFT that processes the video image after it is captured. The hardware vendor can include a post-processing plug-in as part of the installation package. If so, the video capture source sets the MF\_DEVICESTREAM\_EXTENSION\_PLUGIN\_CLSID attribute to the CLSID of the plug-in.

To get this attribute, do the following:

1.  Query the media source for the [**IMFMediaSourceEx**](/windows/win32/mfidl/nn-mfidl-imfmediasourceex?branch=master) interface.
2.  Call [**IMFMediaSourceEx::GetStreamAttributes**](/windows/win32/mfidl/nf-mfidl-imfmediasourceex-getstreamattributes?branch=master) to get an [**IMFAttributes**](/windows/win32/mfobjects/nn-mfobjects-imfattributes?branch=master) pointer for the stream.
3.  Call [**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master) to get the attribute.

To create the plug-in, call [**CoCreateInstance**](com.cocreateinstance).

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 





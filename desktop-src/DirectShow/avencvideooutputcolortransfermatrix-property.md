---
Description: Specifies the conversion matrix from the YCbCr color space to the RGB color space for the encoded video.
ms.assetid: 48891204-397b-4b2b-8550-7a77461db06c
title: AVEncVideoOutputColorTransferMatrix property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncVideoOutputColorTransferMatrix property

Specifies the conversion matrix from the Y'Cb'Cr' color space to the R'G'B' color space for the encoded video.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoOutputColorTransferMatrix**

## Property value

The value of this property is a member of the [**eAVEncVideoColorTransferMatrix**](/windows/win32/codecapi/ne-codecapi-eavencvideocolortransfermatrix?branch=master) enumeration.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/win32/Strmif/nn-strmif-icodecapi?branch=master)
</dt> </dl>

 

 





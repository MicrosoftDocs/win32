---
Description: Gets or sets the video decoding speed.
ms.assetid: 76F7013D-C172-4D31-93BC-EA3D186EB14C
title: AVDecVideoFastDecodeMode property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVDecVideoFastDecodeMode property

Gets or sets the video decoding speed.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoFastDecodeMode**

## Property value

The value of this property can range from 0 to 32, where 0 indicates normal decoding and 32 is the fastest decoding mode. The exact behavior depends on the decoder implementation. Not every increment between 1 and 32 necessarily defines is a distinct mode.

The [**eAVFastDecodeMode**](/windows/win32/codecapi/ne-codecapi-eavfastdecodemode?branch=master) enumeration contains some predefined modes for this property.

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

 

 





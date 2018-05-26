---
Description: Specifies the size of the video access units, in bytes. This property applies only to variable bit rate (VBR) control modes.
ms.assetid: bb46b171-d70a-4e01-88c4-321a210a0220
title: AVEncVideoCodedVideoAccessUnitSize property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncVideoCodedVideoAccessUnitSize property

Specifies the size of the video access units, in bytes. This property applies only to variable bit rate (VBR) control modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoCodedVideoAccessUnitSize**

## Property value

This property is returned as a range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/win32/Strmif/nf-strmif-icodecapi-getparameterrange?branch=master).

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

 

 





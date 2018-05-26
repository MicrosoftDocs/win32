---
Description: Specifies the maximum bit rate, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.
ms.assetid: 053fdad0-dc5f-4af1-84a6-bb7c0dac7e79
title: AVEncCommonMaxBitRate property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncCommonMaxBitRate property

Specifies the maximum bit rate, in bits per second. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonMaxBitRate**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/win32/Strmif/nf-strmif-icodecapi-getparameterrange?branch=master).

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

 

 





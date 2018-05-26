---
Description: Specifies the time interval over which the average bit rate applies. This property is used in conjunction with the AVEncCommonMeanBitRate property.
ms.assetid: 3cf26f46-e8ac-448a-a031-800915cad1ef
title: AVEncCommonMeanBitRateInterval property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AVEncCommonMeanBitRateInterval property

Specifies the time interval over which the average bit rate applies. This property is used in conjunction with the [**AVEncCommonMeanBitRate**](avenccommonmeanbitrate-property.md) property.

This property is read/write.

## Data type

**UINT64** (**VT\_UI8**)

## Property GUID

**CODECAPI\_AVEncCommonMeanBitRateInterval**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/win32/Strmif/nf-strmif-icodecapi-getparameterrange?branch=master).

## Remarks

For two-pass variable bit rate (VBR) encoding, the value zero indicates that the time interval is the entire duration of the content. For single-pass constant bit rate (CBR) encoding, the value zero indicates that the encoder selects the interval (typically 0.5 seconds).

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

 

 





---
Description: Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.
ms.assetid: 5574ee3c-ccb3-4ff6-8280-efe5626e6dd6
title: MFPKEY\_BUFFERFULLNESSINFIRSTBYTE Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFPKEY\_BUFFERFULLNESSINFIRSTBYTE Property

Specifies whether the encoded video bit stream contains a buffer fullness value with every key frame.

## Constant for IPropertyBag

g\_wszWMVCBufferFullnessInFirstByte

## Data Type

VT\_BOOL

## Remarks

You must set an output type before getting this value.

You can get the value of this property using [IWMCodecProps::GetCodecProp](/windows/win32/wmcodecdsp/nf-wmcodecdsp-iwmcodecprops-getcodecprop?branch=master). If you use **IPropertyBag**, you must first set the FOURCC value of the desired compressed format with the [MFPKEY\_FOURCC](mfpkey-fourccproperty.md) property.

Having the buffer fullness in the first byte of all key frames enables you to determine the buffer size required when concatenating compressed video streams.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

 





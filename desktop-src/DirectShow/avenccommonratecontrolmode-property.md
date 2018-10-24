---
Description: Specifies the rate control mode.
ms.assetid: 4a0d49b1-30da-4ebe-abff-3fceef6dd94a
title: AVEncCommonRateControlMode property
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AVEncCommonRateControlMode property

Specifies the rate control mode.

Applications can set this property to specify the rate control mode. Encoders can also return this property as a capability.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonRateControlMode**

## Property value

The value of this property is a member of the [**eAVEncCommonRateControlMode**](https://msdn.microsoft.com/en-us/library/Dd388772(v=VS.85).aspx) enumeration.

## Remarks

This property is also used with [H.264 UVC 1.5 camera encoders](https://msdn.microsoft.com/library/windows/desktop/jj218765).

[CODECAPI\_AVEncVideoTemporalLayerCount](https://msdn.microsoft.com/library/windows/desktop/hh869834), [CODECAPI\_AVEncVideoUsage](https://msdn.microsoft.com/library/windows/desktop/hh869856), and CODECAPI\_AVEncCommonRateControlMode are static encoder properties. Once set, these will only take effect after a set media type is called on the camera’s output pin.

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

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 





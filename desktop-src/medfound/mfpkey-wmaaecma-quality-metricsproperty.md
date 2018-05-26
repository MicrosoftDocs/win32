---
Description: Retrieves quality metrics on acoustic echo cancellation (AEC) from the Voice Capture DSP.
ms.assetid: de2e86ae-0469-471f-9105-0bb38a59b428
title: MFPKEY\_WMAAECMA\_QUALITY\_METRICS Property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFPKEY\_WMAAECMA\_QUALITY\_METRICS Property

Retrieves quality metrics on acoustic echo cancellation (AEC) from the Voice Capture DSP.

## Constant for IPropertyBag

Available only by using [**IPropertyStore**](properties.IPropertyStore).

## Data Type

VT\_BLOB

## Remarks

The value of this property is an [AecQualityMetrics\_Struct](/windows/win32/wmcodecdsp/ns-wmcodecdsp-tagaecqualitymetrics_struct?branch=master) structure. This property is read-only.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Wmcodecdsp.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Voice Capture DSP](voicecapturedmo.md)
</dt> </dl>

 

 





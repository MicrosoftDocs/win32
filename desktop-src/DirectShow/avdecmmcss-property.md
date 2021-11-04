---
description: Specifies the Multimedia Class Scheduler Service (MMCSS) class for the decoding thread.
ms.assetid: 77724879-62e4-439e-9dd0-3642cd7f75ca
title: AVDecMmcss property (Uuids.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecMmcss property

Specifies the Multimedia Class Scheduler Service (MMCSS) class for the decoding thread.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVDecMmcssClass**

## Property value

The value of this property is the name of the MMCSS class.

## Remarks

MMCSS enables applications to ensure that time-sensitive processing has prioritized access to CPU resources. It works by elevating registered threads to higher thread priorities while periodically decreasing their priorities to yield time to other processes.

The recommended value for audio decoders is "Audio," and the recommended value for video decoders is "Playback."

If the MMCSS service is not available or the specified MMCSS class does not exist, setting the property has no effect.

## Requirements



| Requirement | Value |
|-------------------|------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Uuids.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 





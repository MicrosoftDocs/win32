---
description: Specifies the target format for an encoder.
ms.assetid: 3d316561-352f-44f9-9978-01301a68e7b6
title: AVEncCommonFormatConstraint property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonFormatConstraint property

Specifies the target format for an encoder.

This property is read/write.

## Data type

**BSTR** (**VT\_BSTR**)

## Property GUID

**CODECAPI\_AVEncCommonFormatConstraint**

## Property value

The value of this property is a **BSTR** that contains the string representation of a GUID. The following GUIDs are defined.



| GUID                                         | Description                     |
|----------------------------------------------|---------------------------------|
| CODECAPI\_GUID\_AVEncCommonFormatATSC        | ATSC cable television.          |
| CODECAPI\_GUID\_AVEncCommonFormatDVB         | DVB cable television.           |
| CODECAPI\_GUID\_AVEncCommonFormatDVD\_DashVR | DVD-VR                          |
| CODECAPI\_GUID\_AVEncCommonFormatDVD\_PlusVR | DVD+VR                          |
| CODECAPI\_GUID\_AVEncCommonFormatDVD\_V      | DVD-Video                       |
| CODECAPI\_GUID\_AVEncCommonFormatHighMAT     | HighMAT                         |
| CODECAPI\_GUID\_AVEncCommonFormatHighMPV     | Not documented in this release. |
| CODECAPI\_GUID\_AVEncCommonFormatMP3         | MPEG Audio Layer-3 (MP3)        |
| CODECAPI\_GUID\_AVEncCommonFormatSVCD        | Super Video CD (SVCD)           |
| CODECAPI\_GUID\_AVEncCommonFormatUnSpecified | Unspecified format.             |
| CODECAPI\_GUID\_AVEncCommonFormatVCD         | Video CD (VCD)                  |



 

## Remarks

Applications can set this property to specify the target format. Encoders can also return this property as a capability.

## Requirements



| Requirement | Value |
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

 

 





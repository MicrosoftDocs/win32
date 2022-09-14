---
description: Specifies whether an encoder must be included in the transcode topology.
ms.assetid: 73f23aed-d1b9-4821-b1ca-0a07f02b6913
title: MF_TRANSCODE_DONOT_INSERT_ENCODER attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TRANSCODE\_DONOT\_INSERT\_ENCODER attribute

Specifies whether an encoder must be included in the transcode topology.

The [**MFCreateTranscodeTopology**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatetranscodetopology) function checks this attribute during topology building. If this attribute is not set, an encoder is inserted in the transcode topology.

## Data type

**UINT32**



| Value                                                                        | Meaning                                                                                                           |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | An encoder is inserted in the transcode topology.<br/>                                                      |
| <dl> <dt>1</dt> </dl> | An encoder is not included in the transcode topology. The source node is connected to the output node.<br/> |



 

## Remarks

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> </dl>

 

 





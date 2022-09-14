---
description: MF_MT_FSSourceTypeDecoded attribute - Specifies whether a decoder can use decode time stamps (DTS) when setting time stamps.
title: MF_MT_FSSourceTypeDecoded
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_MT\_FSSourceTypeDecoded attribute

Specifies that a media type is auto-decoded.

## Data type

**BOOL** stored as **UINT32**


## Remarks
A media type is marked an attribute to indicate this doesn't exist on the physical source and is synthesized by the pipeline. A value of 1 (TRUE) indicates that the media type is synthesized. A value of 0 (FALSE), or the value not being present, indicates that it is not.

In the current release, this attribute should be specified using the following GUID value rather than the MD_MT_FSSourceTypeDecoded constant:

```ea031a62-8bbb-43c5-b5c4-572d2d231c18```


## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> </dl>

 

 





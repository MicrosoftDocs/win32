---
description: Specifies the maximum packet size for an ASF file, in bytes.
ms.assetid: c43423c2-a5f2-411c-aa47-802a3c808ad8
title: MF_ASFPROFILE_MAXPACKETSIZE attribute (Wmcontainer.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_ASFPROFILE\_MAXPACKETSIZE attribute

Specifies the maximum packet size for an ASF file, in bytes.

## Data type

**UINT32**

## Remarks

This attribute applies to ASF profile objects. To set this attribute, use the [**IMFASFProfile**](/windows/desktop/api/wmcontainer/nn-wmcontainer-imfasfprofile) interface.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Wmcontainer.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[ASF Attributes](asf-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> </dl>

 

 





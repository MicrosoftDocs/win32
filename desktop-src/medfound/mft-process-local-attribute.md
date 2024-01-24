---
description: Specifies whether a Media Foundation transform (MFT) is registered only in the applications process.
ms.assetid: e10d6378-8e85-4f73-9fa3-a2e954fc8249
title: MFT_PROCESS_LOCAL_Attribute attribute (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFT\_PROCESS\_LOCAL\_Attribute attribute

Specifies whether a Media Foundation transform (MFT) is registered only in the application's process.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32).

To set this attribute, call [**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32).

## Remarks

This attribute is used as follows:

1.  The application registers a local MFT by calling either the [**MFTRegisterLocal**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocal) or [**MFTRegisterLocalByCLSID**](/windows/desktop/api/mfapi/nf-mfapi-mftregisterlocalbyclsid) function. These functions register the MFT in the application's process.
2.  The [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function is called to enumerate MFTs that match a particular set of criteria. The application might call the **MFTEnumEx** function directly, but more often this function is called by the topology loader.
3.  The [**MFTEnumEx**](/windows/desktop/api/mfapi/nf-mfapi-mftenumex) function retrieves an array of [**IMFActivate**](/windows/desktop/api/mfobjects/nn-mfobjects-imfactivate) pointers, each representing an activation object for an MFT. If an MFT is registered locally, the MFT\_PROCESS\_LOCAL\_Attribute attribute is set to **TRUE** on the corresponding activation object.

The default value for this attribute is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Transform Attributes](transform-attributes.md)
</dt> </dl>

 

 





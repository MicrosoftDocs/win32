---
Description: 'Specifies whether a Media Foundation transform (MFT) is registered only in the application's process.'
ms.assetid: 'e10d6378-8e85-4f73-9fa3-a2e954fc8249'
title: 'MFT\_PROCESS\_LOCAL\_Attribute attribute'
---

# MFT\_PROCESS\_LOCAL\_Attribute attribute

Specifies whether a Media Foundation transform (MFT) is registered only in the application's process.

## Data type

**UINT32**

## Get/set

To get this attribute, call [**IMFAttributes::GetUINT32**](imfattributes-getuint32.md).

To set this attribute, call [**IMFAttributes::SetUINT32**](imfattributes-setuint32.md).

## Remarks

This attribute is used as follows:

1.  The application registers a local MFT by calling either the [**MFTRegisterLocal**](mftregisterlocal.md) or [**MFTRegisterLocalByCLSID**](mftregisterlocalbyclsid.md) function. These functions register the MFT in the application's process.
2.  The [**MFTEnumEx**](mftenumex.md) function is called to enumerate MFTs that match a particular set of criteria. The application might call the **MFTEnumEx** function directly, but more often this function is called by the topology loader.
3.  The [**MFTEnumEx**](mftenumex.md) function retrieves an array of [**IMFActivate**](imfactivate.md) pointers, each representing an activation object for an MFT. If an MFT is registered locally, the MFT\_PROCESS\_LOCAL\_Attribute attribute is set to **TRUE** on the corresponding activation object.

The default value for this attribute is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                          |
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

 

 





---
description: Contains the category GUID for a Media Foundation transform (MFT).
ms.assetid: 3c0948fc-42ea-4e43-a312-c98038020214
title: MFPKEY_CATEGORY property (Mftransform.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFPKEY\_CATEGORY property

Contains the category GUID for a Media Foundation transform (MFT).



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**GUID** (**CLSID**\*)

VT\_CLSID

**puuid**



## Remarks

The value of this property is a GUID that identifies the MFT category. For a list of categories, see [**MFT\_CATEGORY**](mft-category.md).

This property is optional and is informational only. An MFT can use this property to report the category under which it is registered. To get this property, query the MFT for the **IPropertyStore** interface.

To enumerate an MFT category, call the [**MFTEnum**](/windows/desktop/api/mfapi/nf-mfapi-mftenum) function. There is no direct link between the **MFTEnum** function and this property.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Mftransform.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Media Foundation Transforms](media-foundation-transforms.md)
</dt> </dl>

 

 





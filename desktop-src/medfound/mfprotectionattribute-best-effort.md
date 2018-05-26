---
Description: Set as an attribute for an IMFOutputSchema object.
ms.assetid: 0CCCAB27-DEB0-41D8-A70C-D6CCEFE0601F
title: MFPROTECTIONATTRIBUTE\_BEST\_EFFORT attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFPROTECTIONATTRIBUTE\_BEST\_EFFORT attribute

Set as an attribute for an [**IMFOutputSchema**](/windows/win32/mfidl/nn-mfidl-imfoutputschema?branch=master) object. If this attribute is present, a failed attempt to apply the protection is ignored. If the associated attribute value is **TRUE**, the protection schema with the [MFPROTECTIONATTRIBUTE\_FAIL\_OVER](mfprotectionattribute-fail-over.md) attribute should be applied.

## Data type

**BOOL** stored as **UINT32**

## Remarks

If **TRUE**, enforce the protection schema with the [MFPROTECTIONATTRIBUTE\_FAIL\_OVER](mfprotectionattribute-fail-over.md) attribute if setting this protection fails.

Set as an attribute for an [**IMFOutputSchema**](/windows/win32/mfidl/nn-mfidl-imfoutputschema?branch=master) object.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[UWP apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2012 \[UWP apps only\]<br/>                                   |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[Media Type Attributes](media-type-attributes.md)
</dt> </dl>

 

 





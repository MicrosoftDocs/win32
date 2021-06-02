---
description: Enables or disables preview mode, which enables the application to overwrite the initial buffering logic.
ms.assetid: 8aa8c6ac-8746-4bf6-9f57-b1426495a275
title: MFNETSOURCE_PREVIEWMODEENABLED property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PREVIEWMODEENABLED property

Enables or disables preview mode, which enables the application to overwrite the initial buffering logic.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**BOOL**

VT\_BOOL

**lVal**



## Remarks

The constant **MFNETSOURCE\_PREVIEWMODEENABLED** defines the GUID for the property key. The property identifier (PID) is zero. This property is set on the network source by passing an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                            |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 





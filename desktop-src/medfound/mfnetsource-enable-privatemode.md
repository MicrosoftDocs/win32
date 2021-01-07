---
description: Enables private download mode in the network source.
ms.assetid: 679661A7-1D31-43F3-A64E-16ADCB5414B0
title: MFNETSOURCE_ENABLE_PRIVATEMODE property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_ENABLE\_PRIVATEMODE property

Enables private download mode in the network source.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**BOOL**

VT\_I4

**lVal**



## Remarks

If this property is **TRUE**, the cache is cleared when the session ends.

The **MFNETSOURCE\_CLIENTGUID** constant defines the GUID for the property key. The property identifier (PID) is zero. To set this property on the network source, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | None supported<br/>                                                          |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 





---
description: The value of the second portion of the &\#0034;cs(User-Agent)&\#0034; field that the network source uses for logging.
ms.assetid: c662a6d6-5e0b-4c28-841d-5774d4103d4b
title: MFNETSOURCE_PLAYERUSERAGENT property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_PLAYERUSERAGENT property

The value of the second portion of the "cs(User-Agent)" field that the network source uses for logging. Applications can set this property to any string value.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

Wide-character string (**WCHAR**\*)

VT\_LPWSTR

**pwszVal**



## Remarks

The constant **MFNETSOURCE\_PLAYERUSERAGENT** defines the GUID for this property key. The property identifier (PID) is zero.

Applications can use this property to configure the network source. To set the property, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Client Logging](client-logging.md)
</dt> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> <dt>

[**MFNETSOURCE\_BROWSERUSERAGENT**](mfnetsource-browseruseragent-property.md)
</dt> </dl>

 

 





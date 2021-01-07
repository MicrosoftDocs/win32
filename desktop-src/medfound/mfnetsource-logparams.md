---
description: Array of strings with the parameters to send to the log server.
ms.assetid: 36d711c7-a1ff-4ef2-b633-5f9f1662801e
title: MFNETSOURCE_LOGPARAMS property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_LOGPARAMS property

Array of strings with the parameters to send to the log server.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**WCHAR\***

VT\_LPWSTR

**pwszVal**



## Remarks

The **MFNETSOURCE\_LOGPARAMS** constant defines the GUID for the property key. The property identifier (PID) is zero. To set this property on the network source, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

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

 

 





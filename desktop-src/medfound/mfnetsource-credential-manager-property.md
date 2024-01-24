---
description: Contains a pointer to the IMFNetCredentialManager interface.
ms.assetid: c0826956-9df1-40ec-8ad1-9e0dca34d847
title: MFNETSOURCE_CREDENTIAL_MANAGER property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MFNETSOURCE\_CREDENTIAL\_MANAGER property

Contains a pointer to the [**IMFNetCredentialManager**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialmanager) interface. Use this property to pass the application's implementation of [**IMFNetCredentialManager**](/windows/desktop/api/mfidl/nn-mfidl-imfnetcredentialmanager) to the network source.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**IUnknown** pointer

VT\_UNKNOWN

**punkVal**



## Remarks

The constant **MFNETSOURCE\_CREDENTIAL\_MANAGER** defines the **GUID** for the property key. The property identifier (PID) is zero.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Network Source Authentication](network-source-authentication.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> </dl>

 

 





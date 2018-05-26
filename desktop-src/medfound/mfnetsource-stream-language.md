---
Description: Stores the string sent in the Accept-Language header.
ms.assetid: b6ac613c-099b-4415-84ad-c0f8ad5f667b
title: MFNETSOURCE\_STREAM\_LANGUAGE property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFNETSOURCE\_STREAM\_LANGUAGE property

Stores the string sent in the Accept-Language header.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**WCHAR\***

VT\_LPWSTR

**pwszVal**



## Remarks

The MFNETSOURCE\_STREAM\_LANGUAGE constant defines the GUID for the property key. The property identifier (PID) is zero. To set this property on the network source, pass an **IPropertyStore** pointer to the source resolver. For more information, see [Configuring a Media Source](configuring-a-media-source.md).

## Requirements



|                                     |                                                                                    |
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

 

 





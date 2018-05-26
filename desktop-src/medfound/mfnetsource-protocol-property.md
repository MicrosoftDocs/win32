---
Description: Specifies the control protocol used by the network source.
ms.assetid: 4de8b8ba-97d9-4269-a16c-1853dc02f674
title: MFNETSOURCE\_PROTOCOL property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MFNETSOURCE\_PROTOCOL property

Specifies the control protocol used by the network source. The value of this property is a member of the [**MFNETSOURCE\_PROTOCOL\_TYPE**](/windows/win32/mfidl/ne-mfidl-_mfnetsource_protocol_type?branch=master) enumeration.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**LONG**

VT\_I4

**lVal**



## Remarks

The constant **MFNETSOURCE\_PROTOCOL** defines the GUID for this property key. The property identifier (PID) is zero.

This property is read-only. To retrieve this property, query the network source for the **IPropertyStore** interface and call **IPropertyStore::GetValue**.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[Networking in Media Foundation](networking-in-media-foundation.md)
</dt> <dt>

[Supported Protocols](supported-protocols.md)
</dt> </dl>

 

 





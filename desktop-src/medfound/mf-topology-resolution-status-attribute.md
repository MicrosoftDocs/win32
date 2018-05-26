---
Description: Specifies the status of an attempt to resolve a topology.
ms.assetid: 7c2410ce-e70b-4303-9dbc-caff4a355d6b
title: MF\_TOPOLOGY\_RESOLUTION\_STATUS attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPOLOGY\_RESOLUTION\_STATUS attribute

Specifies the status of an attempt to resolve a topology.

## Data type

**UINT32**

## Remarks

The topology loader or the Media Session might set this attribute on a topology. The value of this attribute is a bitwise **OR** of flags from the [**MF\_TOPOLOGY\_RESOLUTION\_STATUS\_FLAGS**](/windows/win32/mfidl/ne-mfidl-_mf_topology_resolution_status_flags?branch=master) enumeration.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfapi.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFTopology**](/windows/win32/mfidl/nn-mfidl-imftopology?branch=master)
</dt> <dt>

[Topology Attributes](topology-attributes.md)
</dt> </dl>

 

 





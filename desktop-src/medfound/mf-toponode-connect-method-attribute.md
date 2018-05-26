---
Description: Specifies how the topology loader connects this topology node, and whether this node is optional.
ms.assetid: 8d70e1af-607b-47c3-9808-091c95fd05b7
title: MF\_TOPONODE\_CONNECT\_METHOD attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_CONNECT\_METHOD attribute

Specifies how the topology loader connects this topology node, and whether this node is optional.

## Data type

**UINT32**

## Remarks

This attribute applies to all node types.

The attribute value is a bitwise **OR** of flags from the [**MF\_CONNECT\_METHOD**](/windows/win32/mfidl/ne-mfidl-_mf_connect_method?branch=master) enumeration. If this attribute is not set, the default value is **MF\_CONNECT\_ALLOW\_DECODER**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getuint32?branch=master)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setuint32?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





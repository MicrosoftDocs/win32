---
Description: Specifies whether a toplogy nodes underlying object is a decrypter.
ms.assetid: 211789d8-5e51-485c-b8f1-cd0ae3e39250
title: MF\_TOPONODE\_DECRYPTOR attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_DECRYPTOR attribute

Specifies whether a toplogy node's underlying object is a decrypter.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to all node types.

If the value of this attribute is nonzero, the node's underlying object is a decrypter.

Applications typically do not use this attribute directly. The Media Session sets this attribute when it creates a node for a decrypter, obtained from the [**IMFInputTrustAuthority::GetDecrypter**](/windows/win32/mfidl/nf-mfidl-imfinputtrustauthority-getdecrypter?branch=master) method.

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

 

 





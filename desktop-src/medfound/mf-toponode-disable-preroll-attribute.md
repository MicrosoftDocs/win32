---
description: Specifies whether the Media Session uses preroll on the media sink represented by this topology node.
ms.assetid: 1781f3a0-6baa-4e06-b2eb-9a8f572aa040
title: MF_TOPONODE_DISABLE_PREROLL attribute (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MF\_TOPONODE\_DISABLE\_PREROLL attribute

Specifies whether the Media Session uses preroll on the media sink represented by this topology node.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to output nodes (**MF\_TOPOLOGY\_OUTPUT\_NODE**).

If the value of this attribute is **TRUE**, the Media Session does not preroll any data to the media sink, even if the media sink exposes the [**IMFMediaSinkPreroll**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasinkpreroll) interface. If the value is **FALSE**, the Media Session prerolls data if the media sink implements **IMFMediaSinkPreroll**. The default value is **FALSE**.

The GUID constant for this attribute is exported from mfuuid.lib.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Alphabetical List of Media Foundation Attributes](alphabetical-list-of-media-foundation-attributes.md)
</dt> <dt>

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





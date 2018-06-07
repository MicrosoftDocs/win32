---
Description: Specifies when a transform is drained.
ms.assetid: 68332106-d1fe-467b-8baa-1e592b9cc243
title: MF\_TOPONODE\_DRAIN attribute
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MF\_TOPONODE\_DRAIN attribute

Specifies when a transform is drained.

## Data type

**UINT32**

## Remarks

This attribute applies to transform nodes (**MF\_TOPOLOGY\_TRANSFORM\_NODE**).

The value of the attribute is a member of the [**MF\_TOPONODE\_DRAIN\_MODE**](/windows/desktop/api/mfidl/ne-mfidl-_mf_toponode_drain_mode) enumeration. If this attribute is not set, the default value is **MF\_TOPONODE\_DRAIN\_DEFAULT**.

Draining is performed by calling [**IMFTransform::ProcessMessage**](/windows/desktop/api/mftransform/nf-mftransform-imftransform-processmessage) on the transform with the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message. For more information, see [**MFT\_MESSAGE\_TYPE**](/windows/desktop/api/mftransform/ne-mftransform-_mft_message_type) enumeration.

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

[**IMFAttributes::GetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-getuint32)
</dt> <dt>

[**IMFAttributes::SetUINT32**](/windows/desktop/api/mfobjects/nf-mfobjects-imfattributes-setuint32)
</dt> <dt>

[**IMFTopologyNode**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynode)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





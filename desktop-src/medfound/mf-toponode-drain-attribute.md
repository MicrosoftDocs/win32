---
Description: Specifies when a transform is drained.
ms.assetid: 68332106-d1fe-467b-8baa-1e592b9cc243
title: MF\_TOPONODE\_DRAIN attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_DRAIN attribute

Specifies when a transform is drained.

## Data type

**UINT32**

## Remarks

This attribute applies to transform nodes (**MF\_TOPOLOGY\_TRANSFORM\_NODE**).

The value of the attribute is a member of the [**MF\_TOPONODE\_DRAIN\_MODE**](/windows/win32/mfidl/ne-mfidl-_mf_toponode_drain_mode?branch=master) enumeration. If this attribute is not set, the default value is **MF\_TOPONODE\_DRAIN\_DEFAULT**.

Draining is performed by calling [**IMFTransform::ProcessMessage**](/windows/win32/mftransform/nf-mftransform-imftransform-processmessage?branch=master) on the transform with the [**MFT\_MESSAGE\_COMMAND\_DRAIN**](mft-message-command-drain.md) message. For more information, see [**MFT\_MESSAGE\_TYPE**](/windows/win32/mftransform/ne-mftransform-_mft_message_type?branch=master) enumeration.

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

 

 





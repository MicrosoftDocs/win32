---
Description: 'Specifies when a transform is flushed.'
ms.assetid: '1e87f58f-546f-4dd4-b218-1458ff17db53'
title: 'MF\_TOPONODE\_FLUSH attribute'
---

# MF\_TOPONODE\_FLUSH attribute

Specifies when a transform is flushed.

## Data type

**UINT32**

## Remarks

This attribute applies to transform nodes (**MF\_TOPOLOGY\_TRANSFORM\_NODE**).

The value of the attribute is a member of the [**MF\_TOPONODE\_FLUSH\_MODE**](mf-toponode-flush-mode.md) enumeration. If this attribute is not set, the default value is **MF\_TOPONODE\_FLUSH\_ALWAYS**.

Flushing is performed by calling [**IMFTransform::ProcessMessage**](imftransform-processmessage.md) on the transform with the [**MFT\_MESSAGE\_COMMAND\_FLUSH**](mft-message-command-flush.md) message. For more information, see [**MFT\_MESSAGE\_TYPE**](mft-message-type.md) enumeration.

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

[**IMFAttributes::GetUINT32**](imfattributes-getuint32.md)
</dt> <dt>

[**IMFAttributes::SetUINT32**](imfattributes-setuint32.md)
</dt> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





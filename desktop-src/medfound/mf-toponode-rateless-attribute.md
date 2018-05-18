---
Description: 'Specifies whether the media sink associated with this topology node is rateless.'
ms.assetid: '81ef7005-a9ab-4f26-bc39-68b27c4f92aa'
title: 'MF\_TOPONODE\_RATELESS attribute'
---

# MF\_TOPONODE\_RATELESS attribute

Specifies whether the media sink associated with this topology node is rateless.

## Data type

**UINT32**

Treat as a Boolean value.

## Remarks

This attribute applies to output nodes (**MF\_TOPOLOGY\_OUTPUT\_NODE**).

If the value of this attribute is nonzero, the Media Session treats the media sink as a rateless sink, regardless of whether the media sink returns the **MEDIASINK\_RATELESS** characteristic. If this attribute is not set, the media sink is assumed not to be rateless.

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

[**IMFMediaSink::GetCharacteristics**](imfmediasink-getcharacteristics.md)
</dt> <dt>

[**IMFTopologyNode**](imftopologynode.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





---
Description: Contains a pointer to the media source associated with a topology node.
ms.assetid: 73b84ab6-bdc2-4b22-9ce4-b79b954476e5
title: MF\_TOPONODE\_SOURCE attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_SOURCE attribute

Contains a pointer to the media source associated with a topology node.

## Data type

**IUnknown\***

## Remarks

This attribute applies to source nodes (**MF\_TOPOLOGY\_SOURCESTREAM\_NODE**).

The value of the atttribute is a pointer to the media source's [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master) interface. This attribute is required.

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

[**IMFAttributes::GetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getunknown?branch=master)
</dt> <dt>

[**IMFAttributes::SetUnknown**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setunknown?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





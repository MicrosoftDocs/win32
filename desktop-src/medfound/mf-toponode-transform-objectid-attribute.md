---
Description: The class identifier (CLSID) of the Media Foundation transform (MFT) associated with this topology node.
ms.assetid: 6aa6e649-d23d-4d8d-be80-2b8814b07a57
title: MF\_TOPONODE\_TRANSFORM\_OBJECTID attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MF\_TOPONODE\_TRANSFORM\_OBJECTID attribute

The class identifier (CLSID) of the Media Foundation transform (MFT) associated with this topology node.

## Data type

**GUID**

## Remarks

This attribute applies to transform nodes (**MF\_TOPOLOGY\_TRANSFORM\_NODE**).

Applications can use this attribute to initialize a transfrom node. If you set this attribute, you do not have to call [**IMFTopologyNode::SetObject**](/windows/win32/mfidl/nf-mfidl-imftopologynode-setobject?branch=master) with a pointer to an MFT or activation object. Conversely, if you call **SetObject**, you do not need to set this attribute. For more information, see [Creating Topologies](creating-topologies.md).

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

[**IMFAttributes::GetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-getguid?branch=master)
</dt> <dt>

[**IMFAttributes::SetGUID**](/windows/win32/mfobjects/nf-mfobjects-imfattributes-setguid?branch=master)
</dt> <dt>

[**IMFTopologyNode**](/windows/win32/mfidl/nn-mfidl-imftopologynode?branch=master)
</dt> <dt>

[Media Foundation Attributes](media-foundation-attributes.md)
</dt> <dt>

[Creating Topologies](creating-topologies.md)
</dt> <dt>

[Topology Node Attributes](topology-node-attributes.md)
</dt> </dl>

 

 





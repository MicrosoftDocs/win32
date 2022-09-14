---
title: sidType (ChannelPublishingType) Element
description: Determines whether to include a security identifier (SID) of the principal with each event written to the channel.
ms.assetid: 3ce176a3-9e21-4646-8c99-7beb687e6847
keywords:
- sidType element EventLog
topic_type:
- apiref
api_name:
- sidType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# sidType (ChannelPublishingType) Element

Determines whether to include a security identifier (SID) of the principal with each event written to the channel.

``` syntax
<xs:element name="sidType">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="None"
             />
            <xs:enumeration
                value="Publishing"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **sidType** element is defined by the [**ChannelPublishingType**](eventmanifestschema-channelpublishingtype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**publishing (ChannelType)**](eventmanifestschema-publishing-channeltype-element.md)
</dt> </dl>

 

 






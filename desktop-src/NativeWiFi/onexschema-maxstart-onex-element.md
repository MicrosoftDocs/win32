---
description: Specifies the maximum number of EAPOL-Start messages sent.
ms.assetid: 4e48f8b6-46eb-426e-ad22-3aa53cb66a17
title: maxStart (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- maxStart
api_type: 
- Schema
api_location: 
---

# maxStart (OneX) Element

The maxStart (OneX) element specifies the maximum number of EAPOL-Start messages sent. After the maximum number of EAPOL-Start messages has been sent, the client assumes that there is no authenticator present on the network.

This element is optional. When maxStart is not specified in a profile, a value of 3 messages is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="maxStart">
    <xs:simpleType>
        <xs:restriction
            base="integer"
        >
            <xs:enumeration
                value="1"
             />
            <xs:enumeration
                value="100"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **maxStart** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 





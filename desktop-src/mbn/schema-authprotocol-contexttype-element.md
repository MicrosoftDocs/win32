---
description: Specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.
ms.assetid: cd3c28d9-8663-4672-94ba-0a53861086cb
title: AuthProtocol (contextType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AuthProtocol
api_type: 
- Schema
---

# AuthProtocol (contextType) Element

The **AuthProtocol (contextType)** element specifies the authentication protocol to be used for activating a Packet Data Protocol (PDP) context.

The element can have one of the following values.

| Value      | Meaning                                                                 |
|------------|-------------------------------------------------------------------------|
| "NONE"     | No authentication protocol.                                             |
| "PAP"      | Unencrypted password authentication.                                    |
| "CHAP"     | Challenge Handshake Authentication Protocol(CHAP).                      |
|  MsCHAPV2" | Use Microsoft s Challenge Handshake Authentication Protocol(CHAP) v2.0. |



 

This element is optional and is used only for GSM profiles. If the element is not specified and the profile is for a GSM device, then the Mobile Broadband service will use **"NONE"**.

``` syntax
<xs:element name="AuthProtocol">
    <xs:simpleType>
        <xs:restriction
            base="token"
        >
            <xs:enumeration
                value="NONE"
             />
            <xs:enumeration
                value="PAP"
             />
            <xs:enumeration
                value="CHAP"
             />
            <xs:enumeration
                value="MsCHAPv2"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **AuthProtocol** element is defined by the [**contextType**](schema-contexttype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**contextType**](schema-contexttype-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Context (MBNProfile)**](schema-context-mbnprofile-element.md)
</dt> </dl>

 

 





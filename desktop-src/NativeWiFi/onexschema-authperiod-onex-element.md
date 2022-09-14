---
description: Specifies the maximum length of time, in seconds, in which a client waits for a response from the authenticator.
ms.assetid: 5cb2e164-913f-4c35-854f-aac8ed180c46
title: authPeriod (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- authPeriod
api_type: 
- Schema
api_location: 
---

# authPeriod (OneX) Element

The authPeriod (OneX) element specifies the maximum length of time, in seconds, in which a client waits for a response from the authenticator. If a response is not received within the specified period, the client assumes that there is no authenticator present on the network.

This element is optional. When authPeriod is not specified in a profile, a value of 18 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="authPeriod">
    <xs:simpleType>
        <xs:restriction
            base="integer"
        >
            <xs:enumeration
                value="1"
             />
            <xs:enumeration
                value="3600"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **authPeriod** element is defined by the [**OneX**](onexschema-onex-element.md) element.

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

 

 





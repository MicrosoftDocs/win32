---
description: Specifies the method of transmission used for EAPOL-Start messages.
ms.assetid: 8d49d19a-8122-4191-bb46-92a2016bcfee
title: supplicantMode (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- supplicantMode
api_type: 
- Schema
api_location: 
---

# supplicantMode (OneX) Element

The supplicantMode (OneX) element specifies the method of transmission used for EAPOL-Start messages. The following table describes the possible values.



| Value               | Description                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| inhibitTransmission | EAPOL-Start messages are not transmitted. Valid for wired LAN profiles only.                                                                                             |
| includeLearning     | The client determines when to send EAPOL-Start packets based on network capability. EAPOL-Start messages are only sent when required. Valid for wired LAN profiles only. |
| compliant           | EAPOL-Start messages are transmitted as specified by 802.1X. Valid for both wired and wireless LAN profiles.                                                             |



 

This element is optional. When supplicantMode is not specified in a profile, a value of `compliant` is used for both wired and wireless LAN profiles.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="supplicantMode">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="inhibitTransmission"
             />
            <xs:enumeration
                value="includeLearning"
             />
            <xs:enumeration
                value="compliant"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **supplicantMode** element is defined by the [**OneX**](onexschema-onex-element.md) element.

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

 

 





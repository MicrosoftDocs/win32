---
description: Is the root element that identifies a Mobile Broadband profile.
ms.assetid: 08302e7f-3024-439b-a2ad-a4ae9487b82b
title: MBNProfile Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MBNProfile
api_type: 
- Schema
---

# MBNProfile Element

The **MBNProfile** element is the root element that identifies a Mobile Broadband profile.

There can only be one element of this type per document.

``` syntax
<xs:element name="MBNProfile">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="Name"
                type="nameType"
             />
            <xs:element name="Description"
                type="nameType"
                minOccurs="0"
             />
            <xs:element name="ICONFilePath"
                type="iconFileType"
                minOccurs="0"
             />
            <xs:element name="IsDefault"
                type="boolean"
             />
            <xs:element name="ProfileCreationType"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="token"
                    >
                        <xs:enumeration
                            value="UserProvisioned"
                         />
                        <xs:enumeration
                            value="AdminProvisioned"
                         />
                        <xs:enumeration
                            value="OperatorProvisioned"
                         />
                        <xs:enumeration
                            value="DeviceProvisioned"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="SubscriberID"
                type="subscriberIdType"
             />
            <xs:element name="SimIccID"
                type="simIccIDType"
                minOccurs="0"
             />
            <xs:element name="HomeProviderName"
                type="providerNameType"
                minOccurs="0"
             />
            <xs:element name="AutoConnectOnInternet"
                type="boolean"
                minOccurs="0"
             />
            <xs:element name="ConnectionMode"
                minOccurs="0"
            >
                <xs:simpleType>
                    <xs:restriction
                        base="string"
                    >
                        <xs:enumeration
                            value="manual"
                         />
                        <xs:enumeration
                            value="auto"
                         />
                        <xs:enumeration
                            value="auto-home"
                         />
                    </xs:restriction>
                </xs:simpleType>
            </xs:element>
            <xs:element name="Context"
                type="contextType"
                minOccurs="0"
             />
            <xs:element name="DataRoamingPartners"
                minOccurs="0"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                          | Type                                                           | Description                                               |
|----------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------|
| [**AutoConnectOnInternet**](schema-autoconnectoninternet-mbnprofile-element.md) | boolean                                                        | Whether the device will automatically connect.<br/> |
| [**ConnectionMode**](schema-connectionmode-mbnprofile-element.md)               |                                                                | The device auto connection settings.<br/>           |
| [**Context**](schema-context-mbnprofile-element.md)                             | [**contextType**](schema-contexttype-complextype.md)          | Data connection setup parameters.<br/>              |
| [**DataRoamingPartners**](schema-dataroamingpartners-mbnprofile-element.md)     |                                                                | Preferred network providers for roaming.<br/>       |
| [**Description**](schema-description-mbnprofile-element.md)                     | [**nameType**](schema-nametype-simpletype.md)                 | Description of the profile.<br/>                    |
| [**HomeProviderName**](schema-homeprovidername-mbnprofile-element.md)           | [**providerNameType**](schema-providernametype-simpletype.md) | Name of the home provider.<br/>                     |
| [**ICONFilePath**](schema-iconfilepath-mbnprofile-element.md)                   | [**iconFileType**](schema-iconfiletype-simpletype.md)         | Path to the icon file.<br/>                         |
| [**IsDefault**](schema-isdefault-mbnprofile-element.md)                         | boolean                                                        | Whether the profile is the default.<br/>            |
| [**Name**](schema-name-mbnprofile-element.md)                                   | [**nameType**](schema-nametype-simpletype.md)                 | Name of the profile.<br/>                           |
| [**ProfileCreationType**](schema-profilecreationtype-mbnprofile-element.md)     |                                                                | Information about the profile creator.<br/>         |
| [**SimIccID**](schema-simiccid-mbnprofile-element.md)                           | [**simIccIDType**](schema-simiccidtype-simpletype.md)         | SIM identification number for GSM devices.<br/>     |
| [**SubscriberID**](schema-subscriberid-mbnprofile-element.md)                   | [**subscriberIdType**](schema-subscriberidtype-simpletype.md) | Unique identifier of the profile.<br/>              |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 





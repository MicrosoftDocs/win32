---
description: Specifies the connenction context of a Mobile Broadband device.
ms.assetid: 513e744d-bd62-43e9-a636-6690867d8b9b
title: contextType Complex Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- contextType
api_type: 
- Schema
---

# contextType Complex Type

The **contextType** complex type specifies the connenction context of a Mobile Broadband device.

``` syntax
<xs:complexType name="contextType">
    <xs:sequence>
        <xs:element name="AccessString"
            minOccurs="0"
        >
            <xs:simpleType>
                <xs:restriction
                    base="token"
                >
                    <xs:minLength
                        value="1"
                     />
                    <xs:maxLength
                        value="100"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
        <xs:element name="UserLogonCred"
            minOccurs="0"
        >
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="UserName"
                        type="nameType"
                     />
                    <xs:element name="IgnorePassword"
                        type="boolean"
                        minOccurs="0"
                     />
                    <xs:element name="Password"
                        type="string"
                        minOccurs="0"
                     />
                </xs:sequence>
            </xs:complexType>
        </xs:element>
        <xs:element name="Compression"
            minOccurs="0"
        >
            <xs:simpleType>
                <xs:restriction
                    base="token"
                >
                    <xs:enumeration
                        value="DISABLE"
                     />
                    <xs:enumeration
                        value="ENABLE"
                     />
                </xs:restriction>
            </xs:simpleType>
        </xs:element>
        <xs:element name="AuthProtocol"
            minOccurs="0"
        >
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
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                               | Type                                           | Description                                                                                    |
|-----------------------------------------------------------------------|------------------------------------------------|------------------------------------------------------------------------------------------------|
| [**AccessString**](schema-accessstring-contexttype-element.md)       |                                                | APN or dial string to be used to establish a data connection<br/>                        |
| [**AuthProtocol**](schema-authprotocol-contexttype-element.md)       |                                                | Authentication protocol to be used for activating a PDP context.<br/>                    |
| [**Compression**](schema-compression-contexttype-element.md)         |                                                | Specifies if compression will be used at the data link for header and data transfer<br/> |
| [**IgnorePassword**](schema-ignorepassword-userlogoncred-element.md) | boolean                                        | How to handle passwords when upgrading profiles.<br/>                                    |
| [**Password**](schema-password-userlogoncred-element.md)             | string                                         | Password used to authenticate a user<br/>                                                |
| [**UserLogonCred**](schema-userlogoncred-contexttype-element.md)     |                                                | Log on credentials for a connection.<br/>                                                |
| [**UserName**](schema-username-userlogoncred-element.md)             | [**nameType**](schema-nametype-simpletype.md) | User name for logon<br/>                                                                 |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



 

 





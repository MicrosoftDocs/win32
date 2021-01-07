---
description: Contains logon credentials for a connection.
ms.assetid: 79c1d277-6284-4adb-a1bd-6c207b37e33e
title: UserLogonCred (contextType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UserLogonCred
api_type: 
- Schema
---

# UserLogonCred (contextType) Element

The **UserLogonCred (contextType)** element contains logon credentials for a connection.

This element can have the following child elements.

-   [**UserName**](schema-username-userlogoncred-element.md)
-   [**Password**](schema-password-userlogoncred-element.md)
-   [**IgnorePassword**](schema-ignorepassword-userlogoncred-element.md)

This element can have a maximum of one occurrence.

This element is optional.

``` syntax
<xs:element name="UserLogonCred">
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
```

The **UserLogonCred** element is defined by the [**contextType**](schema-contexttype-complextype.md) complex type.

## Child elements



| Element                                                               | Type                                           | Description                                                 |
|-----------------------------------------------------------------------|------------------------------------------------|-------------------------------------------------------------|
| [**IgnorePassword**](schema-ignorepassword-userlogoncred-element.md) | boolean                                        | How to handle passwords when upgrading profiles.<br/> |
| [**Password**](schema-password-userlogoncred-element.md)             | string                                         | User password.<br/>                                   |
| [**UserName**](schema-username-userlogoncred-element.md)             | [**nameType**](schema-nametype-simpletype.md) | User name.<br/>                                       |



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

 

 





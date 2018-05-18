---
Description: 'Defines a collection of name/value pairs that represent extended terms or custom properties.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3548af01-ec00-428c-af90-0390bfa3d414'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection Complex Type
---

# NameValueCollection Complex Type

Defines a collection of name/value pairs that represent extended terms or custom properties.

``` syntax
<xs:complexType name="NameValueCollection">
    <xs:sequence>
        <xs:element name="Term"
            type="NameValue"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                     | Type                                                 | Description                                     |
|-------------------------------------------------------------|------------------------------------------------------|-------------------------------------------------|
| [**Term**](jobschema-term-namevaluecollection1-element.md) | [**NameValue**](jobschema-namevalue-complextype.md) | An extended term or custom property.<br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 





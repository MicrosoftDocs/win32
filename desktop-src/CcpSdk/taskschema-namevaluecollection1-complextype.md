---
Description: 'Defines a collection of name/value pairs that represent extended terms and custom properties for a task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3ad93324-2a35-4e4b-827f-54651aa18da3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection1 Complex Type
---

# NameValueCollection1 Complex Type

Defines a collection of name/value pairs that represent extended terms and custom properties for a task.

``` syntax
<xs:complexType name="NameValueCollection1">
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



| Element                                                      | Type                                                  | Description                                      |
|--------------------------------------------------------------|-------------------------------------------------------|--------------------------------------------------|
| [**Term**](taskschema-term-namevaluecollection1-element.md) | [**NameValue**](taskschema-namevalue-complextype.md) | An extended term or custom property. <br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 





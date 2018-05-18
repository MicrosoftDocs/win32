---
Description: 'Defines a name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e06223ff-a84f-40bd-bb9a-99b9a17000ea'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValue Complex Type
---

# NameValue Complex Type

Defines a name/value pair.

``` syntax
<xs:complexType name="NameValue">
    <xs:sequence>
        <xs:element name="Name"
            type="string"
            minOccurs="0"
            maxOccurs="1"
         />
        <xs:element name="Value"
            type="string"
            minOccurs="0"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                             | Type   | Description                                   |
|-----------------------------------------------------|--------|-----------------------------------------------|
| [**Name**](taskschema-name-namevalue-element.md)   | string | The name of the name/value pair. <br/>  |
| [**Value**](taskschema-value-namevalue-element.md) | string | The value of the name/value pair. <br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 





---
Description: 'Defines a collection of name/value pairs that represent environment variables.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '287743b3-2141-4f69-a667-94e4601ab1b4'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection Complex Type
---

# NameValueCollection Complex Type

Defines a collection of name/value pairs that represent environment variables.

``` syntax
<xs:complexType name="NameValueCollection">
    <xs:sequence>
        <xs:element name="Variable"
            type="NameValue"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                             | Type                                                  | Description                         |
|---------------------------------------------------------------------|-------------------------------------------------------|-------------------------------------|
| [**Variable**](taskschema-variable-namevaluecollection-element.md) | [**NameValue**](taskschema-namevalue-complextype.md) | An environment variable.<br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 





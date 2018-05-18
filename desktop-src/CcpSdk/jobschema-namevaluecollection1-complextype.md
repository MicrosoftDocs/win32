---
Description: 'Defines a collection of name/value pairs that represent environment variables for the tasks in the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'df3c48f0-95dd-40f0-aa08-74d8df974d5d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection1 Complex Type
---

# NameValueCollection1 Complex Type

Defines a collection of name/value pairs that represent environment variables for the tasks in the job.

``` syntax
<xs:complexType name="NameValueCollection1">
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



| Element                                                            | Type                                                 | Description                         |
|--------------------------------------------------------------------|------------------------------------------------------|-------------------------------------|
| [**Variable**](jobschema-variable-namevaluecollection-element.md) | [**NameValue**](jobschema-namevalue-complextype.md) | An environment variable.<br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 





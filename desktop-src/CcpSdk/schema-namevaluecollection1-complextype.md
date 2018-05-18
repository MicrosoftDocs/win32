---
Description: 'Defines a collection of name/value pairs that represent environment variables.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2518d8f4-c473-4ec4-a80c-b3455d7c80bc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection1 Complex Type
---

# NameValueCollection1 Complex Type

Defines a collection of name/value pairs that represent environment variables.

``` syntax
<xs:complexType name="NameValueCollection1">
    <xs:sequence>
        <xs:element name="Variable"
            type="NameValue"
            minOccurs="0"
            maxOccurs="unbounded"
            nillable="true"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                          | Type                                              | Description                         |
|------------------------------------------------------------------|---------------------------------------------------|-------------------------------------|
| [**Variable**](schema-variable-namevaluecollection1-element.md) | [**NameValue**](schema-namevalue-complextype.md) | An environment variable.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 





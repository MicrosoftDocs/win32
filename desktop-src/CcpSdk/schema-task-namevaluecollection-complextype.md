---
Description: 'Defines a collection of name/value pairs that represent environment variables.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3e5a8165-ee53-4c09-b362-a15b5f4e0268'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection
---

# NameValueCollection

Defines a collection of name/value pairs that represent environment variables.

``` syntax
<xs:complexType name="NameValueCollection">
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



| Element                                                         | Type                                                   | Description                         |
|-----------------------------------------------------------------|--------------------------------------------------------|-------------------------------------|
| [**Variable**](schema-variable-namevaluecollection-element.md) | [**NameValue**](schema-task-namevalue-complextype.md) | An environment variable.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Complex Types](schema-task-complex-types.md)
</dt> </dl>

 

 





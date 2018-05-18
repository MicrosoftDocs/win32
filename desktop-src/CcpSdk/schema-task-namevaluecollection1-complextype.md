---
Description: 'Defines a collection of name/value pairs that represent extended task terms.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '84c73910-52ab-4da6-90f5-b4df261c3335'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection1 Complex Type
---

# NameValueCollection1 Complex Type

Defines a collection of name/value pairs that represent extended task terms.

``` syntax
<xs:complexType name="NameValueCollection1">
    <xs:sequence>
        <xs:element name="Term"
            type="NameValue"
            minOccurs="0"
            maxOccurs="unbounded"
            nillable="true"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                  | Type                                                   | Description                       |
|----------------------------------------------------------|--------------------------------------------------------|-----------------------------------|
| [**Term**](schema-term-namevaluecollection1-element.md) | [**NameValue**](schema-task-namevalue-complextype.md) | An extended task term.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Complex Types](schema-task-complex-types.md)
</dt> </dl>

 

 





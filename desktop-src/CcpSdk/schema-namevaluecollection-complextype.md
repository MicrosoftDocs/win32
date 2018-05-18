---
Description: 'Defines a collection of name/value pairs that represent extended terms for a job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f2ea8ba6-8160-49d5-8239-5f2995ec7265'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValueCollection
---

# NameValueCollection

Defines a collection of name/value pairs that represent extended terms for a job or task.

``` syntax
<xs:complexType name="NameValueCollection">
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



| Element                                                 | Type                                              | Description                  |
|---------------------------------------------------------|---------------------------------------------------|------------------------------|
| [**Term**](schema-term-namevaluecollection-element.md) | [**NameValue**](schema-namevalue-complextype.md) | An extended term.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 





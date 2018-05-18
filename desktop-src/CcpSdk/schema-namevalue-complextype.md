---
Description: 'Defines a name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1ef9d22e-e84f-4936-9d49-b6e1f7f9ee88'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: NameValue
---

# NameValue

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



| Element                                         | Type                                                            | Description           |
|-------------------------------------------------|-----------------------------------------------------------------|-----------------------|
| [**Name**](schema-name-namevalue-element.md)   | [string](https://msdn.microsoft.com/library/system.string.aspx) | The name.<br/>  |
| [**Value**](schema-value-namevalue-element.md) | [string](https://msdn.microsoft.com/library/system.string.aspx) | The value.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 





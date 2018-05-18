---
Description: 'Defines a name/value pair.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3240efa1-2771-44bc-b42c-21006ef34fca'
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



| Element                                              | Type                                                            | Description           |
|------------------------------------------------------|-----------------------------------------------------------------|-----------------------|
| [**Name**](schema-task-name-namevalue-element.md)   | [string](https://msdn.microsoft.com/library/system.string.aspx) | The name.<br/>  |
| [**Value**](schema-task-value-namevalue-element.md) | [string](https://msdn.microsoft.com/library/system.string.aspx) | The value.<br/> |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Complex Types](schema-task-complex-types.md)
</dt> </dl>

 

 





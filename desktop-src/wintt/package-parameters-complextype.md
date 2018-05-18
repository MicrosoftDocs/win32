---
title: Parameters Complex Type
description: Defines a collection of parameters.
ms.assetid: 'ebce9a18-a70e-410c-b262-760a298f0592'
keywords: ["Parameters complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Parameters
api_type:
- Schema
---

# Parameters Complex Type

Defines a collection of parameters.

``` syntax
<xs:complexType name="Parameters">
    <xs:sequence>
        <xs:element name="Parameter"
            type="dcmPS:Parameter"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element   | Type                                                     | Description                                                                                                                   |
|-----------|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Parameter | [**dcmPS:Parameter**](package-parameter-complextype.md) | A collection of parameters that are used to provide values for the substitution strings found the display strings.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Parameters (DisplayInformation) Element**](package-parameters-displayinformation-element.md)
</dt> <dt>

[**Parameters (Script) Element**](package-parameters-script-element.md)
</dt> </dl>

 

 






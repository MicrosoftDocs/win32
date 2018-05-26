---
title: Parameter Complex Type
description: Defines a parameter name and default value.
ms.assetid: 4fae1ae9-03f6-4b41-bac2-7220268c4829
keywords:
- Parameter complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Parameter
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Parameter Complex Type

Defines a parameter name and default value.

``` syntax
<xs:complexType name="Parameter">
    <xs:sequence>
        <xs:element name="Name"
            type="dcmPS:Name"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="DefaultValue"
            type="xs:string"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element      | Type                                          | Description                                                                        |
|--------------|-----------------------------------------------|------------------------------------------------------------------------------------|
| DefaultValue | xs:string                                     | The default value to use for the parameter if a value is not specified.<br/> |
| Name         | [**dcmPS:Name**](package-name-simpletype.md) | The name of the parameter.<br/>                                              |



## Remarks

Parameters are used to provide substitution values. The substitution string (for example, %*name*%) uses the parameter name. The value depends on the context in which the parameter is used.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Parameter (Parameters) Element**](package-parameter-parameters-element.md)
</dt> <dt>

[**Parameters Complex Type**](package-parameters-complextype.md)
</dt> </dl>

 

 






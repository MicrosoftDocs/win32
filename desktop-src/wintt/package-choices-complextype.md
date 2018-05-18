---
title: Choices Complex Type
description: Defines a collection of choices to display to the user.
ms.assetid: 'ea186559-3e63-4ea1-a4ea-dca487062fe3'
keywords: ["Choices complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Choices
api_type:
- Schema
---

# Choices Complex Type

Defines a collection of choices to display to the user.

``` syntax
<xs:complexType name="Choices">
    <xs:sequence>
        <xs:element name="Choice"
            type="dcmPS:Choice"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element | Type                                               | Description                                                                              |
|---------|----------------------------------------------------|------------------------------------------------------------------------------------------|
| Choice  | [**dcmPS:Choice**](package-choice-complextype.md) | A list of choices. The choices are displayed in the order they were entered. <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Choices Complex Type**](package-choices-complextype.md)
</dt> <dt>

[**Choices (MultipleResponseInteraction) Element**](package-choices-multipleresponseinteraction-element.md)
</dt> <dt>

[**Choices (SingleResponseInteraction) Element**](package-choices-singleresponseinteraction-element.md)
</dt> </dl>

 

 






---
title: SingleResponseInteractions Complex Type
description: Defines a collection of interactions that let the user select a single choice from a list of choices.
ms.assetid: 86741051-2e62-40cf-b5b4-3fc536d749bc
keywords:
- SingleResponseInteractions complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- SingleResponseInteractions
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SingleResponseInteractions Complex Type

Defines a collection of interactions that let the user select a single choice from a list of choices.

``` syntax
<xs:complexType name="SingleResponseInteractions">
    <xs:sequence>
        <xs:element name="SingleResponseInteraction"
            type="dcmPS:SingleResponseInteraction"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                   | Type                                                                                     | Description                                                                                              |
|---------------------------|------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| SingleResponseInteraction | [**dcmPS:SingleResponseInteraction**](package-singleresponseinteraction-complextype.md) | A collection of interactions that let the user select a single choice from a list of choices.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Interactions Complex Type**](package-interactions-complextype.md)
</dt> <dt>

[**SingleResponseInteractions (Interactions) Element**](package-singleresponseinteractions-interactions-element.md)
</dt> </dl>

 

 






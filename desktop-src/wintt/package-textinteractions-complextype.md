---
title: TextInteractions Complex Type
description: Defines a collection of interactions that request input from the user.
ms.assetid: 8acf4597-322f-4ae9-aa07-115790e612de
keywords:
- TextInteractions complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- TextInteractions
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TextInteractions Complex Type

Defines a collection of interactions that request input from the user.

``` syntax
<xs:complexType name="TextInteractions">
    <xs:sequence>
        <xs:element name="TextInteraction"
            type="dcmPS:TextInteraction"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element         | Type                                                                 | Description                                                               |
|-----------------|----------------------------------------------------------------------|---------------------------------------------------------------------------|
| TextInteraction | [**dcmPS:TextInteraction**](package-textinteraction-complextype.md) | A collection of interactions that request input from the user.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Interactions Complex Type**](package-interactions-complextype.md)
</dt> <dt>

[**TextInteractions (Interactions) Element**](package-textinteractions-interactions-element.md)
</dt> </dl>

 

 






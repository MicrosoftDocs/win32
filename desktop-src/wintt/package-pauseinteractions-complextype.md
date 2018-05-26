---
title: PauseInteractions Complex Type
description: Defines a collection of interactions that provide instructions to the user.
ms.assetid: a9da89a3-0610-41fb-85fb-0b0a11421ae6
keywords:
- PauseInteractions complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- PauseInteractions
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# PauseInteractions Complex Type

Defines a collection of interactions that provide instructions to the user.

``` syntax
<xs:complexType name="PauseInteractions">
    <xs:sequence>
        <xs:element name="PauseInteraction"
            type="dcmPS:PauseInteraction"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element          | Type                                                                   | Description                                                                    |
|------------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| PauseInteraction | [**dcmPS:PauseInteraction**](package-pauseinteraction-complextype.md) | A collection of interactions that provide instructions to the user.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Interactions Complex Type**](package-interactions-complextype.md)
</dt> <dt>

[**PauseInteractions (Interactions) Element**](package-pauseinteractions-interactions-element.md)
</dt> </dl>

 

 






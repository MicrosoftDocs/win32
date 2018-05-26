---
title: LaunchUIInteractions Complex Type
description: Defines a collection of interactions that launch UI applications.
ms.assetid: 9c2284cd-2cf8-433e-9f89-0b3b5fa8625d
keywords:
- LaunchUIInteractions complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- LaunchUIInteractions
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# LaunchUIInteractions Complex Type

Defines a collection of interactions that launch UI applications.

``` syntax
<xs:complexType name="LaunchUIInteractions">
    <xs:sequence>
        <xs:element name="LaunchUIInteraction"
            type="dcmPS:LaunchUIInteraction"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element             | Type                                                                         | Description                                                           |
|---------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| LaunchUIInteraction | [**dcmPS:LaunchUIInteraction**](package-launchuiinteraction-complextype.md) | A collection of interactions that launch UI applications. <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Interactions Complex Type**](package-interactions-complextype.md)
</dt> <dt>

[**LaunchUIInteractions (Interactions) Element**](package-launchuiinteractions-interactions-element.md)
</dt> </dl>

 

 






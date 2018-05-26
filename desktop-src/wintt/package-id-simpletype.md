---
title: ID Simple Type
description: Defines a string that you use to specify an identifier value.
ms.assetid: 1cd58767-032b-4d09-9e34-4016a611728e
keywords:
- ID simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- ID
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ID Simple Type

Defines a string that you use to specify an identifier value.

``` syntax
<xs:simpleType name="ID">
    <xs:restriction
        base="Name"
    >
        <xs:pattern
            value="[^\']+"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **ID** simple type is a [**Name**](package-name-simpletype.md) that is restricted by the following pattern:

-   `[^\']+`

    Inherits the restrictions from [**Name**](package-name-simpletype.md) and further restricts the string by not allowing the single quote character.

## Remarks

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**GlobalRootcause**](package-globalrootcause-complextype.md)
</dt> <dt>

[**LaunchUIInteraction**](package-launchuiinteraction-complextype.md)
</dt> <dt>

[**LocalRootcause**](package-localrootcause-complextype.md)
</dt> <dt>

[**MultipleResponseInteraction**](package-multipleresponseinteraction-complextype.md)
</dt> <dt>

[**PauseInteraction**](package-pauseinteraction-complextype.md)
</dt> <dt>

[**Resolvers**](package-resolvers-complextype.md)
</dt> <dt>

[**SingleResponseInteraction**](package-singleresponseinteraction-complextype.md)
</dt> <dt>

[**TextInteraction**](package-textinteraction-complextype.md)
</dt> </dl>

 

 






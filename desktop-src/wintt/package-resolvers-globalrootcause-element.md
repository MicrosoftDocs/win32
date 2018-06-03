---
title: Resolvers (GlobalRootcause) Element
description: Contains a collection of resolver scripts to run.
ms.assetid: 8bbfb90e-281b-4623-9579-398326dbdc9d
keywords:
- Resolvers element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Resolvers
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resolvers (GlobalRootcause) Element

Contains a collection of resolver scripts to run.

``` syntax
<xs:element name="Resolvers">
    <xs:unique name="No_global_resolver_may_have_the_same_ID">
        <xs:selector
            xpath="Resolver"
         />
        <xs:field
            xpath="ID"
         />
    </xs:unique>
</xs:element>
```

The **Resolvers** element is defined by the [**GlobalRootcause**](package-globalrootcause-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






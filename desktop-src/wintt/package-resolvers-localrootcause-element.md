---
title: Resolvers (LocalRootcause) Element
description: Contains a collection of resolver scripts to run.
ms.assetid: '7a354706-3f6f-4cf5-936e-a84bc35fd068'
keywords: ["Resolvers element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Resolvers
api_type:
- Schema
---

# Resolvers (LocalRootcause) Element

Contains a collection of resolver scripts to run.

``` syntax
<xs:element name="Resolvers">
    <xs:unique name="No_local_resolver_may_have_the_same_ID">
        <xs:selector
            xpath="Resolver"
         />
        <xs:field
            xpath="ID"
         />
    </xs:unique>
</xs:element>
```

The **Resolvers** element is defined by the [**LocalRootcause**](package-localrootcause-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






---
title: Parameters (LaunchUIInteraction) Element
description: A list of parameter names.
ms.assetid: '7c27570e-44e6-4366-941a-d06bd93371dc'
keywords: ["Parameters element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Parameters
api_type:
- Schema
---

# Parameters (LaunchUIInteraction) Element

A list of parameter names.

``` syntax
<xs:element name="Parameters">
    <xs:unique name="No_cmdline_parameters_may_have_the_same_name">
        <xs:selector
            xpath="Parameter"
         />
        <xs:field
            xpath="Name"
         />
    </xs:unique>
</xs:element>
```

The **Parameters** element is defined by the [**LaunchUIInteraction**](package-launchuiinteraction-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






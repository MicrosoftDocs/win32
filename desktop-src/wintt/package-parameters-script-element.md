---
title: Parameters (Script) Element
description: A list of parameter names.
ms.assetid: 6957b81b-7a65-41a9-b922-4e1558ed0085
keywords:
- Parameters element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Parameters
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Parameters (Script) Element

A list of parameter names.

``` syntax
<xs:element name="Parameters">
    <xs:unique name="No_script_parameters_may_have_the_same_name">
        <xs:selector
            xpath="Parameter"
         />
        <xs:field
            xpath="Name"
         />
    </xs:unique>
</xs:element>
```

The **Parameters** element is defined by the [**Script**](package-script-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






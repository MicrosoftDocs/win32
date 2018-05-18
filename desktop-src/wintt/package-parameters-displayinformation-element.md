---
title: Parameters (DisplayInformation) Element
description: A list of parameter names.
ms.assetid: '51243f09-25ea-4b98-a661-0ebbd05267a9'
keywords: ["Parameters element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Parameters
api_type:
- Schema
---

# Parameters (DisplayInformation) Element

A list of parameter names.

``` syntax
<xs:element name="Parameters">
    <xs:unique name="No_display_parameters_may_have_the_same_name">
        <xs:selector
            xpath="Parameter"
         />
        <xs:field
            xpath="Name"
         />
    </xs:unique>
</xs:element>
```

The **Parameters** element is defined by the [**DisplayInformation**](package-displayinformation-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






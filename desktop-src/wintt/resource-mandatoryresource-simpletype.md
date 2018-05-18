---
title: MandatoryResource Simple Type
description: Defines a string type that must contain content.
ms.assetid: 'd0f91a9f-bc9d-473c-9f5b-d76dce5466d1'
keywords: ["MandatoryResource simple type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- MandatoryResource
api_type:
- Schema
---

# MandatoryResource Simple Type

Defines a string type that must contain content.

``` syntax
<xs:simpleType name="MandatoryResource">
    <xs:restriction
        base="string"
    >
        <xs:maxLength
            value="1024"
         />
        <xs:minLength
            value="1"
         />
    </xs:restriction>
</xs:simpleType>
```

## Remarks

The string must contain at least one character but no more than 1,024 characters.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DisplayInformation**](package-displayinformation-complextype.md)
</dt> </dl>

 

 






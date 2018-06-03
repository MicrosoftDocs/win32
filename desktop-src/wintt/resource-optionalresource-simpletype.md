---
title: OptionalResource Simple Type
description: Defines a string type that may or may not contain content.
ms.assetid: b7caee52-1373-4b89-b208-efa48fd81ea5
keywords:
- OptionalResource simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- OptionalResource
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OptionalResource Simple Type

Defines a string type that may or may not contain content.

``` syntax
<xs:simpleType name="OptionalResource">
    <xs:restriction
        base="string"
    >
        <xs:maxLength
            value="1024"
         />
        <xs:minLength
            value="0"
         />
    </xs:restriction>
</xs:simpleType>
```

## Remarks

The string can be empty or contain up to 1,024 characters.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DisplayInformation**](package-displayinformation-complextype.md)
</dt> </dl>

 

 






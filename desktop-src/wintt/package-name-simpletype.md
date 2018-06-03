---
title: Name Simple Type
description: Defines a string that you use to specify a name value.
ms.assetid: b360fd73-f91a-4a76-9c50-4ae61507af54
keywords:
- Name simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Name
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Name Simple Type

Defines a string that you use to specify a name value.

``` syntax
<xs:simpleType name="Name">
    <xs:restriction
        base="xs:string"
    >
        <xs:maxLength
            value="256"
         />
        <xs:minLength
            value="1"
         />
        <xs:pattern
            value="[^ :/\r\n\t\\]+"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **Name** simple type is a xs:string that is restricted by the following pattern:

-   `[^ :/\r\n\t\\]+`

    You can specify any character except a space, colon, slash, carriage return, newline character, tab, or backslash.

## Remarks

The string must contain a least one character but no more than 256 characters.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**ID**](package-id-simpletype.md)
</dt> <dt>

[**Parameter**](package-parameter-complextype.md)
</dt> <dt>

[**Script**](package-script-complextype.md)
</dt> </dl>

 

 






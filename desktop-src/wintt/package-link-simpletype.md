---
title: Link Simple Type
description: Defines a string that you use to specify a URL.
ms.assetid: 2e7d5220-c80d-44a5-b675-bef5741796b1
keywords:
- Link simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Link
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Link Simple Type

Defines a string that you use to specify a URL.

``` syntax
<xs:simpleType name="Link">
    <xs:restriction
        base="xs:string"
    >
        <xs:pattern
            value="(http[s]?:\/\/.+)?"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **Link** simple type is a xs:string that is restricted by the following pattern:

-   `(http[s]?:\/\/.+)?`

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**GlobalDiagnosticPackage**](package-globaldiagnosticpackage-complextype.md)
</dt> </dl>

 

 






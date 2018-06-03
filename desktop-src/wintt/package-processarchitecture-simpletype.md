---
title: ProcessArchitecture Simple Type
description: Defines the possible process architecture values.
ms.assetid: 922d1915-4767-44c6-98d7-00657f2b7929
keywords:
- ProcessArchitecture simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- ProcessArchitecture
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ProcessArchitecture Simple Type

Defines the possible process architecture values.

``` syntax
<xs:simpleType name="ProcessArchitecture">
    <xs:restriction
        base="xs:string"
    >
        <xs:enumeration
            value="Any"
         />
        <xs:enumeration
            value="x86"
         />
        <xs:enumeration
            value="amd64"
         />
        <xs:enumeration
            value="ia64"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **ProcessArchitecture** simple type defines the following values.



| Value | Description                                                 |
|-------|-------------------------------------------------------------|
| Any   | Supports any architecture. <br/>                      |
| x86   | Supports the 32-bit architecture. <br/>               |
| amd64 | Supports the 64-bit architecture. <br/>               |
| ia64  | Supports the 64-bit Itanium-based architecture. <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Script**](package-script-complextype.md)
</dt> </dl>

 

 






---
title: Version Simple Type
description: Defines a string that you use to specify a version value.
ms.assetid: 33ccc068-e21e-44a1-8a17-ae82f37c40b1
keywords:
- Version simple type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Version
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Version Simple Type

Defines a string that you use to specify a version value.

``` syntax
<xs:simpleType name="Version">
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
            value="[0-9]([.][0-9]+)+"
         />
    </xs:restriction>
</xs:simpleType>
```

## Patterns

The **Version** simple type is a xs:string that is restricted by the following pattern:

-   `[0-9]([.][0-9]+)+`

    Typically, version numbers are in the form *major*.*minor* (for example, 1.0). At a minimum, you must specify a *major* value; the *major* value can be only a single digit in the range from 0 through 9. The remainder of the version string can contain zero or more integer values delimited by a period (for example, 1.2.1234.1).

## Remarks

The version string is limited to 256 characters.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DiagnosticIdentification**](package-diagnosticidentification-complextype.md)
</dt> <dt>

[**GlobalDiagnosticPackage**](package-globaldiagnosticpackage-complextype.md)
</dt> <dt>

[**LocalDiagnosticPackage**](package-localdiagnosticpackage-complextype.md)
</dt> <dt>

[**SupportedOSVersion**](package-supportedosversion-complextype.md)
</dt> </dl>

 

 






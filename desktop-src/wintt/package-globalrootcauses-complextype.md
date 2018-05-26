---
title: GlobalRootcauses Complex Type
description: Defines a collection of global root causes.
ms.assetid: 0c19e4ad-a90c-4608-b1fa-1e2ff9701c7f
keywords:
- GlobalRootcauses complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- GlobalRootcauses
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GlobalRootcauses Complex Type

Defines a collection of global root causes.

``` syntax
<xs:complexType name="GlobalRootcauses">
    <xs:sequence>
        <xs:element name="Rootcause"
            type="dcmPS:GlobalRootcause"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element   | Type                                                                 | Description                          |
|-----------|----------------------------------------------------------------------|--------------------------------------|
| Rootcause | [**dcmPS:GlobalRootcause**](package-globalrootcause-complextype.md) | A root causes to detect. <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**LocalRootcauses Complex Type**](package-localrootcauses-complextype.md)
</dt> <dt>

[**Rootcauses (GlobalDiagnosticPackage) Element**](package-rootcauses-globaldiagnosticpackage-element.md)
</dt> </dl>

 

 






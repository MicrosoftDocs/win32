---
title: Rootcauses (GlobalDiagnosticPackage) Element
description: Contains a collection of root causes to detect.
ms.assetid: '5797f3d2-7523-40b0-a350-6a787631421d'
keywords: ["Rootcauses element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Rootcauses
api_type:
- Schema
---

# Rootcauses (GlobalDiagnosticPackage) Element

Contains a collection of root causes to detect.

``` syntax
<xs:element name="Rootcauses">
    <xs:unique name="No_global_rootcause_may_have_the_same_ID">
        <xs:selector
            xpath="Rootcause"
         />
        <xs:field
            xpath="ID"
         />
    </xs:unique>
</xs:element>
```

The **Rootcauses** element is defined by the [**GlobalDiagnosticPackage**](package-globaldiagnosticpackage-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






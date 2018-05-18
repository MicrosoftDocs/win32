---
title: Rootcauses (LocalDiagnosticPackage) Element
description: Contains a collection of root causes to detect.
ms.assetid: 'add775d6-5d72-4f24-8116-f64eda88391e'
keywords: ["Rootcauses element Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Rootcauses
api_type:
- Schema
---

# Rootcauses (LocalDiagnosticPackage) Element

Contains a collection of root causes to detect.

``` syntax
<xs:element name="Rootcauses">
    <xs:unique name="No_local_rootcause_may_have_the_same_ID">
        <xs:selector
            xpath="Rootcause"
         />
        <xs:field
            xpath="ID"
         />
    </xs:unique>
</xs:element>
```

The **Rootcauses** element is defined by the [**LocalDiagnosticPackage**](package-localdiagnosticpackage-complextype.md) complex type.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






---
title: LocalRootcauses Complex Type
description: Defines a collection of local root causes.
ms.assetid: '94c00ae3-e59d-4ae0-80c4-1a1d7c76dd8f'
keywords: ["LocalRootcauses complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- LocalRootcauses
api_type:
- Schema
---

# LocalRootcauses Complex Type

Defines a collection of local root causes.

``` syntax
<xs:complexType name="LocalRootcauses">
    <xs:sequence>
        <xs:element name="Rootcause"
            type="dcmPS:LocalRootcause"
            minOccurs="1"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element   | Type                                                               | Description                         |
|-----------|--------------------------------------------------------------------|-------------------------------------|
| Rootcause | [**dcmPS:LocalRootcause**](package-localrootcause-complextype.md) | A root cause to detect. <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**Rootcauses (LocalDiagnosticPackage) Element**](package-rootcauses-localdiagnosticpackage-element.md)
</dt> </dl>

 

 






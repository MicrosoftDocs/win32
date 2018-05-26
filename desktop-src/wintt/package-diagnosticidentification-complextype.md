---
title: DiagnosticIdentification Complex Type
description: Identifies a troubleshooting pack.
ms.assetid: 9461d631-5eed-42c5-b98f-cd601e0ef2a7
keywords:
- DiagnosticIdentification complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- DiagnosticIdentification
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DiagnosticIdentification Complex Type

Identifies a troubleshooting pack.

``` syntax
<xs:complexType name="DiagnosticIdentification">
    <xs:sequence>
        <xs:element name="ID"
            type="dcmPS:ID"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Version"
            type="dcmPS:Version"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element | Type                                                | Description                                                                      |
|---------|-----------------------------------------------------|----------------------------------------------------------------------------------|
| ID      | [**dcmPS:ID**](package-id-simpletype.md)           | A string that identifies the pack (for example, AeroDiagnostic).<br/>      |
| Version | [**dcmPS:Version**](package-version-simpletype.md) | A string that specifies this version of the pack (for example, 1.0). <br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**DiagnosticIdentification (GlobalDiagnosticPackage) Element**](package-diagnosticidentification-globaldiagnosticpackage-element.md)
</dt> <dt>

[**DiagnosticIdentification (LocalDiagnosticPackage) Element**](package-diagnosticidentification-localdiagnosticpackage-element.md)
</dt> </dl>

 

 






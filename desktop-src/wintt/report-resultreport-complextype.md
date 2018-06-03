---
title: ResultReport Complex Type
description: Defines the contents of the result report for a troubleshooting package that ran.
ms.assetid: 6cbd81fe-e9de-4d08-9d51-ad46643b2022
keywords:
- ResultReport complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- ResultReport
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ResultReport Complex Type

Defines the contents of the result report for a troubleshooting package that ran.

``` syntax
<xs:complexType name="ResultReport">
    <xs:sequence>
        <xs:element name="Header"
            type="dcmRR:Header"
            maxOccurs="1"
            minOccurs="1"
         />
        <xs:element name="Package"
            type="dcmRR:Package"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
    <xs:attribute name="SchemaVersion"
        type="xsd:string"
        use="required"
     />
</xs:complexType>
```

## Child elements



| Element     | Type                                                | Description                                                                                                               |
|-------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Header**  | [**dcmRR:Header**](report-header-complextype.md)   | Defines the section that contains general information about the computer and troubleshooting package that ran.<br/> |
| **Package** | [**dcmRR:Package**](report-package-complextype.md) | Defines the section that contains the results from the troubleshooting package that ran.<br/>                       |



## Attributes



| Name          | Type           | Description                                                                  |
|---------------|----------------|------------------------------------------------------------------------------|
| SchemaVersion | **xsd:string** | The version of the report schema used to write the result report.<br/> |



## Remarks

WTP always produces a results report when a troubleshooting package runs. The report captures the detection, resolution, and verification details of the troubleshooting package and the status of each phase.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






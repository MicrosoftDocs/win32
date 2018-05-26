---
title: DetectionInformation Complex Type
description: Defines a section of the report that contains a collection of custom details that the package author added to the report.
ms.assetid: 75e4448a-d415-45a4-a2eb-0eddef4afa31
keywords:
- DetectionInformation complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- DetectionInformation
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DetectionInformation Complex Type

Defines a section of the report that contains a collection of custom details that the package author added to the report.

``` syntax
<xs:complexType name="DetectionInformation">
    <xs:sequence>
        <xs:element name="DetailedInformation"
            type="dcmRR:DetailedInformation"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                 | Type                                                                          | Description                                                                                       |
|-------------------------|-------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| **DetailedInformation** | [**dcmRR:DetailedInformation**](https://msdn.microsoft.com/library/windows/desktop/ee692417) | Contains the collection of custom details that the package author added to the report.<br/> |



## Remarks

The detection information can be captured for a specific root cause (see the [**RootCause**](report-rootcause-complextype.md) complex type) or for the troubleshooting package in general (see the [**Problem**](report-problem-complextype.md) complex type).

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






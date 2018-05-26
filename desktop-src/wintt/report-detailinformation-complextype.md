---
title: DetailedInformation Complex Type
description: Defines the collection of custom details that the package author added to the report.
ms.assetid: 38530a3b-28af-4987-9f37-98f5b21a0f56
keywords:
- DetailedInformation complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- DetailedInformation
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DetailedInformation Complex Type

Defines the collection of custom details that the package author added to the report.

``` syntax
<xs:complexType name="DetailedInformation">
    <xs:sequence>
        <xs:element name="Detail"
            type="dcmRR:Detail"
            maxOccurs="unbounded"
            minOccurs="0"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element    | Type                                              | Description                                                                                                                                                                              |
|------------|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Detail** | [**dcmRR:Detail**](report-detail-complextype.md) | Defines a custom detail in the report. The package author adds the detail using the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet from one of the package scripts.<br/> |



## Remarks

Where the custom detail is included in the report depends on how and where the package author called the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet. If the author called the Update-DiagReport cmdlet from the resolver script, the detail is included in the resolution section of the root cause. If the call is made from the troubleshooter script and includes the *-RootcauseId* parameter, the detail is added to the **DetectionInformation** section of the specific root cause (see the [**RootCause**](report-rootcause-complextype.md) complex type); otherwise, the detail is added to the general **DetectionInformation** section of the report (see [**Problem**](report-problem-complextype.md) complex type).

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






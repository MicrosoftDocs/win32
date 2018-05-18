---
title: Problem Complex Type
description: Defines the section of the report that contains all the problems that the troubleshooting package is trying to detect and fix.
ms.assetid: '86c2be71-9112-4b48-8dc2-7df070d5383e'
keywords: ["Problem complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Problem
api_type:
- Schema
---

# Problem Complex Type

Defines the section of the report that contains all the problems that the troubleshooting package is trying to detect and fix.

``` syntax
<xs:complexType name="Problem">
    <xs:sequence>
        <xs:element name="DetectionInformation"
            type="dcmRR:DetectionInformation"
            maxOccurs="1"
            minOccurs="1"
         />
        <xs:element name="RootCauseInformation"
            type="dcmRR:RootCauseInformation"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                  | Type                                                                          | Description                                                                                                                |
|--------------------------|-------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| **DetectionInformation** | [**dcmRR:DetectionInformation**](report-detectioninformation-complextype.md) | Defines the section of the report that contains the custom details that the package author added to the report.<br/> |
| **RootCauseInformation** | [**dcmRR:RootCauseInformation**](report-rootcauseinformation-complextype.md) | Defines the section of the report that contains the list of root causes and their results.<br/>                      |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






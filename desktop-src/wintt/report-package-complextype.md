---
title: Package Complex Type
description: Defines the section of the results report that contains the results from running the troubleshooting package.
ms.assetid: 37dfd5f6-9672-44cb-bba8-ec2fd0d2aa49
keywords:
- Package complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Package
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Package Complex Type

Defines the section of the results report that contains the results from running the troubleshooting package.

``` syntax
<xs:complexType name="Package">
    <xs:sequence>
        <xs:element name="Problem"
            type="dcmRR:Problem"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element     | Type                                                | Description                                                                                                                                 |
|-------------|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| **Problem** | [**dcmRR:Problem**](report-problem-complextype.md) | Defines the section of the report that contains all the problems that the troubleshooting package is trying to detect and solve.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






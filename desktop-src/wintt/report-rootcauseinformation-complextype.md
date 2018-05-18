---
title: RootCauseInformation Complex Type
description: Defines the section of the report that contains the list of root causes that the troubleshooting pack can detect.
ms.assetid: '42b14f4f-d9d6-4b58-87b9-68e7cdac2abd'
keywords: ["RootCauseInformation complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- RootCauseInformation
api_type:
- Schema
---

# RootCauseInformation Complex Type

Defines the section of the report that contains the list of root causes that the troubleshooting pack can detect.

``` syntax
<xs:complexType name="RootCauseInformation">
    <xs:sequence>
        <xs:element name="RootCause"
            type="dcmRR:RootCause"
            maxOccurs="unbounded"
            minOccurs="0"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element       | Type                                                    | Description                                                  |
|---------------|---------------------------------------------------------|--------------------------------------------------------------|
| **RootCause** | [**dcmRR:RootCause**](report-rootcause-complextype.md) | Defines a root cause that the package can detect.<br/> |



## Remarks

The list contains all root causes defined in the package plus any instances of a root cause (for information on a root cause instance, see the *-InstanceId* parameter of the [Update-DiagRootCause](update-diagrootcause-cmdlet.md) cmdlet).

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






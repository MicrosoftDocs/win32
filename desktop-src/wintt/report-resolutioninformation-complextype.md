---
title: ResolutionInformation Complex Type
description: Defines the collection of resolvers that can fix the root cause issue.
ms.assetid: 'e498fd33-f319-446d-a1f9-96076e4063ad'
keywords: ["ResolutionInformation complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- ResolutionInformation
api_type:
- Schema
---

# ResolutionInformation Complex Type

Defines the collection of resolvers that can fix the root cause issue.

``` syntax
<xs:complexType name="ResolutionInformation">
    <xs:sequence>
        <xs:element name="Resolution"
            type="dcmRR:Resolution"
            maxOccurs="unbounded"
            minOccurs="0"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element        | Type                                                      | Description                                                                        |
|----------------|-----------------------------------------------------------|------------------------------------------------------------------------------------|
| **Resolution** | [**dcmRR:Resolution**](report-resolution-complextype.md) | Defines information about a resolver that can fix the root cause issue.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






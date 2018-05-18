---
title: Contents Complex Type
description: Defines the contents of the custom detail that the package author added to the report.
ms.assetid: '3bc346a1-cf5c-447b-a0aa-286d185dc924'
keywords: ["Contents complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- Contents
api_type:
- Schema
---

# Contents Complex Type

Defines the contents of the custom detail that the package author added to the report.

``` syntax
<xs:complexType name="Contents">
    <xs:sequence>
        <xs:any
            minOccurs="0"
            maxOccurs="unbounded"
            processContents="lax"
            namespace="##any"
         />
    </xs:sequence>
</xs:complexType>
```

## Remarks

The contents depends on whether the package author used the *-Xml* or *-File* parameter when calling the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet. If the author used the *-Xml* parameter, the value of the **Contents** node is any well-formed XML.

If the author used the *-File* parameter, the **Contents** node contains a **Data** node that specifies the name of the file that contains the custom detail. The **Id** attribute of the **Data** node is "FileName", the **Name** attribute is "File Name", and the value of the **Data** node is the name of the file that contains the custom detail. The location of the file is relative to the location of the report (the report and file reside in the same folder).

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






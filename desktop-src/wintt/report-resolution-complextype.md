---
title: Resolution Complex Type
description: Defines information about a resolver that the package can run to fix the root cause issue.
ms.assetid: d9d9d3d6-9bc6-4452-8476-c42267e203fe
keywords:
- Resolution complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Resolution
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resolution Complex Type

Defines information about a resolver that the package can run to fix the root cause issue.

``` syntax
<xs:complexType name="Resolution">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="2"
            minOccurs="2"
         />
        <xs:element name="DetailedInformation"
            type="dcmRR:DetailedInformation"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
    <xs:attribute name="id"
        type="xsd:string"
        use="required"
     />
    <xs:attribute name="name"
        type="xsd:string"
        use="required"
     />
</xs:complexType>
```

## Child elements



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Data</strong></td>
<td>[<strong>dcmRR:Data</strong>](report-data-complextype.md)</td>
<td>The resolution contains a <strong>Data</strong> element for each of the following properties:<br/>
<ul>
<li>The description of the resolver. The <strong>Id</strong> attribute for this property is Description.</li>
<li>The status that indicates whether the package ran the resolver. Possible values are:
<ul>
<li>Not Run   the package did not run the resolver</li>
<li>Succeeded   the package ran the resolver (indicates that the resolver ran and did not fail but does not indicate that the resolver fixed the issue)</li>
<li>Failed   the package ran the resolver but the resolver failed</li>
<li>Informational   the resolver did not specify a script to fix the issue but instead provided text that was displayed to the user that asked them to perform an action in an attempt to fix the issue.</li>
</ul>
The <strong>Id</strong> attribute for this property is Status.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
<tr class="even">
<td><strong>DetailedInformation</strong></td>
<td>[<strong>dcmRR:DetailedInformation</strong>](https://msdn.microsoft.com/library/windows/desktop/ee692417)</td>
<td>Defines the custom detailed resolution information that the package author adds to the report. The information is added if the resolver script calls the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.<br/></td>
</tr>
</tbody>
</table>



## Attributes



| Name | Type           | Description                                             |
|------|----------------|---------------------------------------------------------|
| id   | **xsd:string** | The identifier that identifies the resolver.<br/> |
| name | **xsd:string** | The name of the resolver.<br/>                    |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






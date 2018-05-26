---
title: RootCause Complex Type
description: Defines a root cause that the package can detect.
ms.assetid: 55040388-068c-4046-96ab-476eb40eaf7b
keywords:
- RootCause complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- RootCause
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RootCause Complex Type

Defines a root cause that the package can detect.

``` syntax
<xs:complexType name="RootCause">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="2"
            minOccurs="2"
         />
        <xs:element name="ResolutionInformation"
            type="dcmRR:ResolutionInformation"
            maxOccurs="1"
            minOccurs="1"
         />
        <xs:element name="DetectionInformation"
            type="dcmRR:DetectionInformation"
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
<td>The root cause contains a <strong>Data</strong> element for each of the following properties:<br/>
<ul>
<li>The description of the root cause. The <strong>Id</strong> attribute for this property is Description.</li>
<li>The status that indicates whether the package tried to detect the root cause. Possible values are:
<ul>
<li>Detected   the root cause was detected but could not determine if the issue was fixed</li>
<li>Not Detected   the root cause was not detected</li>
<li>Not Checked   the troubleshooter script was not called</li>
<li>Fixed   the root cause was detected and fixed.</li>
<li>Not Fixed   the root cause was detected but not fixed.</li>
</ul>
The troubleshooter sets the Detected and Not Detected status values, and the verifier sets the Fixed and Not Fixed status values. The <strong>Id</strong> attribute for this property is Status.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
<tr class="even">
<td><strong>DetectionInformation</strong></td>
<td>[<strong>dcmRR:DetectionInformation</strong>](report-detectioninformation-complextype.md)</td>
<td>Defines the section of the report that contains the custom details that the package author added to the report for this root cause. The custom detail is added to this section only if the script specifies the <em>-RootCauseId</em> parameter when it calls the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.<br/></td>
</tr>
<tr class="odd">
<td><strong>ResolutionInformation</strong></td>
<td>[<strong>dcmRR:ResolutionInformation</strong>](report-resolutioninformation-complextype.md)</td>
<td>Defines the collection of resolvers that can fix the root cause issue.<br/></td>
</tr>
</tbody>
</table>



## Attributes



| Name | Type           | Description                                                       |
|------|----------------|-------------------------------------------------------------------|
| id   | **xsd:string** | An identifier that uniquely identifies the root cause.<br/> |
| name | **xsd:string** | The name of the root cause.<br/>                            |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






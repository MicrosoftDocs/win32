---
title: Detail Complex Type
description: Defines a custom detail that the package author added to the report.
ms.assetid: 171936ec-8b24-4b4f-aee6-78a6e8ffa91a
keywords:
- Detail complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Detail
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Detail Complex Type

Defines a custom detail that the package author added to the report.

``` syntax
<xs:complexType name="Detail">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="1"
            minOccurs="1"
         />
        <xs:element name="Contents"
            type="dcmRR:Contents"
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
    <xs:attribute name="verbosity"
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
<td><strong>Contents</strong></td>
<td>[<strong>dcmRR:Contents</strong>](report-contents-complextype.md)</td>
<td>Contains the custom detail. The content is an XML fragment if the author used the <em>-Xml</em> parameter when calling the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet; otherwise, if the author used the <em>-File</em> parameter, the content is a <strong>Data</strong> element that specifies the location of the file that contains the custom detail.<br/></td>
</tr>
<tr class="even">
<td><strong>Data</strong></td>
<td>[<strong>dcmRR:Data</strong>](report-data-complextype.md)</td>
<td>The Detail section contains a <strong>Data</strong> element for the following property:<br/>
<ul>
<li>The description of the custom detail. The <strong>Id</strong> attribute for this property is Description. The description comes from the <em>-Description</em> parameter of the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
</tbody>
</table>



## Attributes



| Name      | Type           | Description                                                                                                                                                             |
|-----------|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| id        | **xsd:string** | The identifier that identifies this detail. The identifier comes from the *-Id* parameter of the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.<br/>   |
| name      | **xsd:string** | The localized name of this detail. The name comes from the *-Name* parameter of the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.<br/>                |
| verbosity | **xsd:string** | The level of verbosity for this detail. For possible values, see the *-Verbosity* parameter of the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet.<br/> |



## Remarks

The package author adds the detail using the [Update-DiagReport](update-diagreport-cmdlet.md) cmdlet from one of the package scripts.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






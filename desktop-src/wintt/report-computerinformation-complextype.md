---
title: ComputerInformation Complex Type
description: Defines information about the computer on which the troubleshooting package ran.
ms.assetid: 7d1675df-3110-415a-8ada-f017a5ae7360
keywords:
- ComputerInformation complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- ComputerInformation
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ComputerInformation Complex Type

Defines information about the computer on which the troubleshooting package ran.

``` syntax
<xs:complexType name="ComputerInformation">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="3"
            minOccurs="3"
         />
    </xs:sequence>
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
<td>The computer information section contains a <strong>Data</strong> element for each of the following properties:<br/>
<ul>
<li>The version number of the operating system. For example, the version number for Windows 7 is 6.1. The <strong>Id</strong> attribute for this property is Version.</li>
<li>The SKU of the operating system. The possible values are &quot;Server&quot; and &quot;Client&quot;. The <strong>Id</strong> attribute for this property is SKU.</li>
<li>The processor architecture on which the troubleshooting package ran. For example, &quot;x86&quot; or &quot;amd64&quot;. The <strong>Id</strong> attribute for this property is Architecture.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
</tbody>
</table>



## Attributes



| Name | Type       | Description                                                                   |
|------|------------|-------------------------------------------------------------------------------|
| name | xsd:string | The name of the computer on which the troubleshooting package ran.<br/> |



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






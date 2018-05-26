---
title: Header Complex Type
description: Defines the section of the report that contains general information about the computer and troubleshooting package that ran.
ms.assetid: fce0c3b2-35f2-48b9-b30e-692a7d26f6cf
keywords:
- Header complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Header
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Header Complex Type

Defines the section of the report that contains general information about the computer and troubleshooting package that ran.

``` syntax
<xs:complexType name="Header">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="2"
            minOccurs="2"
         />
        <xs:element name="ComputerInformation"
            type="dcmRR:ComputerInformation"
            maxOccurs="1"
            minOccurs="1"
         />
        <xs:element name="PackageInformation"
            type="dcmRR:PackageInformation"
            maxOccurs="unbounded"
            minOccurs="1"
         />
        <xs:element name="MetaPackageInformation"
            type="dcmRR:PackageInformation"
            maxOccurs="1"
            minOccurs="1"
         />
    </xs:sequence>
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
<td><strong>ComputerInformation</strong></td>
<td>[<strong>dcmRR:ComputerInformation</strong>](report-computerinformation-complextype.md)</td>
<td>Contains details about the computer on which the troubleshooting package ran.<br/></td>
</tr>
<tr class="even">
<td><strong>Data</strong></td>
<td>[<strong>dcmRR:Data</strong>](report-data-complextype.md)</td>
<td>The header contains a <strong>Data</strong> element for each of the following properties:<br/>
<ul>
<li>The local date and time that the package ran. The <strong>Id</strong> attribute for this property is Time.</li>
<li>A value (true or false) that indicates whether the user ran the package with elevated rights. The <strong>Id</strong> attribute for this property is RunningAsAdmin.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
<tr class="odd">
<td><strong>MetaPackageInformation</strong></td>
<td>[<strong>dcmRR:PackageInformation</strong>](report-packageinformation-complextype.md)</td>
<td>Contains general information about the package.<br/></td>
</tr>
<tr class="even">
<td><strong>PackageInformation</strong></td>
<td>[<strong>dcmRR:PackageInformation</strong>](report-packageinformation-complextype.md)</td>
<td>Contains information about each troubleshooter in the package. If the package is a global troubleshooting package, the report will contain a single <strong>PackageInformation</strong> node. However, for a local troubleshooting package, the report will contain a <strong>PackageInformation</strong> node for each troubleshooter in the package.<br/></td>
</tr>
</tbody>
</table>



## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






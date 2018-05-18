---
title: PackageInformation Complex Type
description: Defines information about a troubleshooting package or a troubleshooter defined within the package.
ms.assetid: 'bcd222e6-f290-4440-8f20-d866550f4351'
keywords: ["PackageInformation complex type Windows Troubleshooting Toolkit"]
topic_type:
- apiref
api_name:
- PackageInformation
api_type:
- Schema
---

# PackageInformation Complex Type

Defines information about a troubleshooting package or a troubleshooter defined within the package.

``` syntax
<xs:complexType name="PackageInformation">
    <xs:sequence>
        <xs:element name="Data"
            type="dcmRR:Data"
            maxOccurs="3"
            minOccurs="3"
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
<td>The package information section contains a <strong>Data</strong> element for each of the following properties:<br/>
<ul>
<li>The version number of the package schema used to write the package manifest. The <strong>Id</strong> attribute for this property is Version.</li>
<li>The name of the publisher that wrote the troublshooting package. The <strong>Id</strong> attribute for this property is Publisher. The name comes from the signature used to sign the security catalog.</li>
<li>The description of the troubleshooting package. The <strong>Id</strong> attribute for this property is Description.</li>
</ul>
The text body of the <strong>Data</strong> element contains the property's value.<br/></td>
</tr>
</tbody>
</table>



## Attributes



| Name | Type       | Description                                                        |
|------|------------|--------------------------------------------------------------------|
| id   | xsd:string | The unique identifier of the troubleshooter or package.<br/> |
| name | xsd:string | The name of the troubleshooter or package.<br/>              |



## Remarks

The package information is used to describe both the troubleshooting package (see the **MetaPackageInformation** element of the [**Header**](report-header-complextype.md) complex type) and a troubleshooter within the package (see the **PackageInformation** element of the **Header** complex type). The information for the **MetaPackageInformation** element is derived internally while the information for the **PackageInformation** element comes from the troubleshooter defined in the package.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 






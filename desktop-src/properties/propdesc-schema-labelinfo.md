---
description: Specifies how the property's labels are displayed.
ms.assetid: 9317aff9-abdd-46c2-aaff-62861925713b
title: labelInfo
ms.topic: article
ms.date: 05/31/2018
---

# labelInfo

Specifies how the property's labels are displayed. There should be only one [labelInfo]() element for each [propertyDescription](./propdesc-schema-propertydescription.md) element.

If there are multiple elements, the last one is used. If no [labelInfo]() element is provided, then the property's label is not displayed; however, this would typically be a defect.

## Syntax


```
<!-- labelInfo -->
<xs:element name="labelInfo">
    <xs:complexType>
        <xs:attribute name="label" type="xs:string"/>
        <xs:attribute name="sortDescription">
            <xs:simpleType>
                <xs:restriction base="xs:string">
                    <xs:enumeration value="General"/>
                    <xs:enumeration value="AToZ"/>
                    <xs:enumeration value="LowestHighest"/>
                    <xs:enumeration value="OldestNewest"/>
                    <xs:enumeration value="SmallestLargest"/>
                </xs:restriction>
            </xs:simpleType>
        </xs:attribute>
        <xs:attribute name="invitationText" type="xs:string"/>
        <xs:attribute name="hideLabel" type="xs:boolean" default="false"/>
    </xs:complexType>
</xs:element>
```



## Element Information



| Parent Element                                                   | Child Elements |
|------------------------------------------------------------------|----------------|
| [propertyDescription](./propdesc-schema-propertydescription.md) | None           |



 

## Attributes




| Attribute | Description | 
|-----------|-------------|
| label | Public. Optional. The label as it is displayed in the UI (for example, the details column label or preview pane). The syntax allows for a direct display string or an indirect display string reference. Use the indirect display string because it can be localized. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getdisplayname"><strong>IPropertyDescription::GetDisplayName</strong></a> returns the resolved display name. | 
| sortDescription | Optional. Specifies the strings offered as sort options. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-getsortdescription"><strong>IPropertyDescription::GetSortDescription</strong></a> returns this sort description. The following values provide the corresponding UI strings.<ul><li>General: "Sort going up" / "Sort going down"</li><li>AToZ: "A on top" / "Z on top"</li><li>LowestHighest: "Lowest on top" / "Highest on top"</li><li>OldestNewest: "Oldest on top" / "Newest on top"</li><li>SmallestLargest: "Smallest on top" / "Largest on top"</li></ul> | 
| invitationText | Optional. The Help string text that is displayed as an instruction to the user for the control or ToolTip (for instance, "Enter author name."). The syntax allows for a direct display string or an indirect display string reference. Use the indirect display string because it can be localized. <a href="/windows/win32/api/propsys/nf-propsys-ipropertydescription-geteditinvitation"><strong>IPropertyDescription::GetEditInvitation</strong></a> returns the resolved invitation text. | 
| hideLabel | Optional. The default is "false". Indicates whether the label is hidden. | 




 

 

 

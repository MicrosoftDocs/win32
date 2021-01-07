---
description: The Scan Profile Schema defines an XML format that can be used to store the properties of Windows Image Acquisition (WIA) items, such as scanners and cameras.
ms.assetid: e0848db3-652a-45be-a18b-99b82420c586
title: Scan Profile Schema
ms.topic: article
ms.date: 05/31/2018
---

# Scan Profile Schema

The Scan Profile Schema defines an XML format that can be used to store the properties of Windows Image Acquisition (WIA) items, such as scanners and cameras. These persistent files enable applications to provide automatic scanning without requiring users to remember the property settings of the items.

Any [**IWiaItem2**](-wia-iwiaitem2.md) device can have a scan profile. However, **IWiaItem2** items of types WIA\_CATEGORY\_FINISHED\_FILE and WIA\_CATEGORY\_ROOT cannot have profiles.

Scan profiles are created and managed through the [**IScanProfile**](-wia-iscanprofile.md), [**IScanProfileMgr**](-wia-iscanprofilemgr.md), and [**IScanProfileUI**](-wia-iscanprofileui.md) interfaces. Users of your application can modify profiles in limited ways using the [**IScanProfileUI::ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method.

All scan profiles have the following elements: `<ProfileGUID>, <DeviceID>, <ProfileName>, <WiaItem>`, and `<Properties>`. The default profile of a device also has a `<Default>` element.

The `<ProfileGUID>` element and the `<DeviceID>` element cannot be changed after the scan profile is created. The values of the `<ProfileName>` element and the `<WiaItem>` element can be modified. The `<Default>` element can be added or deleted. This can be done programatically using the [**IScanProfile::SetName**](-wia-iscanprofile-setname.md), [**IScanProfile::SetItem**](-wia-iscanprofile-setitem.md), and [**IScanProfileMgr::SetDefault**](-wia-iscanprofilemgr-setdefault.md) methods. These properties can also be changed by users through the [**IScanProfileUI::ScanProfileDialog**](-wia-iscanprofileui-scanprofiledialog.md) method.

The `<Properties>` element contains `<Property>` children. Use these to add any WIA item or device property to the profile. You can also develop your own image acquistion `<Property>` children. This makes the Scan Profile Schema extensible. (For more information about extending the schema, see [Defining Custom Properties](-wia-defining-custom-properties.md), [**IScanProfile::GetProperty**](-wia-iscanprofile-getproperty.md), and [**IScanProfile::SetProperty**](-wia-iscanprofile-setproperty.md).)

Here is the complete Scan Profile Schema. A sample profile follows.


```
<?xml version="1.0"?>
<xs:schema xmlns:xs="https://www.w3.org/2001/XMLSchema"
            targetNamespace="https://www.microsoft.com"
            xmlns="https://www.microsoft.com"
            elementFormDefault="qualified">

<xs:element name="ScanProfile">
            <xs:complexType>
            <xs:sequence>
                        <xs:element name="ProfileGUID" type="xs:string"/>
                        <xs:element name="DeviceID" type="xs:string"/>
<xs:element name="ProfileName" type="xs:string"/>
                        <xs:element name="Default" minOccurs="0">
                                    <xs:complexType>
                                    </xs:complexType>
                        </xs:element>
                        <xs:element name="WiaItem" type="xs:string"/>
                        <xs:element name="Properties" type="Properties"/>
            </xs:sequence>
            </xs:complexType>
</xs:element>
 
<xs:complexType name="Properties">
<xs:sequence>
            <xs:element name="Property" maxOccurs="unbounded" minOccurs="0">
            <xs:complexType>
            <xs:simpleContent>
                        <xs:extension base="xs:string">
                                    <xs:attribute name="id" type="xs:integer" use="required"/>
                                    <xs:attribute name="type" type="xs:integer" use="required"/>
                        </xs:extension>
            </xs:simpleContent>
            </xs:complexType>
            </xs:element>
</xs:sequence>
</xs:complexType>
 
</xs:schema>
```



Click **Show Example** to see a sample profile.


```
<ScanProfile>
    <ProfileGUID>
        {F862E217-32B0-4396-987A-2191224925CD}
    </ProfileGUID>
    <DeviceID>
        {6BDD1FC6-810F-11D0-BEC7-08002BE2092F}\0001
    </DeviceID>
    <ProfileName>
        Last used settings
    </ProfileName>
    <WiaItem>
        {FB607B1F-43F3-488B-855B-FB703EC342A6}
    </WiaItem>
    <Properties>
        <Property id="4103" type="3">
            3
        </Property>
        <Property id="4106" type="72">
            {B96B3CAB-0728-11D3-9D7B-0000F81EF32E}
        </Property>
        <Property id="6147" type="3">
            300
        </Property>
        <Property id="6154" type="3">
            0
        </Property>
        <Property id="6155" type="3">
            0
        </Property>
    </Properties>
</ScanProfile>
```



## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[**IScanProfile::GetProperty**](-wia-iscanprofile-getproperty.md)
</dt> <dt>

[**IScanProfile::SetProperty**](-wia-iscanprofile-setproperty.md)
</dt> <dt>

**Conceptual**
</dt> <dt>

[WIA Property Constants](-wia-wia-property-constants.md)
</dt> <dt>

[Defining Custom Properties](-wia-defining-custom-properties.md)
</dt> </dl>

 

 




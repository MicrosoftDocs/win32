---
description: Contains a wired LAN policy.
ms.assetid: c06bdbc4-4199-4eec-a22f-684745912970
title: LANPolicy Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LANPolicy
api_type: 
- Schema
api_location: 
---

# LANPolicy Element

The LANPolicy element contains a wired LAN policy. This element is the unique root element for a wired network policy profile.

The target namespace for the **LANPolicy** element is `https://www.microsoft.com/networking/LAN/policy/v1`.

``` syntax
<xs:element name="LANPolicy">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="name"
                type="nameType"
             />
            <xs:element name="description"
                type="nameType"
                minOccurs="0"
             />
            <xs:element name="globalFlags">
                <xs:complexType>
                    <xs:sequence>
                        <xs:element name="enableAutoConfig"
                            type="boolean"
                         />
                        <xs:any
                            processContents="lax"
                            minOccurs="0"
                            maxOccurs="unbounded"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:element name="profileList"
                minOccurs="0"
            >
                <xs:complexType>
                    <xs:sequence>
                        <xs:any
                            processContents="lax"
                            maxOccurs="unbounded"
                            namespace="##other"
                         />
                    </xs:sequence>
                </xs:complexType>
            </xs:element>
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

## Child elements



| Element                                                                           | Type                                                     | Description                                                                                                                                                                          |
|-----------------------------------------------------------------------------------|----------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**description**](lan-policyschema-description-lanpolicy-element.md)             | [**nameType**](lan-policyschema-nametype-simpletype.md) | Contains the description of a wired LAN policy. <br/>                                                                                                                          |
| [**enableAutoConfig**](lan-policyschema-enableautoconfig-globalflags-element.md) | boolean                                                  | Specifies whether machines use the built-in automatic configuration service to manage connections to wired networks that require layer 2 authentication (such as 802.1X).<br/> |
| [**globalFlags**](lan-policyschema-globalflags-lanpolicy-element.md)             |                                                          | Contains the global settings for the automatic configuration of wired networks. <br/>                                                                                          |
| [**name**](lan-policyschema-name-lanpolicy-element.md)                           | [**nameType**](lan-policyschema-nametype-simpletype.md) | Contains the name of a wired LAN policy. <br/>                                                                                                                                 |
| [**profileList**](lan-policyschema-profilelist-lanpolicy-element.md)             |                                                          | Contains a list of profiles to be applied at the domain or machine level. <br/>                                                                                                |



## Remarks

To view the list of child elements in a tree-like structure, see [LAN\_policy Schema Elements](lan-policyschema-elements.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 





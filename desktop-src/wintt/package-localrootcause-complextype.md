---
title: LocalRootcause Complex Type
description: Specifies the troubleshooter, resolver, and verifier that act on a single root cause.
ms.assetid: 9a318f8c-7f09-4114-ba70-ffbd51f99fc9
keywords:
- LocalRootcause complex type Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- LocalRootcause
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LocalRootcause Complex Type

Specifies the troubleshooter, resolver, and verifier that act on a single root cause.

``` syntax
<xs:complexType name="LocalRootcause">
    <xs:sequence>
        <xs:element name="ID"
            type="dcmPS:ID"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="DisplayInformation"
            type="dcmPS:DisplayInformation"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Troubleshooter"
            type="dcmPS:Troubleshooter"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="Resolvers"
            type="dcmPS:Resolvers"
            minOccurs="1"
            maxOccurs="1"
        >
            <xs:unique name="No_local_resolver_may_have_the_same_ID">
                <xs:selector
                    xpath="Resolver"
                 />
                <xs:field
                    xpath="ID"
                 />
            </xs:unique>
        </xs:element>
        <xs:element name="Verifier"
            type="dcmPS:Verifier"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ContextParameters"
            type="dcmPS:Parameters"
            minOccurs="1"
            maxOccurs="1"
         />
        <xs:element name="ExtensionPoint"
            type="dcmPS:ExtensionPoint"
            minOccurs="1"
            maxOccurs="1"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element            | Type                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ContextParameters  | [**dcmPS:Parameters**](package-parameters-complextype.md)                 | Context parameters are used for extension points that contain substitution strings (for example, %param%). Each substitution string is replaced with the value of the same named parameter specified in the **ContextParameters** element. <br/> You can also specify the Keywords parameter that MSDT will use in the event that the root cause is detected but not fixed. The value is a localized resource (for example, "@resource.dll,-123") that contains one or more keywords; each keyword is separated by a plus (+) sign (for example, keyword1+keyword2).<br/> If the user clicks **Explore additional options**, the keywords are used to find related information if the user then clicks **Help and Support**, **Windows Communities**, or **Related Troubleshooters**.<br/> For **Help and Support**, the keywords are used in a logical OR operation and for **Windows Communities** and **Related Troubleshooters**, the keywords are used in a logical AND operation.<br/> You can specify keywords here or as an extension point of the package (see the **ExtensionPoint** child element of the [**LocalDiagnosticPackage**](package-localdiagnosticpackage-complextype.md) complex type).<br/> |
| DisplayInformation | [**dcmPS:DisplayInformation**](package-displayinformation-complextype.md) | The name and description of the root cause to use in the UI. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ExtensionPoint     | [**dcmPS:ExtensionPoint**](package-extensionpoint-complextype.md)         | Used by the client to extend the functionality of the Rootcause node. The MSDT client does not support extensions for the Rootcause node. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ID                 | [**dcmPS:ID**](package-id-simpletype.md)                                  | A string identifier that identifies the local root cause.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Resolvers          | [**dcmPS:Resolvers**](package-resolvers-complextype.md)                   | The resolver script to run.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Troubleshooter     | [**dcmPS:Troubleshooter**](package-troubleshooter-complextype.md)         | The troubleshooter script to run.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Verifier           | [**dcmPS:Verifier**](package-verifier-complextype.md)                     | The verifier script to run. <br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |



## Remarks

You must specify the troubleshooter and resolver scripts; however, the verifier script is optional.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**LocalRootcauses Complex Type**](package-localrootcauses-complextype.md)
</dt> <dt>

[**Rootcause (LocalRootcauses) Element**](package-rootcause-localrootcauses-element.md)
</dt> </dl>

 

 






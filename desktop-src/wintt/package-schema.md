---
title: Package Schema
ms.assetid: 5e475d28-bc38-4855-8149-a0aecf1b2955
description: 
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Package Schema

The Package schema defines the following elements and types that you use to write a troubleshooting manifest:

-   [Package Elements](package-elements.md)
-   [Package Simple Types](package-simple-types.md)
-   [Package Complex Types](package-complex-types.md)

A troubleshooter manifest contains the following components:

-   Troubleshooter—determines whether a root cause (issue) exists on the computer.
-   Resolver—fixes the issue.
-   Verifier—verifies that the issue was resolved.

To create your manifest, consider using the Windows Troubleshooting Pack Designer tool. In addition to helping you author your manifest, the tool also creates a catalog for the troubleshooting pack, signs the pack, and creates a cabinet file that you can use to distribute the pack. The Windows SDK includes the tool in the \\Bin\\TSPDesigner folder.

If you use Visual Studio as your XML editor, add the package and resource schema to the project (see the XML menu). The XML editor provides Intellisense, inline schema validation, and other features to make writing the manifest easy and accurate.

## The package schema

The following is the package schema that you can use to validate your manifest. Copy this schema and the [Resource](resource-schema.md) schema to the same folder.


```XML
<?xml version="1.0" encoding="utf-8"?>

<xs:schema xmlns:dcmPS="http://www.microsoft.com/schemas/dcm/package/2007" 
           xmlns:xs="http://www.w3.org/2001/XMLSchema" 
           xmlns:dcmRS="http://www.microsoft.com/schemas/dcm/resource/2007" 
           targetNamespace="http://www.microsoft.com/schemas/dcm/package/2007" 
           elementFormDefault="unqualified">

  <xs:import namespace="http://www.microsoft.com/schemas/dcm/resource/2007" schemaLocation="resource_schema.xsd"/>

  <xs:simpleType name="Version">
    <xs:restriction base="xs:string">
      <xs:maxLength value="256"/>
      <xs:minLength value="1"/>
      <xs:pattern value="[0-9]([.][0-9]+)+"/>
    </xs:restriction>
  </xs:simpleType>
 
  <xs:simpleType name="Name">
    <xs:restriction base="xs:string">
      <xs:maxLength value="256"/>
      <xs:minLength value="1"/>
      <xs:pattern value="[^ :/\r\n\t\\]+"/>
    </xs:restriction>
  </xs:simpleType>
 
  <xs:simpleType name="ID">
    <xs:restriction base="dcmPS:Name">
      <xs:pattern value="[^\']+"/>
    </xs:restriction>
  </xs:simpleType>
 
  <xs:complexType name="DiagnosticIdentification">
    <xs:sequence>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Version" type="dcmPS:Version" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="ExtensionPoint">
    <xs:sequence>
      <xs:any minOccurs="0" maxOccurs="unbounded" namespace="##any" processContents="lax"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Parameter">
    <xs:sequence>
      <xs:element name="Name" type="dcmPS:Name" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DefaultValue" type="xs:string" minOccurs="1" maxOccurs="1"/>      
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Parameters">
    <xs:sequence>
      <xs:element name="Parameter" type="dcmPS:Parameter" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="DisplayInformation">
    <xs:sequence>
      <xs:element name="Parameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_display_parameters_may_have_the_same_name">
          <xs:selector xpath="Parameter"/>
          <xs:field xpath="Name"/>
        </xs:unique>
      </xs:element>
      <xs:element name="Name" type="dcmRS:MandatoryResource" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Description" type="dcmRS:OptionalResource" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="SupportedOSVersion">
    <xs:simpleContent>
      <xs:extension base="dcmPS:Version">
        <xs:attribute name="clientSupported" type="xs:boolean" use="required"/>
        <xs:attribute name="serverSupported" type="xs:boolean" use="required"/>
      </xs:extension>
    </xs:simpleContent>
  </xs:complexType>
 
  <xs:simpleType name="ProcessArchitecture">
    <xs:restriction base="xs:string">
      <xs:enumeration value="Any"/>
      <xs:enumeration value="x86"/>
      <xs:enumeration value="amd64"/>
      <xs:enumeration value="ia64"/>
    </xs:restriction>
  </xs:simpleType>
 
  <xs:complexType name="Script">
    <xs:sequence>
      <xs:element name="Parameters" type="dcmPS:Parameters" minOccurs="0" maxOccurs="1">
        <xs:unique name="No_script_parameters_may_have_the_same_name">
          <xs:selector xpath="Parameter"/>
          <xs:field xpath="Name"/>
        </xs:unique>
      </xs:element>
      <xs:element name="ProcessArchitecture" type="dcmPS:ProcessArchitecture" minOccurs="0" maxOccurs="1"/>
      <xs:element name="RequiresElevation" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
      <xs:element name="RequiresInteractivity" type="xs:boolean" minOccurs="0" maxOccurs="1"/>
      <xs:element name="FileName" type="dcmPS:Name" minOccurs="0" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Resolvers">
    <xs:sequence>
      <xs:element name="Resolver" minOccurs="0" maxOccurs="unbounded">
        <xs:complexType>
          <xs:sequence>
            <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
            <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
            <xs:element name="RequiresConsent" type="xs:boolean" minOccurs="1" maxOccurs="1"/>            
            <xs:element name="Script" type="dcmPS:Script" minOccurs="1" maxOccurs="1"/>
            <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
          </xs:sequence>
        </xs:complexType>
      </xs:element>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Troubleshooter">
    <xs:sequence>
      <xs:element name="Script" type="dcmPS:Script" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Verifier">
    <xs:sequence>
      <xs:element name="Script" type="dcmPS:Script" minOccurs="0" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="0" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="LocalRootcause">
    <xs:sequence>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Troubleshooter" type="dcmPS:Troubleshooter" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Resolvers" type="dcmPS:Resolvers" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_local_resolver_may_have_the_same_ID">
          <xs:selector xpath="Resolver"/>
          <xs:field xpath="ID"/>
        </xs:unique>
      </xs:element>
      <xs:element name="Verifier" type="dcmPS:Verifier" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="GlobalRootcause">
    <xs:sequence>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Resolvers" type="dcmPS:Resolvers" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_global_resolver_may_have_the_same_ID">
          <xs:selector xpath="Resolver"/>
          <xs:field xpath="ID"/>
        </xs:unique>
      </xs:element>
      <xs:element name="Verifier" type="dcmPS:Verifier" minOccurs="1" maxOccurs="1"/>        
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="GlobalRootcauses">
    <xs:sequence>
      <xs:element name="Rootcause" type="dcmPS:GlobalRootcause" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="LocalRootcauses">
    <xs:sequence>
      <xs:element name="Rootcause" type="dcmPS:LocalRootcause" minOccurs="1" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Choice">
    <xs:sequence>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Value" type="xs:string" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>      
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="Choices">
    <xs:sequence>
      <xs:element name="Choice" type="dcmPS:Choice" minOccurs="0" maxOccurs="unbounded"/>
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="LaunchUIInteraction">
    <xs:sequence>
      <xs:element name="Parameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_cmdline_parameters_may_have_the_same_name">
          <xs:selector xpath="Parameter"/>
          <xs:field xpath="Name"/>
        </xs:unique>
      </xs:element>    
      <xs:element name="CommandLine" type="xs:string" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>  
 
  <xs:complexType name="PauseInteraction">
    <xs:sequence>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>  
 
  <xs:complexType name="TextInteraction">
    <xs:sequence>
      <xs:element name="RegularExpression" type="xs:string" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>  
 
  <xs:complexType name="MultipleResponseInteraction">
    <xs:sequence>
      <xs:element name="AllowDynamicResponses" type="xs:boolean" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Choices" type="dcmPS:Choices" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>
  
  <xs:complexType name="SingleResponseInteraction">
    <xs:sequence>
      <xs:element name="AllowDynamicResponses" type="xs:boolean" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Choices" type="dcmPS:Choices" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ID" type="dcmPS:ID" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="ContextParameters" type="dcmPS:Parameters" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>  
 
  <xs:complexType name="LaunchUIInteractions">
    <xs:sequence>
      <xs:element name="LaunchUIInteraction" type="dcmPS:LaunchUIInteraction" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="PauseInteractions">
    <xs:sequence>
      <xs:element name="PauseInteraction" type="dcmPS:PauseInteraction" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="TextInteractions">
    <xs:sequence>
      <xs:element name="TextInteraction" type="dcmPS:TextInteraction" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="MultipleResponseInteractions">
    <xs:sequence>
      <xs:element name="MultipleResponseInteraction" type="dcmPS:MultipleResponseInteraction" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>
  </xs:complexType>
 
  <xs:complexType name="SingleResponseInteractions">
    <xs:sequence>
      <xs:element name="SingleResponseInteraction" type="dcmPS:SingleResponseInteraction" minOccurs="0" maxOccurs="unbounded"/>  
    </xs:sequence>
  </xs:complexType>  
  
  <xs:complexType name="Interactions">
    <xs:sequence>
      <xs:element name="SingleResponseInteractions" type="dcmPS:SingleResponseInteractions" minOccurs="1" maxOccurs="1"/>
      <xs:element name="MultipleResponseInteractions" type="dcmPS:MultipleResponseInteractions" minOccurs="1" maxOccurs="1"/>
      <xs:element name="TextInteractions" type="dcmPS:TextInteractions" minOccurs="1" maxOccurs="1"/>
      <xs:element name="PauseInteractions" type="dcmPS:PauseInteractions" minOccurs="1" maxOccurs="1"/>
      <xs:element name="LaunchUIInteractions" type="dcmPS:LaunchUIInteractions" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
  </xs:complexType>  
 
  <xs:complexType name="GlobalDiagnosticPackage">
    <xs:sequence>
      <xs:element name="DiagnosticIdentification" type="dcmPS:DiagnosticIdentification" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="PrivacyLink" type="xs:string" minOccurs="1" maxOccurs="1"/>
      <xs:element name="PowerShellVersion" type="dcmPS:Version" minOccurs="1" maxOccurs="1"/>
      <xs:element name="SupportedOSVersion" type="dcmPS:SupportedOSVersion" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Troubleshooter" type="dcmPS:Troubleshooter" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Rootcauses" type="dcmPS:GlobalRootcauses" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_global_rootcause_may_have_the_same_ID">
          <xs:selector xpath="Rootcause"/>
          <xs:field xpath="ID"/>
        </xs:unique>
      </xs:element>
      <xs:element name="Interactions" type="dcmPS:Interactions" minOccurs="1" maxOccurs="1"/> 
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="SchemaVersion" type="dcmPS:Version" use="required"/>
    <xs:attribute name="Localized" type="xs:boolean" use="required"/>
  </xs:complexType>
 
  <xs:complexType name="LocalDiagnosticPackage">
    <xs:sequence>
      <xs:element name="DiagnosticIdentification" type="dcmPS:DiagnosticIdentification" minOccurs="1" maxOccurs="1"/>
      <xs:element name="DisplayInformation" type="dcmPS:DisplayInformation" minOccurs="1" maxOccurs="1"/>
      <xs:element name="PrivacyLink" type="xs:string" minOccurs="1" maxOccurs="1"/>      
      <xs:element name="PowerShellVersion" type="dcmPS:Version" minOccurs="1" maxOccurs="1"/>        
      <xs:element name="SupportedOSVersion" type="dcmPS:SupportedOSVersion" minOccurs="1" maxOccurs="1"/>
      <xs:element name="Rootcauses" type="dcmPS:LocalRootcauses" minOccurs="1" maxOccurs="1">
        <xs:unique name="No_local_rootcause_may_have_the_same_ID">
          <xs:selector xpath="Rootcause"/>
          <xs:field xpath="ID"/>
        </xs:unique>
      </xs:element>
      <xs:element name="Interactions" type="dcmPS:Interactions" minOccurs="1" maxOccurs="1"/> 
      <xs:element name="ExtensionPoint" type="dcmPS:ExtensionPoint" minOccurs="1" maxOccurs="1"/>
    </xs:sequence>
    <xs:attribute name="SchemaVersion" type="dcmPS:Version" use="required"/>
    <xs:attribute name="Localized" type="xs:boolean" use="required"/>
  </xs:complexType>
 
  <xs:element name="DiagnosticPackage" type="dcmPS:GlobalDiagnosticPackage"/>
  <xs:element name="AdvDiagnosticPackage" type="dcmPS:LocalDiagnosticPackage"/>
 
</xs:schema>
```



 

 





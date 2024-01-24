---
description: The following is the complete listing of the manifest file schema.
ms.assetid: 5a4040a4-66ed-44ea-a07f-6410f88d1446
title: Manifest File Schema
ms.topic: article
ms.date: 05/31/2018
---

# Manifest File Schema

The following is the complete listing of the manifest file schema.

```xml syntax
<?xml version="1.0" ?> 
  <Schema xmlns="urn:schemas-microsoft-com:xml-data" xmlns:dt="urn:schemas-microsoft-com:datatypes" 
   name="urn:schemas-microsoft-com:asm.v1" xmlns:asmv3="urn:schemas-microsoft-com:asm.v3" >
  <!--  Attributes 
  --> 
  <AttributeType name="manifestVersion" dt:type="enumeration" dt:values="1.0" /> 
  <AttributeType name="name" dt:type="string" /> 
  <AttributeType name="type" dt:type="string" /> 
  <AttributeType name="publicKeyToken" dt:type="bin.hex" /> 
  <AttributeType name="language" dt:type="string" /> 
  <AttributeType name="processorArchitecture" dt:type="string" /> 
  <AttributeType name="version" dt:type="string" /> 
  <AttributeType name="optional" dt:type="enumeration" dt:values="yes no" /> 
  <AttributeType name="clsid" dt:type="string" /> 
  <AttributeType name="description" dt:type="string" /> 
  <AttributeType name="threadingModel" dt:type="string" /> 
  <AttributeType name="tlbid" dt:type="string" /> 
  <AttributeType name="progid" dt:type="string" /> 
  <AttributeType name="helpdir" dt:type="string" /> 
  <AttributeType name="iid" dt:type="string" /> 
  <AttributeType name="numMethods" dt:type="ui4" /> 
  <AttributeType name="resourceid" dt:type="string" /> 
  <AttributeType name="flags" dt:type="enumeration" dt:values="control hidden restricted hasdiskimage" /> 
  <AttributeType name="hashalg" dt:type="enumeration" dt:values="SHA1 SHA MD5 MD4 MD2" /> 
  <AttributeType name="hash" dt:type="bin.hex" /> 
  <AttributeType name="proxyStubClsid32" dt:type="string" /> 
  <AttributeType name="baseInterface" dt:type="string" /> 
  <AttributeType name="versioned" dt:type="enumeration" dt:values="yes no" /> 
  <AttributeType name="oldVersion" dt:type="string" /> 
  <AttributeType name="newVersion" dt:type="string" /> 
  <AttributeType name="size" dt:type="ui8" /> 
  <AttributeType name="runtimeVersion" dt:type="string" /> 
  <!--  Elements
  --> 
  <ElementType name="assembly" order="seq" model="closed" content="eltOnly">
  <attribute type="manifestVersion" required="yes" /> 
  <group order="many" minOccurs="0" maxOccurs="*">
  <element type="assemblyIdentity" minOccurs="1" maxOccurs="1" /> 
  <element type="noInheritable" minOccurs="0" maxOccurs="1" /> 
  </group>
  <group order="many" minOccurs="0" maxOccurs="*">
  <element type="description" minOccurs="0" maxOccurs="1" /> 
  <element type="noInherit" minOccurs="0" maxOccurs="1" /> 
  <element type="noInheritable" minOccurs="0" maxOccurs="1" /> 
  <element type="comInterfaceExternalProxyStub" minOccurs="0" /> 
  <element type="dependency" minOccurs="0" /> 
  <element type="file" minOccurs="0" /> 
  <element type="clrClass" minOccurs="0" /> 
  <element type="clrSurrogate" minOccurs="0" /> 
  </group>
  </ElementType>
  <ElementType name="supportedOS" order="seq" model="closed" content="eltOnly">
  <attribute type="Id" required="yes" /> 
  </ElementType>
  <ElementType name="clrClass" model="closed" content="eltOnly">
  <attribute type="name" required="yes" /> 
  <attribute type="clsid" required="yes" /> 
  <attribute type="progid" required="no" /> 
  <attribute type="tlbid" required="no" /> 
  <attribute type="description" required="no" /> 
  <attribute type="runtimeVersion" required="no" /> 
  <attribute type="threadingModel" required="no" /> 
  <element type="progid" minOccurs="0" maxOccurs="*" /> 
  </ElementType>
  <ElementType name="clrSurrogate" model="closed" content="empty">
  <attribute type="clsid" required="yes" /> 
  <attribute type="name" required="yes" /> 
  <attribute type="runtimeVersion" required="no" /> 
  </ElementType>
  <ElementType name="assemblyIdentity" model="closed">
  <attribute type="name" required="yes" /> 
  <attribute type="version" required="no" /> 
  <attribute type="type" required="no" /> 
  <attribute type="processorArchitecture" required="no" /> 
  <attribute type="publicKeyToken" required="no" /> 
  <attribute type="language" required="no" /> 
  </ElementType>
  <ElementType name="comInterfaceProxyStub" model="closed">
  <attribute type="iid" required="yes" /> 
  <attribute type="name" required="yes" /> 
  <attribute type="tlbid" required="no" /> 
  <attribute type="numMethods" required="no" /> 
  <attribute type="proxyStubClsid32" required="no" /> 
  <attribute type="baseInterface" required="no" /> 
  </ElementType>
  <ElementType name="description" /> 
  <ElementType name="dependency" model="closed" content="eltOnly">
  <element type="dependentAssembly" minOccurs="0" maxOccurs="1" /> 
  <attribute type="optional" required="no" /> 
  </ElementType>
  <ElementType name="dependentAssembly" model="closed" content="eltOnly">
  <element type="assemblyIdentity" minOccurs="1" maxOccurs="1" /> 
  <element type="bindingRedirect" minOccurs="0" maxOccurs="*" /> 
  </ElementType>
  <ElementType name="bindingRedirect" model="closed" content="empty">
  <attribute type="oldVersion" required="yes" /> 
  <attribute type="newVersion" required="yes" /> 
  </ElementType>
  <ElementType name="file" model="closed" content="eltOnly">
  <attribute type="name" required="yes" /> 
  <attribute type="hash" required="no" /> 
  <attribute type="hashalg" required="no" /> 
  <attribute type="size" required="no" /> 
  <group order="many" minOccurs="0" maxOccurs="*">
  <element type="comClass" minOccurs="0" /> 
  <element type="comInterfaceProxyStub" minOccurs="0" /> 
  <element type="typelib" minOccurs="0" /> 
  <element type="windowClass" minOccurs="0" /> 
  </group>
  </ElementType>
  <ElementType name="comClass" model="closed" content="eltOnly">
  <attribute type="clsid" required="yes" /> 
  <attribute type="threadingModel" required="no" /> 
  <attribute type="progid" required="no" /> 
  <attribute type="tlbid" required="no" /> 
  <attribute type="description" required="no" /> 
  <element type="progid" minOccurs="0" maxOccurs="*" /> 
  </ElementType>
  <ElementType name="comInterfaceExternalProxyStub" model="closed" content="empty">
  <attribute type="iid" required="yes" /> 
  <attribute type="name" required="yes" /> 
  <attribute type="tlbid" required="no" /> 
  <attribute type="numMethods" required="no" /> 
  <attribute type="proxyStubClsid32" required="no" /> 
  <attribute type="baseInterface" required="no" /> 
  </ElementType>
  <ElementType name="typelib" model="closed" content="empty">
  <attribute type="tlbid" required="yes" /> 
  <attribute type="version" required="yes" /> 
  <attribute type="helpdir" required="yes" /> 
  <attribute type="resourceid" required="no" /> 
  <attribute type="flags" required="no" /> 
  </ElementType>
  <ElementType name="windowClass" model="closed" content="textOnly">
  <attribute type="versioned" required="no" /> 
  </ElementType>
  <ElementType name="noInherit" model="closed" content="empty" /> 
  <ElementType name="noInheritable" model="closed" content="empty" /> 
  <ElementType name="progid" /> 

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2005/WindowsSettings
  --> 
  <ElementType name="dpiAware" /> 
  <ElementType name="autoElevate" /> 
  <ElementType name="disableTheming" /> 

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2011/WindowsSettings
  --> 
  <ElementType name="disableWindowFiltering" /> 
  <ElementType name="printerDriverIsolation" /> 
    
  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2013/WindowsSettings
  --> 
  <ElementType name="highResolutionScrollingAware" /> 
  <ElementType name="ultraHighResolutionScrollingAware" /> 

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2016/WindowsSettings
  -->
  <ElementType name="dpiAwareness" />
  <ElementType name="longPathAware" />

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2017/WindowsSettings
  -->
  <ElementType name="gdiScaling" />

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2019/WindowsSettings
  -->
  <ElementType name="activeCodePage" />

  <!-- WindowsSettings elements from XML namespace http://schemas.microsoft.com/SMI/2020/WindowsSettings
  -->
  <ElementType name="heapType" />

  </Schema>
```

 

 




---
title: Resource Schema
ms.assetid: f58d68c2-bed0-4057-87ca-e038496028c9
description: 
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Schema

The Resource schema defines the simple types used by the [Package schema](package-schema.md):

-   [Resource Simple Types](resource-simple-types.md)

The following is the resource schema that you can use to validate your manifest. Copy this schema and the [Package](package-schema.md) schema to the same folder.


```XML
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:dcmRS="http://www.microsoft.com/schemas/dcm/resource/2007" xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://www.microsoft.com/schemas/dcm/resource/2007" elementFormDefault="unqualified">

  <xs:simpleType name="MandatoryResource">
    <xs:restriction base="xs:string">
      <xs:maxLength value="1024"/>
      <xs:minLength value="1"/>
    </xs:restriction>
  </xs:simpleType>

  <xs:simpleType name="OptionalResource">
    <xs:restriction base="xs:string">
      <xs:maxLength value="1024"/>
      <xs:minLength value="0"/>
    </xs:restriction>
  </xs:simpleType>

</xs:schema>
```



 

 





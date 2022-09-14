---
title: Web Service Extension File
description: This section outlines Web Service extension file.
ms.assetid: 856d4ff5-2292-4d87-ae7c-19b100fd1cb3
keywords:
- Web Service Extension File Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# Web Service Extension File

This section outlines Web Service extension file.


WSX file (WCF service extension) is our extension file to allow application to manipulate local behaviors that do not affect wire data representation. It should be extensible that we can add new features in the future without breaking interoperability.

The overall structure of WSX would mimic the structure of XSD or WSDL file, which is a XML file that maintains the same structure as the main input file. Extra attributes on the same named token in main file would specify the attributes that application wants to control over the default behavior.

We might not do anything here in M3. In V1, I can see we support the following attributes:

Usage Specifying count argument/parameter field.

This is an element attribute but applicable to array type only. IsCountOf attribute specifies the array element. The count field/parameter does not appear on wire.

``` syntax
<xs:schema xmlns:tns="http://Example.org" elementFormDefault="qualified" 
targetNamespace="http://Example.org" xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <element name="FooInParam">
  <complexType> 
   <!-- MyArray field is presented in WSDL file as an element -->
    <element name="MyArrayCount" IsCountOf="MyArray"></element>
   </complexType>
  </element>
 </xs:schema>
```

Specifying read/write callback for custom type

These attributes force wsutil.exe to generate [**WS\_CUSTOM\_TYPE**](/windows/desktop/api/WebServices/ne-webservices-ws_type) for specified type. custom\_readcallback attribute specifies the [**read callback**](/windows/desktop/api/WebServices/nc-webservices-ws_read_type_callback) routine, and custom\_writecallback specifies the [**write callback**](/windows/desktop/api/WebServices/nc-webservices-ws_write_type_callback) routine.

``` syntax
<xs:schema xmlns:tns="http://Example.org" elementFormDefault="qualified" 
targetNamespace="http://Example.org" xmlns:xs="http://www.w3.org/2001/XMLSchema">
 <element name="mytype" custom_readcallback="myreadcallback" custom_writecallback="mywritecallback"> 
 </element>
</xs:schema>
```

We can have a matching WSX file to describe its local behavior:

``` syntax
<xs:schema xmlns:tns="http://Example.org" elementFormDefault="qualified" 
targetNamespace="http://Example.org" xmlns:xs="http://www.w3.org/2001/XMLSchema">

 <element name="FooInParam" DataValidationRoutine="MyArrayValidation">
  <complexType> 
   <element name="MyLocalArrayCount" IsCountOf="MyArray"></element> 
  </complexType>
 </element>
</xs:schema>
```

WsUtil.exe generates the following prototype for the structure:

``` syntax
typedef struct FooInParam
{
  ULONG MyLocalArrayCount;
  int * MyArray;
};
```

 

 





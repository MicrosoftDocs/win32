---
title: DerivedTypeExample
description: This example writes and reads derived types using Wsutil generated C++ helper functions. See WS\_TYPE\_ATTRIBUTE\_FIELD\_MAPPING for more about derived type descriptions.
ms.assetid: 279663c0-8797-4f87-aaec-8cb8d4046a05
keywords:
- DerivedTypeExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# DerivedTypeExample

This example writes and reads derived types using Wsutil generated C++ helper functions. See [**WS\_TYPE\_ATTRIBUTE\_FIELD\_MAPPING**](/windows/desktop/api/WebServices/ne-webservices-ws_field_mapping) for more about derived type descriptions.

-   [DerivedType.cpp](#derivedtypecpp)
-   [DerivedType.xsd](#derivedtypexsd)
-   [Related topics](#related-topics)

## DerivedType.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include "WebServices.h"
#include "process.h"
#include "stdio.h"
#include "string.h"
#include "DerivedType.xsd.h"

// Print out rich error info
void PrintError(HRESULT errorCode, WS_ERROR* error)
{
    wprintf(L"Failure: errorCode=0x%lx\n", errorCode);

    if (errorCode == E_INVALIDARG || errorCode == WS_E_INVALID_OPERATION)
    {
        // Correct use of the APIs should never generate these errors
        wprintf(L"The error was due to an invalid use of an API.  This is likely due to a bug in the program.\n");
        DebugBreak();
    }

    HRESULT hr = NOERROR;
    if (error != NULL)
    {
        ULONG errorCount;
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &string);
            if (FAILED(hr))
            {
                goto Exit;
            }
            wprintf(L"%.*s\n", string.length, string.chars);
        }
    }
Exit:
    if (FAILED(hr))
    {
        wprintf(L"Could not get error string (errorCode=0x%lx)\n", hr);
    }
}

void PrintPayloadType(PayloadBaseType* payloadType)
{
    if (payloadType == NULL)
    {
        return;
    }

    Payload1Type* payload1Type = payloadType->AsPayload1Type();
    if (payload1Type == NULL)
    {
        // This is a base type
        printf("base type\n");
        printf("Id %d\n", payloadType->Id);
        
    }
    else
    {
        // this is derived type
        printf("derived type\n");
        printf("Id %d\n", payloadType->Id);
        printf("BoolValue %d\n", payload1Type->BoolValue);
        wprintf(
            L"StringValue %.*s\n", 
            payload1Type->StringValue.length,
            payload1Type->StringValue.chars);
    }
}


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_XML_BUFFER* xmlBuffer = NULL;
    WS_HEAP* heap = NULL;
    WS_XML_READER* xmlReader = NULL;
    WS_XML_WRITER* xmlWriter = NULL;
    PayloadBaseType* baseType = NULL;
    Payload1Type* payload1Type = NULL;
    
    WS_XML_STRING dataElement = WS_XML_STRING_VALUE("data");
    WS_XML_STRING emptyNamespace = WS_XML_STRING_VALUE("");
    WS_STRING stringValue = WS_STRING_VALUE(L"hello world");
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create a heap to store deserialized data
    hr = WsCreateHeap(
        /*maxSize*/ 4096, 
        /*trimSize*/ 512, 
        NULL, 
        0, 
        &heap, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(
        NULL,
        0, 
        &xmlReader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create an XML writer
    hr = WsCreateWriter(
        NULL, 
        0, 
        &xmlWriter, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Create an XML buffer on the specified heap
    hr = WsCreateXmlBuffer(
        heap, 
        NULL, 
        0, 
        &xmlBuffer, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set the writer to output to the XML buffer
    hr = WsSetOutputToBuffer(
        xmlWriter, 
        xmlBuffer, 
        NULL, 
        0, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create a wrapper element for the two embedded elements
    hr = WsWriteStartElement(
        xmlWriter,
        NULL,
        &dataElement,
        &emptyNamespace,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    baseType = new PayloadBaseType();
    if (baseType == NULL)
    {
        goto Exit;
    }
    baseType->Id = 1;
    
    payload1Type = new Payload1Type();
    if (payload1Type == NULL)
    {
        goto Exit;
    }
    payload1Type->Id = 2;
    payload1Type->BoolValue = FALSE;
    payload1Type->StringValue = stringValue;
    // Write the base type using the element description of the base type.
    // An xsi:type attribute will be added to the XML document for the element
    // indicating this is the base type.
    hr = WsWriteElement(
        xmlWriter,
        &DerivedType_xsd.globalElements.PayloadBase, 
        WS_WRITE_REQUIRED_VALUE,
        baseType, 
        sizeof(PayloadBaseType), 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Write the derived type using the element description of the base type.
    // An xsi:type attribute will be added to the XML document for the element
    // indicating this is the derived type.
    hr = WsWriteElement(
        xmlWriter,
        &DerivedType_xsd.globalElements.PayloadBase, 
        WS_WRITE_REQUIRED_VALUE,
        payload1Type, 
        sizeof(Payload1Type), 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsWriteEndElement(
        xmlWriter,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Flush writer so all XML content is put in the buffer
    hr = WsFlushWriter(xmlWriter, 0, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set the reader input to current position of XML buffer
    hr = WsSetInputToBuffer(xmlReader, xmlBuffer, NULL, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Read pass the wrapper element
    hr = WsReadToStartElement(
        xmlReader,
        &dataElement,
        &emptyNamespace,
        NULL,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        
    
    hr = WsReadStartElement(
        xmlReader,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    PayloadBaseType* outBaseType = NULL;
    
    // Read the first element using element description for the base
    // type. The type of returning structure is that of that base type.
    hr = WsReadElement(
        xmlReader,
        &DerivedType_xsd.globalElements.PayloadBase, 
        WS_READ_REQUIRED_POINTER,
        heap,
        &outBaseType,
        sizeof(PayloadBaseType*),
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    PrintPayloadType(outBaseType);
    
    // Read the second element using element description for the base
    // type. The type of returning structure is that of the derived type.
    hr = WsReadElement(
        xmlReader,
        &DerivedType_xsd.globalElements.PayloadBase, 
        WS_READ_REQUIRED_POINTER,
        heap,
        &outBaseType,
        sizeof(PayloadBaseType*),
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    PrintPayloadType(outBaseType);
    
    hr = WsReadEndElement(
        xmlReader,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    
    delete baseType;
    delete payload1Type;
    
    if (xmlReader != NULL)
    {
        WsFreeReader(xmlReader);
    }
    if (xmlWriter != NULL)
    {
        WsFreeWriter(xmlWriter);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    if (heap != NULL)
    {
        WsFreeHeap(heap);
    }
    
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}
```



## DerivedType.xsd

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema targetNamespace="https://example.org/derivedTypes"
           xmlns:tns="https://example.org/derivedTypes"
    elementFormDefault="qualified"
    xmlns:xs="https://www.w3.org/2001/XMLSchema">
  <xs:complexType name="PayloadBaseType">
    <xs:sequence>
      <xs:element minOccurs="0" name="Id" type="xs:int" />
    </xs:sequence>
  </xs:complexType>
  <xs:element name="PayloadBase" type="tns:PayloadBaseType" />

  <xs:complexType name="Payload1Type">
    <xs:complexContent >
      <xs:extension base="tns:PayloadBaseType">
        <xs:sequence>
          <xs:element minOccurs="0" name="BoolValue" type="xs:boolean" />
          <xs:element minOccurs="0" name="StringValue"  type="xs:string" />
        </xs:sequence>
      </xs:extension>
    </xs:complexContent>
  </xs:complexType>
  <xs:element name="Payload1" type="tns:Payload1Type" />
</xs:schema>
```

## Related topics

<dl> <dt>

[**WS\_TYPE\_ATTRIBUTE\_FIELD\_MAPPING**](/windows/desktop/api/WebServices/ne-webservices-ws_field_mapping)
</dt> </dl>

 

 





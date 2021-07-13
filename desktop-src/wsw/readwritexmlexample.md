---
title: ReadWriteXmlExample
description: Review an XML read/write example that uses Windows Web Services API (WWSAPI). This example writes XML to an XML buffer, and then reads it back out.
ms.assetid: e9802e3c-c8a0-4b68-bba5-cdafb7250298
keywords:
- ReadWriteXmlExample Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# ReadWriteXmlExample

This example writes XML to an XML buffer, and then reads it back out.

-   [ReadWriteXml.cpp](#readwritexmlcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## ReadWriteXml.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include "WebServices.h"
#include "process.h"
#include "string.h"
#include "PurchaseOrder.wsdl.h"

struct PurchaseOrderDictionary
{
    WS_XML_DICTIONARY dictionary;
    WS_XML_STRING quantity;
    WS_XML_STRING productName;
    WS_XML_STRING purchaseOrderType;
    WS_XML_STRING purchaseOrderNamespace;
};

static PurchaseOrderDictionary purchaseOrderDictionary =
{
    { 
        { 0x89d3da8b, 0xec46, 0x4fe8, { 0x9a, 0xb4, 0x48, 0x62, 0xb2, 0x69, 0x71, 0x8a } },
        &purchaseOrderDictionary.quantity,
        4, 
        TRUE 
    },
    WS_XML_STRING_DICTIONARY_VALUE("quantity", &purchaseOrderDictionary.dictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("productName", &purchaseOrderDictionary.dictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("PurchaseOrderType", &purchaseOrderDictionary.dictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("http://example.com", &purchaseOrderDictionary.dictionary, 3),
};


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

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_HEAP* heap = NULL;
    WS_XML_BUFFER* xmlBuffer = NULL;
    WS_XML_WRITER* xmlWriter = NULL;
    WS_XML_READER* xmlReader = NULL;
    WS_STRING productName = WS_STRING_VALUE(L"Pencil");
    
    // Command line parameter specifies whether to use typed or untyped api
    BOOL typed;
    if (argc == 2)
    {
        wchar_t* arg = argv[1];
        if (wcscmp(arg, L"typed") == 0)
        {
            typed = TRUE;
        }
        else if (wcscmp(arg, L"untyped") == 0)
        {
            typed = FALSE;
        }
        else
        {
            wprintf(L"Invalid command line argument '%s'\n", arg);
            return 1;
        }
    }
    else
    {
        wprintf(L"usage : WsReadWriteXml.exe [typed|untyped]\n");
        return 1;
    }
    
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
        /*maxSize*/ 2048, 
        /*trimSize*/ 512, 
        NULL, 
        0, 
        &heap, 
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
    
    // Write xml into the buffer
    if (typed)
    {
        // Initialize body data
        _PurchaseOrderType purchaseOrder;
        purchaseOrder.quantity = 1;
        purchaseOrder.productName = productName;
    
        // Write purchase order
        hr = WsWriteElement(
            xmlWriter, 
            &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
            WS_WRITE_REQUIRED_VALUE,
            &purchaseOrder, 
            sizeof(purchaseOrder), 
            error);
    
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    else
    {
        // Write purchase order start element
        hr = WsWriteStartElement(xmlWriter, NULL, &purchaseOrderDictionary.purchaseOrderType, &purchaseOrderDictionary.purchaseOrderNamespace, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write quantity element
        int quantity = 1;
        hr = WsWriteStartElement(xmlWriter, NULL, &purchaseOrderDictionary.quantity, &purchaseOrderDictionary.purchaseOrderNamespace, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteValue(xmlWriter, WS_INT32_VALUE_TYPE, &quantity, sizeof(quantity), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteEndElement(xmlWriter, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write product name start element
        hr = WsWriteStartElement(xmlWriter, NULL, &purchaseOrderDictionary.productName, &purchaseOrderDictionary.purchaseOrderNamespace, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write product name
        hr = WsWriteChars(xmlWriter, productName.chars, productName.length, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write product name end element
        hr = WsWriteEndElement(xmlWriter, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write purchase order end element
        hr = WsWriteEndElement(xmlWriter, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    
    // Flush writer so all XML content is put in the buffer
    hr = WsFlushWriter(xmlWriter, 0, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(NULL, 0, &xmlReader, error);
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
    
    if (typed)
    {
        // Read purchase order into heap
        _PurchaseOrderType* purchaseOrder;
        hr = WsReadElement(xmlReader, &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
            WS_READ_REQUIRED_POINTER, heap, &purchaseOrder, sizeof(purchaseOrder), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Print out purchase order contents
        wprintf(L"%ld, %.*s\n", 
            purchaseOrder->quantity, 
            purchaseOrder->productName.length,
            purchaseOrder->productName.chars);
    
        // Done with purchase order
        WsResetHeap(heap, NULL);
    }
    else
    {
        // Read to purchase order element
        hr = WsReadToStartElement(xmlReader, &purchaseOrderDictionary.purchaseOrderType, &purchaseOrderDictionary.purchaseOrderNamespace, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read purchase order element
        hr = WsReadStartElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read to quantity element
        hr = WsReadToStartElement(xmlReader, &purchaseOrderDictionary.quantity, &purchaseOrderDictionary.purchaseOrderNamespace, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read quantity element as integer
        long quantity;
        hr = WsReadStartElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsReadValue(xmlReader, WS_INT32_VALUE_TYPE, &quantity, sizeof(quantity), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsReadEndElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read to product name element
        hr = WsReadToStartElement(xmlReader, &purchaseOrderDictionary.productName, &purchaseOrderDictionary.purchaseOrderNamespace, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read product name start element
        hr = WsReadStartElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read product name into buffer
        WCHAR productName[100];
        ULONG length = 0;
        ULONG available = WsCountOf(productName) - 1; // leave space for terminating '\0'
        for (;;)
        {
            // Read next block of chars
            ULONG charsRead;
            hr = WsReadChars(xmlReader, &productName[length], available, &charsRead, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
    
            if (charsRead == 0)
            {
                // No more chars
                break;
            }
    
            length += charsRead;
            available -= charsRead;
    
            if (available == 0)
            {
                hr = WS_E_INVALID_FORMAT;
                goto Exit;
            }
        }
    
        // Zero terminate product name string
        productName[length] = L'\0';
    
        // Print out purchase order contents
        wprintf(L"%ld, %s\n", 
            quantity, 
            productName);
    
        // Read product name end element
        hr = WsReadEndElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read purchase order end element
        hr = WsReadEndElement(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    
    if (heap != NULL)
    {
        WsFreeHeap(heap);
    }
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
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}

```



## PurchaseOrder.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="http://example.org" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" 
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
    targetNamespace="http://example.org">
    <wsdl:types>
        <xsd:schema targetNamespace="http://example.org" elementFormDefault="qualified">
            <xsd:element name="PurchaseOrderType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="quantity" type="xsd:int"/>
                        <xsd:element minOccurs="0" name="productName" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="OrderConfirmationType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                        <xsd:element minOccurs="0" name="expectedShipDate" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="GetOrderStatusType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="GetOrderStatusResponseType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                        <xsd:element minOccurs="0" name="status" type="xsd:string"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="OrderNotFoundFaultType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="orderID" type="xsd:unsignedInt"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>
    <wsdl:message name="PurchaseOrder">
        <wsdl:part name="parameters" element="tns:PurchaseOrderType"/>
    </wsdl:message>
    <wsdl:message name="OrderConfirmation">
        <wsdl:part name="parameters" element="tns:OrderConfirmationType"/>
    </wsdl:message>
    <wsdl:message name="GetOrderStatus">
        <wsdl:part name="parameters" element="tns:GetOrderStatusType"/>
    </wsdl:message>
    <wsdl:message name="GetOrderStatusResponse">
        <wsdl:part name="parameters" element="tns:GetOrderStatusResponseType"/>
    </wsdl:message>
    <wsdl:message name="OrderNotFoundFault">
        <wsdl:part name="parameters" element="tns:OrderNotFoundFaultType"/>
    </wsdl:message>
    <wsdl:portType name="IPurchaseOrder">
        <wsdl:operation name="Order">
            <wsdl:input message="tns:PurchaseOrder" wsaw:Action="http://example.org/purchaseorder"/>
            <wsdl:output message="tns:OrderConfirmation" wsaw:Action="http://example.org/orderconfirmation"/>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <wsdl:input message="tns:GetOrderStatus" wsaw:Action="http://example.org/getorderstatus"/>
            <wsdl:output message="tns:GetOrderStatusResponse" wsaw:Action="http://example.org/getorderstatusresponse"/>
            <wsdl:fault name="OrderNotFound" message="tns:OrderNotFoundFault" wsaw:Action="http://example.org/ordernotfound"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="PurchaseOrderBinding" type="tns:IPurchaseOrder">
        <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Order">
            <soap:operation soapAction="http://example.org/purchaseorder" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <soap:operation soapAction="http://example.org/getorderstatus" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
            <wsdl:fault name="OrderNotFound">
                <soap:body use="literal"/>
            </wsdl:fault>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="PurchaseOrderService">
        <wsdl:port name="IPurchaseOrder" binding="tns:PurchaseOrderBinding">
            <soap:address location="http://example.org/IPurchaseOrder"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

## Makefile

``` syntax
#------------------------------------------------------------
# Copyright (C) Microsoft.  All rights reserved.
#------------------------------------------------------------

!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsReadWriteXml.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\ReadWriteXml.obj: ReadWriteXml.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" ReadWriteXml.cpp

$(OUTDIR)\WsReadWriteXml.exe: $(OUTDIR)\ReadWriteXml.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsReadWriteXml.exe $(OUTDIR)\ReadWriteXml.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsReadWriteXml.PDB

clean:
    $(CLEANUP)
```

 

 





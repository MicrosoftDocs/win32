---
title: MessageEncodingExample
description: This example encodes and decodes a message.
ms.assetid: b1f0a1df-22be-4c86-9a7a-0a4d4f363206
keywords:
- MessageEncodingExample Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# MessageEncodingExample

This example encodes and decodes a message.

-   [MessageEncoding.cpp](#messageencodingcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## MessageEncoding.cpp


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

#define MaxMessageSize 2048

struct MyCallbackState
{
    BYTE messageBuffer[MaxMessageSize];
    ULONG messageSize;
};

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_XML_WRITER* xmlWriter = NULL;
    WS_XML_READER* xmlReader = NULL;
    WS_MESSAGE* message = NULL;
    WS_HEAP* heap = NULL;
    
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
    
    // Create a message
    hr = WsCreateMessage(
        WS_ENVELOPE_VERSION_SOAP_1_2, 
        WS_ADDRESSING_VERSION_1_0, 
        NULL, 
        0, 
        &message, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Encode some messages
    for (int i = 0; i < 100; i++)
    {
        // Initialize the message
        hr = WsInitializeMessage(message, WS_BLANK_MESSAGE, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Set the writer to buffer the output
        WS_XML_WRITER_BUFFER_OUTPUT writerOutput;
        ZeroMemory(&writerOutput, sizeof(writerOutput));
        writerOutput.output.outputType = WS_XML_WRITER_OUTPUT_TYPE_BUFFER;
    
        WS_XML_WRITER_TEXT_ENCODING writerEncoding;
        ZeroMemory(&writerEncoding, sizeof(writerEncoding));
        writerEncoding.encoding.encodingType = WS_XML_WRITER_ENCODING_TYPE_TEXT;
        writerEncoding.charSet = WS_CHARSET_UTF8;
        hr = WsSetOutput(xmlWriter, &writerEncoding.encoding, &writerOutput.output, NULL, 0, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write the message start (headers)
        hr = WsWriteEnvelopeStart(message, xmlWriter, NULL, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Initialize purchase order
        _PurchaseOrderType purchaseOrderToWrite;
        purchaseOrderToWrite.quantity = 100;
        purchaseOrderToWrite.productName.chars = L"Pencil";
        purchaseOrderToWrite.productName.length = 6;
    
        // Write purchase order as the body of the message
        hr = WsWriteBody(
            message, 
            &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
            WS_WRITE_REQUIRED_VALUE,
            &purchaseOrderToWrite, 
            sizeof(purchaseOrderToWrite), 
            error);
    
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Write the end of the message
        hr = WsWriteEnvelopeEnd(message, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Flush the xml writer to make sure all data has been written to callback
        hr = WsFlushWriter(xmlWriter, 0, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Reset message so we can reuse it
        hr = WsResetMessage(message, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        WS_BYTES buffer;
        hr = WsGetWriterProperty(xmlWriter, WS_XML_WRITER_PROPERTY_BYTES, &buffer, sizeof(buffer), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Set the reader input to be the encoded message
        WS_XML_READER_BUFFER_INPUT bufferInput;
        ZeroMemory(&bufferInput, sizeof(bufferInput));
        bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
        bufferInput.encodedData = buffer.bytes;
        bufferInput.encodedDataSize = buffer.length;
    
        WS_XML_READER_TEXT_ENCODING readerEncoding;
        readerEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
        readerEncoding.charSet = WS_CHARSET_UTF8;
        hr = WsSetInput(xmlReader, &readerEncoding.encoding, &bufferInput.input, NULL, 0, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read the message start (headers)
        hr = WsReadEnvelopeStart(message, xmlReader, NULL, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Read the body of the message as a purchase order
        _PurchaseOrderType* purchaseOrder;
        hr = WsReadBody(message, &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
            WS_READ_REQUIRED_POINTER, heap, &purchaseOrder, sizeof(purchaseOrder), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Print out purchase order
        wprintf(L"%ld, %.*s\n", 
            purchaseOrder->quantity, 
            purchaseOrder->productName.length,
            purchaseOrder->productName.chars);
    
        // Read the end of the message
        hr = WsReadEnvelopeEnd(message, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Reset message so we can reuse it
        hr = WsResetMessage(message, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Reset heap
        hr = WsResetHeap(heap, error);
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
    
    if (message != NULL)
    {
        WsFreeMessage(message);
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
    if (heap != NULL)
    {
        WsFreeHeap(heap);
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
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsMessageEncoding.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\MessageEncoding.obj: MessageEncoding.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" MessageEncoding.cpp

$(OUTDIR)\WsMessageEncoding.exe: $(OUTDIR)\MessageEncoding.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsMessageEncoding.exe $(OUTDIR)\MessageEncoding.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsMessageEncoding.PDB

clean:
    $(CLEANUP)
```

 

 





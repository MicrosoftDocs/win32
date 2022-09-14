---
title: StreamingHttpClientExample
description: This example shows an HTTP client that does request-reply using the streaming APIs.
ms.assetid: dd391506-6f14-4d3a-bd65-96a338b3f7cd
keywords:
- StreamingHttpClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# StreamingHttpClientExample

This example shows an HTTP client that does request-reply using the streaming APIs.

-   [StreamingHttpClient.cpp](#streaminghttpclientcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## StreamingHttpClient.cpp


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


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_CHANNEL* channel = NULL;
    WS_MESSAGE* requestMessage = NULL;
    WS_MESSAGE* replyMessage = NULL;
    WS_HEAP* heap = NULL;
    WS_STRING productName = WS_STRING_VALUE(L"Pencil");
    WS_STRING serviceUrl = WS_STRING_VALUE(L"http://localhost/example");
    WS_ENDPOINT_ADDRESS address = {};
    HANDLE serverStartedEvent = NULL;
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Set up a property indicating streamined input and output
    WS_TRANSFER_MODE transferMode = WS_STREAMED_TRANSFER_MODE;
    WS_CHANNEL_PROPERTY transferModeProperty;
    transferModeProperty.id = WS_CHANNEL_PROPERTY_TRANSFER_MODE;
    transferModeProperty.value = &transferMode;
    transferModeProperty.valueSize = sizeof(transferMode);
    
    // Create a HTTP request channel
    hr = WsCreateChannel(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, 
        &transferModeProperty, 
        1, 
        NULL, 
        &channel, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an event to synchronize the client and server processes.
    serverStartedEvent = CreateEventW(
        NULL, 
        TRUE, 
        FALSE, 
        L"WebServicesExampleServerStartedEvent");
    if (NULL == serverStartedEvent)
    {
        wprintf(
            L"Failed to create the client-server synchronization event (errorCode=0x%lx).\n",
            GetLastError());
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    // Wait for the server to startup.
    DWORD win32Error;
    win32Error = WaitForSingleObject(serverStartedEvent, 10000);
    if (WAIT_OBJECT_0 != win32Error)
    {
        if (WAIT_FAILED == win32Error)
        {
            win32Error = GetLastError();
        }
        wprintf(
            L"Failed to wait for the client-server synchronization event (errorCode=0x%lx).\n", 
            win32Error);
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    
    // Initialize address of service
    address.url = serviceUrl;
    
    // Open channel to address
    hr = WsOpenChannel(
        channel, 
        &address, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &requestMessage, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &replyMessage, 
        error);
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
    
    // Send request messages and receive reply messages
    for (int i = 0; i < 10; i++)
    {
        // Initialize message headers of the request message
        hr = WsInitializeMessage(
            requestMessage, 
            WS_BLANK_MESSAGE, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Add the action header to the request message
        hr = WsSetHeader(
            requestMessage, 
            WS_ACTION_HEADER, 
            WS_XML_STRING_TYPE,
            WS_WRITE_REQUIRED_VALUE,
            PurchaseOrder_wsdl.messages.PurchaseOrder.action, 
            sizeof(*PurchaseOrder_wsdl.messages.PurchaseOrder.action), 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        
        // Generate a unique message ID that will be used for the request message
        WS_UNIQUE_ID messageID;
        ZeroMemory(
            &messageID, 
            sizeof(messageID));
        
        DWORD status = UuidCreate(
            &messageID.guid);
        if (status != RPC_S_OK)
        {
            hr = E_FAIL;
            goto Exit;
        }
    
        // Add the message ID to the request message
        hr = WsSetHeader(
            requestMessage, 
            WS_MESSAGE_ID_HEADER, 
            WS_UNIQUE_ID_TYPE,
            WS_WRITE_REQUIRED_VALUE,
            &messageID, 
            sizeof(messageID), 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Send the message headers of the request message
        hr = WsWriteMessageStart(
            channel, 
            requestMessage, 
            NULL, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Stream out some purchase orders
        for (int j = 0; j < 10; j++)
        {
            // Initialize body data
            _PurchaseOrderType purchaseOrder;
            purchaseOrder.quantity = 1;
            purchaseOrder.productName = productName;
    
            // Serialize body data into message
            hr = WsWriteBody(
                requestMessage, 
                &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
                WS_WRITE_REQUIRED_VALUE,
                &purchaseOrder, 
                sizeof(purchaseOrder),
                error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
            // Send accumulated message data once at least 4096 bytes have been accumulated
            hr = WsFlushBody(
                requestMessage, 
                4096, 
                NULL, 
                error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        }
    
        // Send the end of the request message
        hr = WsWriteMessageEnd(
            channel, 
            requestMessage, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Receive the headers of the reply message
        hr = WsReadMessageStart(
            channel, 
            replyMessage, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Stream in all the confirmations
        for (;;)
        {
            // Make sure we have at least once confirmation buffered.  Each confirmation
            // may be up to 1024 bytes in size.
            hr = WsFillBody(
                    replyMessage, 
                    1024, 
                    NULL, 
                    error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
            // Try to deserialize a confirmation into the heap
            _OrderConfirmationType* orderConfirmation;
            hr = WsReadBody(
                    replyMessage, 
                    &PurchaseOrder_wsdl.globalElements.OrderConfirmationType,
                    WS_READ_OPTIONAL_POINTER, 
                    heap, 
                    &orderConfirmation, 
                    sizeof(orderConfirmation), 
                    error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
            // If there are no more confirmations, break out of the loop
            if (orderConfirmation == NULL)
            {
                break;
            }
    
            // Print out confirmation contents
            wprintf(L"%.*s\n",
                orderConfirmation->expectedShipDate.length,
                orderConfirmation->expectedShipDate.chars);
    
            // Reset the heap which frees the confirmation data that was deserialized
            hr = WsResetHeap(
                heap, 
                error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        }
    
        // Receive the end of the reply message
        hr = WsReadMessageEnd(
                channel, 
                replyMessage, 
                NULL, 
                error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Reset message so it can be used again
        hr = WsResetMessage(
            replyMessage, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
        // Reset message so it can be used again
        hr = WsResetMessage(
            requestMessage, 
            error);
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
    
    if (channel != NULL)
    {
        // Close the channel
        WsCloseChannel(channel, NULL, error);
    }
    if (requestMessage != NULL)
    {
        WsFreeMessage(requestMessage);
    }
    if (replyMessage != NULL)
    {
        WsFreeMessage(replyMessage);
    }
    if (channel != NULL)
    {
        WsFreeChannel(channel);
    }
    
    if (NULL != serverStartedEvent)
    {
        CloseHandle(serverStartedEvent);
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
#------------------------------------------------------------
# Copyright (C) Microsoft.  All rights reserved.
#------------------------------------------------------------

!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsStreamingHttpClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\StreamingHttpClient.obj: StreamingHttpClient.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" StreamingHttpClient.cpp

$(OUTDIR)\WsStreamingHttpClient.exe: $(OUTDIR)\StreamingHttpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsStreamingHttpClient.exe $(OUTDIR)\StreamingHttpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsStreamingHttpClient.PDB

clean:
    $(CLEANUP)
```

 

 





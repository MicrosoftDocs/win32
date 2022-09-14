---
title: StreamingHttpServerExample
description: This example shows an HTTP server that accepts a channel, and does request-reply processing in a streaming fashion.
ms.assetid: c108a5b3-923c-439c-8d86-7003a76ff45d
keywords:
- StreamingHttpServerExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# StreamingHttpServerExample

This example shows an HTTP server that accepts a channel, and does request-reply processing in a streaming fashion.

-   [StreamingHttpServer.cpp](#streaminghttpservercpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## StreamingHttpServer.cpp


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
    WS_LISTENER* listener = NULL;
    WS_HEAP* heap = NULL;
    WS_MESSAGE* requestMessage = NULL;
    WS_MESSAGE* replyMessage = NULL;
    static const WS_STRING shipDate = WS_STRING_VALUE(L"1/1/2006");
    WS_STRING uri = WS_STRING_VALUE(L"http://+:80/example");
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
    
    // Create a listener
    hr = WsCreateListener(
        WS_CHANNEL_TYPE_REPLY, 
        WS_HTTP_CHANNEL_BINDING, 
        NULL, 0, 
        NULL, 
        &listener, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Open listener 
    hr = WsOpenListener(
        listener, 
        &uri, 
        NULL, 
        error);
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
    
    // Create a channel suitable for accepting from the listener
    hr = WsCreateChannelForListener(
        listener, 
        &transferModeProperty, 
        1, 
        &channel, 
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
    // Server is started, set the event to signal the clients.
    if (!SetEvent(
            serverStartedEvent))
    {
        wprintf(
            L"Failed to set the client-server synchronization event (errorCode=0x%lx).\n", 
            GetLastError());
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    
    // Receive messages and send replies
    for (int i = 0; i < 10; i++)
    {
        // Accept a channel from the client
        hr = WsAcceptChannel(listener, channel, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
            // Receive the message start (headers)
            hr = WsReadMessageStart(
                channel, 
                requestMessage, 
                NULL, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
            // Get action value
            WS_XML_STRING receivedAction;    
            hr = WsGetHeader(
                requestMessage, 
                WS_ACTION_HEADER, 
                WS_XML_STRING_TYPE,
                WS_READ_REQUIRED_VALUE, NULL, 
                &receivedAction, 
                sizeof(receivedAction), 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
            // Make sure action is what we expect
            hr = WsXmlStringEquals(
                    &receivedAction, 
                    PurchaseOrder_wsdl.messages.PurchaseOrder.action, 
                    error);
        
            if (hr != S_OK)
            {
                hr = WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
                goto Exit;
            }
        
            // Initialize the reply message based on the request
            hr = WsInitializeMessage(
                replyMessage, 
                WS_REPLY_MESSAGE, 
                requestMessage, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
            // Write the start of the reply message (headers)
            hr = WsWriteMessageStart(
                channel, 
                replyMessage, 
                NULL, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
            // Read the contents of the request body, and send response body
            for (;;)
            {
                // Make sure we have at least one purchase order buffered in the request message.  
                // Each purchase order may be up to 1024 bytes in size.
                hr = WsFillBody(
                    requestMessage, 
                    1024, 
                    NULL, 
                    error);
        if (FAILED(hr))
        {
            goto Exit;
        }
                // Deserialize purchase order into heap (if any more)
                _PurchaseOrderType* purchaseOrder;
                hr = WsReadBody(
                    requestMessage, 
                    &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
                    WS_READ_OPTIONAL_POINTER, 
                    heap, 
                    &purchaseOrder, 
                    sizeof(purchaseOrder), 
                    error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
                // NULL indicates no more purchase orders
                if (purchaseOrder == NULL)
                {
                    break;
                }
        
                // Print out purchase order contents
                wprintf(L"%ld, %.*s\n", 
                    purchaseOrder->quantity, 
                    purchaseOrder->productName.length,
                    purchaseOrder->productName.chars);
        
                // Serialize a confirmation into the reply message
                _OrderConfirmationType orderConfirmation;
                orderConfirmation.expectedShipDate = shipDate;
                orderConfirmation.orderID = 123;
        
                hr = WsWriteBody(
                    replyMessage, 
                    &PurchaseOrder_wsdl.globalElements.OrderConfirmationType, 
                    WS_WRITE_REQUIRED_VALUE,
                    &orderConfirmation, 
                    sizeof(orderConfirmation),
                    error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
                // Flush the confirmation data if at least 4096 bytes have been accumulated
                hr = WsFlushBody(
                    replyMessage, 
                    4096, 
                    NULL, 
                    error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
                // Free purchase order
                hr = WsResetHeap(
                    heap, 
                    error);
        if (FAILED(hr))
        {
            goto Exit;
        }
            }
        
            // Read the end of the message
            hr = WsReadMessageEnd(
                channel, 
                requestMessage, 
                NULL, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
            // Write the end of the message
            hr = WsWriteMessageEnd(
                channel, 
                replyMessage, 
                NULL, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
            
            // Reset the message so it can be used again
            hr = WsResetMessage(
                requestMessage, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
            
            // Reset the message so it can be used again
            hr = WsResetMessage(
                replyMessage, 
                error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        if (channel != NULL)
        {
            // Close the channel
            WsCloseChannel(channel, NULL, error);
        }
        
            // Reset the channel so it can be used again
            hr = WsResetChannel(
                channel, 
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
    if (listener != NULL)
    {
        // Close the listener if it was opened
        WsCloseListener(listener, NULL, error);
    }
    if (channel != NULL)
    {
        WsFreeChannel(channel);
    }
    if (listener != NULL)
    {
        WsFreeListener(listener);
    }
    if (requestMessage != NULL)
    {
        WsFreeMessage(requestMessage);
    }
    if (replyMessage != NULL)
    {
        WsFreeMessage(replyMessage);
    }
    
    if (NULL != serverStartedEvent)
    {
        CloseHandle(serverStartedEvent);
    }
    
    if (heap != NULL)
    {
        WsFreeHeap(heap);
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

all: $(OUTDIR) $(OUTDIR)\WsStreamingHttpServer.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\StreamingHttpServer.obj: StreamingHttpServer.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" StreamingHttpServer.cpp

$(OUTDIR)\WsStreamingHttpServer.exe: $(OUTDIR)\StreamingHttpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsStreamingHttpServer.exe $(OUTDIR)\StreamingHttpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsStreamingHttpServer.PDB

clean:
    $(CLEANUP)
```

 

 





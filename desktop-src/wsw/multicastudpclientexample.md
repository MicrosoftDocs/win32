---
title: MulticastUdpClientExample
description: This example shows a UDP client that multicasts a request and then waits for reply messages from servers.
ms.assetid: 61ca7e05-1a60-43b2-9ff7-cb355fae2f77
keywords:
- MulticastUdpClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# MulticastUdpClientExample

This example shows a UDP client that multicasts a request and then waits for reply messages from servers.

-   [MulticastUdpClient.cpp](#multicastudpclientcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## MulticastUdpClient.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef _WINSOCKAPI_
#define _WINSOCKAPI_   /* Prevent inclusion of winsock.h in windows.h */
#endif
#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include "WebServices.h"
#include "process.h"
#include "string.h"
#include "winsock2.h"
#include "Iphlpapi.h"
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

struct THREAD_INFO
{
    WS_CHANNEL* channel;
};

// This thread is used to receive reply messages
DWORD WINAPI ReceiverThread(void* parameter)
{
    HRESULT hr = NOERROR;
    THREAD_INFO* threadInfo = (THREAD_INFO*)parameter;
    WS_CHANNEL* channel = threadInfo->channel;
    WS_MESSAGE* message = NULL;
    WS_ERROR* error = NULL;
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
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &message, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Go into a receive loop.  The loop terminates when the
    // main thread aborts the channel (causing subsequent receives
    // to fail).
    for (;;)
    {
        // Receive start of reply message (headers)
        hr = WsReadMessageStart(channel, message, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Get action value
        WS_XML_STRING receivedAction;
        hr = WsGetHeader(
            message, 
            WS_ACTION_HEADER, 
            WS_XML_STRING_TYPE,
            WS_READ_REQUIRED_VALUE, 
            NULL, 
            &receivedAction, 
            sizeof(receivedAction), 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Make sure action is what we expect
        if (WsXmlStringEquals(&receivedAction, PurchaseOrder_wsdl.messages.OrderConfirmation.action, error) != S_OK)
        {
            hr = WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
            goto Exit;
        }
    
        // Read the order confirmation from the body
        _OrderConfirmationType* orderConfirmation;
        hr = WsReadBody(message, &PurchaseOrder_wsdl.globalElements.OrderConfirmationType, 
            WS_READ_REQUIRED_POINTER, heap, &orderConfirmation, sizeof(orderConfirmation), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Receive end of message
        hr = WsReadMessageEnd(channel, message, NULL, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        // Print out confirmation contents
        wprintf(L"%.*s\n",
            orderConfirmation->expectedShipDate.length,
            orderConfirmation->expectedShipDate.chars);
    
        // Reset message so it can used again
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
    // Print out the error.  Ignore aborted errors, which are
    // caused by the client thread aborting the channel.
    if (FAILED(hr) && hr != WS_E_OPERATION_ABORTED)
    {
        PrintError(hr, error);
    }
    if (message != NULL)
    {
        WsFreeMessage(message);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    if (heap != NULL)
    {
        WsFreeHeap(heap);
    }
    return hr;
}

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_CHANNEL* channel = NULL;
    WS_MESSAGE* message = NULL;
    IP_ADAPTER_ADDRESSES* adapterAddresses = NULL;
    HANDLE receiverThreadHandle = NULL;
    WS_STRING serviceUrl = WS_STRING_VALUE(L"soap.udp://239.255.255.250:809");
    WS_STRING productName = WS_STRING_VALUE(L"Pencil");
    WS_STRING toUrl = WS_STRING_VALUE(L"http://localhost/request");
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
    
    ULONG addressFamily = AF_INET;
    // First see how much space is needed for adapter addresses
    ULONG adapterBufferSize = 0;
    ULONG retVal = GetAdaptersAddresses(addressFamily, 0, NULL, NULL, &adapterBufferSize);
    if (retVal != ERROR_BUFFER_OVERFLOW)
    {
        hr = HRESULT_FROM_WIN32(retVal);
        goto Exit;
    }
        
    // Allocate space for information about adapters
    adapterAddresses = (IP_ADAPTER_ADDRESSES*)HeapAlloc(GetProcessHeap(), 0, adapterBufferSize);
    if (adapterAddresses == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto Exit;
    }
    
    // Get list of adapters
    retVal = GetAdaptersAddresses(AF_INET, 0, NULL, adapterAddresses, &adapterBufferSize);
    if (retVal != 0)
    {
        hr = HRESULT_FROM_WIN32(retVal);
        goto Exit;
    }
    
    
    // Create a UDP duplex channel
    hr = WsCreateChannel(
        WS_CHANNEL_TYPE_DUPLEX, 
        WS_UDP_CHANNEL_BINDING, 
        NULL, 
        0, 
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
    
    // Initialize address to the multicast address to send to
    WS_ENDPOINT_ADDRESS address;
    address.url = serviceUrl;
    address.headers = NULL;
    address.extensions = NULL;
    address.identity = NULL;
    
    // Open channel to address
    hr = WsOpenChannel(channel, &address, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Generate a unique message ID that will be used for all messages
    WS_UNIQUE_ID messageID;
    ZeroMemory(&messageID, sizeof(messageID));
    if (UuidCreate(&messageID.guid) != RPC_S_OK)
    {
        hr = E_FAIL;
        goto Exit;
    }
    
    // Create a thread that will receive messages
    THREAD_INFO receiverThreadInfo;
    receiverThreadInfo.channel = channel;
    receiverThreadHandle = CreateThread(NULL, 0, ReceiverThread, &receiverThreadInfo, 0, NULL);
    if (receiverThreadHandle == NULL)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    
    hr = WsCreateMessageForChannel(
        channel,
        NULL, 
        0, 
        &message, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Initialize body data
    _PurchaseOrderType purchaseOrder;
    purchaseOrder.quantity = 100;
    purchaseOrder.productName = productName;
    
    // Send the same message twice
    for (int i = 0; i < 2; i++)
    {
        // For each adapter
        for (IP_ADAPTER_ADDRESSES* adapterAddress = adapterAddresses; 
             adapterAddress != NULL; adapterAddress = adapterAddress->Next)
        {
            // Only send on the loopback adapter
            if (adapterAddress->IfType != IF_TYPE_SOFTWARE_LOOPBACK)
            {
                continue;
            }
        
            // Get multicast interface index
            ULONG interfaceIndex = adapterAddress->IfIndex;
        
            // Set property on channel which controls which multicast adapater address
            // is used when sending to a multicast address.
            hr = WsSetChannelProperty(channel, WS_CHANNEL_PROPERTY_MULTICAST_INTERFACE, 
                &interfaceIndex, sizeof(interfaceIndex), error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Initialize message headers
            hr = WsInitializeMessage(message, WS_BLANK_MESSAGE, NULL, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Add the action header
            hr = WsSetHeader(
                message, 
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
        
            // Add the message ID
            hr = WsSetHeader(
                message, 
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
        
            // Set the reply to address to be a anonymous URI (modeled as a 0 length URI), which 
            // indicates to the receiver that they should reply using the source IP address.
            WS_ENDPOINT_ADDRESS replyTo;
            ZeroMemory(&replyTo, sizeof(replyTo));
        
            hr = WsSetHeader(
                message, 
                WS_REPLY_TO_HEADER, 
                WS_ENDPOINT_ADDRESS_TYPE,
                WS_WRITE_REQUIRED_VALUE,
                &replyTo, 
                sizeof(replyTo),
                error);
        
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Address the message to differ from the destination.  When the message
            // is addressed manually, the endpoint address specified at open time 
            // will only be used to determine the destination of the message (not
            // to determine the value of the To header).  In this case, the message is
            // addressed to a stable address.
            WS_ENDPOINT_ADDRESS to;
            ZeroMemory(&to, sizeof(to));
            to.url = toUrl;
        
            hr = WsAddressMessage(message, &to, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Write the message headers
            hr = WsWriteMessageStart(channel, message, NULL, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Write the body data
            hr = WsWriteBody(
                message, 
                &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
                WS_WRITE_REQUIRED_VALUE,
                &purchaseOrder, 
                sizeof(purchaseOrder),
                error);
        
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Send the entire message
            hr = WsWriteMessageEnd(channel, message, NULL, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        
            // Reset message so it can used again
            hr = WsResetMessage(message, error);
            if (FAILED(hr))
            {
                goto Exit;
            }
        }
    }
    
    // Wait for replies to be processed by the receiver thread
    Sleep(1000);
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    
    if (receiverThreadHandle != NULL)
    {
        // Abort the channel. This will cause the next receive to fail.
        WsAbortChannel(channel, error);
    
        // Wait for the receive thread to exit, and clean up the handle.
        WaitForSingleObject(receiverThreadHandle, INFINITE);
        CloseHandle(receiverThreadHandle);
    }
    
    if (channel != NULL)
    {
        // Close the channel
        WsCloseChannel(channel, NULL, error);
    }
    
    if (message != NULL)
    {
        WsFreeMessage(message);
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
    if (adapterAddresses != NULL)
    {
        HeapFree(GetProcessHeap(), 0, adapterAddresses);
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

all: $(OUTDIR) $(OUTDIR)\WsHttpClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\HttpClient.obj: HttpClient.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpClient.cpp

$(OUTDIR)\WsHttpClient.exe: $(OUTDIR)\HttpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpClient.exe $(OUTDIR)\HttpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsHttpClient.PDB

clean:
    $(CLEANUP)
```

 

 





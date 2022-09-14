---
title: AsyncStreamingTcpClientExample
description: This example shows a TCP client that sends one-way messages in an asynchronous streaming fashion.
ms.assetid: b0040b3d-d830-421a-bbf1-afb0cac47599
keywords:
- AsyncStreamingTcpClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# AsyncStreamingTcpClientExample

This example shows a TCP client that sends one-way messages in an asynchronous streaming fashion.

-   [AsyncStreamingTcpClient.cpp](#asyncstreamingtcpclientcpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## AsyncStreamingTcpClient.cpp


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

HANDLE serverStartedEvent = NULL;

struct SEND_STATE
{
    WS_CHANNEL* channel;
    WS_MESSAGE* message;
    ULONG messageCount;
    ULONG orderCount;
};

HRESULT CALLBACK Send1(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send2(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send3(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send4(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send5(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send6(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send7(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send8(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Send1(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    SEND_STATE* sendState = (SEND_STATE*)state;

    next->function = Send2;

    // Create a TCP duplex session channel
    hr = WsCreateChannel(
        WS_CHANNEL_TYPE_DUPLEX_SESSION, 
        WS_TCP_CHANNEL_BINDING, 
        NULL, 
        0, 
        NULL, 
        &sendState->channel, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Initialize address of service
    WS_ENDPOINT_ADDRESS address;
    address.url.chars = L"net.tcp://localhost/example";
    address.url.length = (ULONG)::wcslen(address.url.chars);
    address.headers = NULL;
    address.extensions = NULL;
    address.identity = NULL;
    
    // Open channel to address
    hr = WsOpenChannel(
        sendState->channel, 
        &address, 
        asyncContext, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
Exit:
    return hr;
}

HRESULT CALLBACK Send2(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(asyncContext);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    hr = WsCreateMessageForChannel(sendState->channel, NULL, 0, &sendState->message, error);
    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Send3;
    sendState->messageCount = 0;
    return NOERROR;
}

HRESULT CALLBACK Send3(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    if (sendState->messageCount >= 100)
    {
        next->function = Send8;
        return NOERROR;
    }

    // Initialize message headers
    hr = WsInitializeMessage(sendState->message, WS_BLANK_MESSAGE, NULL, error);
    if (FAILED(hr))
    {
        return hr;
    }

    // Add the action header
    hr = WsSetHeader(
        sendState->message, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE,
        WS_WRITE_REQUIRED_VALUE,
        PurchaseOrder_wsdl.messages.PurchaseOrder.action, 
        sizeof(*PurchaseOrder_wsdl.messages.PurchaseOrder.action),
        error);

    if (FAILED(hr))
    {
        return hr;
    }

    // Send the message headers
    sendState->orderCount = 0;
    next->function = Send4;
    return WsWriteMessageStart(sendState->channel, sendState->message, asyncContext, error);
}

static const WS_STRING pencil = WS_STRING_VALUE(L"Pencil");

HRESULT CALLBACK Send4(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }
    
    // Get the writer for the body
    WS_XML_WRITER* writer;
    hr = WsGetMessageProperty(sendState->message, WS_MESSAGE_PROPERTY_BODY_WRITER, &writer, sizeof(writer), error);
    if (FAILED(hr))
    {
        return hr;
    }

    if (sendState->orderCount >= 100)
    {
        next->function = Send6;
        return NOERROR;
    }

    // Initialize body data
    _PurchaseOrderType purchaseOrder;
    purchaseOrder.quantity = 1;
    purchaseOrder.productName = pencil;

    // Write body data
    hr = WsWriteElement(
        writer, 
        &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
        WS_WRITE_REQUIRED_VALUE,
        &purchaseOrder, 
        sizeof(purchaseOrder), 
        error);

    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Send5;
    return WsFlushWriter(writer, 128, asyncContext, error);
}

HRESULT CALLBACK Send5(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    sendState->orderCount++;
    next->function = Send4;
    return NOERROR;
}

HRESULT CALLBACK Send6(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Send the end of the message
    next->function = Send7;
    return WsWriteMessageEnd(sendState->channel, sendState->message, asyncContext, error);
}

HRESULT CALLBACK Send7(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(asyncContext);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Reset message so it can be used again
    hr = WsResetMessage(sendState->message, error);
    if (FAILED(hr))
    {
        return hr;
    }

    sendState->messageCount++;
    next->function = Send3;
    return NOERROR;
}

HRESULT CALLBACK Send8(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    SEND_STATE* sendState = (SEND_STATE*)state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Close the channel
    next->function = NULL;
    return WsCloseChannel(sendState->channel, asyncContext, error);
}

struct THREAD_INFO
{
    HRESULT hr;
    HANDLE handle;
};

static void CALLBACK OnSendComplete(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state)
{
    UNREFERENCED_PARAMETER(callbackModel);

    THREAD_INFO* threadInfo = (THREAD_INFO*)state;
    threadInfo->hr = hr;
    SetEvent(threadInfo->handle);
}

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    
    WS_ASYNC_STATE asyncState;
    SEND_STATE sendState;
    sendState.channel = NULL;
    sendState.message = NULL;
    sendState.messageCount = 0;
    sendState.orderCount = 0;
    
    THREAD_INFO threadInfo;
    threadInfo.hr = NOERROR;
    threadInfo.handle = NULL;
        
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
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    threadInfo.handle = CreateEvent(NULL, TRUE, FALSE, NULL);
    if (threadInfo.handle == NULL)
    {
        goto Exit;
    }
    
    WS_ASYNC_CONTEXT sendComplete;
    sendComplete.callback = OnSendComplete;
    sendComplete.callbackState = &threadInfo;
    
    hr = WsAsyncExecute(&asyncState, Send1, WS_LONG_CALLBACK, &sendState, &sendComplete, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    if (hr == WS_S_ASYNC)
    {
        WaitForSingleObject(threadInfo.handle, INFINITE);
        hr = threadInfo.hr;
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
    
    if (threadInfo.handle != NULL)
    {
        CloseHandle(threadInfo.handle);
    }
        
    if (sendState.channel != NULL)
    {
        // Close the channel
        WsCloseChannel(sendState.channel, NULL, error);
    }
    if (sendState.message != NULL)
    {
        WsFreeMessage(sendState.message);
    }
    if (sendState.channel != NULL)
    {
        WsFreeChannel(sendState.channel);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    
    if (NULL != serverStartedEvent)
    {
        CloseHandle(serverStartedEvent);
    }
    
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}

```



## PurchaseOrder.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="https://example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/" 
    targetNamespace="https://example.org">
    <wsdl:types>
        <xsd:schema targetNamespace="https://example.org" elementFormDefault="qualified">
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
            <wsdl:input message="tns:PurchaseOrder" wsaw:Action="https://example.org/purchaseorder"/>
            <wsdl:output message="tns:OrderConfirmation" wsaw:Action="https://example.org/orderconfirmation"/>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <wsdl:input message="tns:GetOrderStatus" wsaw:Action="https://example.org/getorderstatus"/>
            <wsdl:output message="tns:GetOrderStatusResponse" wsaw:Action="https://example.org/getorderstatusresponse"/>
            <wsdl:fault name="OrderNotFound" message="tns:OrderNotFoundFault" wsaw:Action="https://example.org/ordernotfound"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="PurchaseOrderBinding" type="tns:IPurchaseOrder">
        <soap:binding transport="https://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Order">
            <soap:operation soapAction="https://example.org/purchaseorder" style="document"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="OrderStatus">
            <soap:operation soapAction="https://example.org/getorderstatus" style="document"/>
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
            <soap:address location="https://example.org/IPurchaseOrder"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsAsyncStreamingTcpClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\AsyncStreamingTcpClient.obj: AsyncStreamingTcpClient.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" AsyncStreamingTcpClient.cpp

$(OUTDIR)\WsAsyncStreamingTcpClient.exe: $(OUTDIR)\AsyncStreamingTcpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsAsyncStreamingTcpClient.exe $(OUTDIR)\AsyncStreamingTcpClient.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsAsyncStreamingTcpClient.PDB

clean:
    $(CLEANUP)
```

 

 





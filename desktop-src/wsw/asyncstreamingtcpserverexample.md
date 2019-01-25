---
title: AsyncStreamingTcpServerExample
description: This example shows a TCP server that receives one-way messages in an asynchronous streaming fashion.
ms.assetid: 8b79735b-f238-4d49-8977-2935fc208d48
keywords:
- AsyncStreamingTcpServerExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# AsyncStreamingTcpServerExample

This example shows a TCP server that receives one-way messages in an asynchronous streaming fashion.

-   [AsyncStreamingTcpServer.cpp](#asyncstreamingtcpservercpp)
-   [PurchaseOrder.wsdl](#purchaseorderwsdl)
-   [Makefile](#makefile)

## AsyncStreamingTcpServer.cpp


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

struct RECEIVE_STATE
{
    WS_LISTENER* listener;
    WS_CHANNEL* channel;
    WS_MESSAGE* message;
    WS_HEAP* heap;
    WS_XML_READER* reader;
};

HRESULT CALLBACK Receive1(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive2(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive3(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive3_5(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive4(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive5(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive6(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive7(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive8(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive9(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive10(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

HRESULT CALLBACK Receive1(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Create a listener
    hr = WsCreateListener(WS_CHANNEL_TYPE_DUPLEX_SESSION, WS_TCP_CHANNEL_BINDING, NULL, 0, NULL, &receiveState->listener, error);
    if (FAILED(hr))
    {
        return hr;
    }

    // Open listener using TCP duplex session
    WS_STRING uri = WS_STRING_VALUE(L"net.tcp://localhost/example");
    next->function = Receive2;
    return WsOpenListener(receiveState->listener, &uri, asyncContext, error);
}

HRESULT CALLBACK Receive2(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
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

    hr = WsCreateChannelForListener(receiveState->listener, NULL, 0, &receiveState->channel, error);
    if (FAILED(hr))
    {
        return hr;
    }

    // Accept a channel from the client
    next->function = Receive3;
    return WsAcceptChannel(receiveState->listener, receiveState->channel, asyncContext, error);
Exit:
    return hr;
}

HRESULT CALLBACK Receive3(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    hr = WsCreateMessageForChannel(receiveState->channel, NULL, 0, &receiveState->message, error);
    if (FAILED(hr))
    {
        return hr;
    }

    // Stop listening for channels
    next->function = Receive4;
    return WsCloseListener(receiveState->listener, asyncContext, error);
}

HRESULT CALLBACK Receive4(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Receive the message start (headers)
    next->function = Receive5;
    return WsReadMessageStart(receiveState->channel, receiveState->message, asyncContext, error);
}

HRESULT CALLBACK Receive5(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    if (hr == WS_S_END)
    {
        next->function = NULL;
        // Close the channel
        return WsCloseChannel(receiveState->channel, asyncContext, error);
    }

    // Get action value
    WS_XML_STRING receivedAction;
    hr = WsGetHeader(
        receiveState->message, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE,
        WS_READ_REQUIRED_VALUE, 
        NULL, 
        &receivedAction, 
        sizeof(receivedAction), 
        error);
    if (FAILED(hr))
    {
        return hr;
    }

    // Make sure action is what we expect
    if (WsXmlStringEquals(&receivedAction, PurchaseOrder_wsdl.messages.PurchaseOrder.action, error) != S_OK)
    {
        return WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
    }

    // Get the reader for the body
    hr = WsGetMessageProperty(receiveState->message, WS_MESSAGE_PROPERTY_BODY_READER, &receiveState->reader, sizeof(receiveState->reader), error);
    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Receive6;
    return NOERROR;
}

HRESULT CALLBACK Receive6(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Receive8;
    return WsFillReader(receiveState->reader, 128, asyncContext, error);
}

HRESULT CALLBACK Receive8(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(asyncContext);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Read purchase order into heap, if there are any more to read.
    _PurchaseOrderType* purchaseOrder;
    hr = WsReadElement(receiveState->reader, &PurchaseOrder_wsdl.globalElements.PurchaseOrderType, 
        WS_READ_OPTIONAL_POINTER, receiveState->heap, &purchaseOrder, sizeof(purchaseOrder), error);
    if (FAILED(hr))
    {
        return hr;
    }

    // If NULL indicates no more purchase orders
    if (purchaseOrder == NULL)
    {
        next->function = Receive9;
        return NOERROR;
    }

    wprintf(L"%ld, %.*s\n", 
        purchaseOrder->quantity, 
        purchaseOrder->productName.length,
        purchaseOrder->productName.chars);
    fflush(stdout);

    // Free purchase order
    hr = WsResetHeap(receiveState->heap, error);
    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Receive6;
    return NOERROR;
}
    
HRESULT CALLBACK Receive9(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    // Free purchase order
    hr = WsResetHeap(receiveState->heap, error);
    if (FAILED(hr))
    {
        return hr;
    }

    next->function = Receive10;
    return WsReadMessageEnd(receiveState->channel, receiveState->message, asyncContext, error);
}

HRESULT CALLBACK Receive10(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state, WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(asyncContext);

    RECEIVE_STATE* receiveState = (RECEIVE_STATE*) state;
    if (FAILED(hr))
    {
        return hr;
    }

    hr = WsResetMessage(receiveState->message, error);
    if (FAILED(hr))
    {
        return hr;
    }
    next->function = Receive4;
    return NOERROR;
}

struct THREAD_INFO
{
    HRESULT hr;
    HANDLE handle;
};

static void CALLBACK OnReceiveComplete(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state)
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
    RECEIVE_STATE receiveState;
    receiveState.listener = NULL;
    receiveState.channel = NULL;
    receiveState.message = NULL;
    receiveState.heap = NULL;
    receiveState.reader = NULL;
    
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
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
        
    // Create a heap to hold body data, with a max size to limit size of purchase order read
    hr = WsCreateHeap(/*maxSize*/ 1024, /*trimSize*/ 1024, NULL, 0, &receiveState.heap, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    threadInfo.handle = CreateEvent(NULL, TRUE, FALSE, NULL);
    if (threadInfo.handle == NULL)
    {
        goto Exit;
    }
    
    WS_ASYNC_CONTEXT receiveComplete;
    receiveComplete.callback = OnReceiveComplete;
    receiveComplete.callbackState = &threadInfo;
    
    hr = WsAsyncExecute(&asyncState, Receive1, WS_LONG_CALLBACK, &receiveState, &receiveComplete, error);
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
    
    if (receiveState.channel != NULL)
    {
        // Close the channel
        WsCloseChannel(receiveState.channel, NULL, error);
    }
    if (receiveState.channel != NULL)
    {
        WsFreeChannel(receiveState.channel);
    }
    if (receiveState.listener != NULL)
    {
        // Close the listener if it was opened
        WsCloseListener(receiveState.listener, NULL, error);
    }
    if (receiveState.listener != NULL)
    {
        WsFreeListener(receiveState.listener);
    }
    if (receiveState.message != NULL)
    {
        WsFreeMessage(receiveState.message);
    }
    if (receiveState.heap != NULL)
    {
        WsFreeHeap(receiveState.heap);
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

all: $(OUTDIR) $(OUTDIR)\WsAsyncStreamingTcpServer.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\PurchaseOrder.wsdl.c: PurchaseOrder.wsdl
     Wsutil.exe /wsdl:PurchaseOrder.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\PurchaseOrder.wsdl.obj: $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\PurchaseOrder.wsdl.c

$(OUTDIR)\AsyncStreamingTcpServer.obj: AsyncStreamingTcpServer.cpp $(OUTDIR)\PurchaseOrder.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" AsyncStreamingTcpServer.cpp

$(OUTDIR)\WsAsyncStreamingTcpServer.exe: $(OUTDIR)\AsyncStreamingTcpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsAsyncStreamingTcpServer.exe $(OUTDIR)\AsyncStreamingTcpServer.obj $(OUTDIR)\PurchaseOrder.wsdl.obj /PDB:$(OUTDIR)\WsAsyncStreamingTcpServer.PDB

clean:
    $(CLEANUP)
```

 

 





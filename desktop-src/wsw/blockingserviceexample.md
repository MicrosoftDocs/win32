---
title: BlockingServiceExample
description: Example service application demonstrating server side call cancellation.
ms.assetid: a0a862bc-521a-477a-854d-58642d497109
keywords:
- BlockingServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# BlockingServiceExample

Example service application demonstrating server side call cancellation.

-   [CancellingService.cpp](#cancellingservicecpp)
-   [BlockUnBlockService.wsdl](#blockunblockservicewsdl)
-   [Makefile](#makefile)

## CancellingService.cpp


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
HANDLE closeServer = NULL;  

#include "BlockUnBlockService.wsdl.h"

static void CALLBACK AbortNotification(
    __in WS_SERVICE_CANCEL_REASON reason, 
    __in_opt void* callbackState)
{
    wprintf(L"Abort Reason is: %d\n", reason);
    fflush(stdout);
    HANDLE unblockMethod = (HANDLE) callbackState;
    SetEvent(unblockMethod);
}

static void CALLBACK FreeState(
    __in_opt void* callbackState)
{
    HANDLE unblockMethod = (HANDLE) callbackState;
    CloseHandle(unblockMethod);
}

static HRESULT CALLBACK Block(
    __in const WS_OPERATION_CONTEXT* context, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(asyncContext);

    HRESULT hr = NOERROR;
    HANDLE unblockMethod = CreateEvent(NULL, FALSE, FALSE, NULL);
    if (!unblockMethod)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }
    hr = WsRegisterOperationForCancel(
        context, 
        AbortNotification, 
        FreeState, 
        unblockMethod, 
        error);
if (FAILED(hr))
{
    goto Exit;
}
    WaitForSingleObject(unblockMethod, INFINITE);
Exit:
    SetEvent(closeServer);
    if (FAILED(hr))
    {
        CloseHandle(unblockMethod);
    }
    return hr;
}

static HRESULT CALLBACK UnBlock(
    __in const WS_OPERATION_CONTEXT* context, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);

    SetEvent(closeServer);
    return NOERROR;
}

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


static const BlockServiceBindingFunctionTable serviceFunctions = {Block, UnBlock};

// Method contract for the service
static const WS_SERVICE_CONTRACT blockServiceContract = 
{
    &BlockUnBlockService_wsdl.contracts.BlockServiceBinding, // comes from the generated header.
    NULL, // for not specifying the default contract
    &serviceFunctions // specified by the user
};


// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_SERVICE_HOST* host = NULL;
    WS_SERVICE_ENDPOINT serviceEndpoint = {};
    const WS_SERVICE_ENDPOINT* serviceEndpoints[1];
    WS_ERROR* error = NULL;
    WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[1];
    const ULONG maxConcurrency = 100;
    serviceEndpoints[0] = &serviceEndpoint;
    serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_MAX_CONCURRENCY;
    serviceProperties[0].value = (void*)&maxConcurrency;
    serviceProperties[0].valueSize = sizeof(maxConcurrency);
    
    // Create Event object for closing the server
    closeServer = CreateEvent(
        NULL, 
        TRUE, 
        FALSE, 
        NULL);
    if (closeServer == NULL)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        goto Exit;
    }   
    
    // Initialize service endpoint
    serviceEndpoint.address.url.chars = L"net.tcp://+/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_TCP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_DUPLEX_SESSION; // the channel type
    serviceEndpoint.contract = &blockServiceContract;  // the contract
    serviceEndpoint.properties = serviceProperties;
    serviceEndpoint.propertyCount = WsCountOf(serviceProperties);
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // Creating a service host
    hr = WsCreateServiceHost(
        serviceEndpoints, 
        1, 
        NULL, 
        0, 
        &host, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    // WsOpenServiceHost to start the listeners in the service host 
    hr = WsOpenServiceHost(
            host, 
            NULL, 
            error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    WaitForSingleObject(closeServer, INFINITE);
    // Aborts the service host so that the blocked method can complete.
    WsAbortServiceHost(host, NULL);
    // Close the service host
    hr = WsCloseServiceHost(host, NULL, error);
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
    if (host != NULL)
    {
        WsFreeServiceHost(host);
    }
    
    
    if (error != NULL)
    {
        WsFreeError(error);
    }
    if (closeServer != NULL)
    {
        CloseHandle(closeServer);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}


```



## BlockUnBlockService.wsdl

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/" 
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:http="https://schemas.xmlsoap.org/wsdl/http/" 
    xmlns:xs="https://www.w3.org/2001/XMLSchema" 
    xmlns:mime="https://schemas.xmlsoap.org/wsdl/mime/" 
    xmlns:tns="https://www.example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    targetNamespace="https://www.example.org" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl">
    <wsdl:types>
        <xs:schema targetNamespace="https://www.example.org" elementFormDefault="qualified">
            <xsd:element name="BlockServiceType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="BlockServiceResponseType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="UnBlockServiceType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="UnBlockServiceResponseType">
                <xsd:complexType/>
            </xsd:element>
        </xs:schema>
    </wsdl:types>
    <wsdl:message name="BlockServiceMessage">
        <wsdl:part name="parameters" element="tns:BlockServiceType"/>
    </wsdl:message>
    <wsdl:message name="BlockServiceResponseMessage">
        <wsdl:part name="parameters" element="tns:BlockServiceResponseType"/>
    </wsdl:message>
    <wsdl:message name="UnBlockServiceMessage">
        <wsdl:part name="parameters" element="tns:UnBlockServiceType"/>
    </wsdl:message>
    <wsdl:message name="UnBlockServiceResponseMessage">
        <wsdl:part name="parameters" element="tns:UnBlockServiceResponseType"/>
    </wsdl:message>
    <wsdl:portType name="IBlockUnBlockService">
        <wsdl:operation name="Block">
            <wsdl:input message="tns:BlockServiceMessage" wsaw:Action="https://www.example.org/Block"/>
            <wsdl:output message="tns:BlockServiceResponseMessage" wsaw:Action="https://www.example.org/BlockResponse"/>
        </wsdl:operation>
        <wsdl:operation name="UnBlock">
            <wsdl:input message="tns:UnBlockServiceMessage" wsaw:Action="https://www.example.org/UnBlock"/>
            <wsdl:output message="tns:UnBlockServiceResponseMessage" wsaw:Action="https://www.example.org/UnBlockResponse"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="BlockServiceBinding" type="tns:IBlockUnBlockService">
        <soap:binding style="document" transport="https://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Block">
            <soap:operation soapAction="https://www.example.org/Block"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="UnBlock">
            <soap:operation soapAction="https://www.example.org/UnBlock"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="BlockUnBlockService">
        <wsdl:port name="BlockingService" binding="tns:BlockServiceBinding">
            <soap:address location="No Target Address"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib Iphlpapi.lib

all: $(OUTDIR) $(OUTDIR)\WsCancellingService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\BlockUnBlockService.wsdl.c: BlockUnBlockService.wsdl
     Wsutil.exe /wsdl:BlockUnBlockService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\BlockUnBlockService.wsdl.obj: $(OUTDIR)\BlockUnBlockService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\BlockUnBlockService.wsdl.c

$(OUTDIR)\CancellingService.obj: CancellingService.cpp $(OUTDIR)\BlockUnBlockService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" CancellingService.cpp

$(OUTDIR)\WsCancellingService.exe: $(OUTDIR)\CancellingService.obj $(OUTDIR)\BlockUnBlockService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsCancellingService.exe $(OUTDIR)\CancellingService.obj $(OUTDIR)\BlockUnBlockService.wsdl.obj /PDB:$(OUTDIR)\WsCancellingService.PDB

clean:
    $(CLEANUP)
```

 

 





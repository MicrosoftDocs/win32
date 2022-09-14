---
title: CallAbandonExample
description: Example client application demonstrating abandoning a call.
ms.assetid: 71253dd6-4f59-4acd-b244-c721834ca381
keywords:
- CallAbandonExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# CallAbandonExample

Example client application demonstrating abandoning a call.

-   [AbandonCallClient.cpp](#abandoncallclientcpp)
-   [BlockUnBlockService.wsdl](#blockunblockservicewsdl)
-   [Makefile](#makefile)

## AbandonCallClient.cpp


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
#include "BlockUnBlockService.wsdl.h"

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

void CALLBACK BlockMethodComplete(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState)
{
    UNREFERENCED_PARAMETER(hr);
    UNREFERENCED_PARAMETER(callbackModel);
    UNREFERENCED_PARAMETER(callbackState);

    wprintf(L"Method Completed\n");
    fflush(stdout);
}

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_HEAP* heap = NULL;
    WS_SERVICE_PROXY* serviceProxy = NULL;
    WS_ENDPOINT_ADDRESS address = {};
    const WS_ASYNC_CONTEXT asyncContext = {BlockMethodComplete, NULL};
    WS_STRING serviceUrl = WS_STRING_VALUE(L"net.tcp://localhost/example");
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
    hr = WsCreateServiceProxy(WS_CHANNEL_TYPE_DUPLEX_SESSION, WS_TCP_CHANNEL_BINDING, NULL, NULL, 0, NULL, 0, &serviceProxy, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    // Initialize address of service
    address.url = serviceUrl;                    
    hr = WsOpenServiceProxy(serviceProxy, &address, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"Calling blocking method async\n");
    hr = BlockServiceBinding_Block(serviceProxy, heap, NULL, 0, &asyncContext, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"Now abandoning call\n");
    fflush(stdout);
    hr = WsAbandonCall(serviceProxy, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    wprintf(L"Now unblocking service\n");
    hr = BlockServiceBinding_UnBlock(serviceProxy, heap, NULL, 0, &asyncContext, error);
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
    if (serviceProxy != NULL)
    {
        WsCloseServiceProxy(serviceProxy, NULL, NULL);
        WsFreeServiceProxy(serviceProxy);
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

all: $(OUTDIR) $(OUTDIR)\WsAbandonCallClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\BlockUnBlockService.wsdl.c: BlockUnBlockService.wsdl
     Wsutil.exe /wsdl:BlockUnBlockService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\BlockUnBlockService.wsdl.obj: $(OUTDIR)\BlockUnBlockService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\BlockUnBlockService.wsdl.c

$(OUTDIR)\AbandonCallClient.obj: AbandonCallClient.cpp $(OUTDIR)\BlockUnBlockService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" AbandonCallClient.cpp

$(OUTDIR)\WsAbandonCallClient.exe: $(OUTDIR)\AbandonCallClient.obj $(OUTDIR)\BlockUnBlockService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsAbandonCallClient.exe $(OUTDIR)\AbandonCallClient.obj $(OUTDIR)\BlockUnBlockService.wsdl.obj /PDB:$(OUTDIR)\WsAbandonCallClient.PDB

clean:
    $(CLEANUP)
```

 

 





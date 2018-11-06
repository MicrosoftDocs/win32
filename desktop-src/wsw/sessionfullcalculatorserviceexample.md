---
title: SessionfullCalculatorServiceExample
description: An implementation of a sessionful calculator service using the Service Host.
ms.assetid: 7501025b-5692-4f89-ad74-c60694c29163
keywords:
- SessionfullCalculatorServiceExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# SessionfullCalculatorServiceExample

An implementation of a sessionful calculator service using the Service Host.

-   [SessionfullCalculatorService.cpp](#sessionfullcalculatorservicecpp)
-   [SessionBasedCalculatorService.wsdl](#sessionbasedcalculatorservicewsdl)
-   [Makefile](#makefile)

## SessionfullCalculatorService.cpp


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
#include <intsafe.h>
#include "SessionBasedCalculatorService.wsdl.h"
HANDLE closeServer = NULL;  
class SessionfulCalculator 
{
    int total;

public:
    static HRESULT CALLBACK Add(
        __in const WS_OPERATION_CONTEXT* context, 
        __in int a, 
        __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
        __in_opt WS_ERROR* error)
    {
        UNREFERENCED_PARAMETER(asyncContext);

        HRESULT hr = NOERROR;
        SessionfulCalculator* calculator = NULL;
        hr = WsGetOperationContextProperty(
                context, 
                WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE, 
                &calculator, 
                sizeof(SessionfulCalculator*), 
                error);
if (FAILED(hr))
{
    goto Exit;
}
        hr = calculator->Add(a);
    Exit:
        return hr;
    }

    static HRESULT CALLBACK Subtract(
        __in const WS_OPERATION_CONTEXT* context, 
        __in int a, 
        __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
        __in_opt WS_ERROR* error)
    {
        UNREFERENCED_PARAMETER(asyncContext);

        HRESULT hr = NOERROR;
        SessionfulCalculator* calculator = NULL;
        hr = WsGetOperationContextProperty(
                context, 
                WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE, 
                &calculator, 
                sizeof(SessionfulCalculator*), 
                error);
if (FAILED(hr))
{
    goto Exit;
}
        hr = calculator->Subtract(a);
    Exit:
        return hr;
    }

    static HRESULT CALLBACK Clear(
        __in const WS_OPERATION_CONTEXT* context, 
        __in const WS_ASYNC_CONTEXT* asyncContext, 
        __in_opt WS_ERROR* error)
    {
        UNREFERENCED_PARAMETER(asyncContext);

        HRESULT hr = NOERROR;
        SessionfulCalculator* calculator = NULL;
        hr = WsGetOperationContextProperty(
                context, 
                WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE, 
                &calculator, 
                sizeof(SessionfulCalculator*), 
                error);
if (FAILED(hr))
{
    goto Exit;
}
        hr = calculator->Clear();
    Exit:
        return hr;
    }

    static HRESULT CALLBACK Total(
        __in const WS_OPERATION_CONTEXT* context, 
        __out int* total, 
        __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
        __in_opt WS_ERROR* error)
    {
        UNREFERENCED_PARAMETER(asyncContext);

        HRESULT hr = NOERROR;
        SessionfulCalculator* calculator = NULL;
        hr = WsGetOperationContextProperty(
                context, 
                WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE, 
                &calculator, 
                sizeof(SessionfulCalculator*), 
                error);
if (FAILED(hr))
{
    goto Exit;
}
        hr = calculator->Total(
                total);
    Exit:
        return hr;
    }

private:
    HRESULT Add(
        __in int a)
    {
        wprintf(
            L"Adding %d to a total of %d\n",
            a, 
            total);
        
        total += a;
        
        fflush(
            stdout);
        return NOERROR;
    }

    HRESULT Subtract(
        __in int a)
    {
        wprintf(
            L"Subtracting %d from a total of %d\n", 
            a, 
            total);
        
        total -= a;
        
        fflush(
            stdout);
        return NOERROR;
    }

    HRESULT Clear()
    {
        total = 0;
        wprintf(
            L"Cleared!\n");
        
        fflush(
            stdout);
        return NOERROR;
    }

    HRESULT Total(int* result)
    {
        wprintf(
            L"The total is %d\n",total);
        *result = total;
        fflush(stdout);
        return NOERROR;
    }
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

HRESULT CALLBACK CreateSessionCalculator(
    __in const WS_OPERATION_CONTEXT* context, 
    __deref_out void** channelState, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(context);
    UNREFERENCED_PARAMETER(asyncContext);
    UNREFERENCED_PARAMETER(error);

    wprintf(
        L"Creating Calculator instance\n");
    SessionfulCalculator* calculator = new SessionfulCalculator();
    if (calculator)
    {
        *channelState = (void*)calculator;
    }
    else
    {
        return E_OUTOFMEMORY;
    }
    return NOERROR;
}

HRESULT CALLBACK FreeSessionCalculator(
    __in const WS_OPERATION_CONTEXT* context, 
    __in const WS_ASYNC_CONTEXT* asyncContext)
{
    UNREFERENCED_PARAMETER(asyncContext);

    SessionfulCalculator* calculator = NULL;
    WsGetOperationContextProperty(
        context, 
        WS_OPERATION_CONTEXT_PROPERTY_CHANNEL_USER_STATE, 
        &calculator, 
        sizeof(SessionfulCalculator*), 
        NULL);
    if (calculator != NULL)
    {    
        wprintf(L"Deleting Calculator instance\n");
        delete calculator;
    }
    
    SetEvent(closeServer);
    return NOERROR;
}

static const 
CalculatorBindingFunctionTable 
calculatorFunctions = {
    SessionfulCalculator::Add, 
    SessionfulCalculator::Subtract, 
    SessionfulCalculator::Total,
    SessionfulCalculator::Clear 
};

// Method contract for the service
static const WS_SERVICE_CONTRACT calculatorServiceContract = 
{
    &SessionBasedCalculatorService_wsdl.contracts.CalculatorBinding, // comes from the generated header.
    NULL, // for not specifying the default contract
    &calculatorFunctions // specified by the user
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
    serviceEndpoints[0] = &serviceEndpoint;
    WS_ERROR* error = NULL;
    WS_SERVICE_ENDPOINT_PROPERTY serviceProperties[2];
    WS_SERVICE_PROPERTY_ACCEPT_CALLBACK acceptCallbackProperty = {CreateSessionCalculator};
    WS_SERVICE_PROPERTY_CLOSE_CALLBACK closeCallbackProperty = {FreeSessionCalculator};
    
    serviceProperties[0].id = WS_SERVICE_ENDPOINT_PROPERTY_ACCEPT_CHANNEL_CALLBACK;
    serviceProperties[0].value = &acceptCallbackProperty;
    serviceProperties[0].valueSize = sizeof(acceptCallbackProperty);
    serviceProperties[1].id = WS_SERVICE_ENDPOINT_PROPERTY_CLOSE_CHANNEL_CALLBACK;
    serviceProperties[1].value = &closeCallbackProperty;
    serviceProperties[1].valueSize = sizeof(closeCallbackProperty);
    
    
    // Initialize service endpoint
    serviceEndpoint.address.url.chars = L"net.tcp://+/example"; // address given as uri
    serviceEndpoint.address.url.length = (ULONG)wcslen(serviceEndpoint.address.url.chars);
    serviceEndpoint.channelBinding = WS_TCP_CHANNEL_BINDING; // channel binding for the endpoint
    serviceEndpoint.channelType = WS_CHANNEL_TYPE_DUPLEX_SESSION; // the channel type
    serviceEndpoint.contract = &calculatorServiceContract;  // the contract
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



## SessionBasedCalculatorService.wsdl

``` syntax
<?xml version="1.0" encoding="UTF-8"?>
<wsdl:definitions 
    xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/" 
    xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:http="http://schemas.xmlsoap.org/wsdl/http/" 
    xmlns:tns="http://www.example.org" 
    xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" 
    targetNamespace="http://www.example.org">
    <wsdl:types>
        <xsd:schema targetNamespace="http://www.example.org" elementFormDefault="qualified">
            <xsd:element name="AddType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="addend" type="xsd:int"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="SubtractType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="subtractend" type="xsd:int"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="TotalResponseType">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="Total" type="xsd:int"/>
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="AddResponseType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="SubtractResponseType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="TotalRequestType">
                <xsd:complexType/>
            </xsd:element>
            <xsd:element name="ClearType">
                <xsd:complexType/>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>
    <wsdl:message name="AddMessage">
        <wsdl:part name="parameters" element="tns:AddType"/>
    </wsdl:message>
    <wsdl:message name="AddResponseMessage">
        <wsdl:part name="parameters" element="tns:AddResponseType"/>
    </wsdl:message>
    <wsdl:message name="SubtractMessage">
        <wsdl:part name="parameters" element="tns:SubtractType"/>
    </wsdl:message>
    <wsdl:message name="SubtractResponseMessage">
        <wsdl:part name="parameters" element="tns:SubtractResponseType"/>
    </wsdl:message>
    <wsdl:message name="TotalRequest">
        <wsdl:part name="parameters" element="tns:TotalRequestType"/>
    </wsdl:message>
    <wsdl:message name="TotalResponse">
        <wsdl:part name="parameters" element="tns:TotalResponseType"/>
    </wsdl:message>
    <wsdl:message name="ClearMessage">
        <wsdl:part name="parameters" element="tns:ClearType"/>
    </wsdl:message>
    <wsdl:portType name="ISessionBasedCalculator">
        <wsdl:operation name="Add">
            <wsdl:input message="tns:AddMessage" wsaw:Action="http://www.example.org/Add"/>
            <wsdl:output message="tns:AddResponseMessage" wsaw:Action="http://www.example.org/AddResponse"/>
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <wsdl:input message="tns:SubtractMessage" wsaw:Action="http://www.example.org/Subtract"/>
            <wsdl:output message="tns:SubtractResponseMessage" wsaw:Action="http://www.example.org/SubtractResponse"/>
        </wsdl:operation>
        <wsdl:operation name="Total">
            <wsdl:output message="tns:TotalResponse" wsaw:Action="http://www.example.org/TotalResponse"/>
            <wsdl:input message="tns:TotalRequest" wsaw:Action="http://www.example.org/Total"/>
        </wsdl:operation>
        <wsdl:operation name="Clear">
            <wsdl:input message="tns:ClearMessage" wsaw:Action="http://www.example.org/Clear"/>
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="CalculatorBinding" type="tns:ISessionBasedCalculator">
        <soap:binding style="document" transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="Add">
            <soap:operation soapAction="http://www.example.org/Add"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <soap:operation soapAction="http://www.example.org/Subtract"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="Total">
            <soap:operation soapAction="http://www.example.org/Total"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal"/>
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="Clear">
            <soap:operation soapAction="http://www.example.org/Clear"/>
            <wsdl:input>
                <soap:body use="literal"/>
            </wsdl:input>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="SessionBasedService">
        <wsdl:port name="Calculator" binding="tns:CalculatorBinding">
            <soap:address location="No Target Address"/>
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

all: $(OUTDIR) $(OUTDIR)\WsSessionfullCalculatorService.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\SessionBasedCalculatorService.wsdl.c: SessionBasedCalculatorService.wsdl
     Wsutil.exe /wsdl:SessionBasedCalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    

$(OUTDIR)\SessionBasedCalculatorService.wsdl.obj: $(OUTDIR)\SessionBasedCalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\SessionBasedCalculatorService.wsdl.c

$(OUTDIR)\SessionfullCalculatorService.obj: SessionfullCalculatorService.cpp $(OUTDIR)\SessionBasedCalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" SessionfullCalculatorService.cpp

$(OUTDIR)\WsSessionfullCalculatorService.exe: $(OUTDIR)\SessionfullCalculatorService.obj $(OUTDIR)\SessionBasedCalculatorService.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsSessionfullCalculatorService.exe $(OUTDIR)\SessionfullCalculatorService.obj $(OUTDIR)\SessionBasedCalculatorService.wsdl.obj /PDB:$(OUTDIR)\WsSessionfullCalculatorService.PDB

clean:
    $(CLEANUP)
```

 

 





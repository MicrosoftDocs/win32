---
title: HttpCalculatorWithSslPolicyClientExample
description: This example shows how to use the wsutil generated policy helper routines to create service proxy to talk to a calculator service, with SSL transport security.
ms.assetid: cf2455d4-0670-4ea2-8ee7-073698bfb765
keywords:
- HttpCalculatorWithSslPolicyClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithSslPolicyClientExample

This example shows how to use the wsutil generated policy helper routines to create service proxy to talk to a calculator service, with SSL transport security. In this setup, the transport connection is protected (signed, encrypted) by SSL which also provides server authentication.

-   [HttpCalculatorWithSslPolicyClient.cpp](#httpcalculatorwithsslpolicyclientcpp)
-   [CalculatorServiceWithPolicy.wsdl](#calculatorservicewithpolicywsdl)
-   [Makefile](#makefile)

## HttpCalculatorWithSslPolicyClient.cpp


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
#include "wincrypt.h"
#include "CalculatorServiceWithPolicy.wsdl.h"

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
    WS_HEAP* heap = NULL;
    WS_SERVICE_PROXY* serviceProxy = NULL;
    int result = 0;
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING url = WS_STRING_VALUE(L"https://localhost:8443/example");
    address.url = url;
    
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
    
$$RC_START_HIGHLIGHT
    
    // Create the proxy
    hr = DefaultBinding_ICalculator_CreateServiceProxy(
        NULL,
        NULL,
        0,
        &serviceProxy, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
$$RC_END_HIGHLIGHT
    
    
    
    hr = WsOpenServiceProxy(serviceProxy, &address, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    hr = DefaultBinding_ICalculator_Add(serviceProxy, 1, 2, &result, heap, NULL, 0, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"%d + %d = %d\n", 1, 2, result);
                   
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



## CalculatorServiceWithPolicy.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="https://Example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:wsu="https://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" 
    xmlns:wsp="https://schemas.xmlsoap.org/ws/2004/09/policy" 
    xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
    targetNamespace="https://Example.org" 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/">
    <wsp:Policy wsu:Id="policy1">
      <wsp:ExactlyOne>
              <sp:TransportBinding xmlns:sp="https://schemas.xmlsoap.org/ws/2005/07/securitypolicy">
                  <wsp:Policy>
                      <sp:TransportToken>
                          <wsp:Policy>
                              <sp:HttpsToken RequireClientCertificate="false" />
                          </wsp:Policy>
                      </sp:TransportToken>
                      <sp:AlgorithmSuite>
                          <wsp:Policy>
                              <sp:Basic256 />
                          </wsp:Policy>
                      </sp:AlgorithmSuite>
                      <sp:Layout>
                          <wsp:Policy>
                              <sp:Strict />
                          </wsp:Policy>
                      </sp:Layout>
                      <sp:IncludeTimestamp />
                  </wsp:Policy>
              </sp:TransportBinding>
      </wsp:ExactlyOne>
    </wsp:Policy>

    <wsdl:types>
        <xsd:schema targetNamespace="https://Example.org" elementFormDefault="qualified" >
            <xsd:element name="Add">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="a" type="xsd:int" />
                        <xsd:element minOccurs="0" name="b" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="AddResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="result" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="Subtract">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="a" type="xsd:int" />
                        <xsd:element minOccurs="0" name="b" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
            <xsd:element name="SubtractResponse">
                <xsd:complexType>
                    <xsd:sequence>
                        <xsd:element minOccurs="0" name="result" type="xsd:int" />
                    </xsd:sequence>
                </xsd:complexType>
            </xsd:element>
        </xsd:schema>
    </wsdl:types>
    <wsdl:message name="ICalculator_Add_InputMessage">
        <wsdl:part name="parameters" element="tns:Add" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Add_OutputMessage">
        <wsdl:part name="parameters" element="tns:AddResponse" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Subtract_InputMessage">
        <wsdl:part name="parameters" element="tns:Subtract" />
    </wsdl:message>
    <wsdl:message name="ICalculator_Subtract_OutputMessage">
        <wsdl:part name="parameters" element="tns:SubtractResponse" />
    </wsdl:message>
    <wsdl:portType name="ICalculator">
        <wsdl:operation name="Add">
            <wsdl:input wsaw:Action="https://Example.org/ICalculator/Add" message="tns:ICalculator_Add_InputMessage" />
            <wsdl:output wsaw:Action="https://Example.org/ICalculator/AddResponse" message="tns:ICalculator_Add_OutputMessage" />
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <wsdl:input wsaw:Action="https://Example.org/ICalculator/Subtract" message="tns:ICalculator_Subtract_InputMessage" />
            <wsdl:output wsaw:Action="https://Example.org/ICalculator/SubtractResponse" message="tns:ICalculator_Subtract_OutputMessage" />
        </wsdl:operation>
    </wsdl:portType>
    <wsdl:binding name="DefaultBinding_ICalculator" type="tns:ICalculator">
        <soap:binding transport="https://schemas.xmlsoap.org/soap/http" />
        <wsp:PolicyReference URI="#policy1" />
        <wsdl:operation name="Add">
            <soap:operation soapAction="https://Example.org/ICalculator/Add" style="document" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
        <wsdl:operation name="Subtract">
            <soap:operation soapAction="https://Example.org/ICalculator/Subtract" style="document" />
            <wsdl:input>
                <soap:body use="literal" />
            </wsdl:input>
            <wsdl:output>
                <soap:body use="literal" />
            </wsdl:output>
        </wsdl:operation>
    </wsdl:binding>
    <wsdl:service name="CalculatorService">
        <wsdl:port name="ICalculator" binding="tns:DefaultBinding_ICalculator">
            <soap:address location="https://Example.org/ICalculator" />
        </wsdl:port>
    </wsdl:service>

</wsdl:definitions>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpCalculatorWithSslPolicyClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorServiceWithPolicy.wsdl.c: CalculatorServiceWithPolicy.wsdl
     Wsutil.exe /wsdl:CalculatorServiceWithPolicy.wsdl:https://Example.org /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorServiceWithPolicy.wsdl.obj: $(OUTDIR)\CalculatorServiceWithPolicy.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorServiceWithPolicy.wsdl.c

$(OUTDIR)\HttpCalculatorWithSslPolicyClient.obj: HttpCalculatorWithSslPolicyClient.cpp $(OUTDIR)\CalculatorServiceWithPolicy.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpCalculatorWithSslPolicyClient.cpp

$(OUTDIR)\WsHttpCalculatorWithSslPolicyClient.exe: $(OUTDIR)\HttpCalculatorWithSslPolicyClient.obj $(OUTDIR)\CalculatorServiceWithPolicy.wsdl.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpCalculatorWithSslPolicyClient.exe $(OUTDIR)\HttpCalculatorWithSslPolicyClient.obj $(OUTDIR)\CalculatorServiceWithPolicy.wsdl.obj /PDB:$(OUTDIR)\WsHttpCalculatorWithSslPolicyClient.PDB

clean:
    $(CLEANUP)
```

 

 





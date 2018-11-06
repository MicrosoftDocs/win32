---
title: WcfPublicServiceSample
description: This examples shows service proxy talking to http //131.107.72.15/Example\_HelloWorld\_Service\_Indigo/HelloWorld.svc wsdl.
ms.assetid: 755e645e-b39c-471c-9220-531dec4fc107
keywords:
- WcfPublicServiceSample Windows Web Services API
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# WcfPublicServiceSample

This examples shows service proxy talking to http://131.107.72.15/Example\_HelloWorld\_Service\_Indigo/HelloWorld.svc?wsdl.

-   [WcfPublicServiceClient.cpp](#wcfpublicserviceclientcpp)
-   [schemas.microsoft.com.2003.10.Serialization.xsd](#schemasmicrosoftcom200310serializationxsd)
-   [tempuri.org.xsd](#tempuriorgxsd)
-   [tempuri.org.wsdl](#tempuriorgwsdl)
-   [Makefile](#makefile)

## WcfPublicServiceClient.cpp


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
#include "schemas.microsoft.com.2003.10.Serialization.xsd.h"
#include "tempuri.org.xsd.h"
#include "tempuri.org.wsdl.h"

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
    WS_SERVICE_PROXY* proxy = NULL;
    WS_HEAP* heap = NULL;
    WS_CHANNEL_PROPERTY channelProperties[2];
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING serviceUrl = WS_STRING_VALUE(L"http://131.107.72.15/Example_HelloWorld_Service_Indigo/HelloWorld.svc");
    WCHAR* greeting = NULL;
    
    WS_ADDRESSING_VERSION addressingVersion = WS_ADDRESSING_VERSION_TRANSPORT;
    channelProperties[0].id = WS_CHANNEL_PROPERTY_ADDRESSING_VERSION;
    channelProperties[0].value = &addressingVersion;
    channelProperties[0].valueSize = sizeof(addressingVersion);
    
    WS_ENVELOPE_VERSION envelopeVersion = WS_ENVELOPE_VERSION_SOAP_1_1;
    channelProperties[1].id = WS_CHANNEL_PROPERTY_ENVELOPE_VERSION;
    channelProperties[1].value = &envelopeVersion;
    channelProperties[1].valueSize = sizeof(envelopeVersion);
    
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
    
    hr = WsCreateServiceProxy(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, 
        NULL, 
        NULL, 
        0, 
        channelProperties,
        WsCountOf(channelProperties),
        &proxy, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    address.url = serviceUrl;
    // Open channel to address
    hr = WsOpenServiceProxy(
        proxy, 
        &address, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = BasicHttpBinding_IHelloWorldService_PersonalizedGreeting(
        proxy,
        L"Native Web Services",
        &greeting,
        heap,
        NULL,
        0,
        NULL,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    wprintf(L"%s\n", 
        greeting);
    
Exit:
    if (FAILED(hr))
    {
        // Print out the error
        PrintError(hr, error);
    }
    fflush(
        stdout);
    if (proxy != NULL)
    {
        WsCloseServiceProxy(
            proxy, 
            NULL, 
            NULL);
    
        WsFreeServiceProxy(
            proxy);
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



## schemas.microsoft.com.2003.10.Serialization.xsd

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:tns="http://schemas.microsoft.com/2003/10/Serialization/" attributeFormDefault="qualified" elementFormDefault="qualified" targetNamespace="http://schemas.microsoft.com/2003/10/Serialization/" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="anyType" nillable="true" type="xs:anyType" />
  <xs:element name="anyURI" nillable="true" type="xs:anyURI" />
  <xs:element name="base64Binary" nillable="true" type="xs:base64Binary" />
  <xs:element name="boolean" nillable="true" type="xs:boolean" />
  <xs:element name="byte" nillable="true" type="xs:byte" />
  <xs:element name="dateTime" nillable="true" type="xs:dateTime" />
  <xs:element name="decimal" nillable="true" type="xs:decimal" />
  <xs:element name="double" nillable="true" type="xs:double" />
  <xs:element name="float" nillable="true" type="xs:float" />
  <xs:element name="int" nillable="true" type="xs:int" />
  <xs:element name="long" nillable="true" type="xs:long" />
  <xs:element name="QName" nillable="true" type="xs:QName" />
  <xs:element name="short" nillable="true" type="xs:short" />
  <xs:element name="string" nillable="true" type="xs:string" />
  <xs:element name="unsignedByte" nillable="true" type="xs:unsignedByte" />
  <xs:element name="unsignedInt" nillable="true" type="xs:unsignedInt" />
  <xs:element name="unsignedLong" nillable="true" type="xs:unsignedLong" />
  <xs:element name="unsignedShort" nillable="true" type="xs:unsignedShort" />
  <xs:element name="char" nillable="true" type="tns:char" />
  <xs:simpleType name="char">
    <xs:restriction base="xs:int" />
  </xs:simpleType>
  <xs:element name="duration" nillable="true" type="tns:duration" />
  <xs:simpleType name="duration">
    <xs:restriction base="xs:duration">
      <xs:pattern value="\-?P(\d*D)?(T(\d*H)?(\d*M)?(\d*(\.\d*)?S)?)?" />
      <xs:minInclusive value="-P10675199DT2H48M5.4775808S" />
      <xs:maxInclusive value="P10675199DT2H48M5.4775807S" />
    </xs:restriction>
  </xs:simpleType>
  <xs:element name="guid" nillable="true" type="tns:guid" />
  <xs:simpleType name="guid">
    <xs:restriction base="xs:string">
      <xs:pattern value="[\da-fA-F]{8}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{4}-[\da-fA-F]{12}" />
    </xs:restriction>
  </xs:simpleType>
  <xs:attribute name="FactoryType" type="xs:QName" />
</xs:schema>
```

## tempuri.org.xsd

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:tns="http://tempuri.org/" elementFormDefault="qualified" targetNamespace="http://tempuri.org/" xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:element name="Greeting">
    <xs:complexType>
      <xs:sequence />
    </xs:complexType>
  </xs:element>
  <xs:element name="GreetingResponse">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" name="GreetingResult" nillable="true" type="xs:string" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="PersonalizedGreeting">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" name="name" nillable="true" type="xs:string" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
  <xs:element name="PersonalizedGreetingResponse">
    <xs:complexType>
      <xs:sequence>
        <xs:element minOccurs="0" name="PersonalizedGreetingResult" nillable="true" type="xs:string" />
      </xs:sequence>
    </xs:complexType>
  </xs:element>
</xs:schema>
```

## tempuri.org.wsdl

``` syntax
<?xml version="1.0" encoding="utf-8"?>
<wsdl:definitions xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd" xmlns:wsa="http://schemas.xmlsoap.org/ws/2004/08/addressing" xmlns:wsap="http://schemas.xmlsoap.org/ws/2004/08/addressing/policy" xmlns:wsp="http://schemas.xmlsoap.org/ws/2004/09/policy" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:msc="http://schemas.microsoft.com/ws/2005/12/wsdl/contract" xmlns:tns="http://tempuri.org/" xmlns:wsaw="http://www.w3.org/2006/05/addressing/wsdl" xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:wsa10="http://www.w3.org/2005/08/addressing" xmlns:wsx="http://schemas.xmlsoap.org/ws/2004/09/mex" xmlns:wsam="http://www.w3.org/2007/05/addressing/metadata" name="HelloWorldService" targetNamespace="http://tempuri.org/" xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/">
  <wsdl:types>
    <xsd:schema targetNamespace="http://tempuri.org/Imports">
      <xsd:import schemaLocation="http://131.107.72.15/Example_HelloWorld_Service_Indigo/HelloWorld.svc?xsd=xsd0" namespace="http://tempuri.org/" />
      <xsd:import schemaLocation="http://131.107.72.15/Example_HelloWorld_Service_Indigo/HelloWorld.svc?xsd=xsd1" namespace="http://schemas.microsoft.com/2003/10/Serialization/" />
    </xsd:schema>
  </wsdl:types>
  <wsdl:message name="IHelloWorldService_Greeting_InputMessage">
    <wsdl:part name="parameters" element="tns:Greeting" />
  </wsdl:message>
  <wsdl:message name="IHelloWorldService_Greeting_OutputMessage">
    <wsdl:part name="parameters" element="tns:GreetingResponse" />
  </wsdl:message>
  <wsdl:message name="IHelloWorldService_PersonalizedGreeting_InputMessage">
    <wsdl:part name="parameters" element="tns:PersonalizedGreeting" />
  </wsdl:message>
  <wsdl:message name="IHelloWorldService_PersonalizedGreeting_OutputMessage">
    <wsdl:part name="parameters" element="tns:PersonalizedGreetingResponse" />
  </wsdl:message>
  <wsdl:portType name="IHelloWorldService">
    <wsdl:operation name="Greeting">
      <wsdl:input wsaw:Action="http://tempuri.org/IHelloWorldService/Greeting" message="tns:IHelloWorldService_Greeting_InputMessage" />
      <wsdl:output wsaw:Action="http://tempuri.org/IHelloWorldService/GreetingResponse" message="tns:IHelloWorldService_Greeting_OutputMessage" />
    </wsdl:operation>
    <wsdl:operation name="PersonalizedGreeting">
      <wsdl:input wsaw:Action="http://tempuri.org/IHelloWorldService/PersonalizedGreeting" message="tns:IHelloWorldService_PersonalizedGreeting_InputMessage" />
      <wsdl:output wsaw:Action="http://tempuri.org/IHelloWorldService/PersonalizedGreetingResponse" message="tns:IHelloWorldService_PersonalizedGreeting_OutputMessage" />
    </wsdl:operation>
  </wsdl:portType>
  <wsdl:binding name="BasicHttpBinding_IHelloWorldService" type="tns:IHelloWorldService">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http" />
    <wsdl:operation name="Greeting">
      <soap:operation soapAction="http://tempuri.org/IHelloWorldService/Greeting" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
    <wsdl:operation name="PersonalizedGreeting">
      <soap:operation soapAction="http://tempuri.org/IHelloWorldService/PersonalizedGreeting" style="document" />
      <wsdl:input>
        <soap:body use="literal" />
      </wsdl:input>
      <wsdl:output>
        <soap:body use="literal" />
      </wsdl:output>
    </wsdl:operation>
  </wsdl:binding>
  <wsdl:service name="HelloWorldService">
    <wsdl:port name="BasicHttpBinding_IHelloWorldService" binding="tns:BasicHttpBinding_IHelloWorldService">
      <soap:address location="http://131.107.72.15/Example_HelloWorld_Service_Indigo/HelloWorld.svc" />
    </wsdl:port>
  </wsdl:service>
</wsdl:definitions>
```

## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib

all: $(OUTDIR) $(OUTDIR)\WsWcfPublicServiceClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\tempuri.org.wsdl.c $(OUTDIR)\tempuri.org.xsd.c $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.c: tempuri.org.wsdl tempuri.org.xsd schemas.microsoft.com.2003.10.Serialization.xsd
     Wsutil.exe /wsdl:tempuri.org.wsdl /xsd:tempuri.org.xsd schemas.microsoft.com.2003.10.Serialization.xsd /out:$(OUTDIR)
    
$(OUTDIR)\tempuri.org.wsdl.obj: $(OUTDIR)\tempuri.org.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\tempuri.org.wsdl.c

$(OUTDIR)\tempuri.org.xsd.obj: $(OUTDIR)\tempuri.org.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\tempuri.org.xsd.c

$(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.obj: $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.c

$(OUTDIR)\WcfPublicServiceClient.obj: WcfPublicServiceClient.cpp $(OUTDIR)\tempuri.org.wsdl.c $(OUTDIR)\tempuri.org.xsd.c $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" WcfPublicServiceClient.cpp

$(OUTDIR)\WsWcfPublicServiceClient.exe: $(OUTDIR)\WcfPublicServiceClient.obj $(OUTDIR)\tempuri.org.wsdl.obj $(OUTDIR)\tempuri.org.xsd.obj $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsWcfPublicServiceClient.exe $(OUTDIR)\WcfPublicServiceClient.obj $(OUTDIR)\tempuri.org.wsdl.obj $(OUTDIR)\tempuri.org.xsd.obj $(OUTDIR)\schemas.microsoft.com.2003.10.Serialization.xsd.obj /PDB:$(OUTDIR)\WsWcfPublicServiceClient.PDB

clean:
    $(CLEANUP)


```

 

 





---
title: HttpCalculatorWithLayeredChannelClientExample
description: This example show how to use the service proxy to talk to an HTTP based calculator service using a custom channel. The custom channel is a layered channel which simply delegates all functionality to the existing HTTP channel.
ms.assetid: 897673df-f3a3-4b38-8b79-c9f1119be6d5
keywords:
- HttpCalculatorWithLayeredChannelClientExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# HttpCalculatorWithLayeredChannelClientExample

This example show how to use the service proxy to talk to an HTTP based calculator service using a custom channel. The custom channel is a layered channel which simply delegates all functionality to the existing HTTP channel.

-   [HttpCalculatorWithLayeredChannelClient.cpp](#httpcalculatorwithlayeredchannelclientcpp)
-   [CalculatorService.wsdl](#calculatorservicewsdl)
-   [LayeredChannel.h](#layeredchannelh)
-   [LayeredChannel.cpp](#layeredchannelcpp)
-   [Makefile](#makefile)

## HttpCalculatorWithLayeredChannelClient.cpp


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
#include "LayeredChannel.h"
#include "CalculatorService.wsdl.h"

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
    WS_SERVICE_PROXY* proxy = NULL;
    
    int result = 0;
    WS_ENDPOINT_ADDRESS address = {};
    WS_STRING url= WS_STRING_VALUE(L"https://localhost/example");
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
    
    // In order to use the custom channel through Service Model,
    // we need to configure it to disable all timeouts.
    WS_CHANNEL_PROPERTY channelPropertyArray[1];
    BOOL enableTimeouts = FALSE;
    channelPropertyArray[0].id = WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS;
    channelPropertyArray[0].value = &enableTimeouts;
    channelPropertyArray[0].valueSize = sizeof(enableTimeouts);
    
    // Set up channel properties for the custom channel
    WS_CHANNEL_PROPERTY customChannelPropertyArray[2];
    
    // Set up channel property that specifies the callbacks that implement the custom channel
    customChannelPropertyArray[0].id = WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_CALLBACKS;
    customChannelPropertyArray[0].value = &layeredChannelCallbacks;
    customChannelPropertyArray[0].valueSize = sizeof(layeredChannelCallbacks);
    
    // Initialize parameters to pass to the layered channel.
    // Note that the parameters structure and it's contents must 
    // remain valid until the proxy object has been freed.  In this 
    // example, the parameters are declared on the stack for
    // simplicity, but in other scenarios they may need to be
    // allocated from the heap.
    LayeredChannelParameters layeredChannelParameters;
    layeredChannelParameters.channelBinding = WS_HTTP_CHANNEL_BINDING;
    layeredChannelParameters.channelProperties = channelPropertyArray;
    layeredChannelParameters.channelPropertyCount = WsCountOf(channelPropertyArray);
    layeredChannelParameters.securityDescription = NULL;
    
    // Specify the channel parameters as a channel property
    customChannelPropertyArray[1].id = WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS;
    customChannelPropertyArray[1].value = &layeredChannelParameters;
    customChannelPropertyArray[1].valueSize = sizeof(layeredChannelParameters);
    
    
    // Create the proxy
    hr = WsCreateServiceProxy(
        WS_CHANNEL_TYPE_REQUEST, 
        WS_CUSTOM_CHANNEL_BINDING, 
        NULL, 
        NULL, 
        0, 
        customChannelPropertyArray,
        WsCountOf(customChannelPropertyArray),
        &proxy, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    
    
    hr = WsOpenServiceProxy(
        proxy, 
        &address, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = DefaultBinding_ICalculator_Add(
        proxy, 
        1, 
        2, 
        &result, 
        heap, 
        NULL, 
        0, 
        NULL, 
        error);
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



## CalculatorService.wsdl

``` syntax
<wsdl:definitions 
    xmlns:soap="https://schemas.xmlsoap.org/wsdl/soap/" 
    xmlns:tns="https://Example.org" 
    xmlns:xsd="https://www.w3.org/2001/XMLSchema" 
    xmlns:wsaw="https://www.w3.org/2006/05/addressing/wsdl" 
    xmlns:soap12="https://schemas.xmlsoap.org/wsdl/soap12/" 
    targetNamespace="https://Example.org" 
    xmlns:wsdl="https://schemas.xmlsoap.org/wsdl/">
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

## LayeredChannel.h


```C++
// A structure containing parameters passed to the custom channel 
// using WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS.
struct LayeredChannelParameters
{
    // The type of the underlying channel
    WS_CHANNEL_BINDING channelBinding;

    // Channel properties to pass to the underlying channel
    WS_CHANNEL_PROPERTY* channelProperties;
    ULONG channelPropertyCount;

    // Security settings for the underlying channel
    WS_SECURITY_DESCRIPTION* securityDescription;
};

// The structure containing instance state for the custom channel
struct CustomChannel
{
    // Underlying channel handle
    WS_CHANNEL* channel;
    BOOL disabledTimeouts;
};

// The set of callbacks that make up the custom channel implementation.
extern WS_CUSTOM_CHANNEL_CALLBACKS layeredChannelCallbacks;
```



## LayeredChannel.cpp


```C++
#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include "WebServices.h"
#include "process.h"
#include <stdio.h>
#include "string.h"
#include "LayeredChannel.h"

HRESULT CustomCreateChannel(
    __in WS_CHANNEL_TYPE channelType, 
    __in_bcount(channelParametersSize) const void* channelParameters, 
    __in ULONG channelParametersSize, 
    __deref_out void** channelInstance, 
    __in_opt WS_ERROR* error)
{
    HRESULT hr;
    CustomChannel* customChannel = NULL;

    // Get the parameters passed via WS_CHANNEL_PROPERTY_CUSTOM_CHANNEL_PARAMETERS
    if (channelParametersSize != sizeof(LayeredChannelParameters))
    {
        return E_INVALIDARG;
    }
    LayeredChannelParameters* layeredChannelParameters = (LayeredChannelParameters*)channelParameters;

    // Allocate the custom channel instance
    customChannel = (CustomChannel*)HeapAlloc(GetProcessHeap(), 0, sizeof(CustomChannel));
    if (customChannel == NULL)
    {
        hr = E_OUTOFMEMORY;
        goto Exit;
    }

    // Create the underlying channel using the passed in parameters
    hr = WsCreateChannel(
        channelType,
        layeredChannelParameters->channelBinding,
        layeredChannelParameters->channelProperties,
        layeredChannelParameters->channelPropertyCount,
        layeredChannelParameters->securityDescription,
        &customChannel->channel,
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }

    // we need to keep track of whether timeouts were disabled to be able to serve
    // the WsGetChannelProperty calls later on.
    for (ULONG i = 0; i < layeredChannelParameters->channelPropertyCount; i ++)
    {
        if (WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS == layeredChannelParameters->channelProperties[i].id)
        {
            customChannel->disabledTimeouts = *(BOOL*)layeredChannelParameters->channelProperties[i].value;
            break;
        }
    }

    // Return the channel instance.  The instance
    // will be freed by the CustomFreeChannel function.
    *channelInstance = customChannel;
    customChannel = NULL;
    hr = NOERROR;

Exit:
    if (customChannel != NULL)
    {
        HeapFree(GetProcessHeap(), 0, customChannel);
    }

    return hr;  
}

void CustomFreeChannel(
    __in void* channelInstance)
{
    CustomChannel* customChannel = (CustomChannel*)channelInstance;

    // Free the underlying channel
    WsFreeChannel(customChannel->channel);

    // Free the instance that was allocated by CustomCreateChannel
    HeapFree(GetProcessHeap(), 0, channelInstance);
}

HRESULT CustomResetChannel(
    __in void* channelInstance, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsResetChannel(customChannel->channel, error);
}

HRESULT CustomAbortChannel(
    __in void* channelInstance, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsAbortChannel(customChannel->channel, error);
}

HRESULT CustomOpenChannel(
    __in void* channelInstance, 
    __in const WS_ENDPOINT_ADDRESS* endpointAddress, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsOpenChannel(customChannel->channel, endpointAddress, asyncContext, error);
}

HRESULT CustomCloseChannel(
    __in void* channelInstance, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsCloseChannel(customChannel->channel, asyncContext, error);
}

HRESULT CustomSetChannelProperty(
    __in void* channelInstance, 
    __in WS_CHANNEL_PROPERTY_ID id, 
    __in_bcount(valueSize) const void* value, 
    __in ULONG valueSize, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsSetChannelProperty(customChannel->channel, id, value, valueSize, error);
}

HRESULT CustomGetChannelProperty(
    __in void* channelInstance, 
    __in WS_CHANNEL_PROPERTY_ID id, 
    __out_bcount(valueSize) void* value, 
    __in ULONG valueSize, 
    __in_opt WS_ERROR* error)
{
    CustomChannel* customChannel = (CustomChannel*)channelInstance;

    // Underlying channels do not support querying WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS.
    // Custom channel keeps track of whether timeouts were disabled and returns here.
    // Service Model queries this property to ensure the timeouts were disabled in the custom channel.
    if (WS_CHANNEL_PROPERTY_ENABLE_TIMEOUTS == id)
    {
        if (sizeof(BOOL) != valueSize)
        {
            return E_INVALIDARG;
        }

        *(BOOL*)value = customChannel->disabledTimeouts;

        return NOERROR;
    }

    // Delegate the rest of the property queries to the underlying channel
    return WsGetChannelProperty(customChannel->channel, id, value, valueSize, error);
}

HRESULT CustomReadMessageStart(
    __in void* channelInstance, 
    __in WS_MESSAGE* message, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsReadMessageStart(customChannel->channel, message, asyncContext, error);
}

HRESULT CustomReadMessageEnd(
    __in void* channelInstance, 
    __in WS_MESSAGE* message, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsReadMessageEnd(customChannel->channel, message, asyncContext, error);
}

HRESULT CustomWriteMessageStart(
    __in void* channelInstance, 
    __in WS_MESSAGE* message, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsWriteMessageStart(customChannel->channel, message, asyncContext, error);
}

HRESULT CustomWriteMessageEnd(
    __in void* channelInstance, 
    __in WS_MESSAGE* message, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsWriteMessageEnd(customChannel->channel, message, asyncContext, error);
}

HRESULT CustomAbandonMessage(
    __in void* channelInstance, 
    __in WS_MESSAGE* message, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsAbandonMessage(customChannel->channel, message, error);
}

HRESULT CustomShutdownSessionChannel(
    __in void* channelInstance, 
    __in_opt const WS_ASYNC_CONTEXT* asyncContext, 
    __in_opt WS_ERROR* error)
{
    // Delegate to the underlying channel
    CustomChannel* customChannel = (CustomChannel*)channelInstance;
    return WsShutdownSessionChannel(customChannel->channel, asyncContext, error);
}

// Initialize the callbacks that will implement the custom channel
WS_CUSTOM_CHANNEL_CALLBACKS layeredChannelCallbacks =
{
    (WS_CREATE_CHANNEL_CALLBACK)&CustomCreateChannel, 
    (WS_FREE_CHANNEL_CALLBACK)&CustomFreeChannel, 
    (WS_RESET_CHANNEL_CALLBACK)&CustomResetChannel, 
    (WS_OPEN_CHANNEL_CALLBACK)&CustomOpenChannel, 
    (WS_CLOSE_CHANNEL_CALLBACK)&CustomCloseChannel, 
    (WS_ABORT_CHANNEL_CALLBACK)&CustomAbortChannel, 
    (WS_GET_CHANNEL_PROPERTY_CALLBACK)&CustomGetChannelProperty, 
    (WS_SET_CHANNEL_PROPERTY_CALLBACK)&CustomSetChannelProperty, 
    (WS_WRITE_MESSAGE_START_CALLBACK)&CustomWriteMessageStart, 
    (WS_WRITE_MESSAGE_END_CALLBACK)&CustomWriteMessageEnd, 
    (WS_READ_MESSAGE_START_CALLBACK)&CustomReadMessageStart, 
    (WS_READ_MESSAGE_END_CALLBACK)&CustomReadMessageEnd, 
    (WS_ABANDON_MESSAGE_CALLBACK)&CustomAbandonMessage, 
    (WS_SHUTDOWN_SESSION_CHANNEL_CALLBACK)&CustomShutdownSessionChannel,
};
```



## Makefile

``` syntax
!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib

all: $(OUTDIR) $(OUTDIR)\WsHttpCalculatorWithLayeredChannelClient.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\CalculatorService.wsdl.c: CalculatorService.wsdl
     Wsutil.exe /wsdl:CalculatorService.wsdl /string:WS_STRING /out:$(OUTDIR)
    
$(OUTDIR)\CalculatorService.wsdl.obj: $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" $(OUTDIR)\CalculatorService.wsdl.c

$(OUTDIR)\HttpCalculatorWithLayeredChannelClient.obj: HttpCalculatorWithLayeredChannelClient.cpp $(OUTDIR)\CalculatorService.wsdl.c
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" HttpCalculatorWithLayeredChannelClient.cpp

$(OUTDIR)\LayeredChannel.obj: LayeredChannel.cpp
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" LayeredChannel.cpp

$(OUTDIR)\WsHttpCalculatorWithLayeredChannelClient.exe: $(OUTDIR)\HttpCalculatorWithLayeredChannelClient.obj $(OUTDIR)\CalculatorService.wsdl.obj $(OUTDIR)\LayeredChannel.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsHttpCalculatorWithLayeredChannelClient.exe $(OUTDIR)\HttpCalculatorWithLayeredChannelClient.obj $(OUTDIR)\CalculatorService.wsdl.obj $(OUTDIR)\LayeredChannel.obj /PDB:$(OUTDIR)\WsHttpCalculatorWithLayeredChannelClient.PDB

clean:
    $(CLEANUP)


```

 

 





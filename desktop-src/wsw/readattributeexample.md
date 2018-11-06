---
title: ReadAttributeExample
description: This example reads an attribute.
ms.assetid: e37946f0-66e0-4fb1-aeee-db4447ed4030
keywords:
- ReadAttributeExample Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# ReadAttributeExample

This example reads an attribute.

## ReadAttribute.cpp


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

#pragma comment(lib, "WebServices.lib")

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


WS_XML_STRING orders = WS_XML_STRING_VALUE("Orders");
WS_XML_STRING purchaseOrder = WS_XML_STRING_VALUE("PurchaseOrder");
WS_XML_STRING id = WS_XML_STRING_VALUE("id");
WS_XML_STRING nameSpace = WS_XML_STRING_VALUE("http://example.com");
WS_XML_STRING emptyNamespace = WS_XML_STRING_VALUE("");

char* xml = 
"<Orders xmlns='http://example.com'>"
    "<PurchaseOrder id='1001'>"
    "</PurchaseOrder>"
    "<PurchaseOrder id='1002'>"
    "</PurchaseOrder>"
    "<PurchaseOrder id='1003'>"
    "</PurchaseOrder>"
"</Orders>";

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_XML_READER* xmlReader = NULL;
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(
        NULL,
        0, 
        &xmlReader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Setup the source input
    WS_XML_READER_BUFFER_INPUT bufferInput;
    ZeroMemory(&bufferInput, sizeof(bufferInput));
    bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    bufferInput.encodedData = (BYTE*)xml;
    bufferInput.encodedDataSize = (ULONG)strlen(xml);
    
    // Setup the source encoding
    WS_XML_READER_TEXT_ENCODING textEncoding;
    ZeroMemory(&textEncoding, sizeof(textEncoding));
    textEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_TEXT;
    textEncoding.charSet = WS_CHARSET_AUTO;
    
    // Setup the reader
    hr = WsSetInput(xmlReader, &textEncoding.encoding, &bufferInput.input, NULL, 0, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    hr = WsReadToStartElement(xmlReader, &orders, &nameSpace, NULL, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    hr = WsReadStartElement(xmlReader, error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    for (;;)
    {
        BOOL found;
        hr = WsReadToStartElement(xmlReader, &purchaseOrder, &nameSpace, &found, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        if (!found)
        {
            break;
        }
        // The attribute we're looking for is from the empty namespace
        ULONG index;
        hr = WsFindAttribute(xmlReader, &id, &emptyNamespace, TRUE, &index, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        hr = WsReadStartAttribute(xmlReader, index, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        __int32 value;
        hr = WsReadValue(xmlReader, WS_INT32_VALUE_TYPE, &value, sizeof(value), error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        printf("Id='%d'\n", value);
        hr = WsReadEndAttribute(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        hr = WsSkipNode(xmlReader, error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    hr = WsReadEndElement(xmlReader, error);
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
    
    if (xmlReader != NULL)
    {
        WsFreeReader(xmlReader);
    }
    if (error != NULL)
    {
        WsFreeError(error);
    }
    fflush(stdout);
    return SUCCEEDED(hr) ? 0 : -1;
}

```



 

 





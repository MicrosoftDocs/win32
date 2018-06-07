---
title: XmlDictionaryExample
description: This example writes a document using a WS\_XML\_DICTIONARY.
ms.assetid: d8185577-3483-4005-84e5-0b10a6698e79
keywords:
- XmlDictionaryExample Native-Web-Services
- WWSAPI
- WWS
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# XmlDictionaryExample

This example writes a document using a WS\_XML\_DICTIONARY.

-   [XmlDictionary.cpp](#xmldictionarycpp)
-   [Makefile](#makefile)

## XmlDictionary.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

#ifndef UNICODE
#define UNICODE
#endif
#include <windows.h>
#include <stdio.h>
#include <WebServices.h>

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
        hr = WsGetErrorProperty(error, WS_ERROR_PROPERTY_STRING_COUNT, &amp;errorCount, sizeof(errorCount));
        if (FAILED(hr))
        {
            goto Exit;
        }
        for (ULONG i = 0; i < errorCount; i++)
        {
            WS_STRING string;
            hr = WsGetErrorString(error, i, &amp;string);
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

struct ColorDictionary
{
    WS_XML_DICTIONARY dictionary;
    WS_XML_STRING red;
    WS_XML_STRING yellow;
    WS_XML_STRING blue;
    WS_XML_STRING green;
};

ColorDictionary colorDictionary =
{
    { 
        { /* fd7d93f6-a9ec-40a5-a492-8bb45b1e3a5f */
            0xfd7d93f6,
            0xa9ec,
            0x40a5,
            {0xa4, 0x92, 0x8b, 0xb4, 0x5b, 0x1e, 0x3a, 0x5f}
        },
        &amp;colorDictionary.red,
        4, 
        TRUE
    },
    WS_XML_STRING_DICTIONARY_VALUE("red", &amp;colorDictionary.dictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("yellow", &amp;colorDictionary.dictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("blue", &amp;colorDictionary.dictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("green", &amp;colorDictionary.dictionary, 3),
};


struct ShapeDictionary
{
    WS_XML_DICTIONARY dictionary;
    WS_XML_STRING circle;
    WS_XML_STRING square;
    WS_XML_STRING triangle;
};

ShapeDictionary shapeDictionary =
{
    { 
        { /* 4eab536f-d3a9-418c-b6d4-26b2b926eafe */
            0x4eab536f,
            0xd3a9,
            0x418c,
            {0xb6, 0xd4, 0x26, 0xb2, 0xb9, 0x26, 0xea, 0xfe}
        },
        &amp;colorDictionary.red,
        3, 
        TRUE
    },
    WS_XML_STRING_DICTIONARY_VALUE("circle", &amp;shapeDictionary.dictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("square", &amp;shapeDictionary.dictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("triangle", &amp;shapeDictionary.dictionary, 2),
};


struct ObjectsDictionary
{
    WS_XML_DICTIONARY dictionary;
    WS_XML_STRING objects;
    WS_XML_STRING color;
    WS_XML_STRING ns;
};

ObjectsDictionary objectsDictionary =
{
    { 
        { /* 34065de6-b672-417f-96dc-c4436a055bf1 */
            0x34065de6,
            0xb672,
            0x417f,
            {0x96, 0xdc, 0xc4, 0x43, 0x6a, 0x05, 0x5b, 0xf1}
        },
        &amp;objectsDictionary.objects,
        3,
        TRUE
    },
    WS_XML_STRING_DICTIONARY_VALUE("objects", &amp;objectsDictionary.dictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("color", &amp;objectsDictionary.dictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("ns", &amp;objectsDictionary.dictionary, 2),
};


struct MergedDictionary
{
    WS_XML_DICTIONARY dictionary;
    WS_XML_STRING strings[32];
    ULONG stringCount;
};

MergedDictionary mergedDictionary =
{
    { 
        { /* 472007e3-7378-4ac3-846d-bf8c63550a73 */
            0x472007e3,
            0x7378,
            0x4ac3,
            {0x84, 0x6d, 0xbf, 0x8c, 0x63, 0x55, 0x0a, 0x73}
        },
        mergedDictionary.strings,
        0,
        FALSE
    },
};

HRESULT DynamicStringCallback(void* callbackState, const WS_XML_STRING* value, BOOL* found, ULONG* id, WS_ERROR* error)
{
    UNREFERENCED_PARAMETER(callbackState);
    UNREFERENCED_PARAMETER(error);

    // Only merge strings that are const
    if (value->dictionary != NULL &amp;&amp; value->dictionary->isConst)
    {
        // See if we've seen this string before
        for (ULONG i = 0; i < mergedDictionary.dictionary.stringCount; i++)
        {
            if (value->length == mergedDictionary.strings[i].length &amp;&amp;
                memcmp(value->bytes, mergedDictionary.strings[i].bytes, value->length) == 0)
            {
                (*found) = TRUE;
                (*id) = mergedDictionary.strings[i].id;
                return NOERROR;
            }
        }
        if (mergedDictionary.dictionary.stringCount < WsCountOf(mergedDictionary.strings))
        {
            // Add this string to the merged dictionary
            ULONG index = mergedDictionary.dictionary.stringCount;
            mergedDictionary.strings[index].bytes = value->bytes;
            mergedDictionary.strings[index].length = value->length;
            mergedDictionary.strings[index].dictionary = &amp;mergedDictionary.dictionary;
            mergedDictionary.strings[index].id = index;
            mergedDictionary.dictionary.stringCount++;
            (*id) = index;
            (*found) = TRUE;
            return NOERROR;
        }
    }
    (*found) = FALSE;
    return NOERROR;
}

// Main entry point
int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    UNREFERENCED_PARAMETER(argc);
    UNREFERENCED_PARAMETER(argv);
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_XML_WRITER* writer = NULL;
    WS_XML_READER* reader = NULL;
    WS_HEAP* heap = NULL;
    
    // Create an error object for storing rich error information
    hr = WsCreateError(
        NULL, 
        0, 
        &amp;error);
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
        &amp;heap, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML writer
    hr = WsCreateWriter(
        NULL, 
        0, 
        &amp;writer, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Setup the output
    WS_XML_WRITER_BUFFER_OUTPUT bufferOutput;
    ZeroMemory(&amp;bufferOutput, sizeof(bufferOutput));
    bufferOutput.output.outputType = WS_XML_WRITER_OUTPUT_TYPE_BUFFER;
    
    // Setup the encoding
    WS_XML_WRITER_BINARY_ENCODING writerEncoding;
    ZeroMemory(&amp;writerEncoding, sizeof(writerEncoding));
    writerEncoding.encoding.encodingType = WS_XML_WRITER_ENCODING_TYPE_BINARY;
    writerEncoding.staticDictionary = &amp;objectsDictionary.dictionary;
    writerEncoding.dynamicStringCallback = (WS_DYNAMIC_STRING_CALLBACK)DynamicStringCallback;
    writerEncoding.dynamicStringCallbackState = NULL;
    
    // Setup the writer
    hr = WsSetOutput(
        writer, 
        &amp;writerEncoding.encoding, 
        &amp;bufferOutput.output, 
        NULL, 
        0, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsWriteStartElement(
        writer, 
        NULL, 
        &amp;objectsDictionary.objects, 
        &amp;objectsDictionary.ns, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Write some xml using strings from all the dictionaries
    WS_XML_STRING* shapes[3] = { &amp;shapeDictionary.triangle, &amp;shapeDictionary.square, &amp;shapeDictionary.circle };
    WS_XML_STRING* colors[3] = { &amp;colorDictionary.green, &amp;colorDictionary.blue, &amp;colorDictionary.red };
    for (ULONG i = 0; i < 3; i++)
    {
        hr = WsWriteStartElement(
            writer, 
            NULL, 
            shapes[i], 
            &amp;objectsDictionary.ns, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteStartAttribute(
            writer, 
            NULL, 
            &amp;objectsDictionary.color, 
            &amp;objectsDictionary.ns, 
            FALSE, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteType(
            writer, 
            WS_ATTRIBUTE_TYPE_MAPPING, 
            WS_XML_STRING_TYPE, NULL, 
            WS_WRITE_REQUIRED_VALUE, 
            colors[i], 
            sizeof(*colors[i]), 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteEndAttribute(
            writer, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsWriteEndElement(
            writer, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    
    hr = WsWriteEndElement(
        writer, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    WS_BYTES bytes;
    hr = WsGetWriterProperty(
        writer, 
        WS_XML_WRITER_PROPERTY_BYTES, 
        &amp;bytes, 
        sizeof(bytes), 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Create an XML reader
    hr = WsCreateReader(
        NULL,
        0, 
        &amp;reader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    // Setup the input
    WS_XML_READER_BUFFER_INPUT bufferInput;
    ZeroMemory(&amp;bufferInput, sizeof(bufferInput));
    bufferInput.input.inputType = WS_XML_READER_INPUT_TYPE_BUFFER;
    bufferInput.encodedData = bytes.bytes;
    bufferInput.encodedDataSize = bytes.length;
    
    // Setup the encoding
    WS_XML_READER_BINARY_ENCODING readerEncoding;
    ZeroMemory(
        &amp;readerEncoding, 
        sizeof(readerEncoding));
    
    readerEncoding.encoding.encodingType = WS_XML_READER_ENCODING_TYPE_BINARY;
    readerEncoding.staticDictionary = &amp;objectsDictionary.dictionary;
    readerEncoding.dynamicDictionary = &amp;mergedDictionary.dictionary;
    
    // Setup the reader
    hr = WsSetInput(
        reader, 
        &amp;readerEncoding.encoding, 
        &amp;bufferInput.input, 
        NULL, 
        0, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    hr = WsReadToStartElement(
        reader, 
        &amp;objectsDictionary.objects, 
        &amp;objectsDictionary.ns, 
        NULL, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    hr = WsReadStartElement(
        reader, 
        error);
    if (FAILED(hr))
    {
        goto Exit;
    }
    
    for (;;)
    {
        BOOL found;
        hr = WsReadToStartElement(
            reader, 
            NULL, 
            NULL, 
            &amp;found, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        if (!found)
        {
            break;
        }
    
        const WS_XML_NODE* node;
        hr = WsGetReaderNode(
            reader, 
            &amp;node, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        const WS_XML_ELEMENT_NODE* elementNode = (WS_XML_ELEMENT_NODE*)node;
        printf("%.*s: ", elementNode->localName->length, elementNode->localName->bytes);
    
        ULONG index;
        hr = WsFindAttribute(
            reader, 
            &amp;objectsDictionary.color, 
            &amp;objectsDictionary.ns, 
            TRUE, 
            &amp;index, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        hr = WsReadStartAttribute(
            reader, 
            index, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        WS_XML_STRING color;
        hr = WsReadType(
            reader, 
            WS_ATTRIBUTE_TYPE_MAPPING, 
            WS_XML_STRING_TYPE, 
            NULL, 
            WS_READ_REQUIRED_VALUE, 
            heap, 
            &amp;color, 
            sizeof(color), 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    
        printf(
            "%.*s\n", 
            color.length, 
            color.bytes);
    
        hr = WsReadEndAttribute(
            reader, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
        
        hr = WsSkipNode(
            reader, 
            error);
        if (FAILED(hr))
        {
            goto Exit;
        }
    }
    
    hr = WsReadEndElement(
        reader, 
        error);
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
    
    if (writer != NULL)
    {
        WsFreeWriter(writer);
    }
    if (reader != NULL)
    {
        WsFreeReader(reader);
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



## Makefile

``` syntax
#------------------------------------------------------------
# Copyright (C) Microsoft.  All rights reserved.
#------------------------------------------------------------

!include <Win32.Mak>

EXTRA_LIBS = WebServices.lib rpcrt4.lib

all: $(OUTDIR) $(OUTDIR)\WsXmlDictionary.exe

"$(OUTDIR)" :
    if not exist "$(OUTDIR)/$(NULL)" mkdir "$(OUTDIR)"
    
$(OUTDIR)\XmlDictionary.obj: XmlDictionary.cpp
    $(cc) $(cdebug) $(cflags) $(cvarsmt) /WX -I$(OUTDIR) /Fo"$(OUTDIR)\\" /Fd"$(OUTDIR)\\" XmlDictionary.cpp

$(OUTDIR)\WsXmlDictionary.exe: $(OUTDIR)\XmlDictionary.obj
    $(link) $(ldebug) $(conlflags) $(conlibsmt) $(EXTRA_LIBS) -out:$(OUTDIR)\WsXmlDictionary.exe $(OUTDIR)\XmlDictionary.obj /PDB:$(OUTDIR)\WsXmlDictionary.PDB

clean:
    $(CLEANUP)

```

 

 





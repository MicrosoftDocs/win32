---
title: FileRepToolExample
description: This is the command line tool that drives the FileRep service.
ms.assetid: e6273036-2e31-4cbb-b72b-8f4d3ade6336
keywords:
- FileRepToolExample Native-Web-Services
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# FileRepToolExample

This is the command line tool that drives the [FileRep service](filerepserviceexample.md). A more detailed description of this sample can be found there.

The command line parameters are as follows:

WsFileRep.exe \<Client Service Url> \<Server Service Url> \<Source File> \<Destination File> \[/encoding:<binary/text/MTOM>\] \[/sync\]

Client Service Url: Mandatory. Url of the client service.

Server Service Url: Mandatory. Url of the server service.

Source File: Mandatory. Fully qualified local name of the source file. The file is located on the machine where the server service runs.

Destination file: Mandatory. Fully qualified local name of the destination file. The file will be located on the machine where the client service runs.

Encoding: Optional. Specifies the message encoding for the messages sent between the client and server services. The encoding used for the communication between the command line tool and the client service cannot be changed for simplicity reasons. Valid parameters are binary, text and MTOM. If the parameter is not specified the default encoding for transport is used.

Sync: Optional. When set, the request completes synchronously. Otherwise the request will complete asynchronously.

-   [Tool.cpp](#toolcpp)
-   [common.h](#commonh)
-   [Related topics](#related-topics)

## Tool.cpp


```C++
//------------------------------------------------------------
// Copyright (C) Microsoft.  All rights reserved.
//------------------------------------------------------------

// This file contains the code for the command line utility.
#include "common.h"
#include "assert.h"
#include "intsafe.h"

// This function closes the channel if it was openend and then frees it.
void CleanupChannel(WS_CHANNEL* channel)
{
    ULONG state = 0;

    if (NULL == channel)
    {
        return;
    }        
#ifdef DBG
    HRESULT hr = WsGetChannelProperty(channel, WS_CHANNEL_PROPERTY_STATE, &state, sizeof(state), NULL);
    assert(SUCCEEDED(hr));
#else
    (void)WsGetChannelProperty(channel, WS_CHANNEL_PROPERTY_STATE, &state, sizeof(state), NULL);
#endif

        
    if (WS_CHANNEL_STATE_OPEN == state || WS_CHANNEL_STATE_FAULTED == state)
    {
        // CloseChannel will close the channel even if it encouters an error. So ignore the error here
        // as this is called only when we destroy the channel.
        WsCloseChannel(channel, NULL, NULL);
    }

    WsFreeChannel(channel);
}

// Currently we only support 3 modes: TCP, HTTP and HTTP with SSL. Thus, this simple check here is
// enough to figure out the proper configuration. This will not be enough once we have more advanced
// security settings. The wire protocol makes these settings explicit so that it does not have
// to be changed in that case. This is only used for the command line.
// For more advanced parsing, WsDecodeUrl should be used.
HRESULT ParseTransport(__in const LPWSTR url, TRANSPORT_MODE *transport, SECURITY_MODE *securityMode)
{
    if (wcsstr(url, L"http:") == url)
    {
        *transport = HTTP_TRANSPORT;    
        *securityMode = NO_SECURITY;
        return NOERROR;
    }
    else if (wcsstr(url, L"https:") == url)
    {
        *transport = HTTP_TRANSPORT;
        *securityMode = SSL_SECURITY;
        return NOERROR;
    }
    else if (wcsstr(url, L"net.tcp:") == url)
    {
        *transport = TCP_TRANSPORT;
        *securityMode = NO_SECURITY;
        return NOERROR;
    }

    return E_FAIL;
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

HRESULT ParseCommandLine(int argc, __in_ecount(argc) wchar_t **argv, bool* synchronous, MESSAGE_ENCODING* messageEncoding)
{
    *synchronous = false;
    *messageEncoding = DEFAULT_ENCODING;

    for (int i = 0; i < argc; i++)
    {
        WCHAR* arg = argv[i];
        if (!_wcsicmp(arg, L"-sync") || !_wcsicmp(arg, L"/sync"))
        {
            *synchronous = true;
        }
        else if (!_wcsicmp(arg, L"-encoding:binary") || !_wcsicmp(arg, L"/encoding:binary"))
        {
            if (DEFAULT_ENCODING != *messageEncoding)
            {
                wprintf(L"Error: More than one encoding specified.\n");
                return E_FAIL;
            }

            *messageEncoding = BINARY_ENCODING;
        }
        else if (!_wcsicmp(arg, L"-encoding:text") || !_wcsicmp(arg, L"/encoding:text"))
        {
            if (DEFAULT_ENCODING != *messageEncoding)
            {
                wprintf(L"Error: More than one encoding specified.\n");
                return E_FAIL;
            }

            *messageEncoding = TEXT_ENCODING;
        }
        else if (!_wcsicmp(arg, L"-encoding:MTOM") || !_wcsicmp(arg, L"/encoding:MTOM"))
        {
            if (DEFAULT_ENCODING != *messageEncoding)
            {
                wprintf(L"Error: More than one encoding specified.\n");
                return E_FAIL;
            }

            *messageEncoding = MTOM_ENCODING;
        }
        else if (!_wcsnicmp(arg, L"-encoding:", 10) || !_wcsnicmp(arg, L"/encoding:", 10))
        {
            wprintf(L"Error: Illegal encoding specified.\n");
            return E_FAIL;
        }
        else
        {
            wprintf(L"Unrecognized parameter: %s.\n", arg);
            return E_FAIL;
        }
    }

    return NOERROR;
}

int __cdecl wmain(int argc, __in_ecount(argc) wchar_t **argv)
{
    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_CHANNEL* channel = NULL;
    WS_MESSAGE* requestMessage = NULL;
    WS_MESSAGE* replyMessage = NULL;
    WS_HEAP* heap = NULL;

    WS_ENDPOINT_ADDRESS address = {};
    UserRequest userRequest;
    UserResponse *userResponse = NULL;  

    if (argc < 5)
    {
        wprintf(L"Usage:\n FileRep.exe <Client Service Url> <Server Service Url> <Source File> <Destination File>");
        wprintf(L"[/encoding:<binary/text/MTOM>] [/sync]\n");

        return -1;
    }

    // required arguments
    LPWSTR clientURL = argv[1];
    LPWSTR serverURL = argv[2];
    LPWSTR sourcePath = argv[3];
    LPWSTR destinationPath = argv[4];

    // optional arguments
    bool synchronous = FALSE;
    MESSAGE_ENCODING messageEncoding = DEFAULT_ENCODING;
    TRANSPORT_MODE clientTransport = HTTP_TRANSPORT;
    TRANSPORT_MODE serverTransport = TCP_TRANSPORT;
    SECURITY_MODE clientSecurityMode = NO_SECURITY;
    SECURITY_MODE serverSecurityMode = NO_SECURITY;

    if (argc > 5)
    {        
        hr = ParseCommandLine(argc - 5, &argv[5], &synchronous, &messageEncoding);
        if (FAILED(hr))
        {
            return -1;
        }
    }  
        
    if (synchronous)
    {
        wprintf(L"Performing synchronous request.\n");
    }
    else
    {
        wprintf(L"Performing asynchronous request.\n");
    }
    if (DEFAULT_ENCODING == messageEncoding)
    {
        wprintf(L"Using default encoding.\n");
    }
    else if (TEXT_ENCODING == messageEncoding)
    {
        wprintf(L"Using text encoding.\n");
    }
    else if (BINARY_ENCODING == messageEncoding)
    {
        wprintf(L"Using binary encoding.\n");
    }
    else if (MTOM_ENCODING == messageEncoding)
    {
        wprintf(L"Using MTOM encoding.\n");
    }

    if (FAILED(ParseTransport(clientURL, &clientTransport, &clientSecurityMode)))
    {
        wprintf(L"Illegal protocol for communicating with the client service.\n");
        return -1;
    }
    if (HTTP_TRANSPORT != clientTransport)
    {
        // Communication from the command line to the client service is restricted to HTTP
        // for simplicity reasons. The client service can accept any protocol and encoding
        // so the protocol can easily be replaced in code here.
        // The communication from client to server service supports all encodings and protocols
        // and this command line lets you specify all of them.
        wprintf(L"Illegal protocol for communicating with the client service.\n");
        return -1;
    }

    // Currently the requests sent to client service are unsecured. The actual file transfer can be secured.
    if (NO_SECURITY != clientSecurityMode)
    {
        wprintf(L"Illegal security mode for communicating with the client service.\n");
        return -1;
    }

    if (FAILED(ParseTransport(serverURL, &serverTransport, &serverSecurityMode)))
    {
        wprintf(L"Illegal protocol for communication between client and server service.\n");
        return -1;
    }

    if (NO_SECURITY == serverSecurityMode)
    {
        wprintf(L"Using unsecured protocol for communication between client and server service.\n");
    }
    
    // Create an error object for storing rich error information.
    IfFailedExit(WsCreateError(NULL, 0, &error));

    // Transferring a file could take a long time. Thus we use a long timeout of one hour.
    // If the user does not want to wait he or she should use the async mode.
    ULONG timeout = 1000*60*60*24;
    WS_CHANNEL_PROPERTY channelProperty[2];
    channelProperty[0].id = WS_CHANNEL_PROPERTY_RECEIVE_RESPONSE_TIMEOUT;
    channelProperty[0].value = &timeout;
    channelProperty[0].valueSize = sizeof(timeout);

    channelProperty[1].id = WS_CHANNEL_PROPERTY_RECEIVE_TIMEOUT;
    channelProperty[1].value = &timeout;
    channelProperty[1].valueSize = sizeof(timeout);

    IfFailedExit(WsCreateChannel(WS_CHANNEL_TYPE_REQUEST, 
        WS_HTTP_CHANNEL_BINDING, channelProperty, 2, NULL, &channel, error));
    
    IfFailedExit(WsCreateMessageForChannel(channel, NULL, 0, &requestMessage, error));   
    IfFailedExit(WsCreateMessageForChannel(channel, NULL, 0, &replyMessage, error));
   
    // Initialize address of service
    address.url.chars = clientURL;
    IfFailedExit(SizeTToULong(wcslen(address.url.chars), &address.url.length));
    
    IfFailedExit(WsOpenChannel(channel, &address, NULL, error));    

    if (synchronous)
    {
        userRequest.requestType = SYNC_REQUEST;
    }
    else
    {
        userRequest.requestType = ASYNC_REQUEST;
    }

    userRequest.serverUri = serverURL;
    userRequest.serverProtocol = serverTransport;
    userRequest.securityMode = serverSecurityMode;
    userRequest.messageEncoding = messageEncoding;
    userRequest.sourcePath = sourcePath;
    userRequest.destinationPath = destinationPath;

    IfFailedExit(WsCreateHeap(65536, 0, NULL, 0, &heap, NULL));

    WS_MESSAGE_DESCRIPTION userRequestMessageDescription;
    userRequestMessageDescription.action = &userRequestAction;
    userRequestMessageDescription.bodyElementDescription = &userRequestElement;

    WS_MESSAGE_DESCRIPTION userResponseMessageDescription;
    userResponseMessageDescription.action = &userResponseAction;
    userResponseMessageDescription.bodyElementDescription = &userResponseElement;
      
    hr = WsRequestReply(
        channel, 
        requestMessage, 
        &userRequestMessageDescription,
        WS_WRITE_REQUIRED_VALUE,
        &userRequest, 
        sizeof(userRequest), 
        replyMessage, 
        &userResponseMessageDescription, 
        WS_READ_REQUIRED_POINTER, 
        heap, 
        &userResponse, 
        sizeof(userResponse), 
        NULL, 
        error);

    if (WS_E_ENDPOINT_FAULT_RECEIVED == hr)
    {
        // We got a fault.
        WS_FAULT* fault;
        IfFailedExit(WsGetFaultErrorProperty(error, WS_FAULT_ERROR_PROPERTY_FAULT, &fault, sizeof(fault)));
        wprintf(L"The server returned a fault:\n");

        for (ULONG i = 0; i < fault->reasonCount; i++)
        {
            if (fault->reasons[i].text.length < 1024)
            {
                wprintf(L"%.*s\n", fault->reasons[i].text.length, fault->reasons[i].text.chars);
            }
            else
            {
                wprintf(L"Fault reason too long to display.\n");
            }
        }           
    } 
    else if (SUCCEEDED(hr))
    {
        if (TRANSFER_ASYNC == userResponse->returnValue)
        {
            wprintf(L"The request is completing asynchronously.\n");
        }
        else if (TRANSFER_SUCCESS == userResponse->returnValue)
        {
            wprintf(L"The request succeeded.\n");
        }
        else
        {
            wprintf(L"Unexpected return value from server.\n");
        }
    }
        
    EXIT
   
    if (FAILED(hr) && WS_E_ENDPOINT_FAULT_RECEIVED != hr)
    {
        wprintf(L"Unexpected failure:\n");
        PrintError(hr, error);
    }
    
    if (requestMessage != NULL)
    {
        WsFreeMessage(requestMessage);
    }
    if (replyMessage != NULL)
    {
        WsFreeMessage(replyMessage);
    }

    CleanupChannel(channel);

    if (error != NULL)
    {
        WsFreeError(error);
    }

    if (NULL != heap)
    {
        WsFreeHeap(heap);
    }

    return SUCCEEDED(hr) ? 0 : -1;
}
```



## common.h


```C++
//------------------------------------------------------------
// Copyright (c) Microsoft Corporation.  All rights reserved.
//------------------------------------------------------------

// This file contains definitions that are shared among client and server.
#include <windows.h>
#include <WebServices.h>
#include <stdio.h>

#pragma comment(lib, "WebServices.lib")

#define CountOf(a) (sizeof(a) / sizeof(*a))
#define ERROR_EXIT ErrorExit:
#define EXIT ErrorExit:
#define EXIT_FUNCTION goto ErrorExit;

#pragma warning(disable : 4127) // Disable warning for the while (0)
#define IfFailedExit(EXPR1) do { hr = (EXPR1); if (FAILED(hr)) { EXIT_FUNCTION } } while (0)
#define IfNullExit(EXPR1) do { if (NULL == EXPR1) { hr = E_OUTOFMEMORY; EXIT_FUNCTION } } while (0)

//
// defines the request message and all related structures
//
struct FileRequest
{
    LONGLONG filePosition; //Starting position of the requested chunk; -1 indicates request for file info.
    LPWSTR fileName; // Fully qualified local file name on the server machine
};

// It is recommended to use a dictionary when dealing with a collection of XML strings.
#pragma warning(disable : 4211) // Disable warning for changing from extern to static
extern WS_XML_DICTIONARY fileRequestDictionary;

static WS_XML_STRING fileRequestDictionaryStrings[] =
{
    WS_XML_STRING_DICTIONARY_VALUE("FilePosition", &fileRequestDictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("FileName", &fileRequestDictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("FileRequest", &fileRequestDictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("https://tempuri.org/FileRep", &fileRequestDictionary, 3),
    WS_XML_STRING_DICTIONARY_VALUE("FileRequest", &fileRequestDictionary, 4),
};

static WS_XML_DICTIONARY fileRequestDictionary =
{
    { /* 615a0125-2a70-4159-bd28-080480339f04 */
    0x615a0125,
    0x2a70,
    0x4159,
    {0xbd, 0x28, 0x08, 0x04, 0x80, 0x33, 0x9f, 0x04}
    },
    fileRequestDictionaryStrings,
    WsCountOf(fileRequestDictionaryStrings),
    true,
};

#define filePositionLocalName fileRequestDictionaryStrings[0]
#define fileNameLocalName fileRequestDictionaryStrings[1]
#define fileRequestLocalName fileRequestDictionaryStrings[2]
#define fileRequestNamespace fileRequestDictionaryStrings[3]
#define fileRequestTypeName fileRequestDictionaryStrings[4]

static WS_FIELD_DESCRIPTION filePositionField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &filePositionLocalName,
    &fileRequestNamespace,
    WS_INT64_TYPE,
    NULL,
    WsOffsetOf(FileRequest, filePosition),
};

static WS_FIELD_DESCRIPTION fileNameField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &fileNameLocalName,
    &fileRequestNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(FileRequest, fileName),
};

static WS_FIELD_DESCRIPTION* fileRequestFields[] = 
{ 
    &filePositionField,
    &fileNameField,
};

static WS_STRUCT_DESCRIPTION fileRequestType =
{
    sizeof(FileRequest),
    __alignof(FileRequest),
    fileRequestFields,
    WsCountOf(fileRequestFields),
    &fileRequestTypeName,
    &fileRequestNamespace,
};

static WS_ELEMENT_DESCRIPTION fileRequestElement = 
{
    &fileRequestLocalName,
    &fileRequestNamespace,
    WS_STRUCT_TYPE,
    &fileRequestType,
};

//
// defines the file description message and all related structures
//

struct FileInfo
{
    LPWSTR fileName;
    LONGLONG fileLength;
    DWORD chunkSize;    
};

extern WS_XML_DICTIONARY fileInfoDictionary;

static WS_XML_STRING fileInfoDictionaryStrings[] =
{
    WS_XML_STRING_DICTIONARY_VALUE("FileName", &fileInfoDictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("FileLength", &fileInfoDictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("ChunkSize", &fileInfoDictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("FileInfo", &fileInfoDictionary, 3),
    WS_XML_STRING_DICTIONARY_VALUE("https://tempuri.org/FileRep", &fileInfoDictionary, 4),
    WS_XML_STRING_DICTIONARY_VALUE("FileInfo", &fileInfoDictionary, 5),
};

static WS_XML_DICTIONARY fileInfoDictionary =
{
    { /* 22b4b751-eede-4d35-9307-50a2fcba3d4e */
    0x22b4b751,
    0xeede,
    0x4d35,
    {0x93, 0x07, 0x50, 0xa2, 0xfc, 0xba, 0x3d, 0x4e}
    },
    fileInfoDictionaryStrings,
    WsCountOf(fileInfoDictionaryStrings),
    true,
};

#define fileNameInfoLocalName fileInfoDictionaryStrings[0]
#define fileLengthLocalName fileInfoDictionaryStrings[1]
#define chunkSizeLocalName fileInfoDictionaryStrings[2]
#define fileInfoLocalName fileInfoDictionaryStrings[3]
#define fileInfoNamespace fileInfoDictionaryStrings[4]
#define fileInfoElementName fileInfoDictionaryStrings[5]

static WS_FIELD_DESCRIPTION fileNameInfoField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &fileNameInfoLocalName,
    &fileInfoNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(FileInfo, fileName),
};

static WS_FIELD_DESCRIPTION fileLengthField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &fileLengthLocalName,
    &fileInfoNamespace,
    WS_INT64_TYPE,
    NULL,
    WsOffsetOf(FileInfo, fileLength),
};

static WS_FIELD_DESCRIPTION chunkSizeField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &chunkSizeLocalName,
    &fileInfoNamespace,
    WS_UINT32_TYPE,
    NULL,
    WsOffsetOf(FileInfo, chunkSize),
};

static WS_FIELD_DESCRIPTION* fileInfoFields[] = 
{ 
    &fileNameInfoField,
    &fileLengthField,
    &chunkSizeField,
};

static WS_STRUCT_DESCRIPTION fileInfoType =
{
    sizeof(FileInfo),
    __alignof(FileInfo),
    fileInfoFields,
    WsCountOf(fileInfoFields),
    &fileInfoElementName,
    &fileInfoNamespace,
};

static WS_ELEMENT_DESCRIPTION fileInfoElement = 
{
    &fileInfoLocalName,
    &fileInfoNamespace,
    WS_STRUCT_TYPE,
    &fileInfoType,
};


//
// defines the file message and all related structures
//
struct FileChunk
{
    LONGLONG chunkPosition; // Starting position of the transmitted chunk. Must match request. Undefined in error case. 
    
    // Size of the content must match the defined chunk length or be last chunk, 
    // in which case size+chunkPosition must match the length of the file.
    WS_BYTES fileContent;  
    LPWSTR error;  // Contains "https://tempuri.org/FileRep/NoError" in the success case.
};

extern WS_XML_DICTIONARY fileChunkDictionary;

static WS_XML_STRING fileChunkDictionaryStrings[] =
{
    WS_XML_STRING_DICTIONARY_VALUE("ChunkPosition", &fileChunkDictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("FileContent", &fileChunkDictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("Error", &fileChunkDictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("FileChunk", &fileChunkDictionary, 3),
    WS_XML_STRING_DICTIONARY_VALUE("https://tempuri.org/FileRep", &fileChunkDictionary, 4),
    WS_XML_STRING_DICTIONARY_VALUE("FileChunk", &fileChunkDictionary, 5),
};

static WS_XML_DICTIONARY fileChunkDictionary =
{
    { /* e99f3780-7a2a-449a-a40f-bf9f4a5db648 */
    0xe99f3780,
    0x7a2a,
    0x449a,
    {0xa4, 0x0f, 0xbf, 0x9f, 0x4a, 0x5d, 0xb6, 0x48}
    },
    fileChunkDictionaryStrings,
    WsCountOf(fileChunkDictionaryStrings),
    true,
};

#define chunkPositionLocalName fileChunkDictionaryStrings[0]
#define fileContentLocalName fileChunkDictionaryStrings[1]
#define errorLocalName fileChunkDictionaryStrings[2]
#define fileChunkLocalName fileChunkDictionaryStrings[3]
#define fileChunkNamespace fileChunkDictionaryStrings[4]
#define fileChunkElementName fileChunkDictionaryStrings[5]

static WS_FIELD_DESCRIPTION chunkPositionField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &chunkPositionLocalName,
    &fileChunkNamespace,
    WS_INT64_TYPE,
    NULL,
    WsOffsetOf(FileChunk, chunkPosition),
};


static WS_FIELD_DESCRIPTION fileContentField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &fileContentLocalName,
    &fileChunkNamespace,
    WS_BYTES_TYPE,
    NULL,
    WsOffsetOf(FileChunk, fileContent),
};

static WS_FIELD_DESCRIPTION errorField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &errorLocalName,
    &fileChunkNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(FileChunk, error),
};

static WS_FIELD_DESCRIPTION* fileChunkFields[] = 
{ 
    &chunkPositionField,
    &fileContentField,
    &errorField,    
};

static WS_STRUCT_DESCRIPTION fileChunkType =
{
    sizeof(FileChunk),
    __alignof(FileChunk),
    fileChunkFields,
    WsCountOf(fileChunkFields),
    &fileChunkElementName,
    &fileChunkNamespace,
};

static WS_ELEMENT_DESCRIPTION fileChunkElement = 
{
    &fileChunkLocalName,
    &fileChunkNamespace,
    WS_STRUCT_TYPE,
    &fileChunkType,
};

typedef enum
{
    HTTP_TRANSPORT = 1,
    TCP_TRANSPORT = 2,
} TRANSPORT_MODE;

typedef enum
{
    NO_SECURITY = 1,
    SSL_SECURITY = 2,   
} SECURITY_MODE;

typedef enum
{
    BINARY_ENCODING = 1,
    TEXT_ENCODING = 2,
    MTOM_ENCODING = 3,
    DEFAULT_ENCODING = 4,
} MESSAGE_ENCODING;

typedef enum
{
    ASYNC_REQUEST = 1,
    SYNC_REQUEST = 2,   
} REQUEST_TYPE;

//
// defines the user request message and all related structures
//
struct UserRequest
{
    REQUEST_TYPE requestType; // If true the request completes synchronously
    LPWSTR serverUri; // Uri of the server service
    TRANSPORT_MODE serverProtocol;
    SECURITY_MODE securityMode;
    MESSAGE_ENCODING messageEncoding; 
    LPWSTR sourcePath; // Fully qualified local file name of the source file
    LPWSTR destinationPath;// Fully qualified local file name of the destination file
};

extern WS_XML_DICTIONARY userRequestDictionary;

static WS_XML_STRING userRequestDictionaryStrings[] =
{
    WS_XML_STRING_DICTIONARY_VALUE("RequestType", &userRequestDictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("ServerUri", &userRequestDictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("ServerProtocol", &userRequestDictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("SecurityMode", &userRequestDictionary, 3),
    WS_XML_STRING_DICTIONARY_VALUE("MessageEncoding", &userRequestDictionary, 4),
    WS_XML_STRING_DICTIONARY_VALUE("SourcePath", &userRequestDictionary, 5),
    WS_XML_STRING_DICTIONARY_VALUE("DestinationPath", &userRequestDictionary, 6),
    WS_XML_STRING_DICTIONARY_VALUE("UserRequest", &userRequestDictionary, 7),
    WS_XML_STRING_DICTIONARY_VALUE("https://tempuri.org/FileRep", &userRequestDictionary, 8),
    WS_XML_STRING_DICTIONARY_VALUE("UserRequest", &userRequestDictionary, 9),
};

static WS_XML_DICTIONARY userRequestDictionary =
{
    { /* 98e77255-271b-4434-abb6-3ab6d3b5a6a4 */
    0x98e77255,
    0x271b,
    0x4434,
    {0xab, 0xb6, 0x3a, 0xb6, 0xd3, 0xb5, 0xa6, 0xa4}
    },
    userRequestDictionaryStrings,
    WsCountOf(userRequestDictionaryStrings),
    true,
};

#define requestTypeLocalName userRequestDictionaryStrings[0]
#define serverUriLocalName userRequestDictionaryStrings[1]
#define serverProtocolLocalName userRequestDictionaryStrings[2]
#define securityModeLocalName userRequestDictionaryStrings[3]
#define messageEncodingLocalName userRequestDictionaryStrings[4]
#define sourcePathLocalName userRequestDictionaryStrings[5]
#define destinationPathLocalName userRequestDictionaryStrings[6]
#define userRequestLocalName userRequestDictionaryStrings[7]
#define userRequestNamespace userRequestDictionaryStrings[8]
#define userRequestTypeName userRequestDictionaryStrings[9]

static WS_FIELD_DESCRIPTION requestTypeField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &requestTypeLocalName,
    &userRequestNamespace,
    WS_INT32_TYPE,
    NULL,
    WsOffsetOf(UserRequest, requestType),
};

static WS_FIELD_DESCRIPTION serverUriField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &serverUriLocalName,
    &userRequestNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(UserRequest, serverUri),
};

static WS_FIELD_DESCRIPTION serverProtocolField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &serverProtocolLocalName,
    &userRequestNamespace,
    WS_INT32_TYPE,
    NULL,
    WsOffsetOf(UserRequest, serverProtocol),
};

static WS_FIELD_DESCRIPTION securityModeField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &securityModeLocalName,
    &userRequestNamespace,
    WS_INT32_TYPE,
    NULL,
    WsOffsetOf(UserRequest, securityMode),
};

static WS_FIELD_DESCRIPTION messageEncodingField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &messageEncodingLocalName,
    &userRequestNamespace,
    WS_INT32_TYPE,
    NULL,
    WsOffsetOf(UserRequest, messageEncoding),
};

static WS_FIELD_DESCRIPTION sourcePathField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &sourcePathLocalName,
    &userRequestNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(UserRequest, sourcePath),
};

static WS_FIELD_DESCRIPTION destinationPathField = 
{ 
    WS_ELEMENT_FIELD_MAPPING,
    &destinationPathLocalName,
    &userRequestNamespace,
    WS_WSZ_TYPE,
    NULL,
    WsOffsetOf(UserRequest, destinationPath),
};

static WS_FIELD_DESCRIPTION* userRequestFields[] = 
{ 
    &requestTypeField,
    &serverUriField,
    &serverProtocolField,
    &securityModeField,
    &messageEncodingField,
    &sourcePathField,
    &destinationPathField,
};

static WS_STRUCT_DESCRIPTION userRequestType =
{
    sizeof(UserRequest),
    __alignof(UserRequest),
    userRequestFields,
    WsCountOf(userRequestFields),
    &userRequestTypeName,
    &userRequestNamespace,
};

static WS_ELEMENT_DESCRIPTION userRequestElement = 
{
    &userRequestLocalName,
    &userRequestNamespace,
    WS_STRUCT_TYPE,
    &userRequestType,
};


//
// defines the user response message and all related structures
//

typedef enum
{
    TRANSFER_SUCCESS = 1, // Failures are returned as faults.
    TRANSFER_ASYNC = 2, // Request completes asynchronously. Client will not be notified of success or failure.
} TRANSFER_RESULTS;

struct UserResponse
{
    TRANSFER_RESULTS returnValue; 
};

extern WS_XML_DICTIONARY userResponseDictionary;

static WS_XML_STRING userResponseDictionaryStrings[] =
{
    WS_XML_STRING_DICTIONARY_VALUE("ReturnValue", &userResponseDictionary, 0),
    WS_XML_STRING_DICTIONARY_VALUE("UserResponse", &userResponseDictionary, 1),
    WS_XML_STRING_DICTIONARY_VALUE("https://tempuri.org/FileRep", &userResponseDictionary, 2),
    WS_XML_STRING_DICTIONARY_VALUE("UserResponse", &userResponseDictionary, 3),
};

static WS_XML_DICTIONARY userResponseDictionary =
{
    { /* 3c13293c-665f-4586-85eb-954a3279a500 */
    0x3c13293c,
    0x665f,
    0x4586,
    {0x85, 0xeb, 0x95, 0x4a, 0x32, 0x79, 0xa5, 0x00}
    },
    userResponseDictionaryStrings,
    WsCountOf(userResponseDictionaryStrings),
    true,
};

#define returnValueLocalName userResponseDictionaryStrings[0]
#define userResponseLocalName userResponseDictionaryStrings[1]
#define userResponseNamespace userResponseDictionaryStrings[2]
#define userResponseTypeName userResponseDictionaryStrings[3]

static WS_FIELD_DESCRIPTION returnValueField = 
{
    WS_ELEMENT_FIELD_MAPPING,
    &returnValueLocalName,
    &userResponseNamespace,
    WS_INT32_TYPE,
    NULL,
    WsOffsetOf(UserResponse, returnValue),
};


static WS_FIELD_DESCRIPTION* userResponseFields[] = 
{ 
    &returnValueField,
};

static WS_STRUCT_DESCRIPTION userResponseType =
{
    sizeof(UserResponse),
    __alignof(UserResponse),
    userResponseFields,
    WsCountOf(userResponseFields),
    &userResponseTypeName,
    &userResponseNamespace,
};

static WS_ELEMENT_DESCRIPTION userResponseElement = 
{
    &userResponseLocalName,
    &userResponseNamespace,
    WS_STRUCT_TYPE,
    &userResponseType,
};


// Set up the action value for the file request message
static WS_XML_STRING fileRequestAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/filerequest");

// Set up the action value for the reply message
static WS_XML_STRING fileReplyAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/filereply");

// Set up the action value for the info message
static WS_XML_STRING fileInfoAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/fileinfo");


// Set up the action value for the user request message
static WS_XML_STRING userRequestAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/userrequest");

// Set up the action value for the user reply message
static WS_XML_STRING userResponseAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/userresponse");

// Set up the action value for the fault message
static WS_XML_STRING faultAction = WS_XML_STRING_VALUE("https://tempuri.org/FileRep/fault");


// We are allowing very large messages so that the server can chose the optimal
// message size. This could be improved by allowing the client and server to negotiate
// this value but that is beyond the scope of this version of the sample.
#define MAXMESSAGESIZE 536870912 //half gigabyte 
```



## Related topics

<dl> <dt>

[FileRepServiceExample](filerepserviceexample.md)
</dt> </dl>

 

 





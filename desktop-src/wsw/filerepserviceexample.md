---
title: FileRepServiceExample
description: FileRep retrieves files from a server and copies them to a client.
ms.assetid: 9f446999-8f10-4ce4-86eb-e9289e131733
keywords:
- FileRepServiceExample Web Services for Windows
- WWSAPI
- WWS
ms.topic: article
ms.date: 05/31/2018
---

# FileRepServiceExample

FileRep retrieves files from a server and copies them to a client. To do so it employs three components - the server service running on the machine with the source file, the client service running on the machine where the destination file will be stored and a command line tool to control the copying. The client and server services are constantly running web services while the command line tool is started by the user and exits after one request.

This sample illustrates the use of the channel and serialization layer.

This is the service. The command line tool can be found [here](filereptoolexample.md).The service has a client and a server mode, where the server sends files and the client receives files.

The command line parameters for the client mode are as follows:

**WsFileRepService.exe client** *\<Service Url>* **\[/reporting:<error/info/verbose>\] \[/encoding:<text/binary/MTOM>\] \[/connections:***\<number of connections>***\]**

<dl> <dt>

<span id="Client"></span><span id="client"></span><span id="CLIENT"></span>Client
</dt> <dd>

Required. Denotes that the service runs as client.

</dd> <dt>

<span id="Service_Url"></span><span id="service_url"></span><span id="SERVICE_URL"></span>Service Url
</dt> <dd>

Required. Denotes the URL the service listens on.

</dd> <dt>

<span id="Encoding"></span><span id="encoding"></span><span id="ENCODING"></span>Encoding
</dt> <dd>

Optional. Specifies the encoding used when communicating with the command line tool. Note that the current tool does not support specifying an encoding for this transfer, so changing this setting will likely produce an error. The setting is there so that the tool can be changed and extended independently of the server.

</dd> <dt>

<span id="Reporting"></span><span id="reporting"></span><span id="REPORTING"></span>Reporting
</dt> <dd>

Optional. Enables error, information or verbose level reporting. The default is error. Messages are printed to the console.

</dd> <dt>

<span id="Connections"></span><span id="connections"></span><span id="CONNECTIONS"></span>Connections
</dt> <dd>

Optional. Specifies the maximum number of concurrent requests that will be processed. If omitted the default is 100.

</dd> </dl>

The command line parameters for the server mode are as follows:

**WsFileRepService.exe server** *\<Service Url>* **\[/reporting:<error/info/verbose>\] \[/encoding:<text/binary/MTOM>\] \[/connections:***\<number of connections>***\] \[/chunk:***\<size of the payload per message in bytes>***\]**

<dl> <dt>

<span id="Server"></span><span id="server"></span><span id="SERVER"></span>Server
</dt> <dd>

Required. Denotes that the service runs as file server.

</dd> <dt>

<span id="Chunk"></span><span id="chunk"></span><span id="CHUNK"></span>Chunk
</dt> <dd>

Optional. The transferred files are broken into chunks of the specified size. Each message contains one chunk. The default is 32768 bytes.

</dd> </dl>

Implementation details. As this sample is written against the channel layer, it has to manually perform certain tasks that the service model layer could do automatically. One such task is channel management. In order to provide a fast response to requests, there are always (up to a limit) several channels ready to accept requests. Having multiple channels ready is more performant in the case of multiple requests than having only one channel as the creation of a channel takes time. Further, reuse of state also improves performance. Sapphire provides APIs to reset most state to avoid having to free and recreate it. This sample takes advantage of that by reusing channel and request state wherever possible and only creating or destroying state when certain thresholds are passed. The code related to channel management can be found in CChannelManager.

The main message processing loop is in CRequest. That class contains the application-independent state and methods needed for an asynchronous Sapphire messaging processing loop. The application-specific code is in CFileRepClient (client service) and CFileRepServer (server service). Both those classes inherit from CFileRep, which contains generic service-related code.

The sample both uses the serializer and performs custom serialization. Custom serialization is used when dealing with large chunks of data to minimize memory consumption by manually optimizing memory allocation for the specific purpose. As this leads to complex, low-level code doing manual serialization should only be done when absolutely necessary.

Message exchange pattern:

-   The client service gets a request message from the command line tool.
-   If the request is asynchronous send back a confirmation immediately.
-   The client service sends a request for file information to the server service. A discovery request is denoted by a chunk position of -1.
-   The server service returns the file information.
-   The client service requests the individual chunks sequentially one by one from the server. Chunks are identified by their position within the file.
-   Repeat until the file transfer is completed or a failure occurred.
-   If the request is synchronous send success or failure message to the command line tool.

For the individual data structures associated with each message, see common.h.

-   [Service.cpp](#servicecpp)
-   [Service.h](#serviceh)
-   [CChannelManager.cpp](#cchannelmanagercpp)
-   [CFileRep.cpp](#cfilerepcpp)
-   [CRequest.cpp](#crequestcpp)
-   [CFileRepClient.cpp](#cfilerepclientcpp)
-   [CFileRepServer.cpp](#cfilerepservercpp)
-   [common.h](#commonh)
-   [FileRep.mc](#filerepmc)
-   [FileRep.rc](#filereprc)
-   [Makefile](#makefile)
-   [Related topics](#related-topics)

## Service.cpp


```C++
// This is the main function of the executable hosting the service.
// It parses the command line and passes the parameters to the service.
// From a Sapphire perspective there is not much to see here.
#include "Service.h"
#include "string.h"
#include "wtypes.h"
#include "stdlib.h"
#include "intsafe.h"

HRESULT ParseCommandLine(int argc, __in_ecount(argc) wchar_t **argv, MESSAGE_ENCODING *messageEncoding,
    DWORD *chunkSize, long *maxConnections, REPORTING_LEVEL *reportingLevel, bool server)
{
    *messageEncoding = DEFAULT_ENCODING;
    *chunkSize = 32768;
    *maxConnections = 100;
    *reportingLevel = REPORT_ERROR;
    bool reportingSet = false;

    // Parse the optional parameters.
    for (int i = 0; i < argc; i++)
    {
        WCHAR* arg = argv[i];
        if (!_wcsicmp(arg, L"-reporting:error") || !_wcsicmp(arg, L"/reporting:error"))
        {
            if (reportingSet)
            {
                wprintf(L"Error: More than one reporting level specified.\n");
                return E_FAIL;
            }

            *reportingLevel = REPORT_ERROR;
            reportingSet = true;
        }
        else if (!_wcsicmp(arg, L"-reporting:info") || !_wcsicmp(arg, L"/reporting:info"))
        {
            if (reportingSet)
            {
                wprintf(L"Error: More than one reporting level specified.\n");
                return E_FAIL;
            }

            reportingSet = true;
            *reportingLevel = REPORT_INFO;
        }
        else if (!_wcsicmp(arg, L"-reporting:verbose") || !_wcsicmp(arg, L"/reporting:verbose"))
        {
            if (reportingSet)
            {
                wprintf(L"Error: More than one reporting level specified.\n");
                return E_FAIL;
            }

            reportingSet = true;
            *reportingLevel = REPORT_VERBOSE;
        }
        else if (wcsstr(arg, L"-reporting:") || wcsstr(arg, L"-reporting:"))
        {
            wprintf(L"Error: Illegal reporting level specified.\n");
            return E_FAIL;
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
        else if (!_wcsnicmp(arg, L"-chunk:", 7) || !_wcsnicmp(arg, L"/chunk:", 7))
        {
            if (!server)
            {
                wprintf(L"Chunk is not a legal setting on the client side.\n");
                return E_FAIL;
            }

            *chunkSize = wcstoul(&arg[7], NULL, 10);    
        }
        else if (!_wcsnicmp(arg, L"-connections:", 13) || !_wcsnicmp(arg, L"/connections:", 13))
        {
            *maxConnections = wcstol(&arg[13], NULL, 10);    
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
    bool server = true;
    TRANSPORT_MODE transport = TCP_TRANSPORT;
    SECURITY_MODE securityMode = NO_SECURITY;

    if (argc < 3)
    {
        wprintf(L"Usage:\n FileRepService.exe <server/client> <Service Url> [/reporting:<error/verbose>] [/encoding:<text/binary/MTOM>]");
        wprintf(L" [/connections:<number of connections>] [/chunk:<size of the payload per message>]\n");

        return -1;
    }

    if (!_wcsicmp(argv[1], L"client"))
    {
        server = false;
    }
    else if (_wcsicmp(argv[1], L"server"))
    {
        wprintf(L"Must specify server or client\n");
        return -1;
    }

    LPWSTR url = argv[2];

    // Default settings of optional parameters.
    MESSAGE_ENCODING messageEncoding = DEFAULT_ENCODING;
    DWORD chunkSize = 32768;
    long maxConnections = 100;
    REPORTING_LEVEL reportingLevel = REPORT_ERROR;

    if (argc > 3)
    {        
        if (FAILED(ParseCommandLine(argc - 3, &argv[3], &messageEncoding, &chunkSize, &maxConnections, &reportingLevel, server)))
        {
            return -1;
        }
    }  
    
    if (FAILED(ParseTransport( url, &transport, &securityMode)))
    {
        wprintf(L"Illegal protocol.\n");
        return -1;
    }

    if (chunkSize > MAXMESSAGESIZE -1024) // 1024 for overhead
    {
        wprintf(L"The chunk size specified exceeded the allowed maximum of %d.\n", MAXMESSAGESIZE);
        return -1;
    }
    else if (0 == chunkSize)
    {
        wprintf(L"The chunk size must be greater than zero.\n");
        return -1;
    }

    if (maxConnections < 1) 
    {
        wprintf(L"You must allow at least one connection.\n");
        return -1;
    }

    CFileRep* fileServer = NULL;

    if (server)
    {
        fileServer = new CFileRepServer(reportingLevel, maxConnections, transport, securityMode, messageEncoding, chunkSize); 
    }
    else
    {
        fileServer = new CFileRepClient(reportingLevel, maxConnections, transport, securityMode, messageEncoding); 
    }

    if (!fileServer)
    {
        wprintf(L"Unable to create service.\n");
        return -1;
    }

    ULONG urlSize;
    if (FAILED(SizeTToULong(::wcslen(url),&urlSize)))
    {
        wprintf(L"url string too long. Exiting.\n");
        return -1;
    }
    
    if (FAILED(fileServer->Start(url, urlSize)))
    {
        wprintf(L"Service startup failed. Exiting.\n");
        return -1;
    }
    
    wprintf(L"Startup complete. Press any key to exit.\n");
    
    (void)getchar();

    fileServer->Stop();
    delete fileServer;
    wprintf(L"Shutdown complete.\n");

    return 0;
}
```



## Service.h


```C++
#include <windows.h>
#include "common.h"

// This header file contains all definitions used by both client and server services.

// Size of each file access when serializing the file into messages. 
// A bigger number here results in fewer file reads while a smaller number reduces 
// memory consumption. This is a sub-chunking of the chunk size set by the user 
// when starting the services. If the chunk size set then is bigger than FILE_CHUNK
// a chunk is read in more than one file access.

#define FILE_CHUNK 131072
#define DISCOVERY_REQUEST -1

// Error Uris used to transmit errors from server service to client service.
namespace GlobalStrings
{   
    static const WCHAR noError[] = L"https://tempuri.org/FileRep/NoError";
    static const WCHAR serializationFailed[] = L"https://tempuri.org/FileRep/SerializationFailed";
    static const WCHAR invalidFileName[] = L"https://tempuri.org/FileRep/InvalidFileName";
    static const WCHAR unableToDetermineFileLength[] = L"https://tempuri.org/FileRep/UnableToDetermineFileLength";
    static const WCHAR invalidRequest[] = L"https://tempuri.org/FileRep/InvalidRequest";
    static const WCHAR outOfRange[] = L"https://tempuri.org/FileRep/OutOfRange";
    static const WCHAR unableToSetFilePointer[] = L"https://tempuri.org/FileRep/UnableToSetFilePointer";
}

class CChannelManager;
class CRequest;

typedef enum
{
    REPORT_ERROR = 1,
    REPORT_INFO = 2,
    REPORT_VERBOSE = 3,
} REPORTING_LEVEL;

typedef enum
{
    INVALID_REQUEST = 1,
    FILE_DOES_NOT_EXIST = 2,
    FAILED_TO_CREATE_FILE,

} FAULT_TYPE;

// This class is the base class for both the client and server service.
class CFileRep
{
public:
    CFileRep(REPORTING_LEVEL errorReporting, long maxChannels, TRANSPORT_MODE transport, 
        SECURITY_MODE security, MESSAGE_ENCODING encoding);    

    ~CFileRep();

    HRESULT Start(__in_ecount(uriLength) const LPWSTR uri, DWORD uriLength);

    // A stop resets all custom state and releases all resources associated with a running instance of the service.
    HRESULT Stop(); 

    inline bool IsRunning() { return started; }

    WS_LISTENER* GetListener() { return listener; }

    CChannelManager* GetChannelManager() { return channelManager; }
    
    virtual HRESULT ProcessMessage(CRequest* request, const WS_XML_STRING* receivedAction) = 0;

    // These have to be public since things like thread creation can fail outside of the class.
    void PrintVerbose(__in_z const WCHAR message[]);  
  
    void PrintInfo(__in_z const WCHAR message[]);   
 
    void PrintError(HRESULT hr, WS_ERROR* error, bool displayAlways);

    void PrintError(__in_z const WCHAR message[], bool displayAlways);    
    
    // The default maximum heap size is set very conservatively to protect against headers of excessive size.
    // Since we are sending large chunks of data round that is not sufficient for us.
    static WS_MESSAGE_PROPERTY CreateHeapProperty()
    {
        static SIZE_T heapSize = MAXMESSAGESIZE * 2;

        static WS_HEAP_PROPERTY heapPropertyArray[] = 
        {
            { WS_HEAP_PROPERTY_MAX_SIZE, &heapSize, sizeof(heapSize) }
        };

        static WS_HEAP_PROPERTIES heapProperties = 
        {
            heapPropertyArray, WsCountOf(heapPropertyArray)
        };

        WS_MESSAGE_PROPERTY ret;
        ret.id = WS_MESSAGE_PROPERTY_HEAP_PROPERTIES;
        ret.value = &heapProperties;
        ret.valueSize = sizeof(heapProperties);
        return ret;
    }

    void GetEncoding(WS_ENCODING* encodingProperty, ULONG *propertyCount);
     
protected: 
    HRESULT InitializeListener();     
    
    WS_STRING uri;
    volatile bool started;
    REPORTING_LEVEL errorReporting;
    long maxChannels;
    TRANSPORT_MODE transportMode;
    MESSAGE_ENCODING encoding;
    SECURITY_MODE securityMode;
    WS_LISTENER* listener;
    CChannelManager* channelManager;
};

// Manages the channels and related state to maximize reuse of structures and performance.
// If there are less channels that are ready to accept a request (called idle channels) 
// than minIdleChannels then we create a new channel and make it listen for incoming requests. 
// If there are more idle channels than maxIdleChannels then we destroy the next channel that 
// becomes idle. There are never more than maxTotalChannels channels overall.
// The reason for having a minimum number of idle channels is that otherwise there would be a 
// bottleneck when multiple requests come in simultaniously as channel creation takes some time.
// The reason for having a maximum number of idle channels is to limit resource consumption.
// Resource reuse is an important performance booster. Resetting a data structure is a lot cheaper 
// than destroying and recreating it later, which is why there are so many reset APIs. 
// However, never destroying resources can also be problematic as you can potentially hold on
// to significant resources much longer than neccessary. This class, using the algorithm described 
// above, tries to find a middle ground.
// If the last issue is not a concern, a simpler and most likely superior implementation is to 
// simply create as many channels and associated resources as needed and to reuse them perpetually
// in their own loop.
class CChannelManager
{
public:
    CChannelManager(CFileRep *server, long minIdleChannels, long maxIdleChannels, long maxTotalChannels);

    ~CChannelManager();

    HRESULT Initialize();

    HRESULT CreateChannels();

    static ULONG WINAPI CreateChannelWorkItem(void* state);

    void CreateChannel(CRequest *request);

    void ChannelCreated();

    void ChannelInUse(); 

    void ChannelFreed();

    void ChannelIdle(); 
    
    static void CALLBACK CleanupCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state);    

    void Stop();

    void WaitForCleanup();

    inline long GetChannelCount() { return totalChannels; }

    inline bool IsRunning() { return running; }

    inline bool ShouldDestroyChannel() { return (!IsRunning() || idleChannels > maxIdleChannels); }

private:    
    inline void PrintVerbose(__in_z const WCHAR message[]) { server->PrintVerbose(message); }

    long minIdleChannels;
    long maxIdleChannels;
    long maxTotalChannels;

    long idleChannels;
    long activeChannels;
    long totalChannels;

    CFileRep* server;
    HANDLE stopEvent;
    volatile bool running;

#if (DBG || _DEBUG)
    bool initialized;
#endif
};

// This class implements the part of the message processing loop that is common to the client and server service.
// It contains the per-channel state as well as the common processing methods.
class CRequest
{
public:
    CRequest(CFileRep* server);

    ~CRequest();

    HRESULT Initialize();

    // Static callback methods. They delegate to their non-static counterparts.
    static HRESULT CALLBACK ResetChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    static HRESULT CALLBACK AcceptChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);    

    static HRESULT CALLBACK ReceiveFirstMessageCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    static HRESULT CALLBACK ReceiveMessageCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);    

    static HRESULT CALLBACK ReadHeaderCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    static HRESULT CALLBACK CloseChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    static HRESULT CALLBACK RequestCompleteCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    static HRESULT CALLBACK HandleFailureCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
        WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);   

    // The non-static counterparts that actually do the work.
    HRESULT ResetChannel(HRESULT hr, WS_ASYNC_OPERATION* next, 
        WS_CALLBACK_MODEL callbackModel, WS_ERROR* error);   

    HRESULT AcceptChannel(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel, 
        const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error); 

    HRESULT ReceiveFirstMessage(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel); 

    HRESULT ReceiveMessage(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel,
        const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);  

    HRESULT ReadHeader(HRESULT hr, WS_ASYNC_OPERATION* next,
        WS_CALLBACK_MODEL callbackModel, WS_ERROR* error);

    HRESULT CloseChannel(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel,
        const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error);

    HRESULT RequestComplete(HRESULT hr, WS_ASYNC_OPERATION* next); 

    HRESULT HandleFailure(HRESULT hr, WS_ASYNC_OPERATION* next, WS_ERROR* error); 


    WS_CHANNEL* GetChannel() { return channel; }

    WS_MESSAGE* GetRequestMessage() { return requestMessage; }

    WS_MESSAGE* GetReplyMessage() { return replyMessage; }

    WS_ERROR* GetError() { return error; }

    CFileRep* GetServer() { return server; }

    // We use SOAP faults to communicate to the tool errors that might be expected 
    // during execution, such as file not found. For critical errors we abort the channel.
    // For internal communication between the services we use status messages that are part
    // of the regular message exchange instead of faults. We could use faults there as well,
    // but we do not want to fault internal communication because for example the user 
    // requested an invalid file.
    HRESULT SendFault(FAULT_TYPE faultType);

    static inline CRequest* GetRequest(void* callbackState);

    WS_ASYNC_STATE asyncState;

private:
    inline void PrintVerbose(__in_z const WCHAR message[]) { server->PrintVerbose(message); }
    
    // State associated with a request. Except the CFileRep pointer, this is not application specific.
    WS_CHANNEL* channel;
    WS_MESSAGE* requestMessage;
    WS_MESSAGE* replyMessage;
    WS_ERROR* error;
    CFileRep* server;
    bool channelInUse;
};


// Server service.
class CFileRepServer : public CFileRep
{
public:
    CFileRepServer(REPORTING_LEVEL errorReporting, DWORD maxChannels, TRANSPORT_MODE transport, 
        SECURITY_MODE security, MESSAGE_ENCODING encoding, DWORD chunkSize) : CFileRep(errorReporting,
        maxChannels, transport, security, encoding)
    {
        this->chunkSize = chunkSize;
    }

    HRESULT ProcessMessage(CRequest* request, const WS_XML_STRING* receivedAction);

protected:
    
    HRESULT SendError(CRequest* request, __in const WCHAR errorMessage[]);
    HRESULT ReadAndSendFile(CRequest* request, __in const LPWSTR fileName, LONGLONG chunkPosition, WS_ERROR *error);
    HRESULT SendFileInfo(CRequest* requeste, __in const LPWSTR fileName, LONGLONG llFileLength, DWORD chunkSize);
    HRESULT ReadAndSendChunk(CRequest* request, long chunkSize, LONGLONG chunkPosition, HANDLE file);

    long chunkSize;
};

// Client service.
class CFileRepClient : public CFileRep
{
public:
    CFileRepClient(REPORTING_LEVEL errorReporting, DWORD maxChannels, TRANSPORT_MODE transport, 
        SECURITY_MODE security, MESSAGE_ENCODING encoding) : CFileRep(errorReporting, maxChannels, 
        transport, security, encoding)
    {
    }

    HRESULT ProcessMessage(CRequest* request, const WS_XML_STRING* receivedAction);

protected:
    HRESULT SendUserResponse(CRequest* request, TRANSFER_RESULTS result);

    HRESULT ProcessUserRequest(CRequest* request, __in const LPWSTR sourcePath,
        __in const LPWSTR destinationPath, __in const LPWSTR serverUri, TRANSPORT_MODE transportMode, 
        SECURITY_MODE securityMode, MESSAGE_ENCODING encoding, REQUEST_TYPE requestType);

    
    HRESULT CreateServerChannel(MESSAGE_ENCODING serverEncoding, TRANSPORT_MODE serverTransportMode, 
        SECURITY_MODE serverSecurityMode, WS_ERROR *error, WS_CHANNEL **channel);

    HRESULT ExtendFile(HANDLE file, LONGLONG length);

    HRESULT ProcessChunk(long chunkSize, HANDLE file, LONGLONG fileLength, WS_MESSAGE *requestMessage, 
        WS_MESSAGE *replyMessage, WS_CHANNEL *channel, WS_ERROR *error, FileRequest *request);


    HRESULT DeserializeAndWriteMessage(WS_MESSAGE *message, long chunkSize, LONGLONG *chunkPosition,
        long *contentLength, HANDLE file);
};

// Helper functions.
void PrintError(HRESULT errorCode, WS_ERROR* error);

HRESULT ParseTransport(__in const LPWSTR url, TRANSPORT_MODE *transport, SECURITY_MODE *securityMode);

void CleanupChannel(WS_CHANNEL* channel);

```



## CChannelManager.cpp


```C++
#include "Service.h"
#include "assert.h"

CChannelManager::CChannelManager(CFileRep* server, long minIdleChannels, long maxIdleChannels, long maxTotalChannels)
{    
    this->minIdleChannels = minIdleChannels;
    this->maxIdleChannels = maxIdleChannels;
    this->maxTotalChannels = maxTotalChannels;

    assert(this->maxIdleChannels >= minIdleChannels);
    assert(this->minIdleChannels <= maxTotalChannels);
    assert(NULL != server);
        
    idleChannels = 0;
    activeChannels = 0;
    totalChannels = 0;
    this->server = server;

    stopEvent = NULL;
    running = true;
}

HRESULT CChannelManager::Initialize()
{
    HRESULT hr = NOERROR;

    stopEvent = CreateEvent(NULL, true, false, NULL); 

    if (NULL == stopEvent)
    {
        server->PrintError(L"CChannelManager::Initialize", true);
        server->PrintError(L"Initialization of event failed. Aborting service startup.", true);

        hr = HRESULT_FROM_WIN32(GetLastError());
    }

    return hr;
}

CChannelManager::~CChannelManager()
{
    // At this point, no outstanding channels should be left.
    assert(0 == idleChannels);
    assert(0 == activeChannels);
    assert(0 == totalChannels);

    if (NULL != stopEvent)
    {
        CloseHandle(stopEvent);
        stopEvent = NULL;
    }   
}

void CChannelManager::ChannelCreated() 
{
    InterlockedIncrement(&idleChannels);
    InterlockedIncrement(&totalChannels);
}

// Channel is processing a request.
void CChannelManager::ChannelInUse() 
{
    InterlockedIncrement(&activeChannels); 

    assert(idleChannels > 0);
    InterlockedDecrement(&idleChannels);    

    // See if we fell below the threshold for available channels.
    // Ignore return value as the failure to create a new channel should not impact the existing channel.
    (void) CreateChannels();
}

// Channel and associated data structures are freed.
void CChannelManager::ChannelFreed() 
{
    assert(idleChannels > 0);
    InterlockedDecrement(&idleChannels);    

    assert(totalChannels > 0);
    long totalChannelsChannelFreed = InterlockedDecrement(&totalChannels);
    
    if (0 == totalChannelsChannelFreed)
    {
        // We only destroy superfluous channels so it should never hit 0
        // unless we are shutting down.
        assert(!IsRunning());
        SetEvent(stopEvent);
    }
}

// Channel is done processing a request and is ready to accept more work.
void CChannelManager::ChannelIdle() 
{
    assert(activeChannels > 0);
    InterlockedDecrement(&activeChannels);     

    InterlockedIncrement(&idleChannels);    
}

// Creates new channels if we are below the threshold for minimum available channels and if we are not at the channel cap.
HRESULT CChannelManager::CreateChannels()
{
    CRequest* request = NULL;
    HRESULT hr = NOERROR;
    server->PrintVerbose(L"Entering CChannelManager::CreateChannels");
  
    if (idleChannels >= minIdleChannels || idleChannels + activeChannels >= maxTotalChannels)
    {
        server->PrintVerbose(L"Leaving CChannelManager::CreateChannels");
        return NOERROR;
    }

    long newChannels = minIdleChannels - idleChannels;
    if (newChannels > maxTotalChannels - idleChannels - activeChannels)
    {
        newChannels = maxTotalChannels - idleChannels - activeChannels;
    }

    for (long i = 0; i < newChannels; i++)
    {
        // Even though our main request processing loop is asynchronous, there is enough
        // synchronous work done (eg state creartion) to warrant farming this out to work items. Also, 
        // WsAsyncExecute can return synchronously if the request ends before the first asynchronous
        // function is called and in that case we dont want to get stuck here by doing this synchronously.

        // This is done here to prevent a race condition. If QueueUserWorkItem fails during startup the
        // service will get torn down. But there could be other work items out there waiting to be executed.
        // So to make sure the shutdown waits until those have been scheduled we increment the channel count here.
        
        if (!IsRunning())
        {
            break;
        }

        // This object contains all request-specific state and the common message processing methods.
        request = new CRequest(server);
        IfNullExit(request);

        // Preallocate as much state as possible.
        IfFailedExit(request->Initialize());

        ChannelCreated();        
        if (!::QueueUserWorkItem(CChannelManager::CreateChannelWorkItem, request, WT_EXECUTELONGFUNCTION))
        {
            // If this fails we are in bad shape, so don't try again.
            hr = HRESULT_FROM_WIN32(GetLastError());
            server->PrintError(L"CChannelManager::CreateChannels", true);
            server->PrintError(hr, NULL, true); 
            delete request;
            
            break;
        }
    }

    EXIT

    server->PrintVerbose(L"Leaving CChannelManager::CreateChannels");
    return hr;
}

ULONG WINAPI CChannelManager::CreateChannelWorkItem(void* state)
{
    assert(NULL != state);

    CRequest* request = (CRequest*) state;  

    request->GetServer()->GetChannelManager()->CreateChannel(request);

    return 0;
}

// A channel goes through a series of states involving the channel manager.
// It starts its life here. We call into CFileRep::CreateOrResetChannel to create the actual channel state.
// After creation, the channel waits for an incoming request and once it gets one processes it.
// Once it is done, we call back into the channel manager which checks if the service is still running
// and if the channel is still needed. That happens in CChannelManager::RequestComplete 
// If it is not needed, the channel and related data structures are freed.
// If it is still needed, the loop repeats as we call into CFileRep::CreateOrResetChannel again. 
// Only this time it reuses the channel data structures instead of creating them.
void CChannelManager::CreateChannel(CRequest* request)
{
    PrintVerbose(L"Entering CChannelManager::CreateChannel");

    WS_ERROR* error = request->GetError();

    WS_ASYNC_CONTEXT asyncContext;
    HRESULT hr = NOERROR;

    if (!IsRunning())
    {
        PrintVerbose(L"Leaving CChannelManager::CreateChannel");
        return;
    }
           
    // We do nothing in the callback
    asyncContext.callback = CleanupCallback;  
    asyncContext.callbackState = request;

    // Start the message processing loop asynchronously. 
    // Use long callbacks since we are going to do significant work in there.
    IfFailedExit(WsAsyncExecute(&request->asyncState, CRequest::AcceptChannelCallback, WS_LONG_CALLBACK,
        request, &asyncContext, error));   
    
    // In the sync case, the cleanup callback is never called so we have to do it here.
    // We only get here after we are done with the channel for good so it is safe to do this.
    if (WS_S_ASYNC != hr)
    {
        delete request;
    }
    
    PrintVerbose(L"Leaving CChannelManager::CreateChannel");
    return;

    ERROR_EXIT

    server->PrintError(L"CChannelManager::CreateChannel", true);
    server->PrintError(hr, error, true); 
    if (NULL != request)
    {
        // Cleans up all the state associated with a request.
        delete request;
    }  

    PrintVerbose(L"Leaving CChannelManager::CreateChannel");
}

#pragma warning(disable : 4100) // The callbacks doesn't use all parameters.

// This is called at the end of an async execution chain. Here we can clean up.
void CALLBACK CChannelManager::CleanupCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* state)
{
    assert(NULL != state);

    CRequest* request = (CRequest*) state;  
    delete request;
}

#pragma warning(default : 4100)

// Sets state to stopped, which prevents new requests from being processed.
void CChannelManager::Stop()
{
    server->PrintVerbose(L"Entering CChannelManager::Stop");
    
    // This is a special case. As we never destroy all channels, there should
    // only be zero channels before shutdown if the creation of all channels failed.
    // In that case we stop here as the regular stop will not be hit.
    if (0 == totalChannels)
    {
        SetEvent(stopEvent);
    }

    running = false;

    server->PrintVerbose(L"Leaving CChannelManager::Stop");
}

// Wait for all outstanding requests to drain.
void CChannelManager::WaitForCleanup()
{
    server->PrintVerbose(L"Entering CChannelManager::WaitForCleanup");
    
    assert(!IsRunning());

    WaitForSingleObject(stopEvent, INFINITE);

    server->PrintVerbose(L"Leaving CChannelManager::WaitForCleanup");    
}
```



## CFileRep.cpp


```C++
#include "Service.h"
#include "strsafe.h"
#include "stdlib.h"
#include "intsafe.h"
#include "assert.h"

// Currently we only support 3 modes: TCP, HTTP and HTTP with SSL. Thus, this simple check here is
// enough to figure out the proper configuration. This will not be enough once we have more advanced
// security settings. The wire protocol makes these settings explicit so that it does not have
// to be changed in that case. This is only used for the command line.
// For more advanced parsing, WsDecodeUrl should be used.
HRESULT ParseTransport(__in const LPWSTR url, TRANSPORT_MODE* transport, SECURITY_MODE* securityMode)
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

CFileRep::CFileRep(REPORTING_LEVEL errorReporting, long maxChannels, TRANSPORT_MODE transport, SECURITY_MODE security, MESSAGE_ENCODING encoding)
{
    assert(maxChannels >=1);
    this->errorReporting = errorReporting;
    this->maxChannels = maxChannels;
    
    this->started = false;
    this->transportMode = transport;
    this->encoding = encoding;
    this->securityMode = security;

    this->listener = NULL;
    this->channelManager = NULL;
}

CFileRep::~CFileRep()
{
    Stop();    
}

HRESULT CFileRep::Start(__in_ecount(uriLength) const LPWSTR uri, DWORD uriLength)
{    
    PrintVerbose(L"Entering CFileRep::Start");
    assert(!started); // Should not be called twice without calling stop first.

    if (started)
    {
        PrintVerbose(L"Leaving CFileRep::Start");
        return S_FALSE;
    }

    HRESULT hr = NOERROR;

    DWORD newLength = 0;
    DWORD bytes = 0;

    IfFailedExit(DWordAdd(uriLength, 1, &newLength));
    IfFailedExit(DWordMult(newLength, sizeof (WCHAR), &bytes));        

    // Make local copy of the URI.
    this->uri.chars = (LPWSTR)HeapAlloc(GetProcessHeap(), 0, bytes);
    IfNullExit(this->uri.chars);

    IfFailedExit(StringCchCopyNW(this->uri.chars, newLength, uri, uriLength));
    
    this->uri.length = uriLength;

    // We are ready to start listening.
    started = true;
    IfFailedExit(InitializeListener());

    PrintInfo(L"Service startup succeeded.\n");
    PrintVerbose(L"Leaving CFileRep::Start");    

    return NOERROR;

    
    ERROR_EXIT

    PrintError(L"Service startup failed.\n", true);        
        
    Stop();  

    if (NULL != this->uri.chars)
    {
        HeapFree(GetProcessHeap(), 0, this->uri.chars);
        this->uri.chars = NULL;
    } 
    
    PrintVerbose(L"Leaving CFileRep::Start");    
    return hr;
}

// We are told to stop the service. Clean up all state.
HRESULT CFileRep::Stop()
{
    PrintVerbose(L"Entering CFileRep::Stop");

    if (!started)
    {
        PrintVerbose(L"Leaving CFileRep::Stop");
        return S_FALSE;
    }

    started = false;
    if (NULL != channelManager)
    {
        channelManager->Stop();
    }

    PrintInfo(L"Shutdown signaled.");

    if (NULL != listener)
    {
        // This aborts the main service loop that waits for incoming requests.        
        // WsCloseListener can fail but will still close the listener in that case. 
        // So we can ignore the error.
        WsCloseListener(listener, NULL, NULL);            
    }

    if (NULL != channelManager)
    {
        channelManager->WaitForCleanup();
        delete channelManager;
        channelManager = NULL;        
    }

    if (NULL != listener)
    {
        WsFreeListener(listener);
        listener = NULL;
    }

    if (NULL != uri.chars)
    {
        HeapFree(GetProcessHeap(), 0, uri.chars);
        uri.chars = NULL;
    }    

    PrintVerbose(L"Leaving CFileRep::Stop");

    return NOERROR;
}

// The following are the error reporting and tracing functions.
void CFileRep::PrintVerbose(__in_z const WCHAR message[])
{
    if (REPORT_VERBOSE <= errorReporting) 
    {
        wprintf(L"FileRep: ");    
        
        wprintf(message);
        wprintf(L"\n");
    }
}

void CFileRep::PrintInfo(__in_z const WCHAR message[])
{
    if (REPORT_INFO <= errorReporting) 
    {
        wprintf(L"FileRep: ");    
        
        wprintf(message);
        wprintf(L"\n");
    }
}

void CFileRep::PrintError(HRESULT hr, WS_ERROR* error, bool displayAlways)
{
    // We don't alyways display errors since in during shutdown certain
    // failures are expected.
    if (!(displayAlways || started))
    {
        return;
    }

    if (REPORT_ERROR <= errorReporting) 
    {
        ::PrintError(hr, error); 
    }
}

void CFileRep::PrintError(__in_z const WCHAR message[], bool displayAlways)
{
    if (!(displayAlways || started))
    {
        return;
    }

    if (REPORT_ERROR <= errorReporting) 
    {
        wprintf(L"FileRep ERROR: ");                    
        wprintf(message);
        wprintf(L"\n");
    }
}

void CFileRep::GetEncoding(WS_ENCODING* encodingProperty, ULONG* propertyCount)
{
    *propertyCount = 1;
    
    if (TEXT_ENCODING == encoding)
    {        
        *encodingProperty = WS_ENCODING_XML_UTF8;
    }
    else if (BINARY_ENCODING == encoding)
    {
        *encodingProperty = WS_ENCODING_XML_BINARY_SESSION_1;
    }
    else if (MTOM_ENCODING == encoding)
    {
        *encodingProperty = WS_ENCODING_XML_MTOM_UTF8;
    }
    else // default encoding
    {
        *propertyCount = 0;
    }
}

// Set up the listener. Each service has exactly one. Accept channels and start the processing.
HRESULT CFileRep::InitializeListener()
{    
    PrintVerbose(L"Entering CFileRep::InitializeListener");

    HRESULT hr = NOERROR;
    WS_ERROR* error = NULL;
    WS_SSL_TRANSPORT_SECURITY_BINDING transportSecurityBinding = {};
    WS_SECURITY_DESCRIPTION securityDescription = {};
    WS_SECURITY_DESCRIPTION* pSecurityDescription = NULL;
    WS_SECURITY_BINDING* securityBindings[1];

    WS_LISTENER_PROPERTY listenerProperties[1];
    WS_CALLBACK_MODEL callbackModel = WS_LONG_CALLBACK;
    listenerProperties[0].id = WS_LISTENER_PROPERTY_ASYNC_CALLBACK_MODEL;
    listenerProperties[0].value = &callbackModel;
    listenerProperties[0].valueSize = sizeof(callbackModel);


    assert(NULL == channelManager);

    IfFailedExit(WsCreateError(NULL, 0, &error));  
   
    if (SSL_SECURITY == securityMode)
    {
        // Initialize a security description for SSL.
        transportSecurityBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE;
        securityBindings[0] = &transportSecurityBinding.binding;
        securityDescription.securityBindings = securityBindings;
        securityDescription.securityBindingCount = WsCountOf(securityBindings);
        pSecurityDescription = &securityDescription;
    }

    if (TCP_TRANSPORT == transportMode) // Create a TCP listener
    {   
        IfFailedExit(WsCreateListener(WS_CHANNEL_TYPE_DUPLEX_SESSION, WS_TCP_CHANNEL_BINDING, 
            listenerProperties, WsCountOf(listenerProperties), pSecurityDescription, &listener, error));
    }
    else // Create an HTTP listener
    {        
        IfFailedExit(WsCreateListener(WS_CHANNEL_TYPE_REPLY, WS_HTTP_CHANNEL_BINDING, 
            listenerProperties, WsCountOf(listenerProperties), pSecurityDescription, &listener, error));
    }        
    
    IfFailedExit(WsOpenListener(listener, &uri, NULL, error));    

    // We put fixed values here to not overly complicate the command line. 
    long maxIdleChannels = 20;
    long minIdleChannels = 10;
    if (maxChannels < maxIdleChannels)
    {
        maxIdleChannels = maxChannels;
        minIdleChannels = maxIdleChannels/2 + 1;
    }

    channelManager = new CChannelManager(this, minIdleChannels, maxIdleChannels, maxChannels);
    IfNullExit(channelManager);
    IfFailedExit(channelManager->Initialize());

    // Spins up a bunch of channels so that we are prepared to handle multipe requests in a timely fashion.
    IfFailedExit(channelManager->CreateChannels());

    if (NULL != error)
    {
        WsFreeError(error);
    }

    PrintVerbose(L"Leaving CFileRep::InitializeListener");

    return NOERROR;


    ERROR_EXIT

    PrintError(L"CFileRep::InitializeListener", true);
    PrintError(hr, error, true); 
        
    // Class state is cleaned up in Stop so only clean up locals even in case of failure.
    if (NULL != error)
    {
        WsFreeError(error);
    }

    PrintVerbose(L"Leaving CFileRep::InitializeListener");
    
    return hr;
}

```



## CRequest.cpp


```C++
#include "Service.h"
#include "strsafe.h"
#include "stdlib.h"
#include "intsafe.h"
#include "assert.h"

// This function closes the channel if it was openend and then frees it.
void CleanupChannel(WS_CHANNEL* channel)
{
    ULONG state = 0;

    if (NULL == channel)
    {
        return;
    }        
    (void)WsGetChannelProperty(channel, WS_CHANNEL_PROPERTY_STATE, &state, sizeof(state), NULL);
        
    if (WS_CHANNEL_STATE_OPEN == state || WS_CHANNEL_STATE_FAULTED == state)
    {
        // CloseChannel will close the channel even if it encouters an error. So ignore the error here
        // as this is called only when we destroy the channel.
        WsCloseChannel(channel, NULL, NULL);
    }

    WsFreeChannel(channel);
}

CRequest::CRequest(CFileRep* server)
{
    assert(NULL != server);
    this->server = server;
    
    channel = NULL;
    requestMessage = NULL;
    replyMessage = NULL;
    error = NULL;
    channelInUse = false;    
}

// Preallocate all state
HRESULT CRequest::Initialize()
{
    assert(NULL == channel);
    assert(NULL == requestMessage);
    assert(NULL == replyMessage);
    assert(NULL == error);

    HRESULT hr = NOERROR;

    ULONG propertyCount = 0;
    WS_ENCODING encoding;

    WS_CHANNEL_PROPERTY encodingProperty;
    encodingProperty.id = WS_CHANNEL_PROPERTY_ENCODING;
    
    server->GetEncoding(&encoding, &propertyCount);
    encodingProperty.value = &encoding;
    encodingProperty.valueSize = sizeof(encoding);
    
    IfFailedExit(WsCreateError(NULL, 0, &error));
    IfFailedExit(WsCreateChannelForListener(server->GetListener(), &encodingProperty, propertyCount, &channel, NULL));        
    IfFailedExit(WsCreateMessageForChannel(channel, NULL, 0, &requestMessage, NULL));    
    IfFailedExit(WsCreateMessageForChannel(channel, NULL, 0, &replyMessage, NULL));
            
    EXIT   

    return hr;
}

CRequest* CRequest::GetRequest(void* callbackState)
{
    assert(NULL != callbackState);
    return ((CRequest *) callbackState);   
}

#pragma warning(disable : 4100) // The callbacks don't always use all parameters.

// The static callback functions.
HRESULT CALLBACK CRequest::ResetChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{       
    return GetRequest(callbackState)->ResetChannel(hr, next, callbackModel, error);
}

HRESULT CALLBACK CRequest::AcceptChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{  
    return GetRequest(callbackState)->AcceptChannel(hr, next, callbackModel, asyncContext, error);
}

HRESULT CALLBACK CRequest::ReceiveFirstMessageCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{         
    return GetRequest(callbackState)->ReceiveFirstMessage(hr, next, callbackModel);
}

HRESULT CALLBACK CRequest::ReceiveMessageCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{    
    return GetRequest(callbackState)->ReceiveMessage(hr, next, callbackModel, asyncContext, error);
}

HRESULT CALLBACK CRequest::ReadHeaderCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    return GetRequest(callbackState)->ReadHeader(hr, next, callbackModel, error);
}

HRESULT CRequest::CloseChannelCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    return GetRequest(callbackState)->CloseChannel(hr, next, callbackModel, asyncContext, error);
}

HRESULT CRequest::RequestCompleteCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{            
    return GetRequest(callbackState)->RequestComplete(hr, next);
}

HRESULT CRequest::HandleFailureCallback(HRESULT hr, WS_CALLBACK_MODEL callbackModel, void* callbackState, 
    WS_ASYNC_OPERATION* next, const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    return GetRequest(callbackState)->HandleFailure(hr, next, error);
}

#pragma warning(default : 4100)

// This is the main service loop used to process requests. It is identical for both the client and server service.
// The functions are listed in the order in which they are called. The static callback functions are put
// seperately as they don't really do anything.

// Creates or resets channel and associated data structures.
HRESULT CRequest::ResetChannel(HRESULT hr, WS_ASYNC_OPERATION* next, 
    WS_CALLBACK_MODEL callbackModel, WS_ERROR* error)
{
    PrintVerbose(L"Entering CRequest::ResetChannel"); 

    // We requested a long callback but got a short one. This is an error conditon usually 
    // triggered by resource shortage. So treat it that way. 
    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    // We always check for failures of the prior function in the next function. This simplifies error handling.
    if (FAILED(hr))
    {
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::ResetChannel"); 
        return hr;
    }

    next->function = CRequest::AcceptChannelCallback;

    IfFailedExit(WsResetError(error));
    IfFailedExit(WsResetChannel(channel, error));
    IfFailedExit(WsResetMessage(requestMessage, error));     
    IfFailedExit(WsResetMessage(replyMessage, error));  

    PrintVerbose(L"Leaving CRequest::ResetChannel");
    return NOERROR;   


    ERROR_EXIT   

    server->PrintError(L"CRequest::ResetChannel", true);
    server->PrintError(hr, error, true);         
     
    PrintVerbose(L"Leaving CRequest::ResetChannel");
    return hr;
}

// Accepts an incoming request on the channel.
HRESULT CRequest::AcceptChannel(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel, 
    const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    PrintVerbose(L"Entering CRequest::AcceptChannel");

    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    if (FAILED(hr))
    {
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::AcceptChannel"); 
        return hr;
    }

    next->function = CRequest::ReceiveFirstMessageCallback;  
    
    PrintVerbose(L"Leaving CRequest::AcceptChannel");
    return WsAcceptChannel(server->GetListener(), channel, asyncContext, error);;
}

// Special case for the first message received to keep the bookkeeping of active channels in order. 
HRESULT CRequest::ReceiveFirstMessage(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel) 
{
    PrintVerbose(L"Entering CRequest::ReceiveFirstMessage");

    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    if (FAILED(hr))
    {
        // We are not destroying a channel on failure, and we also cannot put the channel to sleep
        // on all failures as that opens up DoS attacks. However, this particular failure is different.
        // It signifies a failure in the infrastructure, and we do not want to spin on this failure.
        // So give it some breathing room to recover, unless we are shut down.
        // Obviously 5 seconds is a heuristic, but a more complex algorithm is out of the scope of this sample.
        if (server->GetChannelManager()->IsRunning())
        {
            Sleep(5000);
        }
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::ReceiveFirstMessage"); 
        return hr;
    }

    next->function = CRequest::ReceiveMessageCallback;

    channelInUse = true;

    server->GetChannelManager()->ChannelInUse();
    PrintVerbose(L"Leaving CRequest::ReceiveFirstMessage");

    return hr;
}

// This function and the next (and their non-static counterparts) represent the message processing loop. 
// WsAsyncExecute will loop between these functions until the channel is closed.
HRESULT CRequest::ReceiveMessage(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel, 
    const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    if (FAILED(hr))
    {
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::ReceiveMessage"); 
        return hr;
    }

    next->function = CRequest::ReadHeaderCallback;
      
    PrintVerbose(L"Leaving CRequest::ReceiveMessage");
    return WsReadMessageStart(channel, requestMessage, asyncContext, error);
}

HRESULT CRequest::ReadHeader(HRESULT hr, WS_ASYNC_OPERATION* next,
    WS_CALLBACK_MODEL callbackModel, WS_ERROR* error)
{
    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    if (FAILED(hr))
    {
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::ReadHeader"); 
        return hr;
    }

    // We are done. Break the loop.
    if (hr == WS_S_END)
    {        
        next->function = CRequest::CloseChannelCallback;

        server->PrintVerbose(L"Leaving CRequest::ReadHeader");        
        return NOERROR;
    }

    next->function = CRequest::ReceiveMessageCallback;    

    // Get action value
    WS_XML_STRING* receivedAction = NULL;
    IfFailedExit(WsGetHeader(
        requestMessage, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE,
        WS_READ_REQUIRED_POINTER,  
        NULL, 
        &receivedAction, 
        sizeof(receivedAction), 
        error));

    // This function is implemented by the derived classes, so the execution forks 
    // depending on whether we are client or server.
    IfFailedExit(server->ProcessMessage(this, receivedAction));
    IfFailedExit(WsResetMessage(requestMessage, error));
    
    PrintVerbose(L"Leaving CRequest::ReadHeader");
    return NOERROR;

    ERROR_EXIT

    if (WS_E_ENDPOINT_ACTION_NOT_SUPPORTED != hr)
    {
        server->PrintError(L"CRequest::ReadHeader", false);
        server->PrintError(hr, error, false); 
    }
        
    PrintVerbose(L"Leaving CRequest::ReadHeader");    
    return hr;
}

HRESULT CRequest::CloseChannel(HRESULT hr, WS_ASYNC_OPERATION* next, WS_CALLBACK_MODEL callbackModel, 
    const WS_ASYNC_CONTEXT* asyncContext, WS_ERROR* error)
{
    PrintVerbose(L"Entering CRequest::CloseChannel"); 

    if (WS_SHORT_CALLBACK == callbackModel)
    {
        hr = E_OUTOFMEMORY;
    }

    if (FAILED(hr))
    {
        next->function = CRequest::HandleFailureCallback;
        PrintVerbose(L"Leaving CRequest::CloseChannel"); 
        return hr;
    }
    else if (S_FALSE != hr)
    {
        // WsCloseChannel overwrites the error so print this here.
        // Note: We also print this if for example the file was 
        // not found as this is not an error from our end.
        server->PrintInfo(L"Request completed without error.");
    }

    next->function = CRequest::RequestCompleteCallback;

    PrintVerbose(L"Leaving CRequest::CloseChannel"); 
    return WsCloseChannel(channel, asyncContext, error); 
}

HRESULT CRequest::RequestComplete(HRESULT hr, WS_ASYNC_OPERATION* next)
{
    PrintVerbose(L"Entering CRequest::RequestComplete");
    
    // The function that got us here is WsCloseChannel. If the channel is in a closeable state,
    // WsCloseChannel is guaranteed to close it. However, it may not be able to close it gracefully.
    // If it is not then it will return an error. As the channel is still getting closed we do not
    // treat that as an error here and thus only print and informational message.
    // If the channel is not in a closeable state, WsCloseChannel will return WS_E_INVALID_OPERATION 
    // and leave the channel unchanged. That is bad because it means our state machine is broken as
    // the channel should be open or faulted when we call WsCloseChannel, and those states are closeable.

    // We don't check for the proper callback type here either, because this is just a pass bookkeeping function.

    assert(hr != WS_E_INVALID_OPERATION);

    if (FAILED(hr))
    {
        server->PrintInfo(L"WsCloseChannel failed. Channel was closed ungracefully.");
    }

    CChannelManager *manager = server->GetChannelManager();        
             
    if (manager->ShouldDestroyChannel())
    {
        // The channel is not needed. Destroy it.
        next->function = NULL; 
    }
    else
    {
        next->function = CRequest::ResetChannelCallback;
    }

    manager->ChannelIdle();
    channelInUse = false;

    PrintVerbose(L"Leaving CRequest::RequestComplete");
    return NOERROR;
}

HRESULT CRequest::HandleFailure(HRESULT hr, WS_ASYNC_OPERATION* next, WS_ERROR* error)                                
{
    PrintVerbose(L"Entering CRequest::HandleFailure");   
    assert(FAILED(hr));

    CChannelManager *manager = server->GetChannelManager(); 

    if (manager->IsRunning())
    {
        WCHAR msg[100];
        hr = StringCchPrintfW(msg, CountOf(msg), L"Request failed with %x.", hr);
        if (SUCCEEDED(hr))
        {
            server->PrintInfo(msg);
        }
        else
        {
            server->PrintInfo(L"Request failed.");   
            assert(FALSE);
        }
        
        if (channelInUse)
        {
            next->function = CRequest::CloseChannelCallback;
            (void)WsAbortChannel(GetChannel(), error);
        }
        else
        {
            next->function = CRequest::ResetChannelCallback;    
        }
    }
    else
    {
        if (channelInUse)
        {
            next->function = CRequest::CloseChannelCallback;
            (void)WsAbortChannel(GetChannel(), error);
        }
        else
        {
            next->function = NULL;    
        }
    }
  
    PrintVerbose(L"Leaving CRequest::HandleFailure");    
    return S_FALSE;
}

// This function creates a fault with a custom string and sends it back to the client.
HRESULT CRequest::SendFault(FAULT_TYPE faultType)
{
    PrintVerbose(L"Entering CRequest::SendFault");

    HRESULT hr = NOERROR;
    WS_HEAP* heap = NULL;
    WS_FAULT fault;
    WS_MESSAGE* replyMessage = GetReplyMessage();
    WS_CHANNEL* channel = GetChannel();
    WS_ERROR* error = GetError();
    WS_ERROR* returnError = NULL;
    HMODULE module = NULL;

    // We cannot use the existing error here as we are filling it with custom state.
    // This error could be cached and reused, but given that errors should be rare
    // we simply destroy and recreate it.
    IfFailedExit(WsCreateError(NULL, 0, &returnError));
    
    // Get the appropriate error string.
    BOOL ret = GetModuleHandleEx(0, NULL, &module);
    if (!ret)
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        EXIT_FUNCTION
    }

    WCHAR errorString[128];
    DWORD lengthInCharacters = FormatMessageW(
        FORMAT_MESSAGE_FROM_HMODULE | FORMAT_MESSAGE_IGNORE_INSERTS, module, 
        (DWORD)faultType, 0, errorString, WsCountOf(errorString), NULL);
    if (lengthInCharacters == 0)
    {            
        hr = HRESULT_FROM_WIN32(GetLastError());
        EXIT_FUNCTION
    }

    WS_STRING string;
    string.chars = errorString;
    string.length = lengthInCharacters;
    IfFailedExit(WsAddErrorString(returnError, &string));
        
    FreeLibrary(module);
    module = NULL;

    WS_ELEMENT_DESCRIPTION elementDescription;
    ZeroMemory(&elementDescription, sizeof(elementDescription));
    elementDescription.type = WS_FAULT_TYPE;
    
    IfFailedExit(WsResetMessage(replyMessage, error));
    IfFailedExit(WsInitializeMessage(replyMessage, WS_BLANK_MESSAGE, GetRequestMessage(), error));
    IfFailedExit(WsSetHeader(
        replyMessage, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE, 
        WS_WRITE_REQUIRED_VALUE, 
        &faultAction, 
        sizeof(faultAction), 
        error));
    IfFailedExit(WsGetMessageProperty(replyMessage, WS_MESSAGE_PROPERTY_HEAP, &heap, sizeof(heap), error));

    // We put it on the message heap so its cleaned up later when the heap is reset or freed.
    IfFailedExit(WsCreateFaultFromError(returnError, E_FAIL, WS_FULL_FAULT_DISCLOSURE, heap, &fault));
    IfFailedExit(WsWriteMessageStart(channel, replyMessage, NULL, error)); 
    IfFailedExit(WsWriteBody(replyMessage, &elementDescription, WS_WRITE_REQUIRED_VALUE, &fault, sizeof(fault), error));
    
    WsWriteMessageEnd(channel, replyMessage, NULL, error);

    WsFreeError(returnError);

    PrintVerbose(L"Leaving CRequest::SendFault");
    return hr;

    ERROR_EXIT

    server->PrintError(L"CRequest::SendFault", true);
    server->PrintError(hr, error, true); 

    if (NULL != module)
    {
        CloseHandle(module);
    }
    if (NULL != returnError)
    {
        WsFreeError(returnError);
    }
    if (NULL != module)
    {
        FreeLibrary(module);
    }
   
    PrintVerbose(L"Leaving CRequest::SendFault");
    return hr;
}

// The CRequest destructor marks the end of a request loop. So in order to keep the functions in
// the order they are used, this is placed here.
CRequest::~CRequest()
{
    server->PrintVerbose(L"Entering CRequest::~CRequest");    

    CleanupChannel(channel);
    
    if (NULL != requestMessage)
    {
        WsFreeMessage(requestMessage);
    }

    if (NULL != replyMessage)
    {
        WsFreeMessage(replyMessage);
    }

    if (NULL != error)
    {
        WsFreeError(error);
    }

    if (NULL != channel)
    {
        server->GetChannelManager()->ChannelFreed();
    }

    server->PrintVerbose(L"Leaving CRequest::~CRequest");
}

```



## CFileRepClient.cpp


```C++
#include "Service.h"
#include "process.h"
#include "string.h"
#include "strsafe.h"
#include "stdlib.h"
#include "intsafe.h"
#include "assert.h"
#include "wtypes.h"

// This file contains the client-service specific code.

// The client version of ProcessMessage. This is the entry point for the application-specific code.
HRESULT CFileRepClient::ProcessMessage(CRequest * request, const WS_XML_STRING* receivedAction)
{    
    PrintVerbose(L"Entering CFileRepClient::ProcessMessage");

    HRESULT hr = NOERROR;

    WS_CHANNEL * channel = request->GetChannel();
    WS_MESSAGE * requestMessage = request->GetRequestMessage();
    WS_ERROR * error = request->GetError();    

     // Make sure action is what we expect
    if (WsXmlStringEquals(receivedAction, &faultAction, error) == S_OK)
    {        
        PrintInfo(L"Received fault message. Aborting.");
        
        hr = E_FAIL;
        EXIT_FUNCTION
    }

    // Make sure action is what we expect
    if (WsXmlStringEquals(receivedAction, &userRequestAction, error) != S_OK)
    {        
        PrintInfo(L"Received unexpected message");
        
        hr = WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
        EXIT_FUNCTION
    }

    // Get the heap of the message
    WS_HEAP* heap;
    IfFailedExit(WsGetMessageProperty(requestMessage, WS_MESSAGE_PROPERTY_HEAP, &heap, sizeof(heap), error));

    // Read user request
    UserRequest* userRequest = NULL;
    IfFailedExit(WsReadBody(requestMessage, &userRequestElement, WS_READ_REQUIRED_POINTER, heap, &userRequest, sizeof(userRequest), error));

    // Read end of message
    IfFailedExit(WsReadMessageEnd(channel, requestMessage, NULL, error));

    // Sanity check
    if (::wcslen(userRequest->sourcePath) >= MAX_PATH || 
        ::wcslen(userRequest->destinationPath) >= MAX_PATH || 
        ::wcslen(userRequest->serverUri) >= MAX_PATH)
    {
        PrintInfo(L"Invalid request");
        hr = request->SendFault(INVALID_REQUEST);
    }    
    else
    {
        hr = ProcessUserRequest(request, userRequest->sourcePath, 
            userRequest->destinationPath, userRequest->serverUri, userRequest->serverProtocol,
            userRequest->securityMode, userRequest->messageEncoding, userRequest->requestType);
    }

    EXIT

    // The caller handles the failures. So just return the error;
    PrintVerbose(L"Leaving CCFileRepClient::ProcessMessage");

    return hr;
}

// The message exchange pattern when transfering a file is as follows:
// - We get a request message from the command line tool
// - If the request is asynchronous send back a confirmation immediately
// - We send a request for file information to the server service. A discovery request is denoted by a chunk position of -1.
// - We get the file information
// - We request the individual chunks sequentially one by one from the server. 
// Chunks are identified by their position within the file. This could be optimized by asynchronously requesting 
// multiple chunks. However, that is beyond the scope of this version of the sample.
// - Repeat until the file transfer is completed or a failure occurred
// - If the request is synchronous send success or failure message to the command line tool.
// For the individual data structures associated with each message, see common.h.
HRESULT CFileRepClient::ProcessUserRequest(CRequest* request, __in const LPWSTR sourcePath, __in const LPWSTR destinationPath, 
    __in const LPWSTR serverUri, TRANSPORT_MODE transportMode, SECURITY_MODE securityMode, 
    MESSAGE_ENCODING encoding, REQUEST_TYPE requestType)
{
    PrintVerbose(L"Entering CFileRepClient::ProcessUserRequest");
    
    HRESULT hr = NOERROR;
    WS_ERROR* error = request->GetError();
    WS_CHANNEL* serverChannel = NULL;
    WS_MESSAGE* serverRequestMessage = NULL;
    WS_MESSAGE* serverReplyMessage = NULL;
    WS_HEAP* heap = NULL;
    HANDLE file = INVALID_HANDLE_VALUE;
    LPWSTR statusMessage = NULL;
    LONGLONG fileLength = 0;
    long chunkSize = -1;
    DWORD transferTime = 0;
    LARGE_INTEGER size;
    size.QuadPart = 0;
    WS_MESSAGE_PROPERTY heapProperty;

    WS_ENDPOINT_ADDRESS address = {};

    if (ASYNC_REQUEST == requestType)
    {
        // In case of an async request, acknowlege request before doing any actual work.
        IfFailedExit(SendUserResponse(request, TRANSFER_ASYNC));
        PrintInfo(L"Asynchronous request. Sending asynchronous acknowledgement.");
    }

    heapProperty = CFileRepClient::CreateHeapProperty();

    IfFailedExit(CreateServerChannel(encoding, transportMode, securityMode, error, &serverChannel));        
    IfFailedExit(WsCreateMessageForChannel(serverChannel, NULL, 0, &serverRequestMessage, error));    
    IfFailedExit(WsCreateMessageForChannel(serverChannel, &heapProperty, 1, &serverReplyMessage, error));
    
    // Initialize address of service
    address.url.chars = serverUri;
    IfFailedExit(SizeTToULong(::wcslen(address.url.chars),&address.url.length));  
    
    // Open channel to address
    IfFailedExit(WsOpenChannel(serverChannel, &address, NULL, error));
    
     // Initialize file request
    FileRequest fileRequest;
    fileRequest.filePosition = DISCOVERY_REQUEST;
    fileRequest.fileName = sourcePath;

    // We ensured that those are not too long earlier
    SIZE_T strLen = ::wcslen(fileRequest.fileName) + address.url.length + 100;

    statusMessage = (LPWSTR)HeapAlloc(GetProcessHeap(), 0, strLen * sizeof (WCHAR));

    // We do not care about the failure value since in the worst case it truncates, which we
    // still would want to display since its better than nothing.
    StringCchPrintfW(statusMessage, strLen, L"Requesting file %s from server %s.", fileRequest.fileName, address.url.chars);

    statusMessage[strLen-1] = L'\0'; // Terminate string in case StringCchPrintfW fails.
    PrintInfo(statusMessage);    
    
    IfFailedExit(WsCreateHeap(65536, 0, NULL, 0, &heap, NULL));

    WS_MESSAGE_DESCRIPTION fileRequestMessageDescription;
    fileRequestMessageDescription.action = &fileRequestAction;
    fileRequestMessageDescription.bodyElementDescription = &fileRequestElement;

    WS_MESSAGE_DESCRIPTION fileInfoMessageDescription;
    fileInfoMessageDescription.action = &fileInfoAction;
    fileInfoMessageDescription.bodyElementDescription = &fileInfoElement;
    
    // Send discovery request and get file info
    FileInfo* fileInfo;
    IfFailedExit(WsRequestReply(
        serverChannel, 
        serverRequestMessage, 
        &fileRequestMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        &fileRequest, 
        sizeof(fileRequest),
        serverReplyMessage, 
        &fileInfoMessageDescription, 
        WS_READ_REQUIRED_POINTER, 
        heap, 
        &fileInfo, 
        sizeof(fileInfo), 
        NULL, 
        error));
    
    fileLength = fileInfo->fileLength;
    chunkSize = fileInfo->chunkSize;
    size.QuadPart = fileLength;

    if (-1 == fileLength || 0 == chunkSize)
    {
        PrintInfo(L"File does not exist on server.");        
        if (SYNC_REQUEST == requestType)
        {    
            hr = request->SendFault(FILE_DOES_NOT_EXIST);  
        }

        EXIT_FUNCTION
    }

    // For simplicity reasons we do not read alternate data streams.
    file = CreateFileW(destinationPath, GENERIC_READ | GENERIC_WRITE, 0, NULL, CREATE_ALWAYS, FILE_ATTRIBUTE_NORMAL, NULL);

    if (INVALID_HANDLE_VALUE == file)
    {
        PrintInfo(L"Failed to create file");

        if (SYNC_REQUEST == requestType)
        {
            hr = request->SendFault(FAILED_TO_CREATE_FILE);
        }
        EXIT_FUNCTION
    }       

    IfFailedExit(ExtendFile(file, fileLength));

    transferTime = GetTickCount();            

    // This loop could be further optimized by asychronously requesting the individual chunks in
    // parallel and then assembling them later. We chose to draw the line regarding perf optimizations
    // for this version of the code here to avoid the complexity of doing asynchronous file assembly.    

    fileRequest.filePosition = 0;
    while (fileRequest.filePosition < fileLength)
    {
        IfFailedExit(ProcessChunk(chunkSize , file, fileLength, serverRequestMessage, 
            serverReplyMessage, serverChannel, error, &fileRequest));                  
    }

    transferTime = GetTickCount() - transferTime;

    if (SYNC_REQUEST == requestType)
    {        
        hr = SendUserResponse(request, TRANSFER_SUCCESS);
    }

    WCHAR perf[255];
    // This assumes that we did not use more than 4 billion chunks, a pretty reasonable assumption.
    DWORD totalChunks = (DWORD)(fileLength/chunkSize) + 1; 
    if (size.HighPart != 0) // Big file
    {
        // Again failures are ignored since it is just a status message.
        StringCchPrintfW(perf, CountOf(perf), L"Transferred %d%d bytes via %d chunks in %d milliseconds.", 
            size.HighPart, size.LowPart, totalChunks, transferTime);
    }
    else
    {
        StringCchPrintfW(perf, CountOf(perf), L"Transferred %d bytes via %d chunks in %d milliseconds.", 
            size.LowPart, totalChunks, transferTime);
    }

    perf[CountOf(perf)-1] = L'\0'; // Ensures that the buffer is terminated even if StringCChPrintfW fails.
    
    PrintInfo(perf);

    // We fall through here even in the success case due to the cleanup that has to be performed in both cases.    
    EXIT

    //Has to come first so file gets properly deleted on error.
    if (INVALID_HANDLE_VALUE != file)
    {
        if (!CloseHandle(file))
        {
            PrintInfo(L"CFileRepClient::ProcessUserRequest - CloseHandle failed. Potential handle leak.");
        }
    }       
       
    if (NULL != serverRequestMessage)
    {
        WsFreeMessage(serverRequestMessage);
    }
    if (NULL != serverReplyMessage)
    {
        WsFreeMessage(serverReplyMessage);
    }

    CleanupChannel(serverChannel);
 
    if (NULL != statusMessage)
    {
        HeapFree(GetProcessHeap(), 0, statusMessage);
    }

    if (NULL != heap)
    {
        WsFreeHeap(heap);
    }

    if (FAILED(hr))
    {
        DeleteFileW(destinationPath);

        PrintError(L"CFileRepClient::ProcessUserRequest", true);
        PrintError(hr, error, true);                
    }

    PrintVerbose(L"Leaving CFileRepClient::ProcessUserRequest");
    
    return hr;
}

HRESULT CFileRepClient::CreateServerChannel(MESSAGE_ENCODING serverEncoding, TRANSPORT_MODE serverTransportMode, 
    SECURITY_MODE serverSecurityMode, WS_ERROR *error, WS_CHANNEL **channel)
{
    PrintVerbose(L"Entering CFileRepClient::CreateServerChannel");

    WS_SSL_TRANSPORT_SECURITY_BINDING transportSecurityBinding = {};
    WS_SECURITY_DESCRIPTION securityDescription = {};
    WS_SECURITY_DESCRIPTION *pSecurityDescription = NULL;
    WS_SECURITY_BINDING* securityBindings[1];
    HRESULT hr = NOERROR;

    WS_CHANNEL_PROPERTY channelProperty[2];

    // The default maximum message size is 64k. This is not enough as the server may chose to send
    // very large messages to maximize throughput.
    ULONG maxMessageSize = MAXMESSAGESIZE;
    channelProperty[0].id = WS_CHANNEL_PROPERTY_MAX_BUFFERED_MESSAGE_SIZE;
    channelProperty[0].value = &maxMessageSize;
    channelProperty[0].valueSize = sizeof(maxMessageSize);

    WS_ENCODING messageEncoding;
    if (TEXT_ENCODING == serverEncoding)
    {        
        messageEncoding = WS_ENCODING_XML_UTF8;
    }
    else if (BINARY_ENCODING == serverEncoding)
    {
        messageEncoding = WS_ENCODING_XML_BINARY_SESSION_1;
    }
    else
    {
        messageEncoding = WS_ENCODING_XML_MTOM_UTF8;
    }

    channelProperty[1].id = WS_CHANNEL_PROPERTY_ENCODING;
    channelProperty[1].value = &messageEncoding;
    channelProperty[1].valueSize = sizeof(messageEncoding);

    ULONG propCount = 1;
    if (DEFAULT_ENCODING != serverEncoding)
    {
        propCount++;
    }
    
    if (SSL_SECURITY == serverSecurityMode)
    {
        // Initialize a security description for SSL
        transportSecurityBinding.binding.bindingType = WS_SSL_TRANSPORT_SECURITY_BINDING_TYPE;
        securityBindings[0] = &transportSecurityBinding.binding;
        securityDescription.securityBindings = securityBindings;
        securityDescription.securityBindingCount = WsCountOf(securityBindings);
        pSecurityDescription = &securityDescription;
    }

    // Create a channel
    if (TCP_TRANSPORT == serverTransportMode)
    {
        hr = WsCreateChannel(WS_CHANNEL_TYPE_DUPLEX_SESSION, WS_TCP_CHANNEL_BINDING, channelProperty, 
            propCount, pSecurityDescription, channel, error);
    }
    else // HTTP
    {
        hr = WsCreateChannel(WS_CHANNEL_TYPE_REQUEST, WS_HTTP_CHANNEL_BINDING, 
            channelProperty, propCount, pSecurityDescription, channel, error);
    }

    PrintVerbose(L"Leaving CFileRepClient::CreateServerChannel");

    return hr;
}

// Extend the file to the total size needed for performance reasons.
// For a synchronous write such as this this is not a big deal, but if this code
// would be made async then it would be. And even now this is more performant.
HRESULT CFileRepClient::ExtendFile(HANDLE file, LONGLONG length)
{
    LARGE_INTEGER size;
    size.QuadPart = length;
    
    if (!SetFilePointerEx(file, size, NULL, FILE_BEGIN))
    {
        PrintError(L"Error extending file.", true);
        return HRESULT_FROM_WIN32(GetLastError());
        
    }
    if (!SetEndOfFile(file))
    {
        PrintError(L"Error extending file.", true);
        return HRESULT_FROM_WIN32(GetLastError());
    }

    size.QuadPart = 0;

    if (!SetFilePointerEx(file, size, NULL, FILE_BEGIN))
    {
        PrintError(L"Error resetting file.", true);
        return HRESULT_FROM_WIN32(GetLastError());
    }

    return NOERROR;
}

HRESULT CFileRepClient::ProcessChunk(long chunkSize, HANDLE file, LONGLONG fileLength, WS_MESSAGE *requestMessage, 
    WS_MESSAGE *replyMessage, WS_CHANNEL *channel, WS_ERROR *error, FileRequest *request)
{
    PrintVerbose(L"Entering CFileRepClient::ProcessChunk");

    LONGLONG pos = request->filePosition;
    LONGLONG chunkPosition = 0;
    long contentLength = 0;
    HRESULT hr = NOERROR;

    IfFailedExit(WsResetMessage(requestMessage, error));
    IfFailedExit(WsResetMessage(replyMessage, error));

    WS_MESSAGE_DESCRIPTION fileRequestMessageDescription;
    fileRequestMessageDescription.action = &fileRequestAction;
    fileRequestMessageDescription.bodyElementDescription = &fileRequestElement;
     
    IfFailedExit(WsSendMessage(
        channel, 
        requestMessage, 
        &fileRequestMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        request, 
        sizeof(*request), 
        NULL, 
        error));

    // Receive start of message (headers).
    IfFailedExit(WsReadMessageStart(channel, replyMessage, NULL, error));
 
    // Get action value.
    WS_XML_STRING* receivedAction = NULL;
    IfFailedExit(WsGetHeader(
        replyMessage, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE,
        WS_READ_REQUIRED_POINTER,  
        NULL, 
        &receivedAction, 
        sizeof(receivedAction), 
        error)); 
    // Make sure action is what we expect.
    if (WsXmlStringEquals(receivedAction, &fileReplyAction, error) != S_OK)
    {
        hr = WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
        PrintInfo(L"Received unexpected message.\n");

        EXIT_FUNCTION
    }                

    IfFailedExit(DeserializeAndWriteMessage(replyMessage, chunkSize, &chunkPosition, &contentLength, file));

    // Read end of message.
    IfFailedExit(WsReadMessageEnd(channel, replyMessage, NULL, error));

    if (contentLength != chunkSize && contentLength + pos != fileLength || pos != chunkPosition)
    {
        PrintError(L"File message was corrupted. Aborting transfer\n", true);
        hr = E_FAIL;
    }        
    else
    {
        request->filePosition = pos + contentLength;
    }


    EXIT

    if (WS_E_INVALID_FORMAT == hr)
    {
        PrintInfo(L"Deserialization of the message failed.");
    }      

    PrintVerbose(L"Leaving CFileRepClient::ProcessChunk");

    return hr;
}

// It is more efficient to manually read this message instead of using the serializer since otherwise the
// byte array would have to be copied around memory multiple times while here we can stream it directly into the file.
// Since the message is simple this is relatively easy to do and makes the perf gain worth the extra effort. In general,
// one should only go down to this level if the performance gain is significant. For most cases the serialization APIs 
// are the better choice and they also make future changes easier to implement.
HRESULT CFileRepClient::DeserializeAndWriteMessage(WS_MESSAGE *message, long chunkSize, 
    LONGLONG *chunkPosition, long *contentLength, HANDLE file)
{
    PrintVerbose(L"Entering CFileServer::DeserializeAndWriteMessage");
    WS_XML_READER *reader = NULL;    
    HRESULT hr = NOERROR;
    LPWSTR errorString = NULL;
    WS_HEAP* heap = NULL;

    // Create a description for the error text field that we read later.
    WS_ELEMENT_DESCRIPTION errorDescription = {&errorLocalName, &fileChunkNamespace, WS_WSZ_TYPE, NULL};

    // To avoid using too much memory we read and write the message in chunks. 
    long bytesToRead = FILE_CHUNK;
    if (bytesToRead > chunkSize)
    {
        bytesToRead = chunkSize;
    }

    BYTE* buf = NULL;
    ULONG length = 0;
    
    // We do not use WS_ERROR here since this function does not print extended error information.
    // The reason for that is that a failure here is likely due to a malformed message coming in, which
    // is probably a client issue and not an error condition for us. So the caller will print a simple status 
    // message if this fails and call it good.
    IfFailedExit(WsGetMessageProperty(message, WS_MESSAGE_PROPERTY_BODY_READER, &reader, sizeof(reader), NULL));

    // Read to FileChunk element
    IfFailedExit(WsReadToStartElement(reader, &fileChunkLocalName, &fileChunkNamespace, NULL, NULL));

    // Read FileChunk start element
    IfFailedExit(WsReadStartElement(reader, NULL));

    // The next four APIs read the chunk position element. There are helper APIs that can do this for you,
    // but they are more complex to use. For simple types such as integers, doing this manually is easiest.
    // For more complex type the serialization APIs should be used.

    // Read to chunkPosition element
    IfFailedExit(WsReadToStartElement(reader, &chunkPositionLocalName, &fileChunkNamespace, NULL, NULL));

    // Read chunk position start element
    IfFailedExit(WsReadStartElement(reader, NULL));
    
    // Read chunk position
    IfFailedExit(WsReadValue(reader, WS_INT64_VALUE_TYPE, chunkPosition, sizeof(*chunkPosition), NULL));
    
    // Read chunk position end element
    IfFailedExit(WsReadEndElement(reader, NULL));
      
    // Read to file content element
    IfFailedExit(WsReadToStartElement(reader, &fileContentLocalName, &fileChunkNamespace, NULL, NULL));
    
    // Read file content start element
    IfFailedExit(WsReadStartElement(reader, NULL));

    buf = (BYTE*)HeapAlloc(GetProcessHeap(), 0, bytesToRead);
    IfNullExit(buf);
    
    // Read file content into buffer
    // We are reading a chunk of the byte array in the message, writing it to disk and then read
    // the next chunk. That way we only need mimimal amounts of memory compared to the total amount
    // of data transferred. The exact way this is done is subject to perf tweaking.    
    while (true)
    {
        // Read next block of bytes.
        ULONG bytesRead = 0;
        IfFailedExit(WsReadBytes(reader, buf, bytesToRead, &bytesRead, NULL));
  
        if (bytesRead == 0)
        {
            // We read it all.
            break;
        }

        length+=bytesRead;

        ULONG count = 0;

        if (!WriteFile(file, buf, bytesRead, &count, NULL))
        {
            PrintError(L"File write error.", true);
            hr = HRESULT_FROM_WIN32(GetLastError());
            EXIT_FUNCTION
        }    

        if (count != bytesRead)
        {
            PrintError(L"File write error.", true);
            hr = E_FAIL;
            EXIT_FUNCTION
        }    
    }          
    
    // Read file content end element
    IfFailedExit(WsReadEndElement(reader, NULL));

     // Read the error string and write it to a heap.
    IfFailedExit(WsCreateHeap(/*maxSize*/ 1024, /*trimSize*/ 1024, NULL, 0, &heap, NULL));

    // Here it pays to use WsReadElementType instead of manually parsing the element since we require heap memory anyway.
    // This can fail if the error message does not fit on the relatively small heap created for it. The server is not
    // expected to use error messages that long. If we get back such a long message we talk to a buggy or rogue server
    // and failing is the right thing to do.
    IfFailedExit(WsReadElement(reader, &errorDescription, WS_READ_REQUIRED_POINTER, heap, 
        &errorString, sizeof(errorString), NULL));            
    // Read file data end element
    IfFailedExit(WsReadEndElement(reader, NULL));

    *contentLength = length;

    if (lstrcmpW(errorString, &GlobalStrings::noError[0]))
    {
        PrintInfo(L"Chunk transfer failed");
        if (errorString)
        {
            PrintInfo(errorString);
        }
        hr = E_FAIL;
    }

    
    EXIT    

    if (NULL != buf)
    {
        HeapFree(GetProcessHeap(), 0, buf);
    }    
    
    if (heap)
    {
        // Clean up errorString.
        WsResetHeap(heap, NULL);
        WsFreeHeap(heap);
    }

    if (FAILED(hr))
    {
        hr = WS_E_INVALID_FORMAT;
    }
    
    PrintVerbose(L"Leaving CFileRepClient::DeserializeAndWriteMessage");

    return hr;
}

// Tell the command line tool what happened to the request.
HRESULT CFileRepClient::SendUserResponse(CRequest* request, TRANSFER_RESULTS result)
{
    PrintVerbose(L"Entering CFileRepClient::SendUserResponse");

    HRESULT hr = NOERROR;
    WS_ERROR* error = request->GetError();
    WS_MESSAGE *replyMessage = request->GetReplyMessage();
    WS_MESSAGE *requestMessage = request->GetRequestMessage();
    WS_CHANNEL *channel = request->GetChannel();
    
    UserResponse userResponse;
    userResponse.returnValue = result;

    WS_MESSAGE_DESCRIPTION userResponseMessageDescription;
    userResponseMessageDescription.action = &userResponseAction;
    userResponseMessageDescription.bodyElementDescription = &userResponseElement;

    hr = WsSendReplyMessage(
        channel, 
        replyMessage, 
        &userResponseMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        &userResponse, 
        sizeof(userResponse), 
        requestMessage, 
        NULL, error);
    if (FAILED(hr))
    {
        PrintError(L"CFileRepClient::SendUserResponse\n", true);
        PrintError(hr, error, true);
    }

    WsResetMessage(replyMessage, NULL);
        
    PrintVerbose(L"Leaving CFileRepClient::SendUserResponse");

    return hr;
}

```



## CFileRepServer.cpp


```C++
// This file contains the server service specific code.
#include "Service.h"
#include "assert.h"

// The server version of ProcessMessage. This is the entry point for the application-specific code.
HRESULT CFileRepServer::ProcessMessage(CRequest* request, const WS_XML_STRING* receivedAction)
{
    PrintVerbose(L"Entering CFileRepServer::ProcessMessage");

    HRESULT hr = NOERROR;
    FileRequest* fileRequest = NULL;
    WS_MESSAGE* requestMessage = request->GetRequestMessage();
    WS_CHANNEL* channel = request->GetChannel();
    WS_ERROR* error = request->GetError();

    // Make sure action is what we expect
    if (WsXmlStringEquals(receivedAction, &fileRequestAction, error) != S_OK)
    {        
        PrintInfo(L"Illegal action");

        hr = WS_E_ENDPOINT_ACTION_NOT_SUPPORTED;
    }
    else
    {
        // Read file request

        WS_HEAP* heap;
        IfFailedExit(WsGetMessageProperty(requestMessage, WS_MESSAGE_PROPERTY_HEAP, &heap, sizeof(heap), error));
        
        IfFailedExit(WsReadBody(requestMessage, &fileRequestElement, WS_READ_REQUIRED_POINTER,
            heap, &fileRequest, sizeof(fileRequest), error));
        IfFailedExit(WsReadMessageEnd(channel, requestMessage, NULL, error));
        
        IfFailedExit(ReadAndSendFile(request, fileRequest->fileName, fileRequest->filePosition, error));
    }

    EXIT
  
    // We do not print error messages here. That is handled in the caller.
    PrintVerbose(L"Leaving CFileRepServer::ProcessMessage");
    return hr;
}

// Performs the actual file transfer.
// This function will fail to produce a valid file on the client if the file was changed in between requests for chunks.
// There are ways to work around that, but doing so is beyond the scope of this version of the sample. A simple fix would be
// to keep the file open between requests and prevent writing, but in the spirit of web services this app does not maintain
// state between requests.
HRESULT CFileRepServer::ReadAndSendFile(CRequest* request, __in const LPWSTR fileName, LONGLONG chunkPosition, WS_ERROR *error)
{
    PrintVerbose(L"Entering CFileRepServer::ReadAndSendFile");

    HANDLE file = NULL;
    HRESULT hr = NOERROR;
        
    file = CreateFileW(fileName, GENERIC_READ, FILE_SHARE_READ, NULL, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);

    if (INVALID_HANDLE_VALUE == file)
    {        
        PrintInfo(L"Invalid file name");
        if (-1 != chunkPosition)
        {
            hr = SendError(request, GlobalStrings::invalidFileName);
        }
        else
        {
            hr = SendFileInfo(request, fileName, -1, chunkSize);
        }

        PrintVerbose(L"Leaving CFileRepServer::ReadAndSendFile");
        return hr;
    }

    LARGE_INTEGER len;

    if (!GetFileSizeEx(file, &len))
    {    
        hr = HRESULT_FROM_WIN32(GetLastError());
        PrintError(L"Unable to determine file length", true);
        if (FAILED(SendError(request, GlobalStrings::unableToDetermineFileLength)))
        {
            PrintError(L"Unable to send failure back", true);
        }

        if (!CloseHandle(file))
        {
            PrintError(L"Unable to close file handle", true);
        }

        // This has its own return path to ensure that the right error info is returned.
        // The main error path would overwrite it.
        PrintVerbose(L"Leaving CFileRepServer::ReadAndSendFile");
        return hr;
    }

    LONGLONG fileLength = len.QuadPart;        

    if (chunkPosition == DISCOVERY_REQUEST)
    {
        PrintInfo(L"Processing discovery message");
        hr = SendFileInfo(request, fileName, fileLength, chunkSize);
    }
    else if (chunkPosition < -1)
    {        
        PrintInfo(L"Invalid request");
        hr = SendError(request, GlobalStrings::invalidRequest);
    }
    else if (chunkPosition >= fileLength)
    {
        PrintInfo(L"Request out of range of the file");
        hr = SendError(request, GlobalStrings::outOfRange);
    }
    else
    {
        long chunkSize = this->chunkSize;
        if (fileLength - chunkPosition < chunkSize)
        {
            chunkSize = (DWORD)(fileLength - chunkPosition);
        }    

        LARGE_INTEGER pos;
        pos.QuadPart = chunkPosition;

        if (!SetFilePointerEx(file, pos, NULL, FILE_BEGIN))
        {        
            PrintError(L"Unable to set file pointer", true);
            hr = E_FAIL;
            
            // Ignore return value as we already have a failure.
            SendError(request, GlobalStrings::unableToSetFilePointer);
         
        }
        else
        {
            hr = ReadAndSendChunk(request, chunkSize, chunkPosition, file);
        }
    }
       
    if (FAILED(hr))
    {
        PrintError(L"CFileRepServer::ReadAndSendFile\n", true);
        PrintError(hr, error, true);
    }
          
    if (!CloseHandle(file))
    {
        hr = HRESULT_FROM_WIN32(GetLastError());
        PrintError(L"Unable to close file handle", true);
    }    
   
    PrintVerbose(L"Leaving CFileRepServer::ReadAndSendFile");
    return hr;
}

// The first message of a file transfer is a discovery request byt the client. This function handles such requests.
HRESULT CFileRepServer::SendFileInfo(CRequest* request, __in const LPWSTR fileName, LONGLONG fileLength, DWORD chunkSize)
{
    PrintVerbose(L"Entering CFileRepServer::SendFileInfo");

    HRESULT hr = NOERROR;
    WS_ERROR* error = request->GetError();
    WS_MESSAGE *replyMessage = request->GetReplyMessage();
    WS_MESSAGE *requestMessage = request->GetRequestMessage();
    WS_CHANNEL *channel = request->GetChannel();
    
    FileInfo fileInfo;
    fileInfo.fileName = fileName;
    fileInfo.fileLength = fileLength;
    fileInfo.chunkSize = chunkSize;

    WS_MESSAGE_DESCRIPTION fileInfoMessageDescription;
    fileInfoMessageDescription.action = &fileInfoAction;
    fileInfoMessageDescription.bodyElementDescription = &fileInfoElement;

    hr = WsSendReplyMessage(
        channel, 
        replyMessage, 
        &fileInfoMessageDescription, 
        WS_WRITE_REQUIRED_VALUE,
        &fileInfo, 
        sizeof(fileInfo), 
        requestMessage, 
        NULL, 
        error);

    if (FAILED(hr))
    {        
        PrintError(L"CFileRepServer::SendFileInfo", true);
        PrintError(hr, error, true);
    }
    
    WsResetMessage(replyMessage, NULL);

    PrintVerbose(L"Leaving CFileRepServer::SendFileInfo");
    return hr;
}

// Reads the data and serializes it into the message. This function does custom serialization for the same
// reason and with the same alrogithm as DeserializeAndWriteMessage.
HRESULT CFileRepServer::ReadAndSendChunk(CRequest* request, long chunkSize, LONGLONG chunkPosition, HANDLE file)
{
    PrintVerbose(L"Entering CFileRepServer::ReadAndSendChunk");

    if (chunkSize < 0 || chunkPosition < 0)
    {
        PrintVerbose(L"Leaving CFileRepServer::ReadAndSendChunk");
        return E_INVALIDARG;
    }

    HRESULT hr = NOERROR;
    WS_XML_WRITER* writer = NULL;
    WS_MESSAGE *replyMessage = request->GetReplyMessage();
    WS_MESSAGE *requestMessage = request->GetRequestMessage();
    WS_ERROR *error = request->GetError();
    WS_CHANNEL *channel = request->GetChannel();
    
    BYTE* buf = NULL;
    LONG length = 0;

    // To avoid using too much memory we read and write the message in chunks. 
    LONG bytesToRead = FILE_CHUNK;
    if (bytesToRead > chunkSize)
    {
        bytesToRead = chunkSize;
    }

    buf = (BYTE*)HeapAlloc(GetProcessHeap(), 0, bytesToRead);
    IfNullExit(buf);

    IfFailedExit(WsInitializeMessage(replyMessage, WS_BLANK_MESSAGE, requestMessage, error));

    // Add the action header
    IfFailedExit(WsSetHeader(
        replyMessage, 
        WS_ACTION_HEADER, 
        WS_XML_STRING_TYPE,
        WS_WRITE_REQUIRED_VALUE,
        &fileReplyAction, 
        sizeof(fileReplyAction), 
        error));
   
    // Send the message headers
    IfFailedExit(WsWriteMessageStart(channel, replyMessage, NULL, error));

    // Get writer to serialize message body    
    IfFailedExit(WsGetMessageProperty(replyMessage, WS_MESSAGE_PROPERTY_BODY_WRITER, &writer, sizeof(writer), error));

    // Write FileChunk start element.
    // This whole code block is the serialization equivalent of the desiralization code.
    IfFailedExit(WsWriteStartElement(writer, NULL, &fileChunkLocalName, &fileChunkNamespace, error));

    // Write chunkPosition element
    IfFailedExit(WsWriteStartElement(writer, NULL, &chunkPositionLocalName, &fileChunkNamespace, error));    
    IfFailedExit(WsWriteValue(writer, WS_INT64_VALUE_TYPE, &chunkPosition, sizeof(chunkPosition), error));  
    IfFailedExit(WsWriteEndElement(writer, error));
        
    // Write fileContent start element
    IfFailedExit(WsWriteStartElement(writer, NULL, &fileContentLocalName, &fileChunkNamespace, error));    

    // Like in the deserialization code, we read the file in multiple steps to avoid
    // having to have everything in memory at once. The message could potentially be
    // big so this is more efficient.
    while (true)
    {
        ULONG bytesRead = 0;

        if (length + bytesToRead > chunkSize)
        {
            bytesToRead = chunkSize - length;
        }
        
        if (!ReadFile(file, buf, bytesToRead, &bytesRead, NULL))
        {        

            PrintError(L"File read error.", true);
            hr = HRESULT_FROM_WIN32(GetLastError());

            EXIT_FUNCTION
        }

        if (0 == bytesRead)
        {
            // We reched the end of the file before filling the chunk. Send a partial chunk.
            break;
        }

        IfFailedExit(WsWriteBytes(writer, buf, bytesRead, error));

        length += bytesRead;

        if (length == chunkSize)
        {
            // We filled the message
            break;
        }
    }    
    
    // Write fileContent end element
    IfFailedExit(WsWriteEndElement(writer, error));

    // Write error element
    IfFailedExit(WsWriteStartElement(writer, NULL, &errorLocalName, &fileChunkNamespace, error));
    const WCHAR* noError = GlobalStrings::noError;
    IfFailedExit(WsWriteType(
        writer, 
        WS_ELEMENT_TYPE_MAPPING,
        WS_WSZ_TYPE, 
        NULL, 
        WS_WRITE_REQUIRED_POINTER, 
        &noError, 
        sizeof(noError), 
        error));
    
    // Closing elements;
    IfFailedExit(WsWriteEndElement(writer, error));
    IfFailedExit(WsWriteEndElement(writer, error));
    IfFailedExit(WsWriteMessageEnd(channel, replyMessage, NULL, error));

    hr = WsResetMessage(replyMessage, NULL);
    HeapFree(GetProcessHeap(), 0, buf);

    PrintVerbose(L"Leaving CFileRepServer::ReadAndSendChunk");
    return hr;


    ERROR_EXIT

    PrintError(L"CFileRepServer::ReadAndSendChunk", true);
    PrintError(hr, error, true); 
        
    WsResetMessage(replyMessage, NULL);
    if (NULL != buf)
    {
        HeapFree(GetProcessHeap(), 0, buf);
    }
        
    PrintVerbose(L"Leaving CFileRepServer::ReadAndSendChunk");
    return hr;
}

// Construct an error message containing no data except the error string.
HRESULT CFileRepServer::SendError(CRequest* request, __in const WCHAR errorMessage[])
{
    PrintVerbose(L"Entering CFileRepServer::SendError");

    HRESULT hr = NOERROR;
    WS_ERROR* error = request->GetError();
    WS_MESSAGE *replyMessage = request->GetReplyMessage();
    WS_MESSAGE *requestMessage = request->GetRequestMessage();
    WS_CHANNEL *channel = request->GetChannel();

    FileChunk fileChunk;
    fileChunk.fileContent.bytes = NULL;
    fileChunk.fileContent.length = 0;
    fileChunk.chunkPosition = -1;
    fileChunk.error = (LPWSTR)errorMessage;

    WS_MESSAGE_DESCRIPTION fileReplyMessageDescription;
    fileReplyMessageDescription.action = &fileReplyAction;
    fileReplyMessageDescription.bodyElementDescription = &fileChunkElement;

    // As there is no large payload we use the serializer here.
    hr = WsSendReplyMessage(
        channel, 
        replyMessage, 
        &fileReplyMessageDescription,
        WS_WRITE_REQUIRED_VALUE,
        &fileChunk, 
        sizeof(fileChunk), 
        requestMessage, 
        NULL, 
        error);

    if (FAILED(hr))
    {
        PrintError(L"CFileRepServer::SendError\n", true);
        PrintError(hr, error, true);
    }

    WsResetMessage(replyMessage, NULL);
    
    PrintVerbose(L"Leaving CFileRepServer::SendError");

    return hr;
}

```



## common.h


```C++
//
// This file contains definitions that are shared among client and server.
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



## FileRep.mc

``` syntax
MessageIdTypedef=ULONG
LanguageNames=
(
    English=0x409:MSG00409
)
SeverityNames=(
    Success=0x0
    Informational=0x1
    Warning=0x2
    Error=0x3
)
FacilityNames=(
    None=0x0
)

; InvalidRequest
MessageId=0x1
Severity=Success
Facility=None
Language=English
Invalid request.
.

; FileDoesNotExist
MessageId=0x2
Severity=Success
Facility=None
Language=English
File does not exist.
.

; FileCreationError
MessageId=0x3
Severity=Success
Facility=None
Language=English
Failed to create file.
.
```

## FileRep.rc

``` syntax
LANGUAGE 0x9,0x1
1 11 "MSG00409.bin"
```

## Makefile

``` syntax
all: WsFileRepService.exe

$FileRep.h FileRep.rc msg00001.bin: FileRep.mc
    mc -U FileRep.mc
    
FileRep.res: FileRep.rc FileRep.h FileRep.rc msg00001.bin 
    rc -r -fo FileRep.res FileRep.rc
    
CFileRep.obj: CFileRep.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD CFileRep.cpp

CFileRepServer.obj: CFileRepServer.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD CFileRepServer.cpp

CFileRepClient.obj: CFileRepClient.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD CFileRepClient.cpp

CChannelManager.obj: CChannelManager.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD CChannelManager.cpp

CRequest.obj: CRequest.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD CRequest.cpp

Service.obj: Service.cpp
    cl -c -DWIN32 -D_WIN32 -DNDEBUG -GS -D_X86_=1 -D_WIN32_WINNT=0x0601 -DCRTAPI1=_cdecl -DCRTAPI2=_cdecl -D_MT -D_DLL -MD Service.cpp

WsFileRepService.exe: Service.obj CFileRep.obj CFileRepServer.obj CFileRepClient.obj CChannelManager.obj CRequest.obj FileRep.res
    link -release -incremental:no -nologo -subsystem:console,6.01 -out:WsFileRepService.exe Service.obj CFileRep.obj CFileRepServer.obj CFileRepClient.obj CChannelManager.obj CRequest.obj FileRep.res
```

## Related topics

<dl> <dt>

[FileRepToolExample](filereptoolexample.md)
</dt> </dl>

 

 





---
description: Before you can write events to a trace session, you must register your provider.
ms.assetid: 76e7202e-74ce-40a3-a04b-9af5117fe20e
title: Writing Manifest-based Events
ms.topic: article
ms.date: 05/31/2018
---

# Writing Manifest-based Events

Before you can write events to a trace session, you must register your provider. Registering a provider tells ETW that your provider is ready to write events to a trace session. A process can register up to 1,024 provider GUIDs; however, you should limit the number of providers that your process registers to one or two.

**Prior to Windows Vista:** There is no limit to the number of providers that a process can register.

To register a manifest-based provider, call the [**EventRegister**](/windows/desktop/api/Evntprov/nf-evntprov-eventregister) function. The function registers the provider's GUID and identifies an optional callback that ETW calls when a controller enables or disables the provider.

Before the provider exits, call the [**EventUnregister**](/windows/desktop/api/Evntprov/nf-evntprov-eventunregister) function to remove the provider's registration from ETW. The [**EventRegister**](/windows/desktop/api/Evntprov/nf-evntprov-eventregister) function returns the registration handle that you pass to the **EventUnregister** function.

[Manifest-based](about-event-tracing.md) providers do not have to implement an [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback) function to receive notifications when a session enables or disables the provider. The callback is optional and is used for informational purposes; you do not need to specify or implement the callback when registering the provider. A manifest-based provider can simply write events and ETW will decide if the event gets logged to a trace session. If an event requires that you perform extensive work to generate the event's data, you may want to call the [**EventEnabled**](/windows/desktop/api/Evntprov/nf-evntprov-eventenabled) or [**EventProviderEnabled**](/windows/desktop/api/Evntprov/nf-evntprov-eventproviderenabled) function first to verify that the event will be written to a session before performing the work.

Typically, you would implement the callback if your provider requires that the controller pass provider-defined filter data (see the *FilterData* parameter of [**EnableCallback**](/windows/desktop/api/Evntprov/nc-evntprov-penablecallback)) to the provider, or the provider uses the context information that it specified when it registered itself (see the *CallbackContext* parameter of [**EventRegister**](/windows/desktop/api/Evntprov/nf-evntprov-eventregister)).

[Manifest-based](about-event-tracing.md) providers call the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) or [**EventWriteString**](/windows/desktop/api/Evntprov/nf-evntprov-eventwritestring) function to write events to a session. If your event data is a string, or if you do not define a manifest for your provider and your event data is a single string, call the [**EventWriteString**](/windows/desktop/api/Evntprov/nf-evntprov-eventwritestring) function to write the event. For event data that contains numeric or complex data types, call the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) function to log the event.

The following example shows how to prepare the event data to be written using the [**EventWrite**](/windows/desktop/api/Evntprov/nf-evntprov-eventwrite) function. The example references the events defined in [Publishing Your Event Schema for a Manifest-based Provider](publishing-your-event-schema-for-a-manifest-base-provider.md).


```C++
#include <windows.h>
#include <stdio.h>
#include <evntprov.h>
#include "provider.h"  // Generated from manifest

#define SUNDAY     0X1
#define MONDAY     0X2
#define TUESDAY    0X4
#define WEDNESDAY  0X8
#define THURSDAY   0X10
#define FRIDAY     0X20
#define SATURDAY   0X40

enum TRANSFER_TYPE {
  Download = 1,
  Upload,
  UploadReply
};

#define MAX_NAMEDVALUES          5  // Maximum array size
#define MAX_PAYLOAD_DESCRIPTORS  9 + (2 * MAX_NAMEDVALUES)

typedef struct _namedvalue {
  LPWSTR name;
  USHORT value;
} NAMEDVALUE, *PNAMEDVALUE;

void wmain(void)
{
    DWORD status = ERROR_SUCCESS;
    REGHANDLE RegistrationHandle = NULL; 
    EVENT_DATA_DESCRIPTOR Descriptors[MAX_PAYLOAD_DESCRIPTORS]; 
    DWORD i = 0;

    // Data to load into event descriptors

    USHORT Scores[3] = {45, 63, 21};
    ULONG pImage = (ULONG)&Scores;
    DWORD TransferType = Upload;
    DWORD Day = MONDAY | TUESDAY;
    LPWSTR Path = L"c:\\path\\folder\\file.ext";
    BYTE Cert[11] = {0x2, 0x4, 0x8, 0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x0, 0x1};
    PBYTE Guid = (PBYTE) &ProviderGuid;
    USHORT ArraySize = MAX_NAMEDVALUES;
    BOOL IsLocal = TRUE;
    NAMEDVALUE NamedValues[MAX_NAMEDVALUES] = { 
        {L"Bill", 1},
        {L"Bob", 2},
        {L"William", 3},
        {L"Robert", 4},
        {L"", 5}
        };

    status = EventRegister(
        &ProviderGuid,      // GUID that identifies the provider
        NULL,               // Callback not used
        NULL,               // Context noot used
        &RegistrationHandle // Used when calling EventWrite and EventUnregister
        );

    if (ERROR_SUCCESS != status)
    {
        wprintf(L"EventRegister failed with %lu\n", status);
        goto cleanup;
    }
  
    // Load the array of data descriptors for the TransferEvent event. 
    // Add the data to the array in the order of the <data> elements
    // defined in the event's template. 
   
    EventDataDescCreate(&Descriptors[i++], &pImage, sizeof(ULONG));
    EventDataDescCreate(&Descriptors[i++], Scores, sizeof(Scores));
    EventDataDescCreate(&Descriptors[i++], Guid, sizeof(GUID));
    EventDataDescCreate(&Descriptors[i++], Cert, sizeof(Cert));
    EventDataDescCreate(&Descriptors[i++], &IsLocal, sizeof(BOOL));
    EventDataDescCreate(&Descriptors[i++], Path, (ULONG)(wcslen(Path) + 1) * sizeof(WCHAR));
    EventDataDescCreate(&Descriptors[i++], &ArraySize, sizeof(USHORT));

    // If your event contains a structure, you should write each member
    // of the structure separately. If the structure contained integral data types
    // such as DWORDs and the data types were aligned on an 8-byte boundary, you 
    // could use the following call to write the structure, however, you are 
    // encouraged to write the members separately.
    //
    // EventDataDescCreate(&EvtData, struct, sizeof(struct));
    //
    // Because the array of structures in this example contains both strings 
    // and numbers, you must write each member of the structure separately.

    for (int j = 0; j < MAX_NAMEDVALUES; j++)
    {
        EventDataDescCreate(&Descriptors[i++], NamedValues[j].name, (ULONG)(wcslen(NamedValues[j].name)+1) * sizeof(WCHAR) );
        EventDataDescCreate(&Descriptors[i++], &(NamedValues[j].value), sizeof(USHORT) );
    }

    EventDataDescCreate(&Descriptors[i++], &Day, sizeof(DWORD));
    EventDataDescCreate(&Descriptors[i++], &TransferType, sizeof(DWORD));

    // Write the event. You do not have to verify if your provider is enabled before
    // writing the event. ETW will write the event to any session that enabled
    // the provider. If no session enabled the provider, the event is not 
    // written. If you need to perform extra work to write an event that you
    // would not otherwise do, you may want to call the EventEnabled function
    // before performing the extra work. The EventEnabled function tells you if a
    // session has enabled your provider, so you know if you need to perform the 
    // extra work or not.

    status = EventWrite(
        RegistrationHandle,              // From EventRegister
        &TransferEvent,                  // EVENT_DESCRIPTOR generated from the manifest
        (ULONG)MAX_PAYLOAD_DESCRIPTORS,  // Size of the array of EVENT_DATA_DESCRIPTORs
        &Descriptors[0]                  // Array of descriptors that contain the event data
        );

    if (status != ERROR_SUCCESS) 
    {
        wprintf(L"EventWrite failed with 0x%x", status);
    }

cleanup:

    EventUnregister(RegistrationHandle);
}
```



When you compile the manifest (see [Compiling an Instrumentation Manifest](../wes/compiling-an-instrumentation-manifest.md)) that the example above uses, it creates the following header file (referenced in the example above).


```C++
//**********************************************************************`
//* This is an include file generated by Message Compiler.             *`
//*                                                                    *`
//* Copyright (c) Microsoft Corporation. All Rights Reserved.          *`
//**********************************************************************`
#pragma once
//+
// Provider Microsoft-Windows-ETWProvider Event Count 1
//+
EXTERN_C __declspec(selectany) const GUID ProviderGuid = {0xd8909c24, 0x5be9, 0x4502, {0x98, 0xca, 0xab, 0x7b, 0xdc, 0x24, 0x89, 0x9d}};
//
// Keyword
//
#define READ_KEYWORD 0x1
#define WRITE_KEYWORD 0x2
#define LOCAL_KEYWORD 0x4
#define REMOTE_KEYWORD 0x8

//
// Event Descriptors
//
EXTERN_C __declspec(selectany) const EVENT_DESCRIPTOR TransferEvent = {0x1, 0x0, 0x0, 0x4, 0x0, 0x0, 0x5};
#define TransferEvent_value 0x1
#define MSG_Provider_Name                    0x90000001L
#define MSG_Event_WhenToTransfer             0xB0000001L
#define MSG_Map_Download                     0xD0000001L
#define MSG_Map_Upload                       0xD0000002L
#define MSG_Map_UploadReply                  0xD0000003L
#define MSG_Map_Sunday                       0xF0000001L
#define MSG_Map_Monday                       0xF0000002L
#define MSG_Map_Tuesday                      0xF0000003L
#define MSG_Map_Wednesday                    0xF0000004L
#define MSG_Map_Thursday                     0xF0000005L
#define MSG_Map_Friday                       0xF0000006L
#define MSG_Map_Saturday                     0xF0000007L
```



 

 

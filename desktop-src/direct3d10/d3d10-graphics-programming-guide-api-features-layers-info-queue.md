---
description: Customize Debug Output with ID3D10InfoQueue (Direct3D 10)
ms.assetid: 082c7783-c53a-4b73-b8f2-3f60e2c2689a
title: Customize Debug Output with ID3D10InfoQueue (Direct3D 10)
ms.topic: article
ms.date: 05/31/2018
---

# Customize Debug Output with ID3D10InfoQueue (Direct3D 10)

The information queue is managed by an interface (see [**ID3D10InfoQueue Interface**](/windows/desktop/api/D3D10SDKLayers/nn-d3d10sdklayers-id3d10infoqueue)) that stores, retrieves, and filters debug messages. The queue consists of: a message queue, an optional storage filter stack, and a optional retrieval filter stack. The storage-filter stack can be used to filter the messages you want stored; the retrieval-filter stack can be used to filter the messages you want stored. Once you have filtered a message, the message will be printed out to the debug window and stored in the appropriate stack.

In general:

-   Call [**ID3D10InfoQueue::AddApplicationMessage**](/windows/desktop/api/D3D10SDKLayers/nf-d3d10sdklayers-id3d10infoqueue-addapplicationmessage) to generate user-defined messages
-   Call [**ID3D10InfoQueue::GetMessage**](/windows/desktop/api/D3D10SDKLayers/nf-d3d10sdklayers-id3d10infoqueue-getmessage) is used to get messages (that pass an optional retrieval filter).

## Registry Controls

Use registry keys to adjust filter settings, adjust break points, and to mute the debug output. The debug layer will check these paths for registry keys; the first path found will be used.

1.  HKCU\\Software\\Microsoft\\Direct3D\\\<user-defined subkey\>
2.  HKLM\\Software\\Microsoft\\Direct3D\\\<user-defined subkey\>
3.  HKCU\\Software\\Microsoft\\Direct3D

Where:

-   HKCU stand for HKEY\_CURRENT\_USER, and HKLM stand for HKEY\_LOCAL\_MACHINE.
-   \<user-defined subkey\> is an arbitrary name to store debug settings for an application

### Filtering Debug Messages using Registry Keys

If the registry contains an InfoQueueStorageFilterOverride key (and is non-zero), then messages (and debug output) can be filtered by adding the following registry controls.

-   DWORD Mute\_CATEGORY\_\* - Debug output if this key is non-zero.
-   DWORD Mute\_SEVERITY\_\* - Debug output is disabled if this key is non-zero.
-   DWORD Mute\_ID\_\* - Message name or number can be used for \* (just like for BreakOn\_ID\_\* described earlier). Debug output is disabled if this key is non-zero.
-   DWORD Unmute\_SEVERITY\_INFO - Debug output is ENABLED if this key is non-zero. By default when InfoQueueStorageFilterOverride is enabled, debug messages with severity INFO are muted - therefore for this key allows INFO to be turned back on.

These controls change whether a message is recorded or displayed; they do not affect whether an API passes or fails.

### Setting Break Conditions using Registry Keys

Applications can be forced to break on a message using the following registry keys.

**EnableBreakOnMessage** - This key enables breaking on messages (and causes i's SetBreakOnCategory()/SetBreakOnSeverity()/SetBreakOnID() settings to be ignored). The actual messages to break on are defined using one or more BreakOn\_\* values defined below.

-   **BreakOn\_CATEGORY\_\*** - Break on any message passing through the storage filters. \* is one of the D3D10\_MESSAGE\_CATEGORY messages.
-   **BreakOn\_SEVERITY\_\*** - Break on any message passing through the storage filters. \* is one of the D3D10\_MESSAGE\_SEVERITY\_ messages.
-   **BreakOn\_ID\_\*** - Break on any message passing through the storage filters. \* is one of the D3D10\_MESSAGE\_ID\_ messages or can be the numerical value of the error enumeration. For example, Suppose the message with ID "D3D10\_MESSAGE\_ID\_HYPOTHETICAL" had the value 123 in the D3D10\_MESSAGE\_ID enumeration. In this case, creating the value BreakOn\_ID\_HYPOTHETICAL=1 or BreakOn\_ID\_123=1 would both accomplish the same thing - break when a message having ID D3D10\_MESSAGE\_ID\_HYPOTHETICAL is encountered.

### Muting Debug Output using Registry Keys

Debug output can be muted using a MuteDebugOutput key. The presence of this value in the registry forces override of the InfoQueue's [**ID3D10InfoQueue::SetMuteDebugOutput**](/windows/desktop/api/D3D10SDKLayers/nf-d3d10sdklayers-id3d10infoqueue-setmutedebugoutput) method. MuteDebugOutput stops messages that pass the storage filter from being sent to debug output.

## Disabling Debug Layer Messages

Debug layer messages can be disabled individualy or as a group at runtime by specifying filters using [**ID3D10InfoQueue::AddStorageFilterEntries**](/windows/desktop/api/D3D10SDKLayers/nf-d3d10sdklayers-id3d10infoqueue-addstoragefilterentries). The *pFilter* argument to **ID3D10InfoQueue::AddStorageFilterEntries** takes a [**D3D10\_INFO\_QUEUE\_FILTER**](/windows/desktop/api/d3d10sdklayers/ns-d3d10sdklayers-d3d10_info_queue_filter) structure that contains an allow list and a deny list. The allow and deny lists are described by [**D3D10\_INFO\_QUEUE\_FILTER\_DESC**](/windows/desktop/api/d3d10sdklayers/ns-d3d10sdklayers-d3d10_info_queue_filter_desc) structures that allow filtering to be specified by catergory, severity and individual message ID.

The following code is an example of setting up the [**ID3D10InfoQueue Interface**](/windows/desktop/api/D3D10SDKLayers/nn-d3d10sdklayers-id3d10infoqueue) to deny the D3D10\_MESSAGE\_ID\_DEVICE\_DRAW\_INDEX\_BUFFER\_TOO\_SMALL message.


```
  //retrieve the ID3D10InfoQueue from a Direct3D device created with the D3D10_CREATE_DEVICE_DEBUG flag
  ID3D10InfoQueue * pInfoQueue;
    g_pd3dDevice->QueryInterface( __uuidof(ID3D10InfoQueue),  (void **)&pInfoQueue );
    
  //set up the list of messages to filter
    D3D10_MESSAGE_ID messageIDs [] = { D3D10_MESSAGE_ID_DEVICE_DRAW_INDEX_BUFFER_TOO_SMALL };
    
  //set the DenyList to use the list of messages
    D3D10_INFO_QUEUE_FILTER filter = { 0 };
    filter.DenyList.NumIDs = 1;
    filter.DenyList.pIDList = messageIDs;
    
  //apply the filter to the info queue
    pInfoQueue->AddStorageFilterEntries( &filter );  
```



## Related topics

<dl> <dt>

[API Layers](d3d10-graphics-programming-guide-api-features-layers.md)
</dt> <dt>

[API Features (Direct3D 10)](d3d10-graphics-programming-guide-api-features.md)
</dt> </dl>

 

 




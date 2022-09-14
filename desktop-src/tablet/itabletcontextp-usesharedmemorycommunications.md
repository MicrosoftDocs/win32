---
description: Provides access to memory shared between tablet threads.
ms.assetid: 047ff598-7d20-49d7-bdd3-498fe5c778c6
title: ITabletContextP::UseSharedMemoryCommunications method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletContextP.UseSharedMemoryCommunications
api_type: 
- COM
api_location: 
- Wisptis.exe
- Wisptis.exe.dll
---

# ITabletContextP::UseSharedMemoryCommunications method

Provides access to memory shared between tablet threads.

## Syntax


```C++
HRESULT UseSharedMemoryCommunications(
  [in]  DWORD pid,
  [out] DWORD *phEventMoreData,
  [out] DWORD *phEventClientReady,
  [out] DWORD *phMutexAccess,
  [out] DWORD *phFileMapping
);
```



## Parameters

<dl> <dt>

*pid* \[in\]
</dt> <dd>

Process id.

</dd> <dt>

*phEventMoreData* \[out\]
</dt> <dd>

Event handle that signals when new data is available to be processed.

</dd> <dt>

*phEventClientReady* \[out\]
</dt> <dd>

Returned event handle used to signal that the client is ready to receive data. Signaled after processing new data.

</dd> <dt>

*phMutexAccess* \[out\]
</dt> <dd>

The mutex granting access to shared memory.

</dd> <dt>

*phFileMapping* \[out\]
</dt> <dd>

Pointer to the shared memory block.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                            | Description                               |
|----------------------------------------------------------------------------------------|-------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success.<br/>                       |
| <dl> <dt>**E\_FAIL**</dt> </dl> | An unspecified error occurred.<br/> |



 

## Remarks

The **UseSharedMemoryCommunications** method is used as part of the Tablet PC shared memory protocol. Since the Wisptis service has a high integrity level (IL), it can store and access data stored in shared memory without needing to elevate its privileges.

The [**SHAREDMEMORY\_HEADER**](sharedmemory-header.md) structure is cast from the data referenced by the file mapping and the raw packet data follows the **SHAREDMEMORY\_HEADER**. Raw packet data can be read off of the shared memory when the event referenced by *pdwEventClientReady* is raised.

The following list describes the sequence of events for accessing and using shared memory.

-   The client sets the clientReady event.
-   The client waits for the moreData event.
-   The client acquires the mutex.
-   The client reads packet data from the section of shared memory after the header and serial numbers after the packets.
-   The client handles data depending on the value of **dwEvent**.
-   The client writes -1 (0xFFFFFFFF) into **dwEvent**.
-   The client releases the mutex.
-   The client sets the clientReady event.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**ITabletContextP Interface**](itabletcontextp.md)
</dt> <dt>

[**UseNamedSharedMemoryCommunications**](itabletcontextp-usenamedsharedmemorycommunications.md)
</dt> </dl>

 

 





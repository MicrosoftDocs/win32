---
description: Sets up shared memory communication for the tablet context.
ms.assetid: 63e6b271-d89a-4c91-9a15-9e41dcdfa363
title: ITabletContextP::UseNamedSharedMemoryCommunications method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletContextP.UseNamedSharedMemoryCommunications
api_type: 
- COM
api_location: 
- Wisptis.exe
- Wisptis.exe.dll
---

# ITabletContextP::UseNamedSharedMemoryCommunications method

Sets up shared memory communication for the tablet context.

## Syntax


```C++
HRESULT UseNamedSharedMemoryCommunications(
  [in]  DWORD  pid,
  [in]  LPCSTR pszCallerSid,
  [in]  LPCSTR pszCallerIntegritySid,
  [out] DWORD  *pdwEventMoreDataId,
  [out] DWORD  *pdwEventClientReadyId,
  [out] DWORD  *pdwMutexAccessId,
  [out] DWORD  *pdwFileMappingId
);
```



## Parameters

<dl> <dt>

*pid* \[in\]
</dt> <dd>

The process ID of the client that accesses shared memory.

</dd> <dt>

*pszCallerSid* \[in\]
</dt> <dd>

The security identifier of the function caller.

</dd> <dt>

*pszCallerIntegritySid* \[in\]
</dt> <dd>

The security identifier that can verify the integrity of the calling function.

</dd> <dt>

*pdwEventMoreDataId* \[out\]
</dt> <dd>

An integer used to construct the name of an event. The event indicates whether there is more data.

</dd> <dt>

*pdwEventClientReadyId* \[out\]
</dt> <dd>

An integer used to construct the name of an event. The event signals that the client is ready to receive data. The event is signaled after processing new data.

</dd> <dt>

*pdwMutexAccessId* \[out\]
</dt> <dd>

A pointer to the access identifier of the shared memory.

</dd> <dt>

*pdwFileMappingId* \[out\]
</dt> <dd>

An integer that identifies the shared memory.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The **UseNamedSharedMemoryCommunications** method is part of the Tablet PC shared memory protocol. A client without elevated privileges passes in a security identifier (SID) and an integrity level security identifier (IL-SID) so that the Tablet service can use access control lists (ACL) to access the shared memory objects. If the client has elevated privileges, it should use UseSharedMemoryCommunications, which is the API that is called if the service already has an elevated privilege.

The [**SHAREDMEMORY\_HEADER**](sharedmemory-header.md) structure stores the shared memory header.

The [**SHAREDMEMORY\_HEADER**](sharedmemory-header.md) structure is cast from the data referenced by the file mapping. The raw packet data follows the **SHAREDMEMORY\_HEADER**. Raw packet data can be read off of the shared memory when the event referenced by *pdwEventClientReadyId* is raised.

The following list describes the sequence of events for accessing and using shared memory.

1.  The client raises the clientReady event.
2.  The client waits for the moreData event.
3.  The client acquires the mutex.
4.  The client reads packet data from the section of shared memory that follows the header. Serial numbers appear in the shared memory after the packet data.
5.  The client handles data depending on the value of **dwEvent**.
6.  The client writes -1 (0xFFFFFFFF) into **dwEvent**.
7.  The client releases the mutex.
8.  The client raises the clientReady event.

The event names are created by formatting the output of this method. The following definitions can be used in conjunction with sprintf or its equivalent to create the event names.


```C++
#define WISPTIS_SM_MORE_DATA_EVENT_NAME     _T("wisptis-1-%d-%u")
#define WISPTIS_SM_CLIENT_DONE_EVENT_NAME   _T("wisptis-2-%d-%u")
#define WISPTIS_SM_SECTION_NAME             _T("wisptis-3-%d-%u")
#define WISPTIS_SM_THREAD_EVENT_NAME        _T("wisptis-4-%u")
```



In each definition, the %d section is replaced with the process ID, and the %u section is replaced with the integer returned in *pdwEventMoreDataId* or *pdwEventClientReadyId*.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



## See also

<dl> <dt>

[**UseSharedMemoryCommunications**](itabletcontextp-usesharedmemorycommunications.md)
</dt> <dt>

[**ITabletContextP**](itabletcontextp.md)
</dt> </dl>

 

 





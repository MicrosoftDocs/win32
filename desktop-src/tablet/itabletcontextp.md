---
description: Represents the tablet context.
ms.assetid: d518c42d-c2f6-4776-bea5-fecdfe48e260
title: ITabletContextP interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletContextP
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletContextP interface

Represents the tablet context.

## Members

The **ITabletContextP** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITabletContextP** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITabletContextP** interface has these methods.



| Method                                                                                           | Description                                                                     |
|:-------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| [**IsTopMostHook**](itabletcontextp-istopmosthook.md)                                           | Indicates if the tablet context is in the top most hook.<br/>             |
| [**Overlap**](itabletcontextp-overlap.md)                                                       | Moves a tablet context to the front or back of the input queue.<br/>      |
| [**TrackInputRect**](itabletcontextp-trackinputrect.md)                                         | Updates the tablet digitizer to window location mapping coordinates.<br/> |
| [**UseNamedSharedMemoryCommunications**](itabletcontextp-usenamedsharedmemorycommunications.md) | Provides access to memory shared between tablet threads.<br/>             |
| [**UseSharedMemoryCommunications**](itabletcontextp-usesharedmemorycommunications.md)           | Provides access to memory shared between tablet threads.<br/>             |



 

## Remarks

Developers should not use this interface.

[**UseNamedSharedMemoryCommunications**](itabletcontextp-usenamedsharedmemorycommunications.md) is only available on Windows Vista and later.

The following code describes how the **ITabletContextP** interface is defined.

``` syntax
[
    object,
    uuid(22F74D0A-694F-4f47-A5CE-AE08A6409AC8),
    pointer_default(unique)
]
interface ITabletContextP : ITabletContext
{

    HRESULT Overlap([in] BOOL bTop, [out] DWORD *pdwtcid);

    HRESULT GetType([out] CONTEXT_TYPE *pct);

    HRESULT TrackInputRect([out] RECT *prcInput);

    HRESULT IsTopMostHook();

    HRESULT GetEventSink(
        [out] ITabletEventSink **ppSink);

    HRESULT UseSharedMemoryCommunications(
        [in]  DWORD pid,
        [out] DWORD *phEventMoreData,
        [out] DWORD *phEventClientReady,
        [out] DWORD *phMutexAccess,
        [out] DWORD *phFileMapping);

    HRESULT UseNamedSharedMemoryCommunications(
        [in] DWORD pid,
        [in, string] LPCTSTR szSid,
        [in, string] LPCTSTR sdIlSid,
        [out] DWORD *pdwEventMoreDataId,
        [out] DWORD *pdwEventClientReadyId,
        [out] DWORD *pdwMutexAccessId,
        [out] DWORD *pdwFileMappingId);
};
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 


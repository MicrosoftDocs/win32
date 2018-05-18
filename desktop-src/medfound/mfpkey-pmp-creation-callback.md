---
Description: 'Sets a callback that creates the PMP Media Session during source resolution.'
ms.assetid: '7277C5E0-BB91-4EEA-9529-64E66D179CDC'
title: 'MFPKEY\_PMP\_Creation\_Callback property'
---

# MFPKEY\_PMP\_Creation\_Callback property

Sets a callback that creates the [PMP Media Session](pmp-media-session.md) during source resolution.



Data type

PROPVARIANT type (vt)

PROPVARIANT member

**IUnknown\***

VT\_UNKNOWN

**punkVal**



## Remarks

Some protected content might require the use of this property. If so, the source resolution process fails with the error code **MF\_E\_RESOLUTION\_REQUIRES\_PMP\_CREATION\_CALLBACK**.

To use this property, do the following.

1.  Call [**PSCreateMemoryPropertyStore**](properties.PSCreateMemoryPropertyStore) to create a property store.
2.  Implement the [**IMFAsyncCallback**](imfasynccallback.md) callback interface.
3.  Set the MFPKEY\_PMP\_Creation\_Callback property on the property store. The value is a pointer to the [**IMFAsyncCallback**](imfasynccallback.md) implementation.
4.  Call [**IMFSourceResolver::BeginCreateObjectFromURL**](imfsourceresolver-begincreateobjectfromurl.md). Pass in a pointer to the property store in the *pProps* parameter.

In the [**IMFAsyncCallback::Invoke**](imfasynccallback-invoke.md) method of your callback interface, do the following.

1.  Call [**MFCreatePMPMediaSession**](mfcreatepmpmediasession.md) to create the [PMP Media Session](pmp-media-session.md).
2.  Call [**IMFGetService::GetService**](imfgetservice-getservice.md) on the PMP Media Session to a pointer to the [**IMFPMPHost**](imfpmphost.md) interface.
3.  Call [**IMFAsyncResult::GetState**](imfasyncresult-getstate.md) on the result object that is passed in the *pAsyncResult* parameter of [**IMFAsyncCallback::Invoke**](imfasynccallback-invoke.md). Query the returned [**IUnknown**](com.iunknown) pointer for the [**IMFAsyncCallback**](imfasynccallback.md) interface.
4.  Call [**MFPutWorkItem**](mfputworkitem.md) with the following parameters:
    -   *dwQueue*: **MFASYNC\_CALLBACK\_QUEUE\_STANDARD**
    -   *pCallback*: The [**IMFAsyncCallback**](imfasynccallback.md) pointer obtained in step 3.
    -   *pState*: The [**IMFPMPHost**](imfpmphost.md) pointer obtained in step 2.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                  |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                        |
| Header<br/>                   | <dl> <dt>Mfidl.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[PMP Media Session](pmp-media-session.md)
</dt> <dt>

[Protected Media Path](protected-media-path.md)
</dt> <dt>

[Source Resolver](source-resolver.md)
</dt> </dl>

 

 





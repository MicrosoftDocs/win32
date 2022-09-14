---
description: Sets a callback that creates the PMP Media Session during source resolution.
ms.assetid: 7277C5E0-BB91-4EEA-9529-64E66D179CDC
title: MFPKEY_PMP_Creation_Callback property (Mfidl.h)
ms.topic: reference
ms.date: 05/31/2018
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

1.  Call [**PSCreateMemoryPropertyStore**](/windows/win32/api/propsys/nf-propsys-pscreatememorypropertystore) to create a property store.
2.  Implement the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) callback interface.
3.  Set the MFPKEY\_PMP\_Creation\_Callback property on the property store. The value is a pointer to the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) implementation.
4.  Call [**IMFSourceResolver::BeginCreateObjectFromURL**](/windows/desktop/api/mfidl/nf-mfidl-imfsourceresolver-begincreateobjectfromurl). Pass in a pointer to the property store in the *pProps* parameter.

In the [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke) method of your callback interface, do the following.

1.  Call [**MFCreatePMPMediaSession**](/windows/desktop/api/mfidl/nf-mfidl-mfcreatepmpmediasession) to create the [PMP Media Session](pmp-media-session.md).
2.  Call [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) on the PMP Media Session to a pointer to the [**IMFPMPHost**](/windows/desktop/api/mfidl/nn-mfidl-imfpmphost) interface.
3.  Call [**IMFAsyncResult::GetState**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasyncresult-getstate) on the result object that is passed in the *pAsyncResult* parameter of [**IMFAsyncCallback::Invoke**](/windows/desktop/api/mfobjects/nf-mfobjects-imfasynccallback-invoke). Query the returned [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) pointer for the [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) interface.
4.  Call [**MFPutWorkItem**](/windows/desktop/api/mfapi/nf-mfapi-mfputworkitem) with the following parameters:
    -   *dwQueue*: **MFASYNC\_CALLBACK\_QUEUE\_STANDARD**
    -   *pCallback*: The [**IMFAsyncCallback**](/windows/desktop/api/mfobjects/nn-mfobjects-imfasynccallback) pointer obtained in step 3.
    -   *pState*: The [**IMFPMPHost**](/windows/desktop/api/mfidl/nn-mfidl-imfpmphost) pointer obtained in step 2.

## Requirements



| Requirement | Value |
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

 

 

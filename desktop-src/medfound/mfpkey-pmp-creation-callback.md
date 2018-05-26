---
Description: Sets a callback that creates the PMP Media Session during source resolution.
ms.assetid: 7277C5E0-BB91-4EEA-9529-64E66D179CDC
title: MFPKEY\_PMP\_Creation\_Callback property
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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
2.  Implement the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) callback interface.
3.  Set the MFPKEY\_PMP\_Creation\_Callback property on the property store. The value is a pointer to the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) implementation.
4.  Call [**IMFSourceResolver::BeginCreateObjectFromURL**](/windows/win32/mfidl/nf-mfidl-imfsourceresolver-begincreateobjectfromurl?branch=master). Pass in a pointer to the property store in the *pProps* parameter.

In the [**IMFAsyncCallback::Invoke**](/windows/win32/mfobjects/nf-mfobjects-imfasynccallback-invoke?branch=master) method of your callback interface, do the following.

1.  Call [**MFCreatePMPMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatepmpmediasession?branch=master) to create the [PMP Media Session](pmp-media-session.md).
2.  Call [**IMFGetService::GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) on the PMP Media Session to a pointer to the [**IMFPMPHost**](/windows/win32/mfidl/nn-mfidl-imfpmphost?branch=master) interface.
3.  Call [**IMFAsyncResult::GetState**](/windows/win32/mfobjects/nf-mfobjects-imfasyncresult-getstate?branch=master) on the result object that is passed in the *pAsyncResult* parameter of [**IMFAsyncCallback::Invoke**](/windows/win32/mfobjects/nf-mfobjects-imfasynccallback-invoke?branch=master). Query the returned [**IUnknown**](com.iunknown) pointer for the [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) interface.
4.  Call [**MFPutWorkItem**](/windows/win32/mfapi/nf-mfapi-mfputworkitem?branch=master) with the following parameters:
    -   *dwQueue*: **MFASYNC\_CALLBACK\_QUEUE\_STANDARD**
    -   *pCallback*: The [**IMFAsyncCallback**](/windows/win32/mfobjects/nn-mfobjects-imfasynccallback?branch=master) pointer obtained in step 3.
    -   *pState*: The [**IMFPMPHost**](/windows/win32/mfidl/nn-mfidl-imfpmphost?branch=master) pointer obtained in step 2.

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

 

 





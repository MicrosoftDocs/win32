---
Description: Service Interfaces
ms.assetid: 264a0e86-49e9-4777-956b-a83e9db52a25
title: Service Interfaces
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Interfaces

Some interfaces in Media Foundation must be obtained by calling [**IMFGetService::GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) instead of by calling **QueryInterface**. The [**GetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) method works like QueryInterface, but with the following differences:

-   It takes a service identifier GUID in addition to the interface identifier.
-   It can return a pointer to another object that implements the interface, instead of returning a pointer to the original object that is queried.

> [!Note]  
> The [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) interface is very similar to the **IServiceProvider** interface used in some other APIs.

 

A *service* is a particular interface obtained from a particular class of objects through the [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) interface. The following services are defined.



| Service identifier                          | Interface                                                                                                                                | Objects that might expose this service                                                                                                            |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_METADATA\_PROVIDER\_SERVICE             | [**IMFMetadataProvider**](/windows/win32/mfidl/nn-mfidl-imfmetadataprovider?branch=master)                                                                                       | Media sources                                                                                                                                     |
| MF\_MEDIASOURCE\_SERVICE                    | [**IMFMediaSource**](/windows/win32/mfidl/nn-mfidl-imfmediasource?branch=master)                                                                                                 | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_PMP\_SERVER\_CONTEXT                    | [**IMFPMPServer**](/windows/win32/mfidl/nn-mfidl-imfpmpserver?branch=master)                                                                                                     | Protected media path (PMP) Media Session.                                                                                                         |
| MF\_QUALITY\_SERVICES                       | [**IMFQualityAdvise**](/windows/win32/mfidl/nn-mfidl-imfqualityadvise?branch=master)                                                                                             | Media sources.                                                                                                                                    |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateControl**](/windows/win32/mfidl/nn-mfidl-imfratecontrol?branch=master)                                                                                                 | Media sources, Media Session                                                                                                                      |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateSupport**](/windows/win32/mfidl/nn-mfidl-imfratesupport?branch=master)                                                                                                 | Media sources, media sinks, Media Session                                                                                                         |
| MF\_REMOTE\_PROXY                           | [**IMFRemoteProxy**](/windows/win32/mfidl/nn-mfidl-imfremoteproxy?branch=master)                                                                                                 | Proxies for remote objects.                                                                                                                       |
| MF\_SAMI\_SERVICE                           | [**IMFSAMIStyle**](/windows/win32/mfidl/nn-mfidl-imfsamistyle?branch=master)                                                                                                     | Synchronized Accessible Media Interchange (SAMI) media source.                                                                                    |
| MF\_SOURCE\_PRESENTATION\_PROVIDER\_SERVICE | [**IMFMediaSourcePresentationProvider**](/windows/win32/mfidl/nn-mfidl-imfmediasourcepresentationprovider?branch=master)                                                         | Sequencer source                                                                                                                                  |
| MF\_TIMECODE\_SERVICE                       | [**IMFTimecodeTranslate**](/windows/win32/mfidl/nn-mfidl-imftimecodetranslate?branch=master)                                                                                     | ASF media source.                                                                                                                                 |
| MF\_TOPONODE\_ATTRIBUTE\_EDITOR\_SERVICE    | [**IMFTopologyNodeAttributeEditor**](/windows/win32/mfidl/nn-mfidl-imftopologynodeattributeeditor?branch=master)                                                                 | Media session                                                                                                                                     |
| MF\_WRAPPED\_OBJECT                         | [**IMFByteStream**](/windows/win32/mfobjects/nn-mfobjects-imfbytestream?branch=master)                                                                                                   | Wrapped objects                                                                                                                                   |
| MF\_WRAPPED\_BUFFER\_SERVICE                |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WRAPPED\_SAMPLE\_SERVIC                 |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WORKQUEUE\_SERVICES                     | [**IMFWorkQueueServices**](/windows/win32/mfidl/nn-mfidl-imfworkqueueservices?branch=master)                                                                                     | Media session                                                                                                                                     |
| MFNET\_SAVEJOB\_SERVICE                     | [**IMFSaveJob**](/windows/win32/mfidl/nn-mfidl-imfsavejob?branch=master)                                                                                                         | Byte streams                                                                                                                                      |
| MFNETSOURCE\_STATISTICS\_SERVICE            | **IPropertyStore**                                                                                                                       | Network source. Use this service to retrieve network statistics. See [**MFNETSOURCE\_STATISTICS Property**](mfnetsource-statistics-property.md). |
| MR\_AUDIO\_POLICY\_SERVICE                  | [**IMFAudioPolicy**](/windows/win32/mfidl/nn-mfidl-imfaudiopolicy?branch=master)                                                                                                 | Audio renderer                                                                                                                                    |
| MR\_BUFFER\_SERVICE                         | **IDirect3DSurface9**                                                                                                                    | DirectX surface buffers                                                                                                                           |
| MR\_CAPTURE\_POLICY\_VOLUME\_SERVICE        | [**IMFSimpleAudioVolume**](/windows/win32/mfidl/nn-mfidl-imfsimpleaudiovolume?branch=master)                                                                                     | Audio capture source                                                                                                                              |
| MR\_POLICY\_VOLUME\_SERVICE                 | [**IMFSimpleAudioVolume**](/windows/win32/mfidl/nn-mfidl-imfsimpleaudiovolume?branch=master)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_STREAM\_VOLUME\_SERVICE                 | [**IMFAudioStreamVolume**](/windows/win32/mfidl/nn-mfidl-imfaudiostreamvolume?branch=master)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirect3DDeviceManager9**](/windows/win32/dxva2api/nn-dxva2api-idirect3ddevicemanager9?branch=master), [**IDirectXVideoAccelerationService**](/windows/win32/dxva2api/nn-dxva2api-idirectxvideoaccelerationservice?branch=master) | Enhanced video renderer (EVR)                                                                                                                     |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirectXVideoMemoryConfiguration**](/windows/win32/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration?branch=master)                                                             | Input pins on the DirectShow EVR filter                                                                                                           |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IMFVideoSampleAllocator Interface**](/windows/win32/mfidl/nn-mfidl-imfvideosampleallocator?branch=master)                                                                     | EVR stream sinks.                                                                                                                                 |
| MR\_VIDEO\_MIXER\_SERVICE                   | Various interfaces exposed by the EVR mixer. See [Using the Video Mixer Controls](using-the-video-mixer-controls.md).                   | EVR                                                                                                                                               |
| MR\_VIDEO\_RENDER\_SERVICE                  | Various interfaces exposed by the EVR presenter. See [Using the Video Display Controls](using-the-video-display-controls.md).           | EVR                                                                                                                                               |



 

You must use [**GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) to get the interfaces listed in this table from the objects listed in this table.

In some cases, an interface is returned as a service by one class of objects, and returned through **QueryInterface** by another class of objects. The reference pages for each interface indicate when to use [**GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) and when to use **QueryInterface**.

> \[!Caution\]  
> An object might be implemented in such a way that it returns a service interface through **QueryInterface** as well as [**GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master). However, using **QueryInterface** when **GetService** is required might lead to compatibility problems later.

 

The [**MFGetService**](/windows/win32/mfidl/nf-mfidl-mfgetservice?branch=master) function is a helper function that queries an object for [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) and then calls the object's [**GetService**](/windows/win32/mfidl/nf-mfidl-imfgetservice-getservice?branch=master) method.

## Examples

The following example queries the Media Session for [**IMFGetService**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master) and gets the [**IMFRateControl**](/windows/win32/mfidl/nn-mfidl-imfratecontrol?branch=master) interface.


```C++
IMFGetService *pGetService = NULL;
IMFRateControl *pRateControl = NULL;
HRESULT hr = S_OK;

hr = pMediaSession->QueryInterface(
    IID_IMFGetService, 
    (void**)&amp;pGetService);

if (SUCCEEDED(hr))
{
    hr = pGetService->GetService(
        MF_RATE_CONTROL_SERVICE, 
        IID_IMFRateControl,
        (void**)&amp;pRateControl);
}
if (SUCCEEDED(hr))
{
    // Use IMFRateControl. (Not shown.)
}

// Clean up.
SAFE_REELEASE(pGetService);
SAFE_RELEASE(pRateControl);
```



The following example is equivalent to the previous example but uses the [**MFGetService**](/windows/win32/mfidl/nf-mfidl-mfgetservice?branch=master) function.


```C++
IMFRateControl *pRateControl = NULL;
HRESULT hr = S_OK;

hr = MFGetService(
    pMediaSession, 
    MF_RATE_CONTROL_SERVICE, 
    IID_IMFRateControl, 
    (void**) &amp;pRateCtl 
); 
if (SUCCEEDED(hr))
{
    // Use IMFRateControl. (Not shown.)
}

// Clean up.
SAFE_RELEASE(pRateControl);
```



## Related topics

<dl> <dt>

[**IMFGetService Interface**](/windows/win32/mfidl/nn-mfidl-imfgetservice?branch=master)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 





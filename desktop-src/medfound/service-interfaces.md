---
description: Service Interfaces
ms.assetid: 264a0e86-49e9-4777-956b-a83e9db52a25
title: Service Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Service Interfaces

Some interfaces in Media Foundation must be obtained by calling [**IMFGetService::GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) instead of by calling **QueryInterface**. The [**GetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) method works like QueryInterface, but with the following differences:

-   It takes a service identifier GUID in addition to the interface identifier.
-   It can return a pointer to another object that implements the interface, instead of returning a pointer to the original object that is queried.

> [!Note]  
> The [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface is very similar to the **IServiceProvider** interface used in some other APIs.

 

A *service* is a particular interface obtained from a particular class of objects through the [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) interface. The following services are defined.



| Service identifier                          | Interface                                                                                                                                | Objects that might expose this service                                                                                                            |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_METADATA\_PROVIDER\_SERVICE             | [**IMFMetadataProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmetadataprovider)                                                                                       | Media sources                                                                                                                                     |
| MF\_MEDIASOURCE\_SERVICE                    | [**IMFMediaSource**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasource)                                                                                                 | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_PMP\_SERVER\_CONTEXT                    | [**IMFPMPServer**](/windows/desktop/api/mfidl/nn-mfidl-imfpmpserver)                                                                                                     | Protected media path (PMP) Media Session.                                                                                                         |
| MF\_QUALITY\_SERVICES                       | [**IMFQualityAdvise**](/windows/desktop/api/mfidl/nn-mfidl-imfqualityadvise)                                                                                             | Media sources.                                                                                                                                    |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol)                                                                                                 | Media sources, Media Session                                                                                                                      |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateSupport**](/windows/desktop/api/mfidl/nn-mfidl-imfratesupport)                                                                                                 | Media sources, media sinks, Media Session                                                                                                         |
| MF\_REMOTE\_PROXY                           | [**IMFRemoteProxy**](/windows/desktop/api/mfidl/nn-mfidl-imfremoteproxy)                                                                                                 | Proxies for remote objects.                                                                                                                       |
| MF\_SAMI\_SERVICE                           | [**IMFSAMIStyle**](/windows/desktop/api/mfidl/nn-mfidl-imfsamistyle)                                                                                                     | Synchronized Accessible Media Interchange (SAMI) media source.                                                                                    |
| MF\_SOURCE\_PRESENTATION\_PROVIDER\_SERVICE | [**IMFMediaSourcePresentationProvider**](/windows/desktop/api/mfidl/nn-mfidl-imfmediasourcepresentationprovider)                                                         | Sequencer source                                                                                                                                  |
| MF\_TIMECODE\_SERVICE                       | [**IMFTimecodeTranslate**](/windows/desktop/api/mfidl/nn-mfidl-imftimecodetranslate)                                                                                     | ASF media source.                                                                                                                                 |
| MF\_TOPONODE\_ATTRIBUTE\_EDITOR\_SERVICE    | [**IMFTopologyNodeAttributeEditor**](/windows/desktop/api/mfidl/nn-mfidl-imftopologynodeattributeeditor)                                                                 | Media session                                                                                                                                     |
| MF\_WRAPPED\_OBJECT                         | [**IMFByteStream**](/windows/desktop/api/mfobjects/nn-mfobjects-imfbytestream)                                                                                                   | Wrapped objects                                                                                                                                   |
| MF\_WRAPPED\_BUFFER\_SERVICE                |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WRAPPED\_SAMPLE\_SERVIC                 |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WORKQUEUE\_SERVICES                     | [**IMFWorkQueueServices**](/windows/desktop/api/mfidl/nn-mfidl-imfworkqueueservices)                                                                                     | Media session                                                                                                                                     |
| MFNET\_SAVEJOB\_SERVICE                     | [**IMFSaveJob**](/windows/desktop/api/mfidl/nn-mfidl-imfsavejob)                                                                                                         | Byte streams                                                                                                                                      |
| MFNETSOURCE\_STATISTICS\_SERVICE            | **IPropertyStore**                                                                                                                       | Network source. Use this service to retrieve network statistics. See [**MFNETSOURCE\_STATISTICS Property**](mfnetsource-statistics-property.md). |
| MR\_AUDIO\_POLICY\_SERVICE                  | [**IMFAudioPolicy**](/windows/desktop/api/mfidl/nn-mfidl-imfaudiopolicy)                                                                                                 | Audio renderer                                                                                                                                    |
| MR\_BUFFER\_SERVICE                         | **IDirect3DSurface9**                                                                                                                    | DirectX surface buffers                                                                                                                           |
| MR\_CAPTURE\_POLICY\_VOLUME\_SERVICE        | [**IMFSimpleAudioVolume**](/windows/desktop/api/mfidl/nn-mfidl-imfsimpleaudiovolume)                                                                                     | Audio capture source                                                                                                                              |
| MR\_POLICY\_VOLUME\_SERVICE                 | [**IMFSimpleAudioVolume**](/windows/desktop/api/mfidl/nn-mfidl-imfsimpleaudiovolume)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_STREAM\_VOLUME\_SERVICE                 | [**IMFAudioStreamVolume**](/windows/desktop/api/mfidl/nn-mfidl-imfaudiostreamvolume)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirect3DDeviceManager9**](/windows/desktop/api/dxva2api/nn-dxva2api-idirect3ddevicemanager9), [**IDirectXVideoAccelerationService**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideoaccelerationservice) | Enhanced video renderer (EVR)                                                                                                                     |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirectXVideoMemoryConfiguration**](/windows/desktop/api/dxva2api/nn-dxva2api-idirectxvideomemoryconfiguration)                                                             | Input pins on the DirectShow EVR filter                                                                                                           |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IMFVideoSampleAllocator Interface**](/windows/desktop/api/mfidl/nn-mfidl-imfvideosampleallocator)                                                                     | EVR stream sinks.                                                                                                                                 |
| MR\_VIDEO\_MIXER\_SERVICE                   | Various interfaces exposed by the EVR mixer. See [Using the Video Mixer Controls](using-the-video-mixer-controls.md).                   | EVR                                                                                                                                               |
| MR\_VIDEO\_RENDER\_SERVICE                  | Various interfaces exposed by the EVR presenter. See [Using the Video Display Controls](using-the-video-display-controls.md).           | EVR                                                                                                                                               |



 

You must use [**GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) to get the interfaces listed in this table from the objects listed in this table.

In some cases, an interface is returned as a service by one class of objects, and returned through **QueryInterface** by another class of objects. The reference pages for each interface indicate when to use [**GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) and when to use **QueryInterface**.

> [!Caution]  
> An object might be implemented in such a way that it returns a service interface through **QueryInterface** as well as [**GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice). However, using **QueryInterface** when **GetService** is required might lead to compatibility problems later.

 

The [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) function is a helper function that queries an object for [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) and then calls the object's [**GetService**](/windows/desktop/api/mfidl/nf-mfidl-imfgetservice-getservice) method.

## Examples

The following example queries the Media Session for [**IMFGetService**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice) and gets the [**IMFRateControl**](/windows/desktop/api/mfidl/nn-mfidl-imfratecontrol) interface.


```C++
IMFGetService *pGetService = NULL;
IMFRateControl *pRateControl = NULL;
HRESULT hr = S_OK;

hr = pMediaSession->QueryInterface(
    IID_IMFGetService, 
    (void**)&pGetService);

if (SUCCEEDED(hr))
{
    hr = pGetService->GetService(
        MF_RATE_CONTROL_SERVICE, 
        IID_IMFRateControl,
        (void**)&pRateControl);
}
if (SUCCEEDED(hr))
{
    // Use IMFRateControl. (Not shown.)
}

// Clean up.
SAFE_REELEASE(pGetService);
SAFE_RELEASE(pRateControl);
```



The following example is equivalent to the previous example but uses the [**MFGetService**](/windows/desktop/api/mfidl/nf-mfidl-mfgetservice) function.


```C++
IMFRateControl *pRateControl = NULL;
HRESULT hr = S_OK;

hr = MFGetService(
    pMediaSession, 
    MF_RATE_CONTROL_SERVICE, 
    IID_IMFRateControl, 
    (void**) &pRateCtl 
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

[**IMFGetService Interface**](/windows/desktop/api/mfidl/nn-mfidl-imfgetservice)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 





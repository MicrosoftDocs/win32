---
Description: Service Interfaces
ms.assetid: '264a0e86-49e9-4777-956b-a83e9db52a25'
title: Service Interfaces
---

# Service Interfaces

Some interfaces in Media Foundation must be obtained by calling [**IMFGetService::GetService**](imfgetservice-getservice.md) instead of by calling **QueryInterface**. The [**GetService**](imfgetservice.md) method works like QueryInterface, but with the following differences:

-   It takes a service identifier GUID in addition to the interface identifier.
-   It can return a pointer to another object that implements the interface, instead of returning a pointer to the original object that is queried.

> [!Note]  
> The [**IMFGetService**](imfgetservice.md) interface is very similar to the **IServiceProvider** interface used in some other APIs.

 

A *service* is a particular interface obtained from a particular class of objects through the [**IMFGetService**](imfgetservice.md) interface. The following services are defined.



| Service identifier                          | Interface                                                                                                                                | Objects that might expose this service                                                                                                            |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| MF\_METADATA\_PROVIDER\_SERVICE             | [**IMFMetadataProvider**](imfmetadataprovider.md)                                                                                       | Media sources                                                                                                                                     |
| MF\_MEDIASOURCE\_SERVICE                    | [**IMFMediaSource**](imfmediasource.md)                                                                                                 | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_PMP\_SERVER\_CONTEXT                    | [**IMFPMPServer**](imfpmpserver.md)                                                                                                     | Protected media path (PMP) Media Session.                                                                                                         |
| MF\_QUALITY\_SERVICES                       | [**IMFQualityAdvise**](imfqualityadvise.md)                                                                                             | Media sources.                                                                                                                                    |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateControl**](imfratecontrol.md)                                                                                                 | Media sources, Media Session                                                                                                                      |
| MF\_RATE\_CONTROL\_SERVICE                  | [**IMFRateSupport**](imfratesupport.md)                                                                                                 | Media sources, media sinks, Media Session                                                                                                         |
| MF\_REMOTE\_PROXY                           | [**IMFRemoteProxy**](imfremoteproxy.md)                                                                                                 | Proxies for remote objects.                                                                                                                       |
| MF\_SAMI\_SERVICE                           | [**IMFSAMIStyle**](imfsamistyle.md)                                                                                                     | Synchronized Accessible Media Interchange (SAMI) media source.                                                                                    |
| MF\_SOURCE\_PRESENTATION\_PROVIDER\_SERVICE | [**IMFMediaSourcePresentationProvider**](imfmediasourcepresentationprovider.md)                                                         | Sequencer source                                                                                                                                  |
| MF\_TIMECODE\_SERVICE                       | [**IMFTimecodeTranslate**](imftimecodetranslate.md)                                                                                     | ASF media source.                                                                                                                                 |
| MF\_TOPONODE\_ATTRIBUTE\_EDITOR\_SERVICE    | [**IMFTopologyNodeAttributeEditor**](imftopologynodeattributeeditor.md)                                                                 | Media session                                                                                                                                     |
| MF\_WRAPPED\_OBJECT                         | [**IMFByteStream**](imfbytestream.md)                                                                                                   | Wrapped objects                                                                                                                                   |
| MF\_WRAPPED\_BUFFER\_SERVICE                |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WRAPPED\_SAMPLE\_SERVIC                 |                                                                                                                                          | Supported in Windows 8.1 and later.<br/>                                                                                                    |
| MF\_WORKQUEUE\_SERVICES                     | [**IMFWorkQueueServices**](imfworkqueueservices.md)                                                                                     | Media session                                                                                                                                     |
| MFNET\_SAVEJOB\_SERVICE                     | [**IMFSaveJob**](imfsavejob.md)                                                                                                         | Byte streams                                                                                                                                      |
| MFNETSOURCE\_STATISTICS\_SERVICE            | **IPropertyStore**                                                                                                                       | Network source. Use this service to retrieve network statistics. See [**MFNETSOURCE\_STATISTICS Property**](mfnetsource-statistics-property.md). |
| MR\_AUDIO\_POLICY\_SERVICE                  | [**IMFAudioPolicy**](imfaudiopolicy.md)                                                                                                 | Audio renderer                                                                                                                                    |
| MR\_BUFFER\_SERVICE                         | **IDirect3DSurface9**                                                                                                                    | DirectX surface buffers                                                                                                                           |
| MR\_CAPTURE\_POLICY\_VOLUME\_SERVICE        | [**IMFSimpleAudioVolume**](imfsimpleaudiovolume.md)                                                                                     | Audio capture source                                                                                                                              |
| MR\_POLICY\_VOLUME\_SERVICE                 | [**IMFSimpleAudioVolume**](imfsimpleaudiovolume.md)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_STREAM\_VOLUME\_SERVICE                 | [**IMFAudioStreamVolume**](imfaudiostreamvolume.md)                                                                                     | Audio renderer                                                                                                                                    |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md), [**IDirectXVideoAccelerationService**](idirectxvideoaccelerationservice.md) | Enhanced video renderer (EVR)                                                                                                                     |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IDirectXVideoMemoryConfiguration**](idirectxvideomemoryconfiguration.md)                                                             | Input pins on the DirectShow EVR filter                                                                                                           |
| MR\_VIDEO\_ACCELERATION\_SERVICE            | [**IMFVideoSampleAllocator Interface**](imfvideosampleallocator.md)                                                                     | EVR stream sinks.                                                                                                                                 |
| MR\_VIDEO\_MIXER\_SERVICE                   | Various interfaces exposed by the EVR mixer. See [Using the Video Mixer Controls](using-the-video-mixer-controls.md).                   | EVR                                                                                                                                               |
| MR\_VIDEO\_RENDER\_SERVICE                  | Various interfaces exposed by the EVR presenter. See [Using the Video Display Controls](using-the-video-display-controls.md).           | EVR                                                                                                                                               |



 

You must use [**GetService**](imfgetservice-getservice.md) to get the interfaces listed in this table from the objects listed in this table.

In some cases, an interface is returned as a service by one class of objects, and returned through **QueryInterface** by another class of objects. The reference pages for each interface indicate when to use [**GetService**](imfgetservice-getservice.md) and when to use **QueryInterface**.

> \[!Caution\]  
> An object might be implemented in such a way that it returns a service interface through **QueryInterface** as well as [**GetService**](imfgetservice-getservice.md). However, using **QueryInterface** when **GetService** is required might lead to compatibility problems later.

 

The [**MFGetService**](mfgetservice.md) function is a helper function that queries an object for [**IMFGetService**](imfgetservice.md) and then calls the object's [**GetService**](imfgetservice-getservice.md) method.

## Examples

The following example queries the Media Session for [**IMFGetService**](imfgetservice.md) and gets the [**IMFRateControl**](imfratecontrol.md) interface.


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



The following example is equivalent to the previous example but uses the [**MFGetService**](mfgetservice.md) function.


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

[**IMFGetService Interface**](imfgetservice.md)
</dt> <dt>

[Media Foundation Platform APIs](media-foundation-platform-apis.md)
</dt> </dl>

 

 





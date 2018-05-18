---
Description: 'This topic describes how to support DirectX Video Acceleration (DXVA) 2.0 in a DirectShow decoder filter.'
ms.assetid: '40deaddb-bb17-4a34-8294-5c7dc8a8a457'
title: 'Supporting DXVA 2.0 in DirectShow'
---

# Supporting DXVA 2.0 in DirectShow

This topic describes how to support DirectX Video Acceleration (DXVA) 2.0 in a DirectShow decoder filter. Specifically, it describes the communication between the decoder and the video renderer. This topic does not describe how to implement DXVA decoding.

-   [Prerequisites](#prerequisites)
-   [Migration Notes](#migration-notes)
-   [Finding a Decoder Configuration](#finding-a-decoder-configuration)
-   [Notifying the Video Renderer](#notifying-the-video-renderer)
-   [Allocating Uncompressed Buffers](#allocating-uncompressed-buffers)
-   [Decoding](#decoding)
-   [Related topics](#related-topics)

## Prerequisites

This topic assumes that you are familiar with writing DirectShow filters. For more information, see the topic [Writing DirectShow Filters](dshow.writing_directshow_filters) in the DirectShow SDK documentation. The code examples in this topic assume that the decoder filter is derived from the [**CTransformFilter**](dshow.ctransformfilter) class, with the following class definition:


```C++
class CDecoder : public CTransformFilter
{
public:
    static CUnknown* WINAPI CreateInstance(IUnknown *pUnk, HRESULT *pHr);

    HRESULT CompleteConnect(PIN_DIRECTION direction, IPin *pPin);

    HRESULT InitAllocator(IMemAllocator **ppAlloc);
    HRESULT DecideBufferSize(IMemAllocator *pAlloc, ALLOCATOR_PROPERTIES *pProp);

    // TODO: The implementations of these methods depend on the specific decoder.
    HRESULT CheckInputType(const CMediaType *mtIn);
    HRESULT CheckTransform(const CMediaType *mtIn, const CMediaType *mtOut);
    HRESULT CTransformFilter::GetMediaType(int,CMediaType *);

private:
    CDecoder(HRESULT *pHr);
    ~CDecoder();

    CBasePin * GetPin(int n);

    HRESULT ConfigureDXVA2(IPin *pPin);
    HRESULT SetEVRForDXVA2(IPin *pPin);

    HRESULT FindDecoderConfiguration(
        /* [in] */  IDirectXVideoDecoderService *pDecoderService,
        /* [in] */  const GUID&amp; guidDecoder, 
        /* [out] */ DXVA2_ConfigPictureDecode *pSelectedConfig,
        /* [out] */ BOOL *pbFoundDXVA2Configuration
        );

private:
    IDirectXVideoDecoderService *m_pDecoderService;

    DXVA2_ConfigPictureDecode m_DecoderConfig;
    GUID                      m_DecoderGuid;
    HANDLE                    m_hDevice;

    FOURCC                    m_fccOutputFormat;
};
```



In the remainder of this topic, the term *decoder* refers to the decoder filter, which receives compressed video and outputs uncompressed video. The term *decoder device* refers to a hardware video accelerator implemented by the graphics driver.

Here are the basic steps that a decoder filter must perform to support DXVA 2.0:

1.  Negotiate a media type.
2.  Find a DXVA decoder configuration.
3.  Notify the video renderer that the decoder is using DXVA decoding.
4.  Provide a custom allocator that allocates Direct3D surfaces.

These steps are described in more detail in the remainder of this topic.

## Migration Notes

If you are migrating from DXVA 1.0, you should be aware of some significant differences between the two versions:

-   DXVA 2.0 does not use the [**IAMVideoAccelerator**](dshow.iamvideoaccelerator) and [**IAMVideoAcceleratorNotify**](dshow.iamvideoacceleratornotify) interfaces, because the decoder can access the DXVA 2.0 APIs directly through the [**IDirectXVideoDecoder**](idirectxvideodecoder.md) interface.
-   During media type negotiation, the decoder does not use a video acceleration GUID as the subtype. Instead, the subtype is just the uncompressed video format (such as NV12), as with software decoding.
-   The procedure for configuring the accelerator has changed. In DXVA 1.0, the decoder calls **Execute** with a **DXVA\_ConfigPictureDecode** structure to configure the accerlator. In DXVA 2.0, the decoder uses the [**IDirectXVideoDecoderService**](idirectxvideodecoderservice.md) interface, as described in the next section.
-   The decoder allocates the uncompressed buffers. The video renderer no longer allocates them.
-   Instead of calling [**IAMVideoAccelerator::DisplayFrame**](dshow.iamvideoaccelerator_displayframe) to display the decoded frame, the decoder delivers the frame to the renderer by calling [**IMemInputPin::Receive**](dshow.imeminputpin_receive), as with software decoding.
-   The decoder is no longer responsible for checking when data buffers are safe for updates. Therefore DXVA 2.0 does not have any method equivalent to [**IAMVideoAccelerator::QueryRenderStatus**](dshow.iamvideoaccelerator_queryrenderstatus).
-   Subpicture blending is done by the video renderer, using the DXVA2.0 video processor APIs. Decoders that provide subpictures (for example, DVD decoders) should send subpicture data on a separate output pin.

For decoding operations, DXVA 2.0 uses the same data structures as DXVA 1.0.

The enhanced video renderer (EVR) filter supports DXVA 2.0. The Video Mixing Renderer filters (VMR-7 and VMR-9) support DXVA 1.0 only.

## Finding a Decoder Configuration

After the decoder negotiates the output media type, it must find a compatible configuration for the DXVA decoder device. You can perform this step inside the output pin's [**CBaseOutputPin::CompleteConnect**](dshow.cbaseoutputpin_completeconnect) method. This step ensures that the graphics driver supports the capabilities needed by the decoder, before the decoder commits to using DXVA.

To find a configuration for the decoder device, do the following:

1.  Query the renderer's input pin for the [**IMFGetService**](imfgetservice.md) interface.
2.  Call [**IMFGetService::GetService**](imfgetservice-getservice.md) to get a pointer to the [**IDirect3DDeviceManager9**](idirect3ddevicemanager9.md) interface. The service GUID is MR\_VIDEO\_ACCELERATION\_SERVICE.
3.  Call [**IDirect3DDeviceManager9::OpenDeviceHandle**](idirect3ddevicemanager9-opendevicehandle.md) to get a handle to the renderer's Direct3D device.
4.  Call [**IDirect3DDeviceManager9::GetVideoService**](idirect3ddevicemanager9-getvideoservice.md) and pass in the device handle. This method returns a pointer to the [**IDirectXVideoDecoderService**](idirectxvideodecoderservice.md) interface.
5.  Call [**IDirectXVideoDecoderService::GetDecoderDeviceGuids**](idirectxvideodecoderservice-getdecoderdeviceguids.md). This method returns an array of decoder device GUIDs.
6.  Loop through the array of decoder GUIDs to find the ones that the decoder filter supports. For example, for an MPEG-2 decoder, you would look for **DXVA2\_ModeMPEG2\_MOCOMP**, **DXVA2\_ModeMPEG2\_IDCT**, or **DXVA2\_ModeMPEG2\_VLD**.

7.  When you find a candidate decoder device GUID, pass the GUID to the [**IDirectXVideoDecoderService::GetDecoderRenderTargets**](idirectxvideodecoderservice-getdecoderrendertargets.md) method. This method returns an array of render target formats, specified as **D3DFORMAT** values.
8.  Loop through the render target formats and look for one that matches your output format. Typically, a decoder device supports a single render target format. The decoder filter should connect to the renderer using this subtype. In the first call to [**CompleteConnect**](dshow.cbaseoutputpin_completeconnect), the decoder can determing the render target format and then return this format as a preferred output type.

9.  Call [**IDirectXVideoDecoderService::GetDecoderConfigurations**](idirectxvideodecoderservice-getdecoderconfigurations.md). Pass in the same decoder device GUID, along with a [**DXVA2\_VideoDesc**](dxva2-videodesc.md) structure that describes the proposed format. The method returns an array of [**DXVA2\_ConfigPictureDecode**](dxva2-configpicturedecode.md) structures. Each structure describes one possible configuration for the decoder device.

10. Assuming that the previous steps are successful, store the Direct3D device handle, the decoder device GUID, and the configuration structure. The filter will use this information to create the decoder device.

The following code shows how to find a decoder configuration.


```C++
HRESULT CDecoder::ConfigureDXVA2(IPin *pPin)
{
    UINT    cDecoderGuids = 0;
    BOOL    bFoundDXVA2Configuration = FALSE;
    GUID    guidDecoder = GUID_NULL;

    DXVA2_ConfigPictureDecode config;
    ZeroMemory(&amp;config, sizeof(config));

    // Variables that follow must be cleaned up at the end.

    IMFGetService               *pGetService = NULL;
    IDirect3DDeviceManager9     *pDeviceManager = NULL;
    IDirectXVideoDecoderService *pDecoderService = NULL;

    GUID   *pDecoderGuids = NULL; // size = cDecoderGuids
    HANDLE hDevice = INVALID_HANDLE_VALUE;

    // Query the pin for IMFGetService.
    HRESULT hr = pPin->QueryInterface(IID_PPV_ARGS(&amp;pGetService));

    // Get the Direct3D device manager.
    if (SUCCEEDED(hr))
    {
        hr = pGetService->GetService(

            MR_VIDEO_ACCELERATION_SERVICE,
            IID_PPV_ARGS(&amp;pDeviceManager)
            );
    }

    // Open a new device handle.
    if (SUCCEEDED(hr))
    {
        hr = pDeviceManager->OpenDeviceHandle(&amp;hDevice);
    } 

    // Get the video decoder service.
    if (SUCCEEDED(hr))
    {
        hr = pDeviceManager->GetVideoService(
            hDevice, IID_PPV_ARGS(&amp;pDecoderService));
    }

    // Get the decoder GUIDs.
    if (SUCCEEDED(hr))
    {
        hr = pDecoderService->GetDecoderDeviceGuids(
            &amp;cDecoderGuids, &amp;pDecoderGuids);
    }

    if (SUCCEEDED(hr))
    {
        // Look for the decoder GUIDs we want.
        for (UINT iGuid = 0; iGuid < cDecoderGuids; iGuid++)
        {
            // Do we support this mode?
            if (!IsSupportedDecoderMode(pDecoderGuids[iGuid]))
            {
                continue;
            }

            // Find a configuration that we support. 
            hr = FindDecoderConfiguration(pDecoderService, pDecoderGuids[iGuid],
                &amp;config, &amp;bFoundDXVA2Configuration);
            if (FAILED(hr))
            {
                break;
            }

            if (bFoundDXVA2Configuration)
            {
                // Found a good configuration. Save the GUID and exit the loop.
                guidDecoder = pDecoderGuids[iGuid];
                break;
            }
        }
    }

    if (!bFoundDXVA2Configuration)
    {
        hr = E_FAIL; // Unable to find a configuration.
    }

    if (SUCCEEDED(hr))
    {
        // Store the things we will need later.

        SafeRelease(&amp;m_pDecoderService);
        m_pDecoderService = pDecoderService;
        m_pDecoderService->AddRef();

        m_DecoderConfig = config;
        m_DecoderGuid = guidDecoder;
        m_hDevice = hDevice;
    }

    if (FAILED(hr))
    {
        if (hDevice != INVALID_HANDLE_VALUE)
        {
            pDeviceManager->CloseDeviceHandle(hDevice);
        }
    }

    SafeRelease(&amp;pGetService);
    SafeRelease(&amp;pDeviceManager);
    SafeRelease(&amp;pDecoderService);
    return hr;
}
HRESULT CDecoder::FindDecoderConfiguration(
    /* [in] */  IDirectXVideoDecoderService *pDecoderService,
    /* [in] */  const GUID&amp; guidDecoder, 
    /* [out] */ DXVA2_ConfigPictureDecode *pSelectedConfig,
    /* [out] */ BOOL *pbFoundDXVA2Configuration
    )
{
    HRESULT hr = S_OK;
    UINT cFormats = 0;
    UINT cConfigurations = 0;

    D3DFORMAT                   *pFormats = NULL;     // size = cFormats
    DXVA2_ConfigPictureDecode   *pConfig = NULL;      // size = cConfigurations

    // Find the valid render target formats for this decoder GUID.
    hr = pDecoderService->GetDecoderRenderTargets(
        guidDecoder,
        &amp;cFormats,
        &amp;pFormats
        );

    if (SUCCEEDED(hr))
    {
        // Look for a format that matches our output format.
        for (UINT iFormat = 0; iFormat < cFormats;  iFormat++)
        {
            if (pFormats[iFormat] != (D3DFORMAT)m_fccOutputFormat)
            {
                continue;
            }

            // Fill in the video description. Set the width, height, format, 
            // and frame rate.
            DXVA2_VideoDesc videoDesc = {0};

            FillInVideoDescription(&amp;videoDesc); // Private helper function.
            videoDesc.Format = pFormats[iFormat];

            // Get the available configurations.
            hr = pDecoderService->GetDecoderConfigurations(
                guidDecoder,
                &amp;videoDesc,
                NULL, // Reserved.
                &amp;cConfigurations,
                &amp;pConfig
                );

            if (FAILED(hr))
            {
                break;
            }

            // Find a supported configuration.
            for (UINT iConfig = 0; iConfig < cConfigurations; iConfig++)
            {
                if (IsSupportedDecoderConfig(pConfig[iConfig]))
                {
                    // This configuration is good.
                    *pbFoundDXVA2Configuration = TRUE;
                    *pSelectedConfig = pConfig[iConfig];
                    break;
                }
            }

            CoTaskMemFree(pConfig);
            break;

        } // End of formats loop.
    }

    CoTaskMemFree(pFormats);

    // Note: It is possible to return S_OK without finding a configuration.
    return hr;
}
```



Because this example is generic, some of the logic has been placed in helper functions that would need to be implemented by the decoder. The following code shows the declarations for these functions:


```C++
// Returns TRUE if the decoder supports a given decoding mode.
BOOL IsSupportedDecoderMode(const GUID&amp; mode);

// Returns TRUE if the decoder supports a given decoding configuration.
BOOL IsSupportedDecoderConfig(const DXVA2_ConfigPictureDecode&amp; config);

// Fills in a DXVA2_VideoDesc structure based on the input format.
void FillInVideoDescription(DXVA2_VideoDesc *pDesc);
```



## Notifying the Video Renderer

If the decoder finds a decoder configuration, the next step is to notify the video renderer that the decoder will use hardware acceleration. You can perform this step inside the [**CompleteConnect**](dshow.cbaseoutputpin_completeconnect) method. This step must occur before the allocator is selected, because it affects how the allocator is selected.

1.  Query the renderer's input pin for the [**IMFGetService**](imfgetservice.md) interface.
2.  Call [**IMFGetService::GetService**](imfgetservice-getservice.md) to get a pointer to the [**IDirectXVideoMemoryConfiguration**](idirectxvideomemoryconfiguration.md) interface. The service GUID is **MR\_VIDEO\_ACCELERATION\_SERVICE**.
3.  Call [**IDirectXVideoMemoryConfiguration::GetAvailableSurfaceTypeByIndex**](idirectxvideomemoryconfiguration-getavailablesurfacetypebyindex.md) in a loop, incrementing the *dwTypeIndex* variable from zero. Stop when the method returns the value **DXVA2\_SurfaceType\_DecoderRenderTarget** in the *pdwType* parameter. This step ensures that the video renderer supports hardware-accelerated decoding. This step will always succeed for the EVR filter.
4.  If the previous step succeeded, call [**IDirectXVideoMemoryConfiguration::SetSurfaceType**](idirectxvideomemoryconfiguration-setsurfacetype.md) with the value DXVA2\_SurfaceType\_DecoderRenderTarget. Calling **SetSurfaceType** with this value puts the video renderer into DXVA mode. When the video renderer is in this mode, the decoder must provide its own allocator.

The following code shows how to notify the video renderer.


```C++
HRESULT CDecoder::SetEVRForDXVA2(IPin *pPin)
{
    HRESULT hr = S_OK;

    IMFGetService                       *pGetService = NULL;
    IDirectXVideoMemoryConfiguration    *pVideoConfig = NULL;

    // Query the pin for IMFGetService.
    hr = pPin->QueryInterface(__uuidof(IMFGetService), (void**)&amp;pGetService);

    // Get the IDirectXVideoMemoryConfiguration interface.
    if (SUCCEEDED(hr))
    {
        hr = pGetService->GetService(
            MR_VIDEO_ACCELERATION_SERVICE, IID_PPV_ARGS(&amp;pVideoConfig));
    }

    // Notify the EVR. 
    if (SUCCEEDED(hr))
    {
        DXVA2_SurfaceType surfaceType;

        for (DWORD iTypeIndex = 0; ; iTypeIndex++)
        {
            hr = pVideoConfig->GetAvailableSurfaceTypeByIndex(iTypeIndex, &amp;surfaceType);
            
            if (FAILED(hr))
            {
                break;
            }

            if (surfaceType == DXVA2_SurfaceType_DecoderRenderTarget)
            {
                hr = pVideoConfig->SetSurfaceType(DXVA2_SurfaceType_DecoderRenderTarget);
                break;
            }
        }
    }

    SafeRelease(&amp;pGetService);
    SafeRelease(&amp;pVideoConfig);

    return hr;
}
```



If the decoder finds a valid configuration and successfully notifies the video renderer, the decoder can use DXVA for decoding. The decoder must implement a custom allocator for its output pin, as described in the next section.

## Allocating Uncompressed Buffers

In DXVA 2.0, the decoder is responsible for allocating Direct3D surfaces to use as uncompressed video buffers. Therefore, the decoder must implement a custom allocator that will create the surfaces. The media samples provided by this allocator will hold pointers to the Direct3D surfaces. The EVR retrieves a pointer to the surface by calling [**IMFGetService::GetService**](imfgetservice-getservice.md) on the media sample. The service identifier is **MR\_BUFFER\_SERVICE**.

To provide the custom allocator, perform the following steps:

1.  Define a class for the media samples. This class can derive from the [**CMediaSample**](dshow.cmediasample) class. Inside this class, do the following:
    -   Store a pointer to the Direct3D surface.
    -   Implement the [**IMFGetService**](imfgetservice.md) interface. In the [**GetService**](imfgetservice-getservice.md) method, if the service GUID is **MR\_BUFFER\_SERVICE**, query the Direct3D surface for the requested interface. Otherwise, **GetService** can return **MF\_E\_UNSUPPORTED\_SERVICE**.
    -   Override the [**CMediaSample::GetPointer**](dshow.cmediasample_getpointer) method to return E\_NOTIMPL.
2.  Define a class for the allocator. The allocator can derive from the [**CBaseAllocator**](dshow.cbaseallocator) class. Inside this class, do the following.
    -   Override the [**CBaseAllocator::Alloc**](dshow.cbaseallocator_alloc) method. Inside this method, call [**IDirectXVideoAccelerationService::CreateSurface**](idirectxvideoaccelerationservice-createsurface.md) to create the surfaces. (The [**IDirectXVideoDecoderService**](idirectxvideodecoderservice.md) interface inherits this method from [**IDirectXVideoAccelerationService**](idirectxvideoaccelerationservice.md).)
    -   Override the [**CBaseAllocator::Free**](dshow.cbaseallocator_free) method to release the surfaces.
3.  In your filter's output pin, override the [**CBaseOutputPin::InitAllocator**](dshow.cbaseoutputpin_initallocator) method. Inside this method, create an instance of your custom allocator.
4.  In your filter, implement the [**CTransformFilter::DecideBufferSize**](dshow.ctransformfilter_decidebuffersize) method. The *pProperties* parameter indicates the number of surfaces that the EVR requires. Add to this value the number of surfaces that your decoder requires, and call [**IMemAllocator::SetProperties**](dshow.imemallocator_setproperties) on the allocator.

The following code shows how to implement the media sample class:


```C++
class CDecoderSample : public CMediaSample, public IMFGetService
{
    friend class CDecoderAllocator;

public:

    CDecoderSample(CDecoderAllocator *pAlloc, HRESULT *phr)
        : CMediaSample(NAME("DecoderSample"), (CBaseAllocator*)pAlloc, phr, NULL, 0),
          m_pSurface(NULL),
          m_dwSurfaceId(0)
    { 
    }

    // Note: CMediaSample does not derive from CUnknown, so we cannot use the
    //       DECLARE_IUNKNOWN macro that is used by most of the filter classes.

    STDMETHODIMP QueryInterface(REFIID riid, void **ppv)
    {
        CheckPointer(ppv, E_POINTER);

        if (riid == IID_IMFGetService)
        {
            *ppv = static_cast<IMFGetService*>(this);
            AddRef();
            return S_OK;
        }
        else
        {
            return CMediaSample::QueryInterface(riid, ppv);
        }
    }
    STDMETHODIMP_(ULONG) AddRef()
    {
        return CMediaSample::AddRef();
    }

    STDMETHODIMP_(ULONG) Release()
    {
        // Return a temporary variable for thread safety.
        ULONG cRef = CMediaSample::Release();
        return cRef;
    }

    // IMFGetService::GetService
    STDMETHODIMP GetService(REFGUID guidService, REFIID riid, LPVOID *ppv)
    {
        if (guidService != MR_BUFFER_SERVICE)
        {
            return MF_E_UNSUPPORTED_SERVICE;
        }
        else if (m_pSurface == NULL)
        {
            return E_NOINTERFACE;
        }
        else
        {
            return m_pSurface->QueryInterface(riid, ppv);
        }
    }

    // Override GetPointer because this class does not manage a system memory buffer.
    // The EVR uses the MR_BUFFER_SERVICE service to get the Direct3D surface.
    STDMETHODIMP GetPointer(BYTE ** ppBuffer)
    {
        return E_NOTIMPL;
    }

private:

    // Sets the pointer to the Direct3D surface. 
    void SetSurface(DWORD surfaceId, IDirect3DSurface9 *pSurf)
    {
        SafeRelease(&amp;m_pSurface);

        m_pSurface = pSurf;
        if (m_pSurface)
        {
            m_pSurface->AddRef();
        }

        m_dwSurfaceId = surfaceId;
    }

    IDirect3DSurface9   *m_pSurface;
    DWORD               m_dwSurfaceId;
};
```



The following code shows how to implement the [**Alloc**](dshow.cbaseallocator_alloc) method on the allocator.


```C++
HRESULT CDecoderAllocator::Alloc()
{
    CAutoLock lock(this);

    HRESULT hr = S_OK;

    if (m_pDXVA2Service == NULL)
    {
        return E_UNEXPECTED;
    }

    hr = CBaseAllocator::Alloc();

    // If the requirements have not changed, do not reallocate.
    if (hr == S_FALSE)
    {
        return S_OK;
    }

    if (SUCCEEDED(hr))
    {
        // Free the old resources.
        Free();

        // Allocate a new array of pointers.
        m_ppRTSurfaceArray = new (std::nothrow) IDirect3DSurface9*[m_lCount];
        if (m_ppRTSurfaceArray == NULL)
        {
            hr = E_OUTOFMEMORY;
        }
        else
        {
            ZeroMemory(m_ppRTSurfaceArray, sizeof(IDirect3DSurface9*) * m_lCount);
        }
    }

    // Allocate the surfaces.
    if (SUCCEEDED(hr))
    {
        hr = m_pDXVA2Service->CreateSurface(
            m_dwWidth,
            m_dwHeight,
            m_lCount - 1,
            (D3DFORMAT)m_dwFormat,
            D3DPOOL_DEFAULT,
            0,
            DXVA2_VideoDecoderRenderTarget,
            m_ppRTSurfaceArray,
            NULL
            );
    }

    if (SUCCEEDED(hr))
    {
        for (m_lAllocated = 0; m_lAllocated < m_lCount; m_lAllocated++)
        {
            CDecoderSample *pSample = new (std::nothrow) CDecoderSample(this, &amp;hr);

            if (pSample == NULL)
            {
                hr = E_OUTOFMEMORY;
                break;
            }
            if (FAILED(hr))
            {
                break;
            }
            // Assign the Direct3D surface pointer and the index.
            pSample->SetSurface(m_lAllocated, m_ppRTSurfaceArray[m_lAllocated]);

            // Add to the sample list.
            m_lFree.Add(pSample);
        }
    }

    if (SUCCEEDED(hr))
    {
        m_bChanged = FALSE;
    }
    return hr;
}
```



Here is the code for the [**Free**](dshow.cbaseallocator_free) method:


```C++
void CDecoderAllocator::Free()
{
    CMediaSample *pSample = NULL;

    do
    {
        pSample = m_lFree.RemoveHead();
        if (pSample)
        {
            delete pSample;
        }
    } while (pSample);

    if (m_ppRTSurfaceArray)
    {
        for (long i = 0; i < m_lAllocated; i++)
        {
            SafeRelease(&amp;m_ppRTSurfaceArray[i]);
        }

        delete [] m_ppRTSurfaceArray;
    }
    m_lAllocated = 0;
}
```



For more information about implementing custom allocators, see the topic [Providing a Custom Allocator](dshow.providing_a_custom_allocator) in the DirectShow SDK documentation.

## Decoding

To create the decoder device, call [**IDirectXVideoDecoderService::CreateVideoDecoder**](idirectxvideodecoderservice-createvideodecoder.md). The method returns a pointer to the [**IDirectXVideoDecoder**](idirectxvideodecoder.md) interface of the decoder device.

On each frame, call [**IDirect3DDeviceManager9::TestDevice**](idirect3ddevicemanager9-testdevice.md) to test the device handle. If the device has changed, the method returns DXVA2\_E\_NEW\_VIDEO\_DEVICE. If this occurs, do the following:

1.  Close the device handle by calling [**IDirect3DDeviceManager9::CloseDeviceHandle**](idirect3ddevicemanager9-closedevicehandle.md).
2.  Release the [**IDirectXVideoDecoderService**](idirectxvideodecoderservice.md) and [**IDirectXVideoDecoder**](idirectxvideodecoder.md) pointers.
3.  Open a new device handle.
4.  Negotiate a new decoder configuration, as described in the section [Finding a Decoder Configuration](#finding-a-decoder-configuration).
5.  Create a new decoder device.

Assuming that the device handle is valid, the decoding process works as follows:

1.  Call [**IDirectXVideoDecoder::BeginFrame**](idirectxvideodecoder-beginframe.md).
2.  Do the following one or more times:
    1.  Call [**IDirectXVideoDecoder::GetBuffer**](idirectxvideodecoder-getbuffer.md) to get a DXVA decoder buffer.
    2.  Fill the buffer.
    3.  Call [**IDirectXVideoDecoder::ReleaseBuffer**](idirectxvideodecoder-releasebuffer.md).
3.  Call [**IDirectXVideoDecoder::Execute**](idirectxvideodecoder-execute.md) to perform the decoding operations on the frame.

DXVA 2.0 uses the same data structures as DXVA 1.0 for decoding operations. For the original set of DXVA profiles (for H.261, H.263, and MPEG-2), these data structures are described in the [DXVA 1.0 specification](http://go.microsoft.com/fwlink/p/?linkid=93647).

Within each pair of [**BeginFrame**](idirectxvideodecoder-beginframe.md)/[**Execute**](idirectxvideodecoder-execute.md) calls, you may call [**GetBuffer**](idirectxvideodecoder-getbuffer.md) multiple times, but only once for each type of DXVA buffer. If you call it twice with the same buffer type, you will overwrite the data.

After calling [**Execute**](idirectxvideodecoder-execute.md), call [**IMemInputPin::Receive**](dshow.imeminputpin_receive) to deliver the frame to the video renderer, as with software decoding. The **Receive** method is asynchronous; after it returns, the decoder can continue decoding the next frame. The display driver prevents any decoding commands from overwriting the buffer while the buffer is in use. The decoder should not reuse a surface to decode another frame until the renderer has released the sample. When the renderer releases the sample, the allocator puts the sample back into its pool of available samples. To get the next available sample, call [**CBaseOutputPin::GetDeliveryBuffer**](dshow.cbaseoutputpin_getdeliverybuffer), which in turn calls [**IMemAllocator::GetBuffer**](dshow.imemallocator_getbuffer). For more information, see the topic [Overview of Data Flow in DirectShow](dshow.overview_of_data_flow_in_directshow) in the DirectShow documentation.

## Related topics

<dl> <dt>

[DirectX Video Acceleration 2.0](directx-video-acceleration-2-0.md)
</dt> </dl>

 

 




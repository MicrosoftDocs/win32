---
description: Rendering a Stream
ms.assetid: 00bfcfd1-6592-43e3-90ad-730c92aa4cd3
title: Rendering a Stream
ms.topic: article
ms.date: 05/31/2018
---

# Rendering a Stream

The client calls the methods in the [**IAudioRenderClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudiorenderclient) interface to write rendering data to an endpoint buffer. For a shared-mode stream, the client shares the endpoint buffer with the audio engine. For an exclusive-mode stream, the client shares the endpoint buffer with the audio device. To request an endpoint buffer of a particular size, the client calls the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method. To get the size of the allocated buffer, which might be different from the requested size, the client calls the [**IAudioClient::GetBufferSize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getbuffersize) method.

To move a stream of rendering data through the endpoint buffer, the client alternately calls the [**IAudioRenderClient::GetBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer) method and the [**IAudioRenderClient::ReleaseBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-releasebuffer) method. The client accesses the data in the endpoint buffer as a series of data packets. The **GetBuffer** call retrieves the next packet so that the client can fill it with rendering data. After writing the data to the packet, the client calls **ReleaseBuffer** to add the completed packet to the rendering queue.

For a rendering buffer, the padding value that is reported by the [**IAudioClient::GetCurrentPadding**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getcurrentpadding) method represents the amount of rendering data that is queued up to play in the buffer. A rendering application can use the padding value to determine how much new data it can safely write to the buffer without the risk of overwriting previously written data that the audio engine has not yet read from the buffer. The available space is simply the buffer size minus the padding size. The client can request a packet size that represents some or all of this available space in its next [**GetBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer) call.

The size of a packet is expressed in *audio frames*. An audio frame in a PCM stream is a set of samples (the set contains one sample for each channel in the stream) that play or are recorded at the same time (clock tick). Thus, the size of an audio frame is the sample size multiplied by the number of channels in the stream. For example, the frame size for a stereo (2-channel) stream with 16-bit samples is four bytes.

The following code example shows how to play an audio stream on the default rendering device:


```C++
//-----------------------------------------------------------
// Play an audio stream on the default audio rendering
// device. The PlayAudioStream function allocates a shared
// buffer big enough to hold one second of PCM audio data.
// The function uses this buffer to stream data to the
// rendering device. The inner loop runs every 1/2 second.
//-----------------------------------------------------------

// REFERENCE_TIME time units per second and per millisecond
#define REFTIMES_PER_SEC  10000000
#define REFTIMES_PER_MILLISEC  10000

#define EXIT_ON_ERROR(hres)  \
              if (FAILED(hres)) { goto Exit; }
#define SAFE_RELEASE(punk)  \
              if ((punk) != NULL)  \
                { (punk)->Release(); (punk) = NULL; }

const CLSID CLSID_MMDeviceEnumerator = __uuidof(MMDeviceEnumerator);
const IID IID_IMMDeviceEnumerator = __uuidof(IMMDeviceEnumerator);
const IID IID_IAudioClient = __uuidof(IAudioClient);
const IID IID_IAudioRenderClient = __uuidof(IAudioRenderClient);

HRESULT PlayAudioStream(MyAudioSource *pMySource)
{
    HRESULT hr;
    REFERENCE_TIME hnsRequestedDuration = REFTIMES_PER_SEC;
    REFERENCE_TIME hnsActualDuration;
    IMMDeviceEnumerator *pEnumerator = NULL;
    IMMDevice *pDevice = NULL;
    IAudioClient *pAudioClient = NULL;
    IAudioRenderClient *pRenderClient = NULL;
    WAVEFORMATEX *pwfx = NULL;
    UINT32 bufferFrameCount;
    UINT32 numFramesAvailable;
    UINT32 numFramesPadding;
    BYTE *pData;
    DWORD flags = 0;

    hr = CoCreateInstance(
           CLSID_MMDeviceEnumerator, NULL,
           CLSCTX_ALL, IID_IMMDeviceEnumerator,
           (void**)&pEnumerator);
    EXIT_ON_ERROR(hr)

    hr = pEnumerator->GetDefaultAudioEndpoint(
                        eRender, eConsole, &pDevice);
    EXIT_ON_ERROR(hr)

    hr = pDevice->Activate(
                    IID_IAudioClient, CLSCTX_ALL,
                    NULL, (void**)&pAudioClient);
    EXIT_ON_ERROR(hr)

    hr = pAudioClient->GetMixFormat(&pwfx);
    EXIT_ON_ERROR(hr)

    hr = pAudioClient->Initialize(
                         AUDCLNT_SHAREMODE_SHARED,
                         0,
                         hnsRequestedDuration,
                         0,
                         pwfx,
                         NULL);
    EXIT_ON_ERROR(hr)

    // Tell the audio source which format to use.
    hr = pMySource->SetFormat(pwfx);
    EXIT_ON_ERROR(hr)

    // Get the actual size of the allocated buffer.
    hr = pAudioClient->GetBufferSize(&bufferFrameCount);
    EXIT_ON_ERROR(hr)

    hr = pAudioClient->GetService(
                         IID_IAudioRenderClient,
                         (void**)&pRenderClient);
    EXIT_ON_ERROR(hr)

    // Grab the entire buffer for the initial fill operation.
    hr = pRenderClient->GetBuffer(bufferFrameCount, &pData);
    EXIT_ON_ERROR(hr)

    // Load the initial data into the shared buffer.
    hr = pMySource->LoadData(bufferFrameCount, pData, &flags);
    EXIT_ON_ERROR(hr)

    hr = pRenderClient->ReleaseBuffer(bufferFrameCount, flags);
    EXIT_ON_ERROR(hr)

    // Calculate the actual duration of the allocated buffer.
    hnsActualDuration = (double)REFTIMES_PER_SEC *
                        bufferFrameCount / pwfx->nSamplesPerSec;

    hr = pAudioClient->Start();  // Start playing.
    EXIT_ON_ERROR(hr)

    // Each loop fills about half of the shared buffer.
    while (flags != AUDCLNT_BUFFERFLAGS_SILENT)
    {
        // Sleep for half the buffer duration.
        Sleep((DWORD)(hnsActualDuration/REFTIMES_PER_MILLISEC/2));

        // See how much buffer space is available.
        hr = pAudioClient->GetCurrentPadding(&numFramesPadding);
        EXIT_ON_ERROR(hr)

        numFramesAvailable = bufferFrameCount - numFramesPadding;

        // Grab all the available space in the shared buffer.
        hr = pRenderClient->GetBuffer(numFramesAvailable, &pData);
        EXIT_ON_ERROR(hr)

        // Get next 1/2-second of data from the audio source.
        hr = pMySource->LoadData(numFramesAvailable, pData, &flags);
        EXIT_ON_ERROR(hr)

        hr = pRenderClient->ReleaseBuffer(numFramesAvailable, flags);
        EXIT_ON_ERROR(hr)
    }

    // Wait for last data in buffer to play before stopping.
    Sleep((DWORD)(hnsActualDuration/REFTIMES_PER_MILLISEC/2));

    hr = pAudioClient->Stop();  // Stop playing.
    EXIT_ON_ERROR(hr)

Exit:
    CoTaskMemFree(pwfx);
    SAFE_RELEASE(pEnumerator)
    SAFE_RELEASE(pDevice)
    SAFE_RELEASE(pAudioClient)
    SAFE_RELEASE(pRenderClient)

    return hr;
}
```



In the preceding example, the PlayAudioStream function takes a single parameter, `pMySource`, which is a pointer to an object that belongs to a client-defined class, MyAudioSource, with two member functions, LoadData and SetFormat. The example code does not include the implementation of MyAudioSource because:

-   None of the class members communicates directly with any of the methods in the interfaces in WASAPI.
-   The class could be implemented in a variety of ways, depending on the requirements of the client. (For example, it might read the rendering data from a WAV file and perform on-the-fly conversion to the stream format.)

However, some information about the operation of the two functions is useful for understanding the example.

The LoadData function writes a specified number of audio frames (first parameter) to a specified buffer location (second parameter). (The size of an audio frame is the number of channels in the stream multiplied by the sample size.) The PlayAudioStream function uses LoadData to fill portions of the shared buffer with audio data. The SetFormat function specifies the format for the LoadData function to use for the data. If the LoadData function is able to write at least one frame to the specified buffer location but runs out of data before it has written the specified number of frames, then it writes silence to the remaining frames.

As long as LoadData succeeds in writing at least one frame of real data (not silence) to the specified buffer location, it outputs 0 through its third parameter, which, in the preceding code example, is an output pointer to the `flags` variable. When LoadData is out of data and cannot write even a single frame to the specified buffer location, it writes nothing to the buffer (not even silence), and it writes the value AUDCLNT\_BUFFERFLAGS\_SILENT to the `flags` variable. The `flags` variable conveys this value to the [**IAudioRenderClient::ReleaseBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-releasebuffer) method, which responds by filling the specified number of frames in the buffer with silence.

In its call to the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method, the PlayAudioStream function in the preceding example requests a shared buffer that has a duration of one second. (The allocated buffer might have a slightly longer duration.) In its initial calls to the [**IAudioRenderClient::GetBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-getbuffer) and [**IAudioRenderClient::ReleaseBuffer**](/windows/desktop/api/Audioclient/nf-audioclient-iaudiorenderclient-releasebuffer) methods, the function fills the entire buffer before calling the [**IAudioClient::Start**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-start) method to begin playing the buffer.

Within the main loop, the function iteratively fills half of the buffer at half-second intervals. Just before each call to the Windows [**Sleep**](/windows/win32/api/synchapi/nf-synchapi-sleep) function in the main loop, the buffer is full or nearly full. When the **Sleep** call returns, the buffer is about half full. The loop ends after the final call to the LoadData function sets the `flags` variable to the value AUDCLNT\_BUFFERFLAGS\_SILENT. At that point, the buffer contains at least one frame of real data, and it might contain as much as a half second of real data. The remainder of the buffer contains silence. The **Sleep** call that follows the loop provides sufficient time (a half second) to play all of the remaining data. The silence that follows the data prevents unwanted sounds before the call to the [**IAudioClient::Stop**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-stop) method stops the audio stream. For more information about **Sleep**, see the Windows SDK documentation.

Following the call to the [**IAudioClient::Initialize**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-initialize) method, the stream remains open until the client releases all of its references to the [**IAudioClient**](/windows/desktop/api/Audioclient/nn-audioclient-iaudioclient) interface and to all references to service interfaces that the client obtained through the [**IAudioClient::GetService**](/windows/desktop/api/Audioclient/nf-audioclient-iaudioclient-getservice) method. The final [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) call closes the stream.

The PlayAudioStream function in the preceding code example calls the [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function to create an enumerator for the audio endpoint devices in the system. Unless the calling program previously called either the **CoCreateInstance** or [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) function to initialize the COM library, the **CoCreateInstance** call will fail. For more information about **CoCreateInstance**, **CoCreateInstance**, and **CoInitializeEx**, see the Windows SDK documentation.

## Related topics

<dl> <dt>

[Stream Management](stream-management.md)
</dt> </dl>

 

 

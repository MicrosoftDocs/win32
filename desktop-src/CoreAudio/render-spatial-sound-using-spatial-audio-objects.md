---
description: This article presents some simple examples that illustrate how to implement spatial sound using static spatial audio objects, dynamic spatial audio objects, and spatial audio objects that use Microsoft's Head Relative Transfer Function (HRTF).
ms.assetid: C99C342E-0BD9-486A-92AA-F8DCB72C1B00
title: Render Spatial Sound Using Spatial Audio Objects
ms.topic: article
ms.date: 05/31/2018
---

# Render Spatial Sound Using Spatial Audio Objects

This article presents some simple examples that illustrate how to implement spatial sound using static spatial audio objects, dynamic spatial audio objects, and spatial audio objects that use Microsoft's Head Relative Transfer Function (HRTF). The implementation steps for all three of these techniques are very similar and this article provides a similarly structured code example for each technique. For complete end-to-end examples of real-world spatial audio implementations, see [Microsoft Spatial Sound samples github repository](https://github.com/Microsoft/Xbox-ATG-Samples/tree/master/UWPSamples/Audio). For an overview of Windows Sonic, Microsoft’s platform-level solution for spatial sound support on Xbox and Windows, see [Spatial Sound](spatial-sound.md).

## Render audio using static spatial audio objects

A static audio object is used to render sound to one of 18 static audio channels defined in the [**AudioObjectType**](/windows/desktop/api/spatialaudioclient/ne-spatialaudioclient-audioobjecttype) enumeration. Each of these channels represents a real or virtualized speaker at a fixed point in space that does not move over time. The static channels that are available on a particular device depend on the spatial sound format being used. For a list of the supported formats and their channel counts, see [Spatial Sound](spatial-sound.md).

When you initialize a spatial audio stream, you must specify which of the available static channels the stream will use. The following example constant definitions can be used to specify common speaker configurations and get the number of channels available for each one.


```C++
const AudioObjectType ChannelMask_Mono = AudioObjectType_FrontCenter;
const AudioObjectType ChannelMask_Stereo = (AudioObjectType)(AudioObjectType_FrontLeft | AudioObjectType_FrontRight);
const AudioObjectType ChannelMask_2_1 = (AudioObjectType)(ChannelMask_Stereo | AudioObjectType_LowFrequency);
const AudioObjectType ChannelMask_Quad = (AudioObjectType)(AudioObjectType_FrontLeft | AudioObjectType_FrontRight | AudioObjectType_BackLeft | AudioObjectType_BackRight);
const AudioObjectType ChannelMask_4_1 = (AudioObjectType)(ChannelMask_Quad | AudioObjectType_LowFrequency);
const AudioObjectType ChannelMask_5_1 = (AudioObjectType)(AudioObjectType_FrontLeft | AudioObjectType_FrontRight | AudioObjectType_FrontCenter | AudioObjectType_LowFrequency | AudioObjectType_SideLeft | AudioObjectType_SideRight);
const AudioObjectType ChannelMask_7_1 = (AudioObjectType)(ChannelMask_5_1 | AudioObjectType_BackLeft | AudioObjectType_BackRight);

const UINT32 MaxStaticObjectCount_7_1_4 = 12;
const AudioObjectType ChannelMask_7_1_4 = (AudioObjectType)(ChannelMask_7_1 | AudioObjectType_TopFrontLeft | AudioObjectType_TopFrontRight | AudioObjectType_TopBackLeft | AudioObjectType_TopBackRight);

const UINT32 MaxStaticObjectCount_7_1_4_4 = 16;
const AudioObjectType ChannelMask_7_1_4_4 = (AudioObjectType)(ChannelMask_7_1_4 | AudioObjectType_BottomFrontLeft | AudioObjectType_BottomFrontRight |AudioObjectType_BottomBackLeft | AudioObjectType_BottomBackRight);

const UINT32 MaxStaticObjectCount_8_1_4_4 = 17;
const AudioObjectType ChannelMask_8_1_4_4 = (AudioObjectType)(ChannelMask_7_1_4_4 | AudioObjectType_BackCenter);
```



The first step in rendering spatial audio is to get the audio endpoint to which audio data will be sent. Create an instance of [**MMDeviceEnumerator**](/windows/desktop/api/Mmdeviceapi/nn-mmdeviceapi-immdeviceenumerator) and call [**GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint) to get the default audio render device.


```C++
HRESULT hr;
Microsoft::WRL::ComPtr<IMMDeviceEnumerator> deviceEnum;
Microsoft::WRL::ComPtr<IMMDevice> defaultDevice;

hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), nullptr, CLSCTX_ALL, __uuidof(IMMDeviceEnumerator), (void**)&deviceEnum);
hr = deviceEnum->GetDefaultAudioEndpoint(EDataFlow::eRender, eMultimedia, &defaultDevice);
```



When you create a spatial audio stream, you must specify the audio format the stream will use by providing a [WAVEFORMATEX](../medfound/mf-mt-audio-prefer-waveformatex-attribute.md) structure. If you are playing back audio from a file, the format is typically determined by the audio file format. This example uses a mono, 32-bit, 48Hz format.


```C++
WAVEFORMATEX format;
format.wFormatTag = WAVE_FORMAT_IEEE_FLOAT;
format.wBitsPerSample = 32;
format.nChannels = 1;
format.nSamplesPerSec = 48000;
format.nBlockAlign = (format.wBitsPerSample >> 3) * format.nChannels;
format.nAvgBytesPerSec = format.nBlockAlign * format.nSamplesPerSec;
format.cbSize = 0;
```



The next step in rendering spatial audio is to initialize a spatial audio stream. First, get an instance of [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) by calling [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate). Call [**ISpatialAudioClient::IsAudioObjectFormatSupported**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-isaudioobjectformatsupported) to make sure that the audio format you are using is supported. Create an event that the audio pipeline will use to notify the app that it is ready for more audio data.

Populate a [**SpatialAudioObjectRenderStreamActivationParams**](/windows/desktop/api/spatialaudioclient/ns-spatialaudioclient-spatialaudioobjectrenderstreamactivationparams) structure that will be used to initialize the spatial audio stream. In this example, the **StaticObjectTypeMask** field is set to the **ChannelMask\_Stereo** constant defined previously in this article, meaning that only the front right and left channels can be used by the audio stream. Because this example uses only static audio objects and no dynamic objects, the **MaxDynamicObjectCount** field is set to 0. The **Category** field is set to a member of the [**AUDIO\_STREAM\_CATEGORY**](/windows/desktop/api/audiosessiontypes/ne-audiosessiontypes-audio_stream_category) enumeration, which defines how the system mixes the sound from this stream with other audio sources.

Call [**ISpatialAudioClient::ActivateSpatialAudioStream**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-activatespatialaudiostream) to activate the stream.


```C++
Microsoft::WRL::ComPtr<ISpatialAudioClient> spatialAudioClient;

// Activate ISpatialAudioClient on the desired audio-device 
hr = defaultDevice->Activate(__uuidof(ISpatialAudioClient), CLSCTX_INPROC_SERVER, nullptr, (void**)&spatialAudioClient);

hr = spatialAudioClient->IsAudioObjectFormatSupported(&format);

// Create the event that will be used to signal the client for more data
HANDLE bufferCompletionEvent = CreateEvent(nullptr, FALSE, FALSE, nullptr);

SpatialAudioObjectRenderStreamActivationParams streamParams;
streamParams.ObjectFormat = &format;
streamParams.StaticObjectTypeMask = ChannelMask_Stereo;
streamParams.MinDynamicObjectCount = 0;
streamParams.MaxDynamicObjectCount = 0;
streamParams.Category = AudioCategory_SoundEffects;
streamParams.EventHandle = bufferCompletionEvent;
streamParams.NotifyObject = nullptr;

PROPVARIANT activationParams;
PropVariantInit(&activationParams);
activationParams.vt = VT_BLOB;
activationParams.blob.cbSize = sizeof(streamParams);
activationParams.blob.pBlobData = reinterpret_cast<BYTE *>(&streamParams);

Microsoft::WRL::ComPtr<ISpatialAudioObjectRenderStream> spatialAudioStream;
hr = spatialAudioClient->ActivateSpatialAudioStream(&activationParams, __uuidof(spatialAudioStream), (void**)&spatialAudioStream);
```



> [!Note]  
> When using the [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) interfaces on an Xbox One Development Kit (XDK) title, you must first call **EnableSpatialAudio** before calling [**IMMDeviceEnumerator::EnumAudioEndpoints**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-enumaudioendpoints) or [**IMMDeviceEnumerator::GetDefaultAudioEndpoint**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdeviceenumerator-getdefaultaudioendpoint). Failure to do so will result in an E\_NOINTERFACE error being returned from the call to Activate. **EnableSpatialAudio** is only available for XDK titles, and does not need to be called for Universal Windows Platform apps running on Xbox One, nor for any non-Xbox One devices.

 

Declare a pointer for an [**ISpatialAudioObject**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobject) that will be used to write audio data to a static channel. Typical apps will use an object for each channel specified in the **StaticObjectTypeMask** field. For simplicity, this example only uses a single static audio object.


```C++
// In this simple example, one object will be rendered
Microsoft::WRL::ComPtr<ISpatialAudioObject> audioObjectFrontLeft;
```



Before entering the audio render loop, call [**ISpatialAudioObjectRenderStream::Start**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-start) to instruct the media pipeline to begin requesting audio data. This example uses a counter to stop the rendering of audio after 5 seconds.

Inside the render loop, wait for the buffer completion event, provided when the spatial audio stream was initialized, to be signaled. You should set a reasonable timeout limit, like 100 ms, when waiting for the event because any change to the render type or endpoint will cause that event to never be signaled. In this case, you can call [**ISpatialAudioObjectRenderStream::Reset**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-reset) to attempt to reset the spatial audio stream.

Next, call [**ISpatialAudioObjectRenderStream::BeginUpdatingAudioObjects**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-beginupdatingaudioobjects) to let the system know that you are about to fill the audio objects' buffers with data. This method returns the number of available dynamic audio objects, not used in this example, and the frame count of the buffer for audio objects rendered by this stream.

If a static spatial audio object has not yet been created, create one or more by calling [**ISpatialAudioObjectRenderStream::ActivateSpatialAudioObject**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstream-activatespatialaudioobject), passing in a value from the [**AudioObjectType**](/windows/desktop/api/spatialaudioclient/ne-spatialaudioclient-audioobjecttype) enumeration indicating the static channel to which the object's audio is rendered.

Next, call [**ISpatialAudioObject::GetBuffer**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectbase-getbuffer) to get a pointer to the spatial audio object's audio buffer. This method also returns the size of the buffer, in bytes. This example uses a helper method, **WriteToAudioObjectBuffer**, to fill the buffer with audio data. This method is shown later in this article. After writing to the buffer, the example checks to see if the 5 second lifetime of the object has been reached, and if so, [**ISpatialAudioObject::SetEndOfStream**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectbase-setendofstream) is called to let the audio pipeline know that no more audio will be written using this object and the object is set to **nullptr** to free up its resources.

After writing data to all of your audio objects, call [**ISpatialAudioObjectRenderStream::EndUpdatingAudioObjects**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-endupdatingaudioobjects) to let the system know the data is ready for rendering. You can only call **GetBuffer** in between a call to **BeginUpdatingAudioObjects** and **EndUpdatingAudioObjects**.


```C++
// Start streaming / rendering 
hr = spatialAudioStream->Start();

// This example will render 5 seconds of audio samples
UINT totalFrameCount = format.nSamplesPerSec * 5;

bool isRendering = true;
while (isRendering)
{
    // Wait for a signal from the audio-engine to start the next processing pass
    if (WaitForSingleObject(bufferCompletionEvent, 100) != WAIT_OBJECT_0)
    {
        hr = spatialAudioStream->Reset();

        if (hr != S_OK)
        {
            // handle the error
            break;
        }
    }

    UINT32 availableDynamicObjectCount;
    UINT32 frameCount;

    // Begin the process of sending object data and metadata
    // Get the number of dynamic objects that can be used to send object-data
    // Get the frame count that each buffer will be filled with 
    hr = spatialAudioStream->BeginUpdatingAudioObjects(&availableDynamicObjectCount, &frameCount);

    BYTE* buffer;
    UINT32 bufferLength;

    if (audioObjectFrontLeft == nullptr)
    {
        hr = spatialAudioStream->ActivateSpatialAudioObject(AudioObjectType::AudioObjectType_FrontLeft, &audioObjectFrontLeft);
        if (hr != S_OK) break;
    }

    // Get the buffer to write audio data
    hr = audioObjectFrontLeft->GetBuffer(&buffer, &bufferLength);

    if (totalFrameCount >= frameCount)
    {
        // Write audio data to the buffer
        WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), frameCount, 200.0f, format.nSamplesPerSec);

        totalFrameCount -= frameCount;
    }
    else
    {
        // Write audio data to the buffer
        WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), totalFrameCount, 750.0f, format.nSamplesPerSec);

        // Set end of stream for the last buffer 
        hr = audioObjectFrontLeft->SetEndOfStream(totalFrameCount);

        audioObjectFrontLeft = nullptr; // Release the object

        isRendering = false;
    }

    // Let the audio engine know that the object data are available for processing now
    hr = spatialAudioStream->EndUpdatingAudioObjects();
};
```



When you are done rendering spatial audio, stop the spatial audio stream by calling [**ISpatialAudioObjectRenderStream::Stop**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-stop). If you are not going to use the stream again, free its resources by calling [**ISpatialAudioObjectRenderStream::Reset**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-reset).


```C++
// Stop the stream
hr = spatialAudioStream->Stop();

// Don't want to start again, so reset the stream to free its resources
hr = spatialAudioStream->Reset();

CloseHandle(bufferCompletionEvent);
```



The **WriteToAudioObjectBuffer** helper method writes either a full buffer of samples or the number of remaining samples specified by our app-defined time limit. This could also be determined, for example, by the number of samples remaining in a source audio file. A simple sin wave, the frequency of which is scaled by the *frequency* input parameter, is generated and written to the buffer.


```C++
void WriteToAudioObjectBuffer(FLOAT* buffer, UINT frameCount, FLOAT frequency, UINT samplingRate)
{
    const double PI = 4 * atan2(1.0, 1.0);
    static double _radPhase = 0.0;

    double step = 2 * PI * frequency / samplingRate;

    for (UINT i = 0; i < frameCount; i++)
    {
        double sample = sin(_radPhase);

        buffer[i] = FLOAT(sample);

        _radPhase += step; // next frame phase

        if (_radPhase >= 2 * PI)
        {
            _radPhase -= 2 * PI;
        }
    }
}
```



## Render audio using dynamic spatial audio objects

Dynamic objects allow you to render audio from an arbitrary position in space, relative to the user. The position and volume of a dynamic audio object can be changed over time. Games will typically use the position of a 3D object in the game world to specify the position of the dynamic audio object associated with it. The following example will use a simple structure, **My3dObject**, to store the minimum set of data needed to represent an object. This data includes a pointer to an [**ISpatialAudioObject**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobject), the position, velocity, volume, and tone frequency for the object, and a value that stores the total number of frames for which the object should render sound.


```C++
struct My3dObject
{
    Microsoft::WRL::ComPtr<ISpatialAudioObject> audioObject;
    Windows::Foundation::Numerics::float3 position;
    Windows::Foundation::Numerics::float3 velocity;
    float volume;
    float frequency; // in Hz
    UINT totalFrameCount;
};
```



The implementation steps for dynamic audio objects is largely the same as the steps for static audio objects described above. First, get an audio endpoint.


```C++
HRESULT hr;
Microsoft::WRL::ComPtr<IMMDeviceEnumerator> deviceEnum;
Microsoft::WRL::ComPtr<IMMDevice> defaultDevice;

hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), nullptr, CLSCTX_ALL, __uuidof(IMMDeviceEnumerator), (void**)&deviceEnum);
hr = deviceEnum->GetDefaultAudioEndpoint(EDataFlow::eRender, eMultimedia, &defaultDevice);
```



Next, initialize the spatial audio stream. Get an instance of [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) by calling [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate). Call [**ISpatialAudioClient::IsAudioObjectFormatSupported**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-isaudioobjectformatsupported) to make sure that the audio format you are using is supported. Create an event that the audio pipeline will use to notify the app that it is ready for more audio data.

Call [**ISpatialAudioClient::GetMaxDynamicObjectCount**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-getmaxdynamicobjectcount) to retrieve the number of dynamic objects supported by the system. If this call returns 0, then dynamic spatial audio objects are not supported or enabled on the current device. For information on enabling spatial audio and for details on the number of dynamic audio objects available for different spatial audio formats, see [Spatial Sound](spatial-sound.md).

When populating the [**SpatialAudioObjectRenderStreamActivationParams**](/windows/desktop/api/spatialaudioclient/ns-spatialaudioclient-spatialaudioobjectrenderstreamactivationparams) structure, set the **MaxDynamicObjectCount** field to the maximum number of dynamic objects your app will use.

Call [**ISpatialAudioClient::ActivateSpatialAudioStream**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-activatespatialaudiostream) to activate the stream.


```C++
// Activate ISpatialAudioClient on the desired audio-device 
Microsoft::WRL::ComPtr<ISpatialAudioClient> spatialAudioClient;
hr = defaultDevice->Activate(__uuidof(ISpatialAudioClient), CLSCTX_INPROC_SERVER, nullptr, (void**)&spatialAudioClient);

hr = spatialAudioClient->IsAudioObjectFormatSupported(&format);

// Create the event that will be used to signal the client for more data
HANDLE bufferCompletionEvent = CreateEvent(nullptr, FALSE, FALSE, nullptr);

UINT32 maxDynamicObjectCount;
hr = spatialAudioClient->GetMaxDynamicObjectCount(&maxDynamicObjectCount);

if (maxDynamicObjectCount == 0)
{
    // Dynamic objects are unsupported
    return;
}

// Set the maximum number of dynamic audio objects that will be used
SpatialAudioObjectRenderStreamActivationParams streamParams;
streamParams.ObjectFormat = &format;
streamParams.StaticObjectTypeMask = AudioObjectType_None;
streamParams.MinDynamicObjectCount = 0;
streamParams.MaxDynamicObjectCount = min(maxDynamicObjectCount, 4);
streamParams.Category = AudioCategory_GameEffects;
streamParams.EventHandle = bufferCompletionEvent;
streamParams.NotifyObject = nullptr;

PROPVARIANT pv;
PropVariantInit(&pv);
pv.vt = VT_BLOB;
pv.blob.cbSize = sizeof(streamParams);
pv.blob.pBlobData = (BYTE *)&streamParams;

Microsoft::WRL::ComPtr<ISpatialAudioObjectRenderStream> spatialAudioStream;;
hr = spatialAudioClient->ActivateSpatialAudioStream(&pv, __uuidof(spatialAudioStream), (void**)&spatialAudioStream);
```



The following is some app-specific code to needed support this example, which will dynamically spawn randomly positioned audio objects and store them in a vector.


```C++
// Used for generating a vector of randomized My3DObject structs
std::vector<My3dObject> objectVector;
std::default_random_engine gen;
std::uniform_real_distribution<> pos_dist(-25, 25); // uniform distribution for random position
std::uniform_real_distribution<> vel_dist(-1, 1); // uniform distribution for random velocity
std::uniform_real_distribution<> vol_dist(0.5, 1.0); // uniform distribution for random volume
std::uniform_real_distribution<> pitch_dist(40, 400); // uniform distribution for random pitch
int spawnCounter = 0;
```



Before entering the audio render loop, call [**ISpatialAudioObjectRenderStream::Start**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-start) to instruct the media pipeline to begin requesting audio data.

Inside the render loop, wait for the buffer completion event we provided when the spatial audio stream was initialized to be signaled. You should set a reasonable timeout limit, like 100 ms, when waiting for the event because any change to the render type or endpoint will cause that event to never be signaled. In this case, you can call [**ISpatialAudioObjectRenderStream::Reset**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-reset) to attempt to reset the spatial audio stream.

Next, call [**ISpatialAudioObjectRenderStream::BeginUpdatingAudioObjects**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-beginupdatingaudioobjects) to let the system know that you are about to fill the audio objects' buffers with data. This method returns the number of available dynamic audio objects and the frame count of the buffer for audio objects rendered by this stream.

Whenever the spawn counter reaches the specified value, we will activate a new dynamic audio object by calling [**ISpatialAudioObjectRenderStream::ActivateSpatialAudioObject**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstream-activatespatialaudioobject) specifying [**AudioObjectType\_Dynamic**](/windows/desktop/api/spatialaudioclient/ne-spatialaudioclient-audioobjecttype). If all available dynamic audio objects have already been allocated, this method will return **SPLAUDCLNT\_E\_NO\_MORE\_OBJECTS**. In this case, you can choose to release one or more previously activated audio objects based on your app-specific prioritization. After the dynamic audio object has been created, it is added to a new **My3dObject** structure, with randomized position, velocity, volume, and frequency values, which is then added to the list of active objects.

Next, iterate over all of the active objects, represented in this example with the app-defined **My3dObject** structure. For each audio object, call [**ISpatialAudioObject::GetBuffer**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectbase-getbuffer) to get a pointer to the spatial audio object's audio buffer. This method also returns the size of the buffer, in bytes. The helper method, **WriteToAudioObjectBuffer**, to fill the buffer with audio data. After writing to the buffer, the example updates the position of the dynamic audio object by calling [**ISpatialAudioObject::SetPosition**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobject-setposition). The volume of the audio object can also be modified by calling [**SetVolume**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobject-setvolume). If you don't update the position or volume of the object, it will retain the position and volume from the last time it was set. If the object's app-defined lifetime has been reached, [**ISpatialAudioObject::SetEndOfStream**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectbase-setendofstream) is called to let the audio pipeline know that no more audio will be written using this object and the object is set to **nullptr** to free up its resources.

After writing data to all of your audio objects, call [**ISpatialAudioObjectRenderStream::EndUpdatingAudioObjects**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-endupdatingaudioobjects) to let the system know the data is ready for rendering. You can only call **GetBuffer** in between a call to **BeginUpdatingAudioObjects** and **EndUpdatingAudioObjects**.


```C++
// Start streaming / rendering 
hr = spatialAudioStream->Start();

do
{
    // Wait for a signal from the audio-engine to start the next processing pass
    if (WaitForSingleObject(bufferCompletionEvent, 100) != WAIT_OBJECT_0)
    {
        break;
    }

    UINT32 availableDynamicObjectCount;
    UINT32 frameCount;

    // Begin the process of sending object data and metadata
    // Get the number of active objects that can be used to send object-data
    // Get the frame count that each buffer will be filled with 
    hr = spatialAudioStream->BeginUpdatingAudioObjects(&availableDynamicObjectCount, &frameCount);

    BYTE* buffer;
    UINT32 bufferLength;

    // Spawn a new dynamic audio object every 200 iterations
    if (spawnCounter % 200 == 0 && spawnCounter < 1000)
    {
        // Activate a new dynamic audio object
        Microsoft::WRL::ComPtr<ISpatialAudioObject> audioObject;
        hr = spatialAudioStream->ActivateSpatialAudioObject(AudioObjectType::AudioObjectType_Dynamic, &audioObject);

        // If SPTLAUDCLNT_E_NO_MORE_OBJECTS is returned, there are no more available objects
        if (SUCCEEDED(hr))
        {
            // Init new struct with the new audio object.
            My3dObject obj = {
                audioObject,
                Windows::Foundation::Numerics::float3(static_cast<float>(pos_dist(gen)), static_cast<float>(pos_dist(gen)), static_cast<float>(pos_dist(gen))),
                Windows::Foundation::Numerics::float3(static_cast<float>(vel_dist(gen)), static_cast<float>(vel_dist(gen)), static_cast<float>(vel_dist(gen))),
                static_cast<float>(static_cast<float>(vol_dist(gen))),
                static_cast<float>(static_cast<float>(pitch_dist(gen))),
                format.nSamplesPerSec * 5 // 5 seconds of audio samples
            };

            objectVector.insert(objectVector.begin(), obj);
        }
    }
    spawnCounter++;

    // Loop through all dynamic audio objects
    std::vector<My3dObject>::iterator it = objectVector.begin();
    while (it != objectVector.end())
    {
        it->audioObject->GetBuffer(&buffer, &bufferLength);

        if (it->totalFrameCount >= frameCount)
        {
            // Write audio data to the buffer
            WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), frameCount, it->frequency, format.nSamplesPerSec);

            // Update the position and volume of the audio object
            it->audioObject->SetPosition(it->position.x, it->position.y, it->position.z);
            it->position += it->velocity;
            it->audioObject->SetVolume(it->volume);

            it->totalFrameCount -= frameCount;

            ++it;
        }
        else
        {
            // If the audio object reaches its lifetime, set EndOfStream and release the object

            // Write audio data to the buffer
            WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), it->totalFrameCount, it->frequency, format.nSamplesPerSec);

            // Set end of stream for the last buffer 
            hr = it->audioObject->SetEndOfStream(it->totalFrameCount);

            it->audioObject = nullptr; // Release the object

            it->totalFrameCount = 0;

            it = objectVector.erase(it);
        }
    }

    // Let the audio-engine know that the object data are available for processing now
    hr = spatialAudioStream->EndUpdatingAudioObjects();
} while (objectVector.size() > 0);
```



When you are done rendering spatial audio, stop the spatial audio stream by calling [**ISpatialAudioObjectRenderStream::Stop**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-stop). If you are not going to use the stream again, free its resources by calling [**ISpatialAudioObjectRenderStream::Reset**](/windows/win32/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioobjectrenderstreambase-reset).


```C++
// Stop the stream 
hr = spatialAudioStream->Stop();

// We don't want to start again, so reset the stream to free it's resources.
hr = spatialAudioStream->Reset();

CloseHandle(bufferCompletionEvent);
```



## Render audio using dynamic spatial audio objects for HRTF

Another set of APIs, [**ISpatialAudioRenderStreamForHrtf**](/windows/win32/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectrenderstreamforhrtf) and [**ISpatialAudioObjectForHrtf**](/windows/desktop/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectforhrtf), enable spatial audio that uses Microsoft's Head-relative Transfer Function (HRTF) to attenuate sounds to simulate the emitter's position in space, relative to the user, which can be changed over time. In addition to position, HRTF audio objects allow you to specify an orientation in space, a directivity in which sound is emitted, such as a cone or cardioid shape, and a decay model as the object moves nearer and further from the virtual listener. Note that these HRTF interfaces are only available when the user has selected Windows Sonic for Headphones as the spatial audio engine for the device. For information on configuring a device to use Windows Sonic for Headphones, see [Spatial Sound](spatial-sound.md).

The [**ISpatialAudioRenderStreamForHrtf**](/windows/win32/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectrenderstreamforhrtf) and [**ISpatialAudioObjectForHrtf**](/windows/desktop/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectforhrtf) APIs allow an application to explicitly use the Windows Sonic for Headphones render path directly. These APIs do not support spatial sound formats such as Dolby Atmos for Home Theater or Dolby Atmos for Headphones, nor consumer-controlled output format switching via the **Sound** control panel, nor playback over speakers. These interfaces are intended for use in Windows Mixed Reality applications that want to use Windows Sonic for Headphones-specific capabilities (such as environmental presets and distance-based rolloff specified programmatically, outside of typical content authoring pipelines). Most games and virtual reality scenarios will prefer to use [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) instead. The implementation steps for both API sets are almost identical, so it is possible to implement both technologies and switch at runtime depending on which feature is available on the current device.

Mixed-reality apps will typically use the position of a 3D object in the virtual world to specify the position of the dynamic audio object associated with it. The following example will use a simple structure, **My3dObjectForHrtf**, to store the minimum set of data needed to represent an object. This data includes a pointer to an [**ISpatialAudioObjectForHrtf**](/windows/desktop/api/spatialaudiohrtf/nn-spatialaudiohrtf-ispatialaudioobjectforhrtf), the position, orientation, velocity, and tone frequency for the object, and a value that stores the total number of frames for which the object should render sound.


```C++
struct My3dObjectForHrtf
{
    Microsoft::WRL::ComPtr<ISpatialAudioObjectForHrtf> audioObject;
    Windows::Foundation::Numerics::float3 position;
    Windows::Foundation::Numerics::float3 velocity;
    float yRotationRads;
    float deltaYRotation;
    float frequency; // in Hz
    UINT totalFrameCount;
};
```



The implementation steps for dynamic HRTF audio objects is largely the same as the steps for dynamic audio objects described in the previous section. First, get an audio endpoint.


```C++
HRESULT hr;
Microsoft::WRL::ComPtr<IMMDeviceEnumerator> deviceEnum;
Microsoft::WRL::ComPtr<IMMDevice> defaultDevice;

hr = CoCreateInstance(__uuidof(MMDeviceEnumerator), nullptr, CLSCTX_ALL, __uuidof(IMMDeviceEnumerator), (void**)&deviceEnum);
hr = deviceEnum->GetDefaultAudioEndpoint(EDataFlow::eRender, eMultimedia, &defaultDevice);
```



Next, initialize the spatial audio stream. Get an instance of [**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) by calling [**IMMDevice::Activate**](/windows/desktop/api/Mmdeviceapi/nf-mmdeviceapi-immdevice-activate). Call [**ISpatialAudioClient::IsAudioObjectFormatSupported**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-isaudioobjectformatsupported) to make sure that the audio format you are using is supported. Create an event that the audio pipeline will use to notify the app that it is ready for more audio data.

Call [**ISpatialAudioClient::GetMaxDynamicObjectCount**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-getmaxdynamicobjectcount) to retrieve the number of dynamic objects supported by the system. If this call returns 0, then dynamic spatial audio objects are not supported or enabled on the current device. For information on enabling spatial audio and for details on the number of dynamic audio objects available for different spatial audio formats, see [Spatial Sound](spatial-sound.md).

When populating the [**SpatialAudioHrtfActivationParams**](/windows/desktop/api/spatialaudiohrtf/ns-spatialaudiohrtf-spatialaudiohrtfactivationparams) structure, set the **MaxDynamicObjectCount** field to the maximum number of dynamic objects your app will use. The activation params for HRTF supports a few additional parameters, such as a [**SpatialAudioHrtfDistanceDecay**](/windows/desktop/api/spatialaudiohrtf/ns-spatialaudiohrtf-spatialaudiohrtfdistancedecay), a [**SpatialAudioHrtfDirectivityUnion**](/windows/desktop/api/spatialaudiohrtf/ns-spatialaudiohrtf-spatialaudiohrtfdirectivityunion), a [**SpatialAudioHrtfEnvironmentType**](/windows/desktop/api/spatialaudiohrtf/ne-spatialaudiohrtf-spatialaudiohrtfenvironmenttype), and a [**SpatialAudioHrtfOrientation**](spatialaudiohrtforientation.md), which specify the default values of these settings for new objects created from the stream. These parameters are optional. Set the fields to **nullptr** to provide no default values.

Call [**ISpatialAudioClient::ActivateSpatialAudioStream**](/windows/desktop/api/spatialaudioclient/nf-spatialaudioclient-ispatialaudioclient-activatespatialaudiostream) to activate the stream.


```C++
// Activate ISpatialAudioClient on the desired audio-device 
Microsoft::WRL::ComPtr<ISpatialAudioClient> spatialAudioClient;
hr = defaultDevice->Activate(__uuidof(ISpatialAudioClient), CLSCTX_INPROC_SERVER, nullptr, (void**)&spatialAudioClient);

Microsoft::WRL::ComPtr<ISpatialAudioObjectRenderStreamForHrtf>  spatialAudioStreamForHrtf;
hr = spatialAudioClient->IsSpatialAudioStreamAvailable(__uuidof(spatialAudioStreamForHrtf), NULL);

hr = spatialAudioClient->IsAudioObjectFormatSupported(&format);

// Create the event that will be used to signal the client for more data
HANDLE bufferCompletionEvent = CreateEvent(nullptr, FALSE, FALSE, nullptr);

UINT32 maxDynamicObjectCount;
hr = spatialAudioClient->GetMaxDynamicObjectCount(&maxDynamicObjectCount);

SpatialAudioHrtfActivationParams streamParams;
streamParams.ObjectFormat = &format;
streamParams.StaticObjectTypeMask = AudioObjectType_None;
streamParams.MinDynamicObjectCount = 0;
streamParams.MaxDynamicObjectCount = min(maxDynamicObjectCount, 4);
streamParams.Category = AudioCategory_GameEffects;
streamParams.EventHandle = bufferCompletionEvent;
streamParams.NotifyObject = NULL;

SpatialAudioHrtfDistanceDecay decayModel;
decayModel.CutoffDistance = 100;
decayModel.MaxGain = 3.98f;
decayModel.MinGain = float(1.58439 * pow(10, -5));
decayModel.Type = SpatialAudioHrtfDistanceDecayType::SpatialAudioHrtfDistanceDecay_NaturalDecay;
decayModel.UnityGainDistance = 1;

streamParams.DistanceDecay = &decayModel;

SpatialAudioHrtfDirectivity directivity;
directivity.Type = SpatialAudioHrtfDirectivityType::SpatialAudioHrtfDirectivity_Cone;
directivity.Scaling = 1.0f;

SpatialAudioHrtfDirectivityCone cone;
cone.directivity = directivity;
cone.InnerAngle = 0.1f;
cone.OuterAngle = 0.2f;

SpatialAudioHrtfDirectivityUnion directivityUnion;
directivityUnion.Cone = cone;
streamParams.Directivity = &directivityUnion;

SpatialAudioHrtfEnvironmentType environment = SpatialAudioHrtfEnvironmentType::SpatialAudioHrtfEnvironment_Large;
streamParams.Environment = &environment;

SpatialAudioHrtfOrientation orientation = { 1,0,0,0,1,0,0,0,1 }; // identity matrix
streamParams.Orientation = &orientation;

PROPVARIANT pv;
PropVariantInit(&pv);
pv.vt = VT_BLOB;
pv.blob.cbSize = sizeof(streamParams);
pv.blob.pBlobData = (BYTE *)&streamParams;

hr = spatialAudioClient->ActivateSpatialAudioStream(&pv, __uuidof(spatialAudioStreamForHrtf), (void**)&spatialAudioStreamForHrtf);
```



The following is some app-specific code to needed support this example, which will dynamically spawn randomly positioned audio objects and store them in a vector.


```C++
// Used for generating a vector of randomized My3DObject structs
std::vector<My3dObjectForHrtf> objectVector;
std::default_random_engine gen;
std::uniform_real_distribution<> pos_dist(-10, 10); // uniform distribution for random position
std::uniform_real_distribution<> vel_dist(-.02, .02); // uniform distribution for random velocity
std::uniform_real_distribution<> yRotation_dist(-3.14, 3.14); // uniform distribution for y-axis rotation
std::uniform_real_distribution<> deltaYRotation_dist(.01, .02); // uniform distribution for y-axis rotation
std::uniform_real_distribution<> pitch_dist(40, 400); // uniform distribution for random pitch

int spawnCounter = 0;
```



Before entering the audio render loop, call [**ISpatialAudioObjectRenderStreamForHrtf::Start**](/previous-versions/windows/desktop/legacy/mt779304(v=vs.85)) to instruct the media pipeline to begin requesting audio data.

Inside the render loop, wait for the buffer completion event we provided when the spatial audio stream was initialized to be signaled. You should set a reasonable timeout limit, like 100 ms, when waiting for the event because any change to the render type or endpoint will cause that event to never be signaled. In this case, you can call [**ISpatialAudioRenderStreamForHrtf::Reset**](/previous-versions/windows/desktop/legacy/mt779303(v=vs.85)) to attempt to reset the spatial audio stream.

Next, call [**ISpatialAudioRenderStreamForHrtf::BeginUpdatingAudioObjects**](/previous-versions/windows/desktop/legacy/mt779299(v=vs.85)) to let the system know that you are about to fill the audio objects' buffers with data. This method returns the number of available dynamic audio objects, not used in this example, and the frame count of the buffer for audio objects rendered by this stream.

Whenever the spawn counter reaches the specified value, we will activate a new dynamic audio object by calling [**ISpatialAudioRenderStreamForHrtf::ActivateSpatialAudioObjectForHrtf**](/windows/win32/api/spatialaudiohrtf/nf-spatialaudiohrtf-ispatialaudioobjectrenderstreamforhrtf-activatespatialaudioobjectforhrtf) specifying [**AudioObjectType\_Dynamic**](/windows/desktop/api/spatialaudioclient/ne-spatialaudioclient-audioobjecttype). If all available dynamic audio objects have already been allocated, this method will return **SPLAUDCLNT\_E\_NO\_MORE\_OBJECTS**. In this case, you can choose to release one or more previously activated audio objects based on your app-specific prioritization. After the dynamic audio object has been created, it is added to a new **My3dObjectForHrtf** structure, with randomized position, rotation, velocity, volume, and frequency values, which is then added to the list of active objects.

Next, iterate over all of the active objects, represented in this example with the app-defined **My3dObjectForHrtf** structure. For each audio object, call [**ISpatialAudioObjectForHrtf::GetBuffer**](/previous-versions/windows/desktop/legacy/mt779271(v=vs.85)) to get a pointer to the spatial audio object's audio buffer. This method also returns the size of the buffer, in bytes. The helper method, **WriteToAudioObjectBuffer**, listed previously in this article, to fill the buffer with audio data. After writing to the buffer, the example updates the position and orientation of the HRTF audio object by calling [**ISpatialAudioObjectForHrtf::SetPosition**](/windows/desktop/api/spatialaudiohrtf/nf-spatialaudiohrtf-ispatialaudioobjectforhrtf-setposition) and [**ISpatialAudioObjectForHrtf::SetOrientation**](/windows/desktop/api/spatialaudiohrtf/nf-spatialaudiohrtf-ispatialaudioobjectforhrtf-setorientation). In this example, a helper method, **CalculateEmitterConeOrientationMatrix**, is used to calculate the orientation matrix given the direction the 3D object is pointing. The implementation of this method is shown below. The volume of the audio object can also be modified by calling [**ISpatialAudioObjectForHrtf::SetGain**](/windows/desktop/api/spatialaudiohrtf/nf-spatialaudiohrtf-ispatialaudioobjectforhrtf-setgain). If you don't update the position, orientation, or volume of the object, it will retain the position, orientation, and volume from the last time it was set. If the object's app-defined lifetime has been reached, [**ISpatialAudioObjectForHrtf::SetEndOfStream**](/previous-versions/windows/desktop/legacy/mt779275(v=vs.85)) is called to let the audio pipeline know that no more audio will be written using this object and the object is set to **nullptr** to free up its resources.

After writing data to all of your audio objects, call [**ISpatialAudioRenderStreamForHrtf::EndUpdatingAudioObjects**](/previous-versions/windows/desktop/legacy/mt779300(v=vs.85)) to let the system know the data is ready for rendering. You can only call **GetBuffer** in between a call to **BeginUpdatingAudioObjects** and **EndUpdatingAudioObjects**.


```C++
// Start streaming / rendering 
hr = spatialAudioStreamForHrtf->Start();

do
{
    // Wait for a signal from the audio-engine to start the next processing pass
    if (WaitForSingleObject(bufferCompletionEvent, 100) != WAIT_OBJECT_0)
    {
        break;
    }

    UINT32 availableDynamicObjectCount;
    UINT32 frameCount;

    // Begin the process of sending object data and metadata
    // Get the number of active objects that can be used to send object-data
    // Get the frame count that each buffer will be filled with 
    hr = spatialAudioStreamForHrtf->BeginUpdatingAudioObjects(&availableDynamicObjectCount, &frameCount);

    BYTE* buffer;
    UINT32 bufferLength;

    // Spawn a new dynamic audio object every 200 iterations
    if (spawnCounter % 200 == 0 && spawnCounter < 1000)
    {
        // Activate a new dynamic audio object
        Microsoft::WRL::ComPtr<ISpatialAudioObjectForHrtf> audioObject;
        hr = spatialAudioStreamForHrtf->ActivateSpatialAudioObjectForHrtf(AudioObjectType::AudioObjectType_Dynamic, &audioObject);

        // If SPTLAUDCLNT_E_NO_MORE_OBJECTS is returned, there are no more available objects
        if (SUCCEEDED(hr))
        {
            // Init new struct with the new audio object.
            My3dObjectForHrtf obj = { audioObject,
                Windows::Foundation::Numerics::float3(static_cast<float>(pos_dist(gen)), static_cast<float>(pos_dist(gen)), static_cast<float>(pos_dist(gen))),
                Windows::Foundation::Numerics::float3(static_cast<float>(vel_dist(gen)), static_cast<float>(vel_dist(gen)), static_cast<float>(vel_dist(gen))),
                static_cast<float>(static_cast<float>(yRotation_dist(gen))),
                static_cast<float>(static_cast<float>(deltaYRotation_dist(gen))),
                static_cast<float>(static_cast<float>(pitch_dist(gen))),
                format.nSamplesPerSec * 5 // 5 seconds of audio samples
            };

            objectVector.insert(objectVector.begin(), obj);
        }
    }
    spawnCounter++;

    // Loop through all dynamic audio objects
    std::vector<My3dObjectForHrtf>::iterator it = objectVector.begin();
    while (it != objectVector.end())
    {
        it->audioObject->GetBuffer(&buffer, &bufferLength);

        if (it->totalFrameCount >= frameCount)
        {
            // Write audio data to the buffer
            WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), frameCount, it->frequency, format.nSamplesPerSec);

            // Update the position and volume of the audio object
            it->audioObject->SetPosition(it->position.x, it->position.y, it->position.z);
            it->position += it->velocity;


            Windows::Foundation::Numerics::float3 emitterDirection = Windows::Foundation::Numerics::float3(cos(it->yRotationRads), 0, sin(it->yRotationRads));
            Windows::Foundation::Numerics::float3 listenerDirection = Windows::Foundation::Numerics::float3(0, 0, 1);
            DirectX::XMFLOAT4X4 rotationMatrix;

            DirectX::XMMATRIX rotation = CalculateEmitterConeOrientationMatrix(emitterDirection, listenerDirection);
            XMStoreFloat4x4(&rotationMatrix, rotation);

            SpatialAudioHrtfOrientation orientation = {
                rotationMatrix._11, rotationMatrix._12, rotationMatrix._13,
                rotationMatrix._21, rotationMatrix._22, rotationMatrix._23,
                rotationMatrix._31, rotationMatrix._32, rotationMatrix._33
            };

            it->audioObject->SetOrientation(&orientation);
            it->yRotationRads += it->deltaYRotation;

            it->totalFrameCount -= frameCount;

            ++it;
        }
        else
        {
            // If the audio object reaches its lifetime, set EndOfStream and release the object

            // Write audio data to the buffer
            WriteToAudioObjectBuffer(reinterpret_cast<float*>(buffer), it->totalFrameCount, it->frequency, format.nSamplesPerSec);

            // Set end of stream for the last buffer 
            hr = it->audioObject->SetEndOfStream(it->totalFrameCount);

            it->audioObject = nullptr; // Release the object

            it->totalFrameCount = 0;

            it = objectVector.erase(it);
        }
    }

    // Let the audio-engine know that the object data are available for processing now
    hr = spatialAudioStreamForHrtf->EndUpdatingAudioObjects();

} while (objectVector.size() > 0);
```



When you are done rendering spatial audio, stop the spatial audio stream by calling [**ISpatialAudioRenderStreamForHrtf::Stop**](/previous-versions/windows/desktop/legacy/mt779305(v=vs.85)). If you are not going to use the stream again, free its resources by calling [**ISpatialAudioRenderStreamForHrtf::Reset**](/previous-versions/windows/desktop/legacy/mt779303(v=vs.85)).


```C++
// Stop the stream 
hr = spatialAudioStreamForHrtf->Stop();

// We don't want to start again, so reset the stream to free it's resources.
hr = spatialAudioStreamForHrtf->Reset();

CloseHandle(bufferCompletionEvent);
```



The following code example shows the implementation of the **CalculateEmitterConeOrientationMatrix** helper method which was used in the example above to calculate the orientation matrix given the direction the 3D object is pointing.


```C++
DirectX::XMMATRIX CalculateEmitterConeOrientationMatrix(Windows::Foundation::Numerics::float3 listenerOrientationFront, Windows::Foundation::Numerics::float3 emitterDirection)
{
    DirectX::XMVECTOR vListenerDirection = DirectX::XMLoadFloat3(&listenerOrientationFront);
    DirectX::XMVECTOR vEmitterDirection = DirectX::XMLoadFloat3(&emitterDirection);
    DirectX::XMVECTOR vCross = DirectX::XMVector3Cross(vListenerDirection, vEmitterDirection);
    DirectX::XMVECTOR vDot = DirectX::XMVector3Dot(vListenerDirection, vEmitterDirection);
    DirectX::XMVECTOR vAngle = DirectX::XMVectorACos(vDot);
    float angle = DirectX::XMVectorGetX(vAngle);

    // The angle must be non-zero
    if (fabsf(angle) > FLT_EPSILON)
    {
        // And less than PI
        if (fabsf(angle) < DirectX::XM_PI)
        {
            return DirectX::XMMatrixRotationAxis(vCross, angle);
        }

        // If equal to PI, find any other non-collinear vector to generate the perpendicular vector to rotate about
        else
        {
            DirectX::XMFLOAT3 vector = { 1.0f, 1.0f, 1.0f };
            if (listenerOrientationFront.x != 0.0f)
            {
                vector.x = -listenerOrientationFront.x;
            }
            else if (listenerOrientationFront.y != 0.0f)
            {
                vector.y = -listenerOrientationFront.y;
            }
            else // if (_listenerOrientationFront.z != 0.0f)
            {
                vector.z = -listenerOrientationFront.z;
            }
            DirectX::XMVECTOR vVector = DirectX::XMLoadFloat3(&vector);
            vVector = DirectX::XMVector3Normalize(vVector);
            vCross = DirectX::XMVector3Cross(vVector, vEmitterDirection);
            return DirectX::XMMatrixRotationAxis(vCross, angle);
        }
    }

    // If the angle is zero, use an identity matrix
    return DirectX::XMMatrixIdentity();
}
```



## Related topics

<dl> <dt>

[Spatial Sound](spatial-sound.md)
</dt> <dt>

[**ISpatialAudioClient**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient)
</dt> <dt>

[**ISpatialAudioObject**](/windows/desktop/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobject)
</dt> </dl>

 

 

---
description: When you create a source voice, you can pass a structure to it that defines callbacks for certain audio events. You can use these callbacks to perform actions or to signal other code.
ms.assetid: 0bace0c5-9171-efd8-9a38-2c2b3452f73f
title: 'How to: Use Source Voice Callbacks'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Use Source Voice Callbacks

When you create a source voice, you can pass a structure to it that defines callbacks for certain audio events. You can use these callbacks to perform actions or to signal other code.

1.  Create a class that inherits from the [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) interface. All member functions of **IXAudio2VoiceCallback** are purely virtual, and must be defined. The only function of interest in this example is [**OnStreamEnd**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voicecallback-onstreamend). Therefore, the rest of the functions are stubs. The **OnStreamEnd** function triggers an event that indicates the sound is done playing.

    ```
    class VoiceCallback : public IXAudio2VoiceCallback
    {
    public:
        HANDLE hBufferEndEvent;
        VoiceCallback(): hBufferEndEvent( CreateEvent( NULL, FALSE, FALSE, NULL ) ){}
        ~VoiceCallback(){ CloseHandle( hBufferEndEvent ); }

        //Called when the voice has just finished playing a contiguous audio stream.
        void OnStreamEnd() { SetEvent( hBufferEndEvent ); }

        //Unused methods are stubs
        void OnVoiceProcessingPassEnd() { }
        void OnVoiceProcessingPassStart(UINT32 SamplesRequired) {    }
        void OnBufferEnd(void * pBufferContext)    { }
        void OnBufferStart(void * pBufferContext) {    }
        void OnLoopEnd(void * pBufferContext) {    }
        void OnVoiceError(void * pBufferContext, HRESULT Error) { }
    };
    ```

    

2.  Create a [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) with [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice) using an instance of the callback class created previously as the pCallback parameter.

    ```
    VoiceCallback voiceCallback;
    if( FAILED(hr = pXaudio2->CreateSourceVoice( &pSourceVoice, (WAVEFORMATEX*)&wfx,
                                 0, XAUDIO2_DEFAULT_FREQ_RATIO, &voiceCallback, NULL, NULL ) ) ) return;
    ```

    

3.  After starting the voice, use the [**WaitForSingleObjectEx**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex) method to wait for the event to be triggered.

    ```
    WaitForSingleObjectEx( voiceCallback.hBufferEndEvent, INFINITE, TRUE );
    ```

    

## Related topics

<dl> <dt>

[Callbacks](callbacks.md)
</dt> <dt>

[XAudio2 Callbacks](xaudio2-callbacks.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[How to: Stream a Sound from Disk](how-to--stream-a-sound-from-disk.md)
</dt> </dl>

 

 

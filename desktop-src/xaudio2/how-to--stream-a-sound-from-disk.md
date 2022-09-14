---
description: You can stream audio data in XAudio2 by creating a separate thread and perform buffer reads of the audio data in the streaming thread, and then use callbacks to control that thread.
ms.assetid: 48b80a66-91c1-973f-069b-6f63422d7154
title: 'How to: Stream a Sound from Disk'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Stream a Sound from Disk

> [!Note]  
> This content applies only to desktop apps and will require revision to function in a Windows Store app. Please refer to the documentation for **CreateFile2**, [CreateEventEx](/windows/win32/api/synchapi/nf-synchapi-createeventexa), [WaitForSingleObjectEx](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex), [SetFilePointerEx](/windows/win32/api/fileapi/nf-fileapi-setfilepointerex), and **GetOverlappedResultEx**. See the StreamEffect Windows 8 sample from the [Windows SDK Samples Gallery](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Windows%208%20app%20samples/%5BC%2B%2B%5D-Windows%208%20app%20samples/C%2B%2B/Windows%208%20app%20samples/XAudio2%20audio%20stream%20effect%20sample%20(Windows%208)).

 

You can stream audio data in XAudio2 by creating a separate thread and perform buffer reads of the audio data in the streaming thread, and then use callbacks to control that thread.

-   [Performing buffer reads in the streaming thread](#performing-buffer-reads-in-the-streaming-thread)
-   [Creating the callback class](#creating-the-callback-class)

## Performing buffer reads in the streaming thread

To perform buffer reads in the streaming thread follow these steps:

1.  Create an array of read buffers.

    ```
    #define STREAMING_BUFFER_SIZE 65536
    #define MAX_BUFFER_COUNT 3
    BYTE buffers[MAX_BUFFER_COUNT][STREAMING_BUFFER_SIZE];
    ```

    

2.  Initialize an OVERLAPPED structure.

    The structure is used to check when an asynchronous disk read has finished.

    ```
    OVERLAPPED Overlapped = {0};
    Overlapped.hEvent = CreateEvent( NULL, TRUE, FALSE, NULL );
    ```

    

3.  Call the [**Start**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start) function on the [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) that will be playing the streaming audio.

    ```
    hr = pSourceVoice->Start( 0, 0 );
    ```

    

4.  Loop while the current read position is not passed the end of the audio file.

    ```
    CurrentDiskReadBuffer = 0;
    CurrentPosition = 0;
    while ( CurrentPosition < cbWaveSize )
    {
        ...
    }
    ```

    

    In the loop, do the following:

    1.  Read a chunk of data from the disk into the current read buffer.

        ```
        DWORD dwRead;
        if( SUCCEEDED(hr) && 0 == ReadFile( hFile, pData, dwDataSize, &dwRead, pOverlapped ) )
            hr = HRESULT_FROM_WIN32( GetLastError() );
            DWORD cbValid = min( STREAMING_BUFFER_SIZE, cbWaveSize - CurrentPosition );
            DWORD dwRead;
            if( 0 == ReadFile( hFile, buffers[CurrentDiskReadBuffer], STREAMING_BUFFER_SIZE, &dwRead, &Overlapped ) )
                hr = HRESULT_FROM_WIN32( GetLastError() );
            Overlapped.Offset += cbValid;

            //update the file position to where it will be once the read finishes
            CurrentPosition += cbValid;
        ```

        

    2.  Use the **GetOverlappedResult** function to wait for the event that signals the read has finished.

        ```
        DWORD NumberBytesTransferred;
        ::GetOverlappedResult(hFile,&Overlapped,&NumberBytesTransferred, TRUE);
        ```

        

    3.  Wait for the number of buffers queued on the [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) to be less than the number of read buffers.

        The state of the [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) is checked with the [**GetState**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-getstate) function.

        ```
        XAUDIO2_VOICE_STATE state;
        while( pSourceVoice->GetState( &state ), state.BuffersQueued >= MAX_BUFFER_COUNT - 1)
        {
            WaitForSingleObject( Context.hBufferEndEvent, INFINITE );
        }
        ```

        

    4.  Submit the current read buffer to the [**source voice**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) using the [**SubmitSourceBuffer**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-submitsourcebuffer) function.

        ```
        XAUDIO2_BUFFER buf = {0};
        buf.AudioBytes = cbValid;
        buf.pAudioData = buffers[CurrentDiskReadBuffer];
        if( CurrentPosition >= cbWaveSize )
        {
            buf.Flags = XAUDIO2_END_OF_STREAM;
        }
        pSourceVoice->SubmitSourceBuffer( &buf );
        ```

        

    5.  Set the current read buffer index to the next buffer.

        ```
        CurrentDiskReadBuffer++;
        CurrentDiskReadBuffer %= MAX_BUFFER_COUNT;
        ```

        

5.  After the loop has finished, wait for the remaining queued buffers to finish playing.

    When the remaining buffers have finished playing, the sound stops, and the thread can exit or be reused to stream another sound.

    ```
    XAUDIO2_VOICE_STATE state;
    while( pSourceVoice->GetState( &state ), state.BuffersQueued > 0 )
    {
        WaitForSingleObjectEx( Context.hBufferEndEvent, INFINITE, TRUE );
    }
    ```

    

## Creating the callback class

To create the callback class, create a class that inherits from the [**IXAudio2VoiceCallback**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) interface.

The class should set an event in its [**OnBufferEnd**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2voicecallback-onbufferend) method. This allows the streaming thread to put itself to sleep until the event signals it that XAudio2 has finished reading from an audio buffer. For more information about using callbacks with XAudio2, see [How to: Use Source Voice Callbacks](how-to--use-source-voice-callbacks.md).


```
struct StreamingVoiceContext : public IXAudio2VoiceCallback
{
    HANDLE hBufferEndEvent;
    StreamingVoiceContext(): hBufferEndEvent( CreateEvent( NULL, FALSE, FALSE, NULL ) ){}
    ~StreamingVoiceContext(){ CloseHandle( hBufferEndEvent ); }
    void OnBufferEnd( void* ){ SetEvent( hBufferEndEvent ); }
    ...
};
```



## Related topics

<dl> <dt>

[Streaming Audio Data](streaming-audio-data.md)
</dt> <dt>

[XAudio2 Callbacks](callbacks.md)
</dt> <dt>

[XAudio2 Programming Guide](programming-guide.md)
</dt> <dt>

[How to: Build a Basic Audio Processing Graph](how-to--build-a-basic-audio-processing-graph.md)
</dt> <dt>

[How to: Use Source Voice Callbacks](how-to--use-source-voice-callbacks.md)
</dt> </dl>

 

 

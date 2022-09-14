---
description: This topic describes the minimum steps required to play previously-loaded audio data in XAudio2.
ms.assetid: 5172b31c-d2af-45aa-5bd4-b62502f3c047
title: 'How to: Play a Sound with XAudio2'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Play a Sound with XAudio2

This topic describes the minimum steps required to play previously-loaded audio data in XAudio2. After you initialize XAudio2 (see [How to: Initialize XAudio2](how-to--initialize-xaudio2.md)) and load the audio data (see How to: [How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md)), you can play a sound by creating a source voice and passing audio data to it.

## To play a sound

1.  Initialize the XAudio2 engine by following the steps described in [How to: Initialize XAudio2](how-to--initialize-xaudio2.md).
2.  Populate a [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) and [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer) structure by following the steps described in [How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md).
    > [!Note]  
    > Depending on the format of the audio data, you may need to use a larger data structure containing a [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure in place of a **WAVEFORMATEX**. See the **WAVEFORMATEX** reference page for more information.

     

3.  Create a source voice by calling the [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice) method on an instance of the XAudio2 engine. The format of the voice is specified by the values set in a [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure.
    ```
    IXAudio2SourceVoice* pSourceVoice;
    if( FAILED(hr = pXAudio2->CreateSourceVoice( &pSourceVoice, (WAVEFORMATEX*)&wfx ) ) ) return hr;
    ```

    

4.  Submit an [**XAUDIO2\_BUFFER**](/windows/desktop/api/xaudio2/ns-xaudio2-xaudio2_buffer) to the source voice using the function [**SubmitSourceBuffer**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-submitsourcebuffer).
    ```
    if( FAILED(hr = pSourceVoice->SubmitSourceBuffer( &buffer ) ) )
        return hr;
    ```

    

    > [!Note]  
    > The audio sample data to which *buffer* points is still 'owned' by the app and must remain allocated and accessible until the sound stops playing.

     

5.  Use the [**Start**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start) function to start the source voice. Since all XAudio2 voices send their output to the mastering voice by default, audio from the source voice automatically makes its way to the audio device selected at initialization. In a more complicated audio graph, the source voice would have to specify the voice to which its output should be sent.
    ```
    if ( FAILED(hr = pSourceVoice->Start( 0 ) ) )
        return hr;
    ```

    

## Notes for Windows Store apps

We recommend that you make use of a [smart pointer](/previous-versions/visualstudio/visual-studio-2012/hh279674(v=vs.110)) to manage the lifetime of XAUDIO2 objects in an exception safe manner. For Windows Store apps, you can use the [**ComPtr**](/previous-versions/visualstudio/visual-studio-2012/br244983(v=vs.110)) smart pointer template from the Windows Runtime C++ Template Library (WRL).


```
Microsoft::WRL::ComPtr<IXAudio2SourceVoice> SourceVoice;
HRESULT hr;
if( FAILED(hr = pXAudio2->CreateSourceVoice( &SourceVoice, (WAVEFORMATEX*)&wfx ) ) )
    throw Platform::Exception::CreateException(hr); 

if( FAILED(hr = SourceVoice->SubmitSourceBuffer( &buffer ) ) )
    throw Platform::Exception::CreateException(hr); 

if ( FAILED(hr = SourceVoice->Start( 0 ) ) )
    throw Platform::Exception::CreateException(hr);
```



> [!Note]  
> Ensure that all smart pointers to XAUDIO2 objects are fully released before you release the [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) object.

 

## Related topics

<dl> <dt>

[XAudio2 Getting Started](getting-started.md)
</dt> <dt>

[How to: Initialize XAudio2](how-to--initialize-xaudio2.md)
</dt> <dt>

[How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md)
</dt> </dl>

 

 

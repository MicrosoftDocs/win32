---
title: 'How to: Play a sound with XAudio2'
description: This topic describes the minimum steps required to play previously-loaded audio data in XAudio2.
ms.assetid: 5172b31c-d2af-45aa-5bd4-b62502f3c047
ms.topic: how-to
ms.date: 08/15/2024
---

# How to: Play a sound with XAudio2

This topic describes the minimum steps required to play previously-loaded audio data in XAudio2.

After you initialize XAudio2 (see [How to: Initialize XAudio2](how-to--initialize-xaudio2.md)) and load the audio data (see How to: [How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md)), you can play a sound by creating a source voice, and passing audio data to it.

## To play a sound

1. First initialize XAudio2 for audio playback by following the steps described in [How to: Initialize XAudio2](./how-to--initialize-xaudio2.md).
2. Then populate a [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure and an [**XAUDIO2_BUFFER**](/windows/win32/api/xaudio2/ns-xaudio2-xaudio2_buffer) structure by following the steps described in [How to: Load audio data files in XAudio2](./how-to--load-audio-data-files-in-xaudio2.md).

    > [!NOTE]  
    > Depending on the format of the audio data, you might need to use a larger data structure (one that *contains* a **WAVEFORMATEX** structure) in place of a **WAVEFORMATEX**. For more info, see the [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) topic.

3. Next, to create what's known as a source voice, call the [**IXAudio2::CreateSourceVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createsourcevoice) method. That will give you a pointer to an [**IXAudio2SourceVoice**](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) interface. The format of the voice is specified by the values set in the [**WAVEFORMATEX**](/windows/win32/api/mmreg/ns-mmreg-waveformatex) structure.

    ```cppwinrt
    IXAudio2SourceVoice* m_pXAudio2SourceVoice{};
    ...
    winrt::check_hresult(m_xAudio2->CreateSourceVoice(&m_pXAudio2SourceVoice, (WAVEFORMATEX*)&wfx)));    
    ```

4. Submit an [**XAUDIO2_BUFFER**](/windows/win32/api/xaudio2/ns-xaudio2-xaudio2_buffer) to the source voice by calling the [**IXAudio2SourceVoice::SubmitSourceBuffer**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-submitsourcebuffer) method.

    ```cppwinrt
    winrt::check_hresult(m_pXAudio2SourceVoice->SubmitSourceBuffer(&xAudio2Buffer));
    ```

    > [!NOTE]
    > The audio sample data pointed to by the *pBuffer* parameter of **SubmitSourceBuffer** is still *owned* by the app, and it must remain allocated and accessible until the sound stops playing.

5. To start the source voice, call the [**IXAudio2SourceVoice::Start**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2sourcevoice-start) method. Since all XAudio2 voices send their output to the mastering voice by default, audio from the source voice automatically makes its way to the audio device that was created/selected at initialization. In a more complicated audio graph, the source voice would need to specify *which* voice its output should be sent to.

    ```cppwinrt
    winrt::check_hresult(m_pXAudio2SourceVoice->Start(0));
    ```

## Smart pointers

For safety and convenience, you can use a smart pointer for the **IXAudio2** interface. But the voice interfaces (such as **IXAudio2MasteringVoice**) don't have a **Release** method, so you'll see a build error if you try to use a smart pointer for those. In these code snippets we use a smart pointer where possible, and a raw pointer where necessary.

## Related topics

* [XAudio2 Getting Started](getting-started.md)
* [How to: Initialize XAudio2](how-to--initialize-xaudio2.md)
* [How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md)

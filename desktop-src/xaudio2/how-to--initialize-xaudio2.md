---
Description: XAudio2 is initialized for audio playback by creating an instance of the XAudio2 engine, and creating a mastering voice.
ms.assetid: 4db2e7fc-0a87-0344-a07c-3abf2b21af32
title: 'How to: Initialize XAudio2'
ms.topic: article
ms.date: 05/31/2018
---

# How to: Initialize XAudio2

XAudio2 is initialized for audio playback by creating an instance of the XAudio2 engine, and creating a mastering voice.

**To initialize XAudio2**

1.  Use the [**XAudio2Create**](/windows/desktop/api/xaudio2/nf-xaudio2-xaudio2create) function to create an instance of the XAudio2 engine.

    ```
    IXAudio2* pXAudio2 = NULL;
    HRESULT hr;
    if ( FAILED(hr = XAudio2Create( &pXAudio2, 0, XAUDIO2_DEFAULT_PROCESSOR ) ) )
        return hr;
    ```

    

2.  Use the [**CreateMasteringVoice**](https://msdn.microsoft.com/library/Hh405048(v=VS.85).aspx) method to create a mastering voice.

    The mastering voices encapsulates an audio device. It is the ultimate destination for all audio that passes through an audio graph.

    ```
    IXAudio2MasteringVoice* pMasterVoice = NULL;
    if ( FAILED(hr = pXAudio2->CreateMasteringVoice( &pMasterVoice ) ) )
        return hr;
    ```

    

## Notes for Windows Store apps

We recommend that you make use of a [smart pointer](https://msdn.microsoft.com/library/Hh279674(v=VS.110).aspx) to manage the lifetime of XAUDIO2 objects in an exception safe manner. For Windows Store apps, you can use the [**ComPtr**](https://msdn.microsoft.com/library/BR244983(v=VS.110).aspx) smart pointer template from the Windows Runtime C++ Template Library (WRL).


```C++
Microsoft::WRL::ComPtr<IXAudio2> XAudio2;
HRESULT hr;
if ( FAILED(hr = XAudio2Create( &XAudio2, 0, XAUDIO2_DEFAULT_PROCESSOR ) ) )
    throw Platform::Exception::CreateException(hr);

IXAudio2MasteringVoice* pMasterVoice = NULL;
if ( FAILED(hr = pXAudio2->CreateMasteringVoice( &pMasterVoice ) ) )
    return hr;
```



> [!Note]  
> Ensure that all smart pointers to XAUDIO2 objects are fully released before you release the [**IXAudio2**](/windows/desktop/api/xaudio2/nn-xaudio2-ixaudio2) object.

 

## Related topics

<dl> <dt>

[XAudio2 Getting Started](getting-started.md)
</dt> <dt>

[How to: Load Audio Data Files in XAudio2](how-to--load-audio-data-files-in-xaudio2.md)
</dt> <dt>

[How to: Play a Sound with XAudio2](how-to--play-a-sound-with-xaudio2.md)
</dt> </dl>

 

 




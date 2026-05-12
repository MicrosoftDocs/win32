---
title: 'How to: Initialize XAudio2'
description: You initialize XAudio2 for audio playback by creating an instance of the XAudio2 engine, and then creating a mastering voice.
ms.assetid: 4db2e7fc-0a87-0344-a07c-3abf2b21af32
ms.topic: how-to
ms.date: 08/14/2024
---

# How to: Initialize XAudio2

You initialize XAudio2 for audio playback by creating an instance of the XAudio2 engine, and then creating a mastering voice.

1. First, you need to have initialized COM. If you're using [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/), then it's taken care of. If you're not certain that your environment has already initialized COM, then you can call [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) as long as you check the return value.

    ```cpp
    HRESULT hr = ::CoInitializeEx(nullptr, COINIT_MULTITHREADED);
    if (FAILED(hr)) return hr;
    ```

2. To create an instance of the XAudio2 engine, call the [**XAudio2Create**](/windows/win32/api/xaudio2/nf-xaudio2-xaudio2create) function. That will give you a pointer to an [**IXAudio2**](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2) interface, and it's a good idea to store that in a class data member. In this snippet we're using a C++/WinRT smart pointer, but you could use a raw pointer if necessary.

    ```cppwinrt
    winrt::com_ptr<IXAudio2> m_xAudio2{};
    ...
    winrt::check_hresult(::XAudio2Create(m_xAudio2.put(), 0, XAUDIO2_DEFAULT_PROCESSOR));
    ```

3. Next, to create what's known as a mastering voice, call the [**IXAudio2::CreateMasteringVoice**](/windows/win32/api/xaudio2/nf-xaudio2-ixaudio2-createmasteringvoice) method. That will give you a pointer to an [**IXAudio2MasteringVoice**](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice) interface. A mastering voices encapsulates an audio device. It's the ultimate destination for all audio that passes through an audio graph.

    ```cppwinrt
    IXAudio2MasteringVoice* m_pXAudio2MasteringVoice{};
    ...
    winrt::check_hresult(xAudio2->CreateMasteringVoice(&m_pXAudio2MasteringVoice));
    ```

## Smart pointers

For safety and convenience, you can use a smart pointer for the **IXAudio2** interface. But the voice interfaces (such as **IXAudio2MasteringVoice**) don't have a **Release** method, so you'll see a build error if you try to use a smart pointer for those. In these code snippets we use a smart pointer where possible, and a raw pointer where necessary.

## Related topics

* [Getting started with XAudio2](./getting-started.md)
* [How to: Load audio data files in XAudio2](./how-to--load-audio-data-files-in-xaudio2.md)
* [How to: Play a sound with XAudio2](./how-to--play-a-sound-with-xaudio2.md)

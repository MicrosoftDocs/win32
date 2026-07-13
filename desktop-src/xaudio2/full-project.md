---
title: A simple XAudio2 project in full
description: This topic shows a single, functioning, C++/WinRT code example that builds into a very simple XAudio2 app that plays a 220Hz sine wave.
ms.topic: how-to
ms.date: 08/16/2024
---

# A simple XAudio2 project in full

The previous topics showed how to initialize XAudio2, load data into an audio buffer, and then play back that audio via XAudio2 voices. This topic pulls all of the steps together into a single, functioning, C++/WinRT code example that builds into a very simple XAudio2 app that plays a 220Hz sine wave.

## Create a new project in Visual Studio

In Visual Studio, create a new C++/WinRT **Blank App, Packaged (WinUI 3 in Desktop)** project. If you name the project *MyXAudio2Project*, then you'll be able to copy-paste the source code below right into the project's source code files without any trouble.

Open each of the following source code files in turn, and edit them to look like the source code listing.

## MainWindow.xaml.idl

```idl
namespace MyXAudio2Project
{
    [default_interface]
    runtimeclass MainWindow : Microsoft.UI.Xaml.Window
    {
        MainWindow();
    }
}
```

## MainWindow.xaml.h

```cppwinrt
#pragma once

#include "MainWindow.g.h"
#include <xaudio2.h>

// Constant literals.
constexpr WORD   BITSPERSSAMPLE = 16;                                                    // 16 bits per sample.
constexpr DWORD  SAMPLESPERSEC = 44100;                                                  // 44,100 samples per second.
constexpr double CYCLESPERSEC = 220.0;                                                   // 220 cycles per second (frequency of the audible tone).
constexpr double VOLUME = 0.5;                                                           // 50% volume.
constexpr WORD   AUDIOBUFFERSIZEINCYCLES = 10;                                           // 10 cycles per audio buffer.
constexpr double PI = 3.14159265358979323846;

// Calculated constants.
constexpr DWORD  SAMPLESPERCYCLE = (DWORD)(SAMPLESPERSEC / CYCLESPERSEC);                // 200 samples per cycle.
constexpr DWORD  AUDIOBUFFERSIZEINSAMPLES = SAMPLESPERCYCLE * AUDIOBUFFERSIZEINCYCLES;   // 2,000 samples per buffer.
constexpr UINT32 AUDIOBUFFERSIZEINBYTES = AUDIOBUFFERSIZEINSAMPLES * BITSPERSSAMPLE / 8; // 4,000 bytes per buffer.

namespace winrt::MyXAudio2Project::implementation
{
    struct MainWindow : MainWindowT<MainWindow>
    {
        std::array<byte, AUDIOBUFFERSIZEINBYTES> m_buffer{};
        winrt::com_ptr<IXAudio2> m_xAudio2{};
        IXAudio2MasteringVoice* m_pXAudio2MasteringVoice{};
        IXAudio2SourceVoice* m_pXAudio2SourceVoice{};

        MainWindow()
        {
            // Xaml objects should not call InitializeComponent during construction.
            // See https://github.com/microsoft/cppwinrt/tree/master/nuget#initializecomponent
        }

        void myButton_Click(IInspectable const& sender, Microsoft::UI::Xaml::RoutedEventArgs const& args);
    };
}

namespace winrt::MyXAudio2Project::factory_implementation
{
    struct MainWindow : MainWindowT<MainWindow, implementation::MainWindow>
    {
    };
}
```

## MainWindow.xaml.cpp

```cppwinrt
#include "pch.h"
#include "MainWindow.xaml.h"
#if __has_include("MainWindow.g.cpp")
#include "MainWindow.g.cpp"
#endif

using namespace winrt;
using namespace Microsoft::UI::Xaml;

// To learn more about WinUI, the WinUI project structure,
// and more about our project templates, see: http://aka.ms/winui-project-info.

namespace winrt::MyXAudio2Project::implementation
{
    void MainWindow::myButton_Click(IInspectable const&, RoutedEventArgs const&)
    {
        myButton().Content(box_value(L"Clicked"));

        // Initialize XAudio2 (create an engine and a mastering voice).
        winrt::check_hresult(::XAudio2Create(m_xAudio2.put(), 0, XAUDIO2_DEFAULT_PROCESSOR));
        winrt::check_hresult(m_xAudio2->CreateMasteringVoice(&m_pXAudio2MasteringVoice));

        // Define a format.
        WAVEFORMATEX waveFormatEx{};
        waveFormatEx.wFormatTag = WAVE_FORMAT_PCM;
        waveFormatEx.nChannels = 1; // 1 channel
        waveFormatEx.nSamplesPerSec = SAMPLESPERSEC;
        waveFormatEx.nBlockAlign = waveFormatEx.nChannels * BITSPERSSAMPLE / 8;
        waveFormatEx.nAvgBytesPerSec = waveFormatEx.nSamplesPerSec * waveFormatEx.nBlockAlign;
        waveFormatEx.wBitsPerSample = BITSPERSSAMPLE;
        waveFormatEx.cbSize = 0;

        // Create a source voice with that format.
        winrt::check_hresult(m_xAudio2->CreateSourceVoice(&m_pXAudio2SourceVoice, &waveFormatEx));

        // Fill a buffer.
        double phase{};
        uint32_t bufferIndex{};
        while (bufferIndex < AUDIOBUFFERSIZEINBYTES)
        {
            phase += (2 * PI) / SAMPLESPERCYCLE;
            int16_t sample = (int16_t)(sin(phase) * INT16_MAX * VOLUME);
            this->m_buffer[bufferIndex++] = (byte)sample; // Values are little-endian.
            this->m_buffer[bufferIndex++] = (byte)(sample >> 8);
        }

        XAUDIO2_BUFFER xAudio2Buffer{};
        xAudio2Buffer.Flags = XAUDIO2_END_OF_STREAM;
        xAudio2Buffer.AudioBytes = AUDIOBUFFERSIZEINBYTES;
        xAudio2Buffer.pAudioData = m_buffer.data();
        xAudio2Buffer.PlayBegin = 0;
        xAudio2Buffer.PlayLength = 0;
        xAudio2Buffer.LoopBegin = 0;
        xAudio2Buffer.LoopLength = 0;
        xAudio2Buffer.LoopCount = XAUDIO2_LOOP_INFINITE;

        // Submit the buffer to the source voice, and start the voice.
        winrt::check_hresult(m_pXAudio2SourceVoice->SubmitSourceBuffer(&xAudio2Buffer));
        winrt::check_hresult(m_pXAudio2SourceVoice->Start(0));
    }
}
```

## Build and run

The project should now build and run. Press the button to hear a 220Hz test tone.

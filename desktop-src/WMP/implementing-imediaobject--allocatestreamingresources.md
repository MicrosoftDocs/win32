---
title: Implementing IMediaObject AllocateStreamingResources
description: Implementing IMediaObject AllocateStreamingResources
ms.assetid: 630550fe-2cca-4bfa-a824-a355f7fc5e02
keywords:
- Windows Media Player plug-ins,Echo sample streaming resources
- plug-ins,Echo sample streaming resources
- digital signal processing plug-ins,Echo sample streaming resources
- DSP plug-ins,Echo sample streaming resources
- Echo DSP plug-in sample,streaming resources
- Echo DSP plug-in sample,delay buffer
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Implementing IMediaObject::AllocateStreamingResources

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

In the Echo sample, the **AllocateStreamingResources** method creates the delay buffer. It does this by doing the following:

1.  Calculating a size for the buffer that corresponds to the specified delay time for the given media type.
2.  Either allocating new memory or reallocating the buffer size if it already exists.
3.  Calling a method that fills the buffer with values representing silence.

The value for silence is different depending upon the bit depth. For 8-bit audio, silence is represented by the hex value 80; for 16-bit audio, silence is represented by zero.

## Calculating the Delay Buffer Size

In order to calculate the size required for the delay buffer, you must first retrieve a **WAVEFORMATEX** structure that contains information about the audio data. The following example retrieves a pointer to this structure from the input **DMO\_MEDIA\_TYPE** structure:


```
// Get a pointer to the WAVEFORMATEX structure.
WAVEFORMATEX *pWave = ( WAVEFORMATEX * ) m_mtInput.pbFormat;
if (NULL == pWave)
{
    return E_FAIL;
}
```



Once you have stored a pointer to the proper **WAVEFORMATEX** structure, you can inspect its members and use them to calculate the required buffer size. The following code example demonstrates this:


```
// Get the size of the buffer required.
m_cbDelayBuffer = (m_dwDelayTime * pWave->nSamplesPerSec * pWave->nBlockAlign) / 1000;
```



This algorithm computes the buffer size by multiplying the delay time, in milliseconds, by the number of samples per millisecond, then multiplying the result by the number of channels, and then multiplying the result by the number of bytes per sample. The number of channels and the number of bytes per sample are not obvious; they are encoded in the nBlockAlign member. Dividing by 1000 reduces the nSamplesPerSec value to samples per millisecond; the millisecond is the desired unit because the delay time is expressed in milliseconds.

## Allocating the Delay Buffer Memory

Once you have calculated the memory requirements, you can allocate the buffer. The buffer may need to be deleted if it exists, such as when the user invokes the property page to change the delay time value. The following code demonstrates allocating the delay buffer:


```
// Test whether a buffer exists.
if (m_pbDelayBuffer)
{
    // A buffer already exists.
    // Delete the delay buffer.
    delete m_pbDelayBuffer;
    m_pbDelayBuffer = NULL;
}

// Allocate the buffer.
m_pbDelayBuffer = new BYTE[m_cbDelayBuffer];

if (!m_pbDelayBuffer)
    return E_OUTOFMEMORY;
```



If the buffer is successfully allocated, you should move the movable pointer to the head of the buffer, as demonstrated in the following example:


```
// Move the echo pointer to the head of the delay buffer.
m_pbDelayPointer = m_pbDelayBuffer;
```



## Filling the Delay Buffer with Silence

It is convenient to write a method to fill the delay buffer with values representing silence. The method should receive the pointer to the valid WAVEFORMATEX structure and then inspect the wBitsPerSample member to determine whether the audio is 8-bit or higher. The following example fills the delay buffer with the correct value for silence:


```
void CEcho::FillBufferWithSilence(WAVEFORMATEX *pWfex)
{
    if (8 == pWfex->wBitsPerSample)
    {
    ::FillMemory(m_pbDelayBuffer, m_cbDelayBuffer, 0x80);
    }
    else
    ::ZeroMemory(m_pbDelayBuffer, m_cbDelayBuffer);
}
```



Remember to add the forward declaration for the function to the header file Echo.h in the private section:


```
void FillBufferWithSilence(WAVEFORMATEX *pWfex);
```



You should add code at the end of AllocateStreamingResources to call this method each time the delay buffer is created or resized. The following example code passes the WAVEFORMATEX pointer named pWave to the new method:


```
// Fill the buffer with values representing silence.
FillBufferWithSilence(pWave);
```



## Reallocating the Delay Buffer Memory

When the user changes the delay time by using the property page, the size of the delay buffer must change as well. You've already added the code to AllocateStreamingResources to resize the buffer, but you need to add a line of code to CEcho::put\_delay to call the resource allocation method each time the property value changes. Here is the code:


```
// Reallocate the delay buffer.
AllocateStreamingResources();
```



## Related topics

<dl> <dt>

[**Working with Streaming Resources**](working-with-streaming-resources.md)
</dt> </dl>

 

 





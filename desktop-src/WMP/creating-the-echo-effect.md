---
title: Creating the Echo Effect
description: Creating the Echo Effect
ms.assetid: 3fac6c74-8221-4656-997b-0f903fae85b7
keywords:
- Windows Media Player plug-ins,Echo sample DoProcessOutput method
- plug-ins,Echo sample DoProcessOutput method
- digital signal processing plug-ins,Echo sample DoProcessOutput method
- DSP plug-ins,Echo sample DoProcessOutput method
- Echo DSP plug-in sample,DoProcessOutput method
- Echo DSP plug-in sample,creating echo effect
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating the Echo Effect

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

You must first remove the code from the wizard sample that scales the audio. From the 8-bit section, remove the following code:


```C++
// Apply scale factor to sample.
i = int( ((double) i) * m_dwDelayTime );

```



(Remember that m\_fScaleFactor was replaced by m\_dwDelayTime.)

From the 16-bit section, remove the following code:


```C++
// Apply scale factor to sample.
i = int( ((double) i) * m_dwDelayTime );

```



The implementation of **DoProcessOutput** provided by the plug-in wizard sample code creates a while loop that iterates one time for each sample in the input buffer provided by Windows Media Player. This loop works the same way for both 8-bit and 16-bit audio, although a separate loop is required for each. In each case, the loop initiates with the following test:


```C++
while (dwSamplesToProcess--)

```



Once inside the loop, the processing routines are very similar for 8-bit and 16-bit audio. The main difference is that the code in the 8-bit section changes the range of data values to -128 through 127, and then converts the range back again before writing the data to the output buffer. This is important to retain the symmetry of the audio waveform during processing.

Now you can begin to add and replace code in the processing loop.

## Retrieve a Sample from the Input Buffer

During each iteration of the loop, a single sample is retrieved from the input buffer. For 8-bit audio, the sample is shifted into the new range, and then the pointer to the input buffer is advanced to the next sample. The following code is from the plug-in wizard:


```C++
// Get the input sample and normalize to -128 .. 127
int i = (*pbInputData++) - 128;

```



For 16-bit audio, the process is the same except for the normalization:


```C++
// Get the input sample.
int i = *pwInputData++;

```



Remember that the pointers in the 16-bit code have been converted to type **short**.

## Retrieve a Sample from the Delay Buffer

Next, retrieve a single sample from the delay buffer. For 8-bit code, the delay samples are stored in their native range of 0 to 255. The following code, which you must add, retrieves an 8-bit delay sample:


```C++
// Get the delay sample and normalize to -128 .. 127
int delay = m_pbDelayPointer[0] - 128;

```



For 16-bit audio, the process is similar:


```C++
// Get the delay sample.
int delay = *pwDelayPointer;

```



## Write the Input Sample to the Delay Buffer

Now, you must store the input sample in the delay buffer in the same location from which you retrieved the delay sample. The following is the code you must add for 8-bit audio:


```C++
// Write the input sample into the delay buffer.
m_pbDelayPointer[0] = i + 128;

```



This is the code to add for the 16-bit section:


```C++
// Write the input sample to the delay buffer.
*pwDelayPointer = i;

```



## Move the Delay Buffer Pointer

Now that the work in the delay buffer is finished for this iteration, you can advance the movable pointer to the delay buffer. If the pointer reaches the end of the circular buffer, you must change its value to point to the head of the buffer. To do this for 8-bit audio, use the following code:


```C++
// Increment the delay pointer.
// If it has passed the end of the buffer,
// then move it to the head of the buffer.
if (++m_pbDelayPointer > pbEOFDelayBuffer)
    m_pbDelayPointer = m_pbDelayBuffer;

```



Here is the code for the 16-bit section:


```C++
// Increment the local delay pointer.
// If it is past the end of the buffer,
// then move it to the head of the buffer.
if (++pwDelayPointer > pwEOFDelayBuffer)
    pwDelayPointer = pwDelayBuffer;

```



Since the pointer in the 16-bit section is really a copy of the member variable, you must remember to update the value in the member variable with the new address. If you fail to do this, the delay buffer pointer will point to the head of the buffer repeatedly and your echo effect will not work as expected. Add the following code to the 16-bit section:


```C++
// Move the global delay pointer.
m_pbDelayPointer = (BYTE *) pwDelayPointer;

```



## Mix the Input Sample with the Delay Sample

This is where you use the wet mix and dry mix values to create the final output sample. You simply multiply each sample by the floating-point value that represents the percentage of the final signal for the sample. Multiply the input sample by the value stored in m\_fDryMix; multiply the delay sample by the value stored in m\_fWetMix. Then, add the two values. The code you must add is identical for the 8-bit and 16-bit sections:


```C++
// Mix the delay with the dry signal.
i = (int)((i * m_fDryMix ) + (delay * m_fWetMix));   

```



## Write the Data to the Output Buffer

Finally, copy the mixed sample to the output buffer, and then advance the output buffer pointer. For 8-bit audio, the plug-in wizard uses the following code to return the sample to its original range:


```C++
// Convert back to 0..255 and write to output buffer.
*pbOutputData++ = (BYTE)(i + 128);

```



For 16-bit audio, the wizard uses the following code as the final step in the processing loop:


```C++
// Write to output buffer.
*pwOutputData++ = i;

```



## Related topics

<dl> <dt>

[**Implementing CEcho::DoProcessOutput**](implementing-cecho--doprocessoutput.md)
</dt> </dl>

 

 





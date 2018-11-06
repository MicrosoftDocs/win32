---
title: Implementing DoProcessOutput
description: Implementing DoProcessOutput
ms.assetid: c6fbcfc0-741b-4aa7-9109-e06810a2e081
keywords:
- Windows Media Player plug-ins,audio DSP
- plug-ins,audio DSP
- digital signal processing plug-ins,DoProcessOutput
- DSP plug-ins,DoProcessOutput
- audio DSP plug-ins,DoProcessOutput
ms.topic: article
ms.date: 05/31/2018
---

# Implementing DoProcessOutput

To process audio data, you'll need to perform several steps in **DoProcessOutput**. The following steps use the plug-in wizard sample code as examples. If you want to create an audio DSP plug-in that processes media content of the same type that the plug-in wizard sample code does, you'll only need to change the actual processing code referred to in step 6. Following are all the steps implemented in **DoProcessOutput**:

-   If the plug-in is not currently enabled, simply copy the data unchanged into the output buffer. If your plug-in converts the data into a different format, you must also do the conversion processing here.

    ```C++
    // Test whether the plug-in is disabled by the user.
    if (!m_bEnabled)
    {
        // Just copy the data without changing it.
        memcpy(pbOutputData, m_pbInputData, *cbBytesProcessed);

        return S_OK;
    }
    
    ```

    

    -   Retrieve a pointer to the input format structure. You'll need to retrieve member data from this structure, so copy the pointer from *m\_mtInput*.**pbformat** to a local pointer variable of a type that matches the format structure type. The following example stores a pointer to a **WAVEFORMATEX** input format structure:

    ```C++
    WAVEFORMATEX *pWave = (WAVEFORMATEX*) m_mtInput.pbFormat;
    
    ```

    

    -   Calculate the number of samples to process. The sample code that the plug-in wizard generates performs this step by dividing the number of bytes to process by the **nBlockAlign** member of the WAVEFORMATEX input format structure, and then multiplying the result by the number of channels, which was stored in the **nChannels** member. The following example is from the plug-in wizard sample code:

    ```C++
    DWORD dwSamplesToProcess = (cbBytesProcessed / pWave->nBlockAlign) * pWave->nChannels;
    
    ```

    

    1.  Determine the bit depth of the audio. The plug-in wizard sample code determines 8-bit or 16-bit audio by inspecting the **wBitsPerSample** member of the **WAVEFORMATEX** structure. It then uses that value in a switch statement to provide separate processing routines for each bit depth. You may need to use a different technique when dealing with other format types and bit depths.
    2.  Create a loop to step through the audio samples in the input buffer.
    3.  Retrieve a sample from the input buffer. You do this by dereferencing the input data pointer and storing the result in a variable of type int. For 16-bit audio, you must recast the BYTE pointer to a short pointer to handle the greater audio sample precision. Once you have the value, you can immediately increment the *pbInputData* pointer so that it points to the next sample. The following examples demonstrate this:

    ```C++
    // For 8-bit audio.
    int i = *pbInputData++;  
    
    ```

    

    -or-

    ```C++
    // For 16-bit audio.
    // Recast the pointer.
    short *pwInputData = (short *) pbInputData; 

    // Enter the loop and then get the input sample.
    int i = *pwInputData++;
    
    ```

    

    1.  Perform the processing. This is where you apply the algorithms that change the sample somehow. What you do here is up to you.
    2.  Write the processed data to the output buffer. Immediately increment the pointer to the output buffer, as in the following example:

    ```C++
    *pwOutputData++ = i;
    
    ```

    

    1.  Repeat the loop until all the samples have been processed.
    2.  Return an appropriate **HRESULT**.

## Related topics

<dl> <dt>

[**Implementing an Audio DSP Plug-in**](implementing-an-audio-dsp-plug-in.md)
</dt> </dl>

 

 





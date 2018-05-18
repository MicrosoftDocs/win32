---
Description: 'The XAPO API provides the IXAPO interface and the CXAPOBase class for building new XAPO types.'
ms.assetid: '34f5c3d5-ee40-e304-7c97-d30c17621d26'
title: 'How to: Create an XAPO'
---

# How to: Create an XAPO

The XAPO API provides the [**IXAPO**](ixapo.md) interface and the [**CXAPOBase**](cxapobase.md) class for building new XAPO types. The **IXAPO** interface contains all of the methods that need to be implemented to create a new XAPO. The **CXAPOBase** class provides a basic implementation of the **IXAPO** interface. **CXAPOBase** implements all of the **IXAPO** interface methods except the [**IXAPO::Process**](ixapo-interface-process.md) method, which is unique to each XAPO.

## To create a new static XAPO

1.  Derive a new XAPO class from the [**CXAPOBase**](cxapobase.md) base class.

    > [!Note]  
    > XAPOs implement the **IUnknown** interface. The [**IXAPO**](ixapo.md) and [**IXAPOParameters**](ixapoparameters.md) interfaces include the three **IUnknown** methods: **QueryInterface**, **AddRef**, and **Release**. [**CXAPOBase**](cxapobase.md) provides implementations of all three of the **IUnknown** methods. A new instance of **CXAPOBase** will have a reference count of 1. It will be destroyed when its reference count becomes 0. To allow XAudio2 to destroy an instance of an XAPO when it is no longer needed, call **IUnknown::Release** on the XAPO after it is added to an XAudio2 effect chain. See [How to: Use an XAPO in XAudio2](how-to--use-an-xapo-in-xaudio2.md) for more information about using an XAPO with XAudio2.

     

2.  Override the [**CXAPOBase**](cxapobase.md) class implementation of the [**IXAPO::LockForProcess**](ixapo-interface-lockforprocess.md) method.

    Overriding [**LockForProcess**](ixapo-interface-lockforprocess.md) allows information about the format of audio data to be stored for use in [**IXAPO::Process**](ixapo-interface-process.md).

3.  Implement the [**IXAPO::Process**](ixapo-interface-process.md) method.

    XAudio2 calls the [**IXAPO::Process**](ixapo-interface-process.md) method whenever an XAPO needs to process audio data. **Process** contains the bulk of the code for an XAPO.

## Implementing the Process Method

The [**IXAPO::Process**](ixapo-interface-process.md) method accepts stream buffers for input and output audio data. A typical XAPO will expect one input stream buffer and one output stream buffer. You should base the processing of data from the input stream buffer on the format specified in the [**LockForProcess**](ixapo-interface-lockforprocess.md) function and any flags passed to the **Process** function with the input stream buffer. Copy the processed input stream buffer data to the output stream buffer. Set the output stream buffer's BufferFlags parameter as either [**XAPO\_BUFFER\_VALID**](xapo-buffer-flags.md) or **XAPO\_BUFFER\_SILENT**.

The following example demonstrates a [**LockForProcess**](ixapo-interface-lockforprocess.md) and [**Process**](ixapo-interface-process.md) implementation that simply copies data from an input buffer to an output buffer. However, there is no processing if the input buffer is marked with [**XAPO\_BUFFER\_SILENT**](xapo-buffer-flags.md).


```
STDMETHOD(LockForProcess) (UINT32 InputLockedParameterCount,
          const XAPO_LOCKFORPROCESS_BUFFER_PARAMETERS* pInputLockedParameters,
          UINT32 OutputLockedParameterCount,
          const XAPO_LOCKFORPROCESS_BUFFER_PARAMETERS* pOutputLockedParameters)
{
    assert(!IsLocked());
    assert(InputLockedParameterCount == 1);
    assert(OutputLockedParameterCount == 1);
    assert(pInputLockedParameters != NULL);
    assert(pOutputLockedParameters != NULL);
    assert(pInputLockedParameters[0].pFormat != NULL);
    assert(pOutputLockedParameters[0].pFormat != NULL);


    m_uChannels = pInputLockedParameters[0].pFormat->nChannels;
    m_uBytesPerSample = (pInputLockedParameters[0].pFormat->wBitsPerSample >> 3);

    return CXAPOBase::LockForProcess(
        InputLockedParameterCount,
        pInputLockedParameters,
        OutputLockedParameterCount,
        pOutputLockedParameters);
}
STDMETHOD_(void, Process)(UINT32 InputProcessParameterCount,
           const XAPO_PROCESS_BUFFER_PARAMETERS* pInputProcessParameters,
           UINT32 OutputProcessParameterCount,
           XAPO_PROCESS_BUFFER_PARAMETERS* pOutputProcessParameters,
           BOOL IsEnabled)
{
    assert(IsLocked());
    assert(InputProcessParameterCount == 1);
    assert(OutputProcessParameterCount == 1);
    assert(NULL != pInputProcessParameters);
    assert(NULL != pOutputProcessParameters);


    XAPO_BUFFER_FLAGS inFlags = pInputProcessParameters[0].BufferFlags;
    XAPO_BUFFER_FLAGS outFlags = pOutputProcessParameters[0].BufferFlags;

    // assert buffer flags are legitimate
    assert(inFlags == XAPO_BUFFER_VALID || inFlags == XAPO_BUFFER_SILENT);
    assert(outFlags == XAPO_BUFFER_VALID || outFlags == XAPO_BUFFER_SILENT);

    // check input APO_BUFFER_FLAGS
    switch (inFlags)
    {
    case XAPO_BUFFER_VALID:
        {
            void* pvSrc = pInputProcessParameters[0].pBuffer;
            assert(pvSrc != NULL);

            void* pvDst = pOutputProcessParameters[0].pBuffer;
            assert(pvDst != NULL);

            memcpy(pvDst,pvSrc,pInputProcessParameters[0].ValidFrameCount * m_uChannels * m_uBytesPerSample);
            break;
        }

    case XAPO_BUFFER_SILENT:
        {
            // All that needs to be done for this case is setting the
            // output buffer flag to XAPO_BUFFER_SILENT which is done below.
            break;
        }

    }

    // set destination valid frame count, and buffer flags
    pOutputProcessParameters[0].ValidFrameCount = pInputProcessParameters[0].ValidFrameCount; // set destination frame count same as source
    pOutputProcessParameters[0].BufferFlags     = pInputProcessParameters[0].BufferFlags;     // set destination buffer flags same as source

}
```



When writing a [**Process**](ixapo-interface-process.md) method, it is important to note XAudio2 audio data is interleaved. This means data from each channel is adjacent for a particular sample number. For example, if there is a 4-channel wave playing into an XAudio2 source voice, the audio data is a sample of channel 0, a sample of channel 1, a sample of channel 2, a sample of channel 3, and then the next sample of channels 0, 1, 2, 3, and so on.

## Related topics

<dl> <dt>

[Audio Effects](audio-effects.md)
</dt> <dt>

[XAPO Overview](xapo-overview.md)
</dt> </dl>

 

 




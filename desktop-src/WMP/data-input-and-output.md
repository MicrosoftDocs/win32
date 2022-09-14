---
title: Data Input and Output
description: Data Input and Output
ms.assetid: a03b5327-65df-4cb9-a639-1e943ac28bfc
keywords:
- Windows Media Player plug-ins,data input and output
- plug-ins,data input and output
- digital signal processing plug-ins,data input and output
- DSP plug-ins,data input and output
ms.topic: article
ms.date: 05/31/2018
---

# Data Input and Output

Windows Media Player provides audio or video data to DSP plug-ins through an input buffer allocated by Windows Media Player. DSP plug-ins return processed data to Windows Media Player through an output buffer that is also allocated by Windows Media Player. Windows Media Player manages the process of passing data between itself and the DSP plug-in by calling methods implemented by the plug-in. For a plug-in acting as a DirectX Media Object (DMO), the process works as follows:

1.  Windows Media Player calls **IMediaObject::ProcessInput**, passing a pointer to an **IMediaBuffer** object to the DSP plug-in.
2.  The DSP plug-in keeps a reference count on the input buffer object. The DSP plug-in returns an appropriate success or failure **HRESULT**.
3.  Windows Media Player calls **IMediaObject::ProcessOutput**, passing a pointer to an array of **DMO\_OUTPUT\_DATA\_BUFFER** structures (which contain output buffers) to the DSP plug-in.
4.  The DSP plug-in processes the data in the input buffer and then copies the data to the appropriate output buffer. The DSP plug-in releases the reference count on the input buffer object when all the data in the buffer has been processed. The DSP plug-in then returns an appropriate success or failure **HRESULT**.
5.  Windows Media Player renders the content in the output buffer.

For a plug-in acting as a Media Foundation Transform (MFT), the process works as follows:

-   Windows Media Player calls **IMFTransform::ProcessInput**, passing a pointer to an **IMFSample** interface object to the DSP plug-in.
    1.  The DSP plug-in keeps a reference count on the **IMFSample** interface. The DSP plug-in returns an appropriate success or failure **HRESULT**.
    2.  Windows Media Player calls **IMFTransform::ProcessOutput**, passing a pointer to an array of **MFT\_OUTPUT\_DATA\_BUFFER** structures (which contain output buffers) to the DSP plug-in.
    3.  The DSP plug-in processes the data in the input buffer and then copies the data to the appropriate output buffer. The DSP plug-in releases the reference count on the input buffer object when all the data in the buffer has been processed. The DSP plug-in then returns an appropriate success or failure **HRESULT**.
    4.  Windows Media Player renders the content in the output buffer.

This process repeats continuously while the plug-in is enabled and Windows Media Player has content to render.

> [!Note]  
> Do not write code that writes data to the input buffer or reads data from the output buffer. Incorrectly accessing data buffers may yield unexpected results.

 

## Related topics

<dl> <dt>

[**DSP Plug-in Developer Overview**](dsp-plug-in-developer-overview.md)
</dt> </dl>

 

 





---
title: About IMediaObject
description: About IMediaObject
ms.assetid: c483f74a-efd8-4a9f-a719-686099755e63
keywords:
- Windows Media Player plug-ins,interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- DSP plug-ins,interfaces
- interfaces,DSP plug-ins
- Windows Media Player plug-ins,IMediaObject interface
- plug-ins,IMediaObject interface
- digital signal processing plug-ins,IMediaObject interface
- DSP plug-ins,IMediaObject interface
- IMediaObject interface
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About IMediaObject

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IMediaObject** interface is the required interface for DMOs. **IMediaObject** contains the methods that a Windows Media Player DSP plug-in uses to get data from Windows Media Player, to process the data, and to return the processed data to Windows Media Player. For complete documentation of the **IMediaObject** interface, see the DirectShow section of the Windows SDK.

The methods of **IMediaObject** can be categorized as follows:

## Methods that Handle Format Negotiation

These are the methods that Windows Media Player calls to get information about the data formats supported by the plug-in. These methods include:

-   **GetInputMaxLatency**
-   **GetInputSizeInfo**
-   **GetInputStreamInfo**
-   **GetInputType**
-   **GetOutputSizeInfo**
-   **GetOutputStreamInfo**
-   **GetOutputType**
-   **GetStreamCount**
-   **SetInputMaxLatency**
-   **SetInputType**
-   **SetOutputType**

Several of these methods, such as **GetInputType** and **SetInputType**, use the **DMO\_MEDIA\_TYPE** structure to describe the format of the data used by a stream. When Windows Media Player calls these methods, it provides a pointer to a **DMO\_MEDIA\_TYPE** structure. If a method such as **SetInputType** specifies the media type information, the plug-in should copy the **DMO\_MEDIA\_TYPE** structure to a member variable and inspect its data members to determine the type of data that Windows Media Player will provide in the input buffer. If a method such as **GetInputType** retrieves the media type information, the plug-in should copy the address of the member variable containing the **DMO\_MEDIA\_TYPE** structure to the pointer provided by Windows Media Player in the parameter list.

Windows Media Player mainly uses two members of the **DMO\_MEDIA\_TYPE** structure:

-   **majortype**: A globally unique identifier (GUID) that specifies the overall category of the media, such as audio or video.
-   **subtype**: A GUID that specifies a more detailed description of the media, such as PCM audio.

These GUIDs can be found in the header named uuids.h, which is included with the Windows SDK.

Methods such as **GetInputSizeInfo** provide information to Windows Media Player about how much memory is required to allocate the processing buffers. Methods such as **GetStreamCount** and **GetOutputStreamInfo** provide information to Windows Media Player about the number and character of the streams supported by the DSP plug-in.

**GetInputMaxLatency** and **SetInputMaxLatency** are implemented by DMOs in special cases. Windows Media Player DSP plug-ins should return E\_NOTIMPL.

## Methods that Specify or Retrieve State Information

These are the methods that Windows Media Player calls to get or set values related to the current state of the plug-in. These methods include:

-   **GetInputCurrentType**
-   **GetInputStatus**
-   **GetOutputCurrentType**

**GetInputCurrentType** and **GetOutputCurrentType** use the **DMO\_MEDIA\_TYPE** structure to return information to Windows Media Player about the media types previously set for the input and output streams. **GetInputStatus** returns a flag that tells Windows Media Player whether the DSP plug-in can accept input data.

## Methods that Handle Buffering and Processing Data

These are the methods that Windows Media Player calls to initiate the various processes that the plug-in performs to do the digital signal processing. These methods include:

-   **AllocateStreamingResources**
-   **Discontinuity**
-   **Flush**
-   **FreeStreamingResources**
-   **Lock**
-   **ProcessInput**
-   **ProcessOutput**

Windows Media Player calls **AllocateStreamingResources** and **FreeStreamingResources** to provide the DSP plug-in with an opportunity to set up or release any additional buffers the plug-in may require for internal processing.

Windows Media Player DSP plug-ins do not need to use the DMO **Discontinuity** method.

Windows Media Player calls **Flush** to direct the DSP plug-in to flush all internally buffered data. The plug-in should release any references to **IMediaBuffer** interfaces, clear any values that specify the time stamp or sample length for the media buffer, and reinitialize any internal states that depend upon the contents of the media sample.

Windows Media Player calls ProcessInput to pass a pointer to an **IMediaBuffer** interface to the DSP plug-in. This interface provides access to the input buffer allocated by Windows Media Player to supply data to the plug-in. Windows Media Player subsequently calls **ProcessOutput** to pass a pointer to an **IMediaBuffer** interface that provides access to the output buffer allocated by Windows Media Player to receive the processed data from the DSP plug-in.

The **IMediaObject** interface includes a method named **Lock**. This method is designed to acquire or release a lock on the DMO to keep the DMO serialized when performing multiple operations. The version of **IMediaObject::Lock** in the wizard code overrides the ATL implementation of **Lock**. Because Windows Media Player serializes calls made to the DMO interface of a DSP plug-in, the implementation of **Lock** simply returns S\_OK. For details about how to create a multithreaded DMO, refer to the DirectShow section of the Windows SDK.

## Related topics

<dl> <dt>

[**Required Interfaces**](required-interfaces.md)
</dt> </dl>

 

 





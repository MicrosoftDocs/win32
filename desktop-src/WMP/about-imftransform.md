---
title: About IMFTransform
description: About IMFTransform
ms.assetid: 889f2d82-148a-4a7e-b78c-37ec86b37e0b
keywords:
- Windows Media Player plug-ins,interfaces
- plug-ins,interfaces
- digital signal processing plug-ins,interfaces
- DSP plug-ins,interfaces
- interfaces,DSP plug-ins
- Windows Media Player plug-ins,IMFTransform interface
- plug-ins,IMFTransform interface
- digital signal processing plug-ins,IMFTransform interface
- DSP plug-ins,IMFTransform interface
- IMFTransform interface
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# About IMFTransform

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **IMFTransform** interface is one of the interfaces that must be implemented by a dual-mode DSP plug-in. Windows Media Player calls the methods of the **IMFTransform** interface to provide data to the plug-in and to retrieve processed data back from the plug-in. For complete documentation of the **IMFTransform** interface, see the Media Foundation section of the Windows SDK.

The methods of **IMFTransform** can be categorized as follows.

## Methods That Handle Format Negotiation

Windows Media Player calls the following methods to get information about the data formats supported by the plug-in.

-   **GetStreamCount**
-   **GetStreamLimits**
-   **GetInputStreamInfo**
-   **GetOutputStreamInfo**
-   **GetInputAvailableType**
-   **GetOutputAvailableType**
-   **SetInputType**
-   **SetOutputType**
-   **GetAttributes**
-   **GetInputStreamAttributes**
-   **GetOutputStreamAttributes**
-   **GetStreamIDs**

## Methods That Specify or Retrieve State Information

Windows Media Player calls the following methods to get or set values related to the current state of the plug-in.

-   **SetInputType**
-   **SetOutputType**
-   **GetInputCurrentType**
-   **GetOutputCurrentType**
-   **GetInputStatus**
-   **AddInputStreams**
-   **DeleteInputStreams**
-   **GetOutputStatus**
-   **SetOutputBounds**

> [!Note]  
> **SetInputType** and **SetOutputType** are used both for format negotiation and for specifying and retrieving state information.

 

## Methods That Handle Buffering and Processing Data

Windows Media Player calls the following methods to initiate the various processes that the plug-in performs to do the digital signal processing.

-   **ProcessInput**
-   **ProcessOutput**
-   **ProcessMessage**
-   **ProcessEvent**

## Related topics

<dl> <dt>

[**Required Interfaces**](required-interfaces.md)
</dt> </dl>

 

 





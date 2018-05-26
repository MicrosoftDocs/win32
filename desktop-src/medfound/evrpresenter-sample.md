---
Description: EVRPresenter Sample
ms.assetid: 791a9816-4c40-4683-8b32-22f73d7fe84d
title: EVRPresenter Sample
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EVRPresenter Sample

Shows how to implement a custom presenter for the [Enhanced Video Renderer](enhanced-video-renderer.md) (EVR). The custom presenter can be used with either the DirectShow EVR filter or the Microsoft Media Foundation EVR sink.

## APIs Demonstrated

This sample demonstrates the following Media Foundation interfaces:

-   [**IMFClockStateSink**](/windows/win32/mfidl/nn-mfidl-imfclockstatesink?branch=master)
-   [**IMFRateSupport**](/windows/win32/mfidl/nn-mfidl-imfratesupport?branch=master)
-   [**IMFTopologyServiceLookupClient**](/windows/win32/evr/nn-evr-imftopologyservicelookupclient?branch=master)
-   [**IMFVideoDeviceID**](/windows/win32/evr/nn-evr-imfvideodeviceid?branch=master)
-   [**IMFVideoDisplayControl**](/windows/win32/evr/nn-evr-imfvideodisplaycontrol?branch=master)
-   [**IMFVideoPresenter**](/windows/win32/evr/nn-evr-imfvideopresenter?branch=master)

## Usage

The EVRPresenter sample builds a DLL that is a COM server for the presenter. Before using the custom presenter, you must register the DLL.

To use this sample in Media Foundation:

1.  Build the sample.
2.  Regsvr32 EvrPresenter.dll.
3.  Build and run the [MFPlayer Sample](mf.mfplayer_sample).
4.  From the **File** menu, select **Open** File.
5.  In the **Open File** dialog box, select **Custom EVR Presenter.**
6.  Select a file for playback.

To use this sample in DirectShow:

1.  Build the sample.
2.  Register EvrPresenter.dll.
3.  Build and run the EVRPlayer sample. This sample is included with the DirectShow samples in the Windows SDK.
4.  From the **File** menu, select **EVR Presenter**.
5.  Select a file for playback.

## Requirements



| Product                                                        | Version   |
|----------------------------------------------------------------|-----------|
| [Windows SDK](http://go.microsoft.com/fwlink/p/?linkid=129787) | Windows 7 |



 

## Downloading the Sample

This sample is available in the [Windows classic samples github repository](https://github.com/Microsoft/Windows-classic-samples/tree/master/Samples/Win7Samples/multimedia/mediafoundation/AudioClip).

## Related topics

<dl> <dt>

[Enhanced Video Renderer](enhanced-video-renderer.md)
</dt> <dt>

[How to Write an EVR Presenter](how-to-write-an-evr-presenter.md)
</dt> <dt>

[Media Foundation SDK Samples](media-foundation-sdk-samples.md)
</dt> </dl>

 

 




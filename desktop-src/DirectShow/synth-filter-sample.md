---
description: Synth Filter Sample
ms.assetid: 2d087967-3734-463f-bc5e-9552290ddc0b
title: Synth Filter Sample
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Synth Filter Sample

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

## Description

The Synth filter is a source filter that generates audio waveforms.

This filter illustrates dynamic graph building. It can switch between uncompressed PCM audio and compressed MS\_ADPCM (Microsoft Adaptive Delta Pulse Code Modulation) format.

This filter appears in GraphEdit as "Audio Synthesizer Filter."

For more information about dynamic graph building, see [Dynamic Graph Building](dynamic-graph-building.md).

## Usage

The Synth filter enables the user to set the waveform, frequency, number of channels, and other properties through the property page. To set either the upper or lower endpoint of the swept frequency range, hold down SHIFT while adjusting the frequency slider. The filter also supports a custom interface, ISynth2, for setting these properties.

To demonstrate the dynamic graph building feature, do the following:

1.  Build the filter and register it with the Regsvr32 utility.
2.  Launch GraphEdit.
3.  Insert the Audio Synthesizer filter. It appears in the DirectShow Filters category.
4.  Render the filter's output pin.
5.  Click the **Play** button.
6.  Open the filter's property page.
7.  In the Output Format area, select PCM or Microsoft ADPCM.

## Programming Notes

This sample contains the following files:

-   Dynsrc.h, Dynsrc.cpp: Contains two base classes for source filters that support dynamic graph building, CDynamicSource and CDynamicSourceStream.
-   ISynth.h: Declares the custom ISynth2 interface for setting properties on the filter.
-   Resource.h: Contains resource constants.
-   Synth.def: Exports the DLL functions needed by the COM library.
-   Synth.h, Synth.cpp: Contains the CAudioSynth class, which generates the audio data, and the CSynthFilter class, which implements the filter.
-   Synth.rc: Contains resources used by the filter.
-   Synthprp.h, Synthprp.cpp: Implements the filter's property page.

The CDynamicSource class is adapted from the [**CSource**](csource.md) base class. It uses one or more output pins derived from the CDynamicSourceStream class. The CDynamicSourceStream class is adapted from the [**CSourceStream**](csourcestream.md) class, but derives from the [**CDynamicOutputPin**](cdynamicoutputpin.md) class rather than the [**CBaseOutputPin**](cbaseoutputpin.md) class.

The CDynamicSource class has the following methods not found in [**CSource**](csource.md):

-   Stop: Signals the stop event ([**CDynamicOutputPin::m\_hStopEvent**](cdynamicoutputpin-m-hstopevent.md)), and shuts down the worker thread for all unconnected pins. On a connected pin, the pin's Inactive method will shut down the worker thread.
-   Pause: Resets the stop event.
-   JoinFilterGraph: Calls the [**CDynamicOutputPin::SetConfigInfo**](cdynamicoutputpin-setconfiginfo.md) method on each pin.

The CDynamicSourceStream class has the following methods not found in [**CSourceStream**](csourcestream.md):

-   DestroySourceThread: Shuts down the worker thread.
-   FatalError: Signals an error to the filter graph manager.
-   OutputPinNeedsToBeReconnected: Signals that the output pin should be reconnected. When this method is called, the worker thread calls the [**CDynamicOutputPin::DynamicReconnect**](cdynamicoutputpin-dynamicreconnect.md) method to reconnect the pin.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\Synth.

## Related topics

<dl> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 




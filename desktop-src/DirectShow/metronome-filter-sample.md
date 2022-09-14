---
description: Metronome Filter Sample
ms.assetid: bb279898-875a-4ce4-ac69-6c58f640fbbd
title: Metronome Filter Sample
ms.topic: article
ms.date: 05/31/2018
---

# Metronome Filter Sample

## Description

This sample filter shows how to implement a reference clock. The filter uses your default microphone input to listen for audio spikes (such as clicks, hand claps, or coughs), which it uses to determine a clock rate.

## Usage

Build the sample project and copy the filter DLL (Metronom.ax) to your Windows system directory. Run the Metronom.reg file to register the DLL.

To use the filter:

1.  Build a filter graph in GraphEdit that renders a video stream.
2.  Delete any rendered audio streams.
3.  Add the Metronome filter to the graph. It appears in the DirectShow Filters category.
4.  Run the graph. The video will begin playing at normal speed.
5.  Clap your hands or use a metronome to set a new speed.

## Programming Notes

This filter works only for video. The audio renderer is not capable of synchronizing to radically different clock rates.

If you clap 92 times per minute (once every ~652 ms), the video will play at the normal rate. You can change this default by changing the value of the constant `BPM` in Metronom.cpp.

If you stop clapping for a period of time and then start clapping again, you must start again at approximately the same speed, or the filter will ignore it. Also, the video playback rate is limited by the CPU speed. If you exceed the limit for any length of time, the filter will stop responding to rate changes. If this happens, stop the graph and restart.

If you implement your own clock, the most important rules is that reference clocks must not go backward. That is, they must never report a time value less than the previous time value.

## Downloading the Sample

To download the DirectShow SDK samples, install the latest version of the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

This sample is installed under the following path: *\[SDK Root\]*\\Samples\\Multimedia\\DirectShow\\Filters\\Metronome.

## Related topics

<dl> <dt>

[**CBaseReferenceClock Class**](cbasereferenceclock.md)
</dt> <dt>

[DirectShow Samples](directshow-samples.md)
</dt> </dl>

 

 




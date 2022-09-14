---
title: Why Use DirectShow
description: Why Use DirectShow
ms.assetid: 0ab33526-73d0-425e-a03f-29c74555f578
keywords:
- Windows Media Format SDK,DirectShow
- Windows Media Format SDK,hardware
- Windows Media Format SDK,Windows Driver Model (WDM)
- Advanced Systems Format (ASF),DirectShow
- ASF (Advanced Systems Format),DirectShow
- Advanced Systems Format (ASF),hardware
- ASF (Advanced Systems Format),hardware
- Advanced Systems Format (ASF),Windows Driver Model (WDM)
- ASF (Advanced Systems Format),Windows Driver Model (WDM)
- DirectShow,about
- DirectShow,hardware
- DirectShow,Windows Driver Model (WDM)
- Windows Driver Model (WDM)
- WDM (Windows Driver Model)
ms.topic: article
ms.date: 05/31/2018
---

# Why Use DirectShow?

There are two main reasons why an application might use DirectShow rather than the Windows Media Format SDK directly: for the convenience of the DirectShow streaming architecture, and for access to hardware.

## Convenience

With DirectShow streaming architecture, it takes only a few method calls to play Windows Media Audio or Windows Media Video files. Creating files is also simplified. You simply specify a profile using the **IConfigAsfWriter** interface on the filter, and DirectShow automatically loads the required components for rendering or writing the streams, and provides the mechanisms for transferring and synchronizing the flow of media data. DirectShow is especially useful when converting content from varied formats into Windows Media Format. You can create DirectShow filter graphs that decode a wide variety of file and compression types, and then feed the decoded streams into the [WM ASF Writer](wm-asf-writer-filter.md) filter. By comparison, the UncompAVItoWMV sample in this SDK works only with uncompressed AVI files. Text streams and arbitrary data streams can also be created and/or rendered through DirectShow, but this might require you to create custom DirectShow filters for processing those streams.

## Access to Hardware

DirectShow is the only way for application code to access Windows Driver Model (WDM)–based hardware devices such as 1394 DV cameras, TV tuners, and USB webcams. If your application must capture data directly from a WDM-based hardware device and transcode it to Windows Media Format, and the Windows Media Encoder SDK does not suit your needs, then DirectShow is the only alternative. DirectShow can also be used to access legacy devices based on Video for Windows.

 

 





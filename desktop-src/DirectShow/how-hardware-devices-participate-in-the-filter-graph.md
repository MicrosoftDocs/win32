---
description: How Hardware Devices Participate in the Filter Graph
ms.assetid: 27e1c097-9bb4-4f9c-b9f9-0d4225c0d290
title: How Hardware Devices Participate in the Filter Graph
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# How Hardware Devices Participate in the Filter Graph

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This article describes how DirectShow interacts with audio and video hardware.

**Wrapper Filters**

All DirectShow filters are user mode software components. In order for a kernel mode hardware device, such as a video capture card, to join a DirectShow filter graph, the device must be represented as a user-mode filter. This function is performed by specialized "wrapper" filters provided with DirectShow. These filters include the [Audio Capture](audio-capture.md) filter, the [VFW Capture](vfw-capture-filter.md) filter, the [TV Tuner](tv-tuner-filter.md) filter, the [TV Audio](tv-audio-filter.md) filter, and the [Analog Video Crossbar](analog-video-crossbar-filter.md) filter. DirectShow also provides a filter called KsProxy, which can represent any type of Windows Driver Model (WDM) streaming device. Hardware vendors can extend KsProxy to support custom functionality, by providing a *Ksproxy plug-in*, which is a COM object aggregated by KsProxy.

The wrapper filters expose COM interfaces that represent the capabilities of the device. The application uses these interfaces to pass information to and from the filter. The filter translates the COM method calls into device driver calls, passes that information to the driver in kernel mode, and then translates the result back to the application. The TV Tuner, TV Audio, Analog Video Crossbar, and KsProxy filters support custom driver properties through the [**IKsPropertySet**](ikspropertyset.md) interface. The VFW Capture filter and the Audio Capture filter are not extensible in this way.

For application developers, wrapper filters enable the application to control devices just as they control any other DirectShow filter. No special programming is required; the details of communicating with the kernel-mode device are encapsulated within the filter.

**Video for Windows Devices**

The VFW Capture filter supports earlier Video for Windows (VfW) capture cards. When a VfW card is present on the target system, it can be discovered and added to the filter graph using the DirectShow [System Device Enumerator](system-device-enumerator.md). For details, see [Enumerating Devices and Filters](enumerating-devices-and-filters.md).

**Audio Capture and Mixing Devices (Sound Cards)**

Newer sound cards have input jacks for microphones and other types of devices. Typically these cards also have on-board mixing capabilities for controlling the volume, treble, and bass of each individual input. In DirectShow, the sound card's inputs and mixer are wrapped by the Audio Capture filter. Each sound card can be discovered with the System Device Enumerator. To view the sound cards in your system, run GraphEdit and select from the Audio Capture Sources category. Each filter in that category is a separate instance of the Audio Capture filter. (See [Using GraphEdit](using-graphedit.md).)

**WDM Streaming Devices**

Newer hardware decoders and capture cards conform to the Windows Driver Model (WDM) specification. These devices have greater functionality than VfW devices. WDM video capture cards can support features that are not available under VfW, including the enumeration of capture formats, programmatic control of video parameters such as hue and brightness, programmatic input selection, and TV Tuner support.

To support WDM streaming devices, DirectShow provides the KsProxy filter (ksproxy.ax). KsProxy has been called the "Swiss Army Knife filter" because it does so many different things. The number of pins on the filter, and the number of COM interfaces exposed by the filter, depend on the capabilities of the underlying driver. KsProxy does not appear in the filter graph under the name "KsProxy." It always takes the friendly name of the device, which is found in the registry. To view the WDM devices on your system, run GraphEdit and select from the WDM Streaming categories. Even if you have only one WDM card on your system, that card might contain more than one device. Each device is represented as a separate filter, and each of these filters is actually KsProxy.

An application uses the System Device Enumerator to find WDM device monikers on the system. KsProxy is instantiated by calling **BindToObject** on the moniker. Because KsProxy can represent all kinds of WDM devices, it must query the driver to determine which property sets the driver supports. Property sets are collections of data structures used by WDM drivers, and also by some user mode filters, such as MPEG-2 software decoders. KsProxy configures itself to expose the COM interfaces that correspond to those property sets. KsProxy translates the COM method calls into property sets and sends these to the driver. Hardware vendors can extend KsProxy by supplying plug-ins, which are vendor-specific interfaces that expose the special capabilities of a device. All these details are hidden from application. The application controls the device by way of KsProxy, in the same way as any other DirectShow filter.

**Kernel Streaming**

WDM devices support kernel streaming, in which data is streamed entirely in kernel mode without ever switching to user mode. Switching between kernel mode and user mode is computationally expensive; kernel streaming allows for high bit rates without burdening the host CPU. WDM-based filters can use kernel streaming to pass multimedia data directly from one hardware device to another, either on the same card or on a different card, without copying the data into the system's main memory.

From an application's point of view, it appears as if the data moves from one user-mode filter to the next. In reality, the data might never pass into user mode at all, but instead might be streamed directly from one kernel-mode device to another until it is rendered on the video graphics card. Some scenarios, such as capture to a file, require that the data pass from kernel mode to user mode at some point. However, this switch does not necessarily require the data to be copied to a new location in memory.

Application developers generally do not need to be concerned with the details of kernel streaming, except as background information. See the Microsoft DDK for more detailed information about WDM, kernel streaming, KsProxy, and related topics.

## Related topics

<dl> <dt>

[The Filter Graph and Its Components](the-filter-graph-and-its-components.md)
</dt> </dl>

 

 




---
title: Device Conformance Templates
description: Device Conformance Templates
ms.assetid: '5172ab39-819a-4d74-8e6e-b275b43f664c'
keywords:
- Windows Media Format SDK,device conformance templates
- codecs,device conformance templates
- device conformance templates,about
- templates,device conformance templates
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Device Conformance Templates

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The Windows Media 9 Series codecs support device conformance templates, which are defined ranges of stream configuration settings and codec algorithms. Each template defines the ranges of values appropriate for certain devices.

In the past, the hardware manufacturers that made devices capable of playing ASF files were all working to their own standards. This resulted in the widely disparate range of capabilities on similar devices that continues today.

With device conformance templates, the Windows Media codecs establish common ground for similar devices. Hardware manufacturers can state which templates their devices conform to, enabling content creators to more confidently target their files to reading devices. It is also easier for player applications to determine whether a file is inappropriate for the device before attempting to play it.

A device conformance template is identified by a string, which is stored as a metadata attribute associated with the stream to which the template applies. For a list of the templates and their strings and parameters, see [Device Conformance Template Parameters](device-conformance-template-parameters.md).

Device conformance templates are supported for all of the Windows Media 9 Series and later codecs except the Windows Media Video 9 Screen codec and the Windows Media Audio 9 Lossless codec.

## Related topics

<dl> <dt>

[**Codec Features**](codec-features.md)
</dt> <dt>

[**Working with Device Conformance Templates**](working-with-device-conformance-templates.md)
</dt> </dl>

 

 





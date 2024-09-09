---
title: Configuring Script Streams
description: Configuring Script Streams
ms.assetid: f8f1656e-69c6-47f7-a8eb-c1039a84ebf3
keywords:
- streams,configuring script streams
- codecs,configuring script streams
- script streams,configuring
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Configuring Script Streams

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Like all arbitrary stream types, script streams need to have a bit rate and buffer window defined for them. The major media type in the [**WM\_MEDIA\_TYPE**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wm_media_type) structure must be set to WMMEDIATYPE\_Script.

Script streams need to have the **formattype** member of **WM\_MEDIA\_TYPE** set to WMFORMAT\_Script, which indicates that the **pbFormat** member points to a [**WMSCRIPTFORMAT**](/previous-versions/windows/desktop/api/wmsdkidl/ns-wmsdkidl-wmscriptformat) structure.

There is only one supported script type, WMSCRIPTTYPE\_TwoStrings.

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> <dt>

[**Script Commands**](script-commands.md)
</dt> </dl>

 

 





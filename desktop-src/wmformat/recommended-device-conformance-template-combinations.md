---
title: Recommended Device Conformance Template Combinations
description: Recommended Device Conformance Template Combinations
ms.assetid: 044f3b4c-fa81-4dac-bdde-13c47be814c6
keywords:
- Windows Media Format SDK,device conformance templates
- Advanced Systems Format (ASF),device conformance templates
- ASF (Advanced Systems Format),device conformance templates
- Windows Media Format SDK,recommended device conformance template combinations
- Advanced Systems Format (ASF),recommended device conformance template combinations
- ASF (Advanced Systems Format),recommended device conformance template combinations
- device conformance templates,recommended combinations
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Recommended Device Conformance Template Combinations

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following table lists recommended combinations of device conformance templates.



| Windows Media Video 9 codec | Windows Media Audio 9 codec | Windows Media Audio 9 Voice codec | Windows Media Audio 9 Professional codec |
|-----------------------------|-----------------------------|-----------------------------------|------------------------------------------|
| SP@LL                       | L2                          | S2                                | \-                                       |
| SP@ML                       | L2                          | S2                                | \-                                       |
| MP@LL                       | L2                          | S2                                | \-                                       |
| MP@ML                       | L3                          | S2                                | M1                                       |
| MP@HL                       | L3                          | S2                                | M2                                       |



 

## Related topics

<dl> <dt>

[**Audio Device Conformance Templates**](audio-device-conformance-templates.md)
</dt> <dt>

[**Device Conformance Template Parameters**](device-conformance-template-parameters.md)
</dt> <dt>

[**Video Device Conformance Templates**](video-device-conformance-templates.md)
</dt> </dl>

 

 





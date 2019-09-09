---
title: Configuring Script Streams
description: Configuring Script Streams
ms.assetid: f8f1656e-69c6-47f7-a8eb-c1039a84ebf3
keywords:
- streams,configuring script streams
- codecs,configuring script streams
- script streams,configuring
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Script Streams

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

 

 





---
description: Writing Capture Filters
ms.assetid: 7dfd1009-da09-49dc-a200-3d7a9f1c70c1
title: Writing Capture Filters
ms.topic: article
ms.date: 05/31/2018
---

# Writing Capture Filters

Writing an audio or video capture filter for DirectShow is not recommended. Instead, DirectShow provides automatic support for audio and video capture devices, using wrapper filters and the [System Device Enumerator](system-device-enumerator.md). For more information about implementing a device driver, refer to the Windows Driver Kit (WDK) documentation.

This section is intended only for developers who need to capture some kind of custom data from an unusual hardware device.

This article contains the following sections:

-   [Pin Requirements for Capture Filters](pin-requirements-for-capture-filters.md)
-   [Implementing a Preview Pin (Optional)](implementing-a-preview-pin--optional.md)
-   [Producing Data in a Capture Filter](producing-data-in-a-capture-filter.md)

## Related topics

<dl> <dt>

[Writing DirectShow Filters](writing-directshow-filters.md)
</dt> </dl>

 

 




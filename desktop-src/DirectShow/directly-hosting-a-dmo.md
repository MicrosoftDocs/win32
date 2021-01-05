---
description: Directly Hosting a DMO
ms.assetid: 10fb99cf-78d9-4519-9aec-23b0daeca9e2
title: Directly Hosting a DMO
ms.topic: article
ms.date: 05/31/2018
---

# Directly Hosting a DMO

This section describes how an application can act as the direct client of a DMO. The application delivers input to the DMO, the DMO creates output, and the application uses the output for rendering, further processing, or anything else. The application is responsible for issues such as memory allocation, timing and synchronization, and threading. These requirements will depend on the nature of the application.

The information in this section also applies if you are writing a component that acts as a layer between an application and a DMO (for example, an ActiveX Control that hosts a DMO). In addition, you should read this section if you are writing a DMO, because it describes the functionality that your DMO must implement.

This section contains the following topics:

-   [Setting Media Types on a DMO](setting-media-types-on-a-dmo.md)
-   [Processing Data in a DMO](processing-data-in-a-dmo.md)
-   [In-Place Processing](in-place-processing.md)
-   [Optional Streams](optional-streams.md)
-   [Implementing IMediaBuffer](implementing-imediabuffer.md)

## Related topics

<dl> <dt>

[Using DMOs](using-dmos.md)
</dt> </dl>

 

 




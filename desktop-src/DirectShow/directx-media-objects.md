---
description: DirectX Media Objects
ms.assetid: e4424740-31b9-4317-8791-6a9aebb0c7e6
title: DirectX Media Objects
ms.topic: article
ms.date: 05/31/2018
---

# DirectX Media Objects

> [!Note]  
> DMOs have been superseded by [Media Foundation Transforms](/windows/desktop/medfound/media-foundation-transforms) (MFTs). The DMO interfaces are still supported. However, if you are writing a custom codec or audio/video processing plug-in, you should consider implementing it as an MFT.

 

DirectX Media Objects (DMOs) are COM-based data-streaming components. In some respects, DMOs are similar to Microsoft DirectShow filters. Like DirectShow filters, DMOs take input data and use it to produce output data. However, the application programming interfaces (APIs) for DMOs are much simpler than the corresponding APIs for DirectShow. As a result, DMOs are easier to create, test, and use. DMOs can be used in many scenarios:

-   Applications based on DirectShow can use DMOs through a DirectShow filter called the [DMO Wrapper](dmo-wrapper-filter.md) filter. The distinction between filters and DMOs is transparent to the application. The application does not directly call the DMO APIs.
-   Applications based on Microsoft DirectSound can use audio effect DMOs. Again, the application is shielded from the low-level DMO APIs by the higher-level DirectSound APIs.
-   Applications can use DMOs directly.

Thus, by writing a DMO, you create a component that can be used in a wide range of applications. This documentation contains the following sections:

-   [About DMOs](about-dmos.md)
-   [Using DMOs](using-dmos.md)
-   [Writing a DMO](writing-a-dmo.md)
-   [Media Parameters](media-parameters.md)
-   [DMO Reference](dmo-reference.md)

## Related topics

<dl> <dt>

[DirectShow](directshow.md)
</dt> </dl>

 

 

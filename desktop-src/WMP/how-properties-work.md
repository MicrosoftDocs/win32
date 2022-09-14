---
title: How Properties Work
description: How Properties Work
ms.assetid: 469af852-593c-4b54-8dc3-b76ad460fa77
keywords:
- Windows Media Player plug-ins,Echo sample properties
- plug-ins,Echo sample properties
- digital signal processing plug-ins,Echo sample properties
- DSP plug-ins,Echo sample properties
- Echo DSP plug-in sample,properties
ms.topic: article
ms.date: 05/31/2018
---

# How Properties Work

Property values are stored in member variables.

Properties are made accessible by method pairs. One method provides the implementation to specify the property value; its name starts with put\_. The other method provides the implementation to retrieve the property value; its name starts with get\_. The interface definition is in Echo.idl. The property method prototypes are in Echo.h. They are implemented in Echo.cpp.

The next three sections will show you how to modify the existing property methods to suit your needs and how to add the methods for an additional property.

-   [Variables to Store Properties](variables-to-store-properties.md)
-   [Modifying the Scale Property](modifying-the-scale-property.md)
-   [Adding the Wet Mix Property](adding-the-wet-mix-property.md)

## Related topics

<dl> <dt>

[**Echo Sample Properties**](echo-sample-properties.md)
</dt> </dl>

 

 





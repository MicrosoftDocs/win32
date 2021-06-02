---
description: This section lists an issue that you might encounter when working with device windows in Direct3D applications.
ms.assetid: 7cfd2ad6-fb85-4303-9fa4-6fe7d16d9951
title: Working with Device Windows (Direct3D 9)
ms.topic: article
ms.date: 05/31/2018
---

# Working with Device Windows (Direct3D 9)

This section lists an issue that you might encounter when working with device windows in Direct3D applications.

-   Direct3D only hooks up the focus windows instead of the device window with the Direct3D message processing function, and only processes the focus window messages. So, the focus window should be the parent of any device window.

## Related topics

<dl> <dt>

[Programming Tips](programming-tips.md)
</dt> </dl>

 

 




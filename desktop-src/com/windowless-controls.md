---
title: Windowless Controls
description: Windowless Controls
ms.assetid: 1759e5db-423c-44cc-b901-f50046c91956
ms.topic: article
ms.date: 05/31/2018
---

# Windowless Controls

The ActiveX Controls 96 specification includes a definition for windowless controls. Such controls do not operate in their own window and require a container to offer a shared window into which the control may draw, see the ActiveX SDK. Windowless controls are designed to be compatible with older control containers by creating their own window in that situation, windowless control containers should host windowed controls in the traditional way with no problem. It may however be useful for a container to distinguish those controls that can operate in a windowless mode, so an appropriate component category is defined.

CATID - {1D06B600-3AE3-11cf-87B9-00AA006C8166} CATID\_WindowlessObject

## Related topics

<dl> <dt>

[Component Categories](component-categories.md)
</dt> </dl>

 

 





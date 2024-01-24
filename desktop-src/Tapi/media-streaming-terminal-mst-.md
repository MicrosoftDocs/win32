---
description: The Media Streaming Terminal (MST) is a dynamic terminal based on use of DirectShow filters. An MSP written using the TAPI 3 MSP Base Classes will incorporate an MST, but MSP authors may choose to implement it without using the base classes.
ms.assetid: 21015c33-2ad1-4472-b346-167953d06a21
title: Media Streaming Terminal (MST)
ms.topic: article
ms.date: 05/31/2018
---

# Media Streaming Terminal (MST)

The Media Streaming Terminal (MST) is a dynamic terminal based on use of DirectShow filters. An MSP written using the [TAPI 3 MSP Base Classes](tapi-3-msp-base-classes.md) will incorporate an MST, but MSP authors may choose to implement it without using the base classes.

To invoke MST creation, an application makes a call to [**ITTerminalSupport::CreateTerminal**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-createterminal) using *pTerminalClass* set to CLSID\_MediaStreamTerminal.

The [**ITAMMediaFormat**](/windows/win32/api/tapi3/nn-tapi3-itammediaformat) and [**ITAllocatorProperties**](/windows/win32/api/tapi3/nn-tapi3-itallocatorproperties) interfaces are then exposed on the terminal, allowing an application to tune streaming performance. These interfaces are declared in Tapi3.h.

Implementation and use of an MST requires familiarity with DirectShow filters and filter graph management. Please refer to the DirectShow material under the Graphic and Multimedia Services node of the Platform Software Development Kit (SDK). The Multimedia Streaming Reference will be particularly useful to MSP authors.

 

 

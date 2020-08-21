---
title: Class Factory Options
description: Class Factory Options
ms.assetid: e9e33e07-7628-4c5e-965d-e12a9c1d69c2
ms.topic: article
ms.date: 05/31/2018
---

# Class Factory Options

An ActiveX Control, by virtue of being a COM object, must have associated server code that supports control creation through [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) as a minimum.

It is optional, not required, that this class object also support [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2) for licensing management. Only those vendors that are concerned about licensing need to support COM's licensing mechanism. In other words, because **IClassFactory2** is the only way to achieve COM-level licensing, this interface is required on the class object for those controls that want to be licensed.

## Related topics

<dl> <dt>

[Controls](controls.md)
</dt> </dl>

 

 
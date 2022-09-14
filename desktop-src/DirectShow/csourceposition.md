---
description: CSourcePosition is an abstract class for implementing the IMediaPosition interface on a source filter.
ms.assetid: 838d2efd-6870-4412-98e2-fb2628e14bf3
title: CSourcePosition class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CSourcePosition
api_type: 
- COM
api_location: 
---

# CSourcePosition class

`CSourcePosition` is an abstract class for implementing the [**IMediaPosition**](/windows/desktop/api/Control/nn-control-imediaposition) interface on a source filter.

This class is obsolete. If your source filter is seekable, it should expose the [**IMediaSeeking**](/windows/desktop/api/Strmif/nn-strmif-imediaseeking) interface instead of **IMediaPosition**. You can use the [**CSourceSeeking**](csourceseeking.md) base class for this purpose.

 

 




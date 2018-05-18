---
Description: 'CSourcePosition is an abstract class for implementing the IMediaPosition interface on a source filter.'
ms.assetid: '838d2efd-6870-4412-98e2-fb2628e14bf3'
title: CSourcePosition class
---

# CSourcePosition class

`CSourcePosition` is an abstract class for implementing the [**IMediaPosition**](imediaposition.md) interface on a source filter.

This class is obsolete. If your source filter is seekable, it should expose the [**IMediaSeeking**](imediaseeking.md) interface instead of **IMediaPosition**. You can use the [**CSourceSeeking**](csourceseeking.md) base class for this purpose.

 

 




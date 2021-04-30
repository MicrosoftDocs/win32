---
description: The CRendererPosPassThru class handles seek commands for renderer filters, by passing them upstream to the next filter.
ms.assetid: 7b532177-939c-4cb7-a6fa-c0133f65c768
title: CRendererPosPassThru class (Ctlutil.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CRendererPosPassThru
api_type: 
- COM
api_location: 
- Strmbase.lib
- Strmbase.dll
- Strmbasd.lib
- Strmbasd.dll
---

# CRendererPosPassThru class

![crendererpospassthru class hierarchy](images/cutil14.png)

The `CRendererPosPassThru` class handles seek commands for renderer filters, by passing them upstream to the next filter.

This class derives from the [**CPosPassThru**](cpospassthru.md) class. It adds support for caching the time stamps from samples as they arrive. Use this class in the same way as the **CPosPassThru** class. Refer to the **CPosPassThru** documentation for details.

The renderer filter must update the `CRendererPosPassThru` object's cached time stamps, as follows:

-   For each sample the filter receives, call the [**CRendererPosPassThru::RegisterMediaTime**](crendererpospassthru-registermediatime.md) method.
-   When the filter is stopped or receives an **EndFlush** call, call the [**CRendererPosPassThru::ResetMediaTime**](crendererpospassthru-resetmediatime.md) method.
-   When the filter receives an end-of-stream notification, call the [**CRendererPosPassThru::EOS**](crendererpospassthru-eos.md) method.

For an example of how to use this class, refer to the [**CBaseRenderer**](cbaserenderer.md) source code.



| Public Methods                                                            | Description                                                         |
|---------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**CRendererPosPassThru**](crendererpospassthru-crendererpospassthru.md) | Constructor method.                                                 |
| [**GetMediaTime**](crendererpospassthru-getmediatime.md)                 | Retrieves the time stamps on the current sample.                    |
| [**RegisterMediaTime**](crendererpospassthru-registermediatime.md)       | Caches the time stamps from the current sample.                     |
| [**ResetMediaTime**](crendererpospassthru-resetmediatime.md)             | Resets the cached time stamps to zero.                              |
| [**EOS**](crendererpospassthru-eos.md)                                   | Updates the cached time stamps after an end-of-stream notification. |



 

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Ctlutil.h (include Streams.h)</dt> </dl>                                                                                   |
| Library<br/> | <dl> <dt>Strmbase.lib (retail builds); </dt> <dt>Strmbasd.lib (debug builds)</dt> </dl> |



 

 





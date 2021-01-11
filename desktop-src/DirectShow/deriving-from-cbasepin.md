---
description: Deriving from CBasePin
ms.assetid: ef453bec-e5a9-4185-94e3-f934e748b11f
title: Deriving from CBasePin
ms.topic: article
ms.date: 05/31/2018
---

# Deriving from CBasePin

To implement a pin using [**CBasePin**](cbasepin.md), you must derive a new class from the base class and override several of its methods. You must override the following methods:

-   [**CBasePin::CheckMediaType**](cbasepin-checkmediatype.md)
-   [**CBasePin::GetMediaType**](cbasepin-getmediatype.md)

You will probably need to override these additional methods:

-   [**CBasePin::Active**](cbasepin-active.md)
-   [**CBasePin::BreakConnect**](cbasepin-breakconnect.md)
-   [**CBasePin::CheckConnect**](cbasepin-checkconnect.md)
-   [**CBasePin::CompleteConnect**](cbasepin-completeconnect.md)
-   [**CBasePin::EndOfStream**](cbasepin-endofstream.md)
-   [**CBasePin::Inactive**](cbasepin-inactive.md)
-   [**CBasePin::Notify**](cbasepin-notify.md)
-   [**CBasePin::Run**](cbasepin-run.md)

Finally, you must must implement the [**IPin::BeginFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-beginflush) and [**IPin::EndFlush**](/windows/desktop/api/Strmif/nf-strmif-ipin-endflush) methods.

Some of these methods are implemented in base classes that derive from **CBasePin**, such as [**CBaseInputPin**](cbaseinputpin.md) and [**CBaseOutputPin**](cbaseoutputpin.md).

## Related topics

<dl> <dt>

[**CBasePin**](cbasepin.md)
</dt> </dl>

 

 




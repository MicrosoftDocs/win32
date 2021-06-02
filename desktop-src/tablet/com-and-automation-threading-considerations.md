---
description: The following Tablet PC threading considerations are specific to when Component Object Model (COM) and Automation are used.
ms.assetid: cf8feba5-a391-4396-a5d8-1ef58df304a7
title: COM and Automation Threading Considerations
ms.topic: article
ms.date: 05/31/2018
---

# COM and Automation Threading Considerations

The following Tablet PC threading considerations are specific to when Component Object Model (COM) and Automation are used.

-   [Thread Safety](#thread-safety)
-   [STA and MTA Applications](#sta-and-mta-applications)
-   [InkCollector and InkOverlay](#inkcollector-and-inkoverlay)
-   [Event Sinks](#event-sinks)
-   [Exceptions within Event Handlers](#exceptions-within-event-handlers)
-   [Related topics](#related-topics)

## Thread Safety

Except for the [InkPicture](inkpicture-control.md) and [InkEdit](inkedit-control.md) controls, Tablet PC objects are thread-safe and are marked as both. By being marked as both, they can run in either a single threaded apartment (STA) or a multithreaded apartment (MTA).

Windows forms use the STA model because windows forms are based on native Win32 windows that are inherently apartment threaded.

## STA and MTA Applications

If your application runs in an MTA or uses the free threaded marshaler (FTM), you must write thread-safe code; however, by doing so you can improve certain event handling performance issues.

## InkCollector and InkOverlay

Your application should not release its final reference to the [**InkCollector**](inkcollector-class.md) or the [**InkOverlay**](inkoverlay-class.md) object, thus destroying the object, directly from the ink thread. Instead, the application should release the **InkCollector** or the **InkOverlay** object from an application thread.

**Caution:** An application that is marked MTA or uses the FTM, which allows direct calls from the ink thread into the application's apartment, can release its final reference to the [**InkCollector**](inkcollector-class.md) or [**InkOverlay**](inkoverlay-class.md) object directly from the ink thread; however, this causes unrecoverable application failure.

## Event Sinks

If your application is not using the FTM and an object and its event sink are created in different apartments, then the event executes on the thread servicing the event sink.

## Exceptions within Event Handlers

Exceptions thrown from within Tablet PC event handlers are consumed and are not visible to the rest or your application. Likewise, HRESULT values are not propagated from Tablet PC event handlers. If an application using the COM layer throws an exception, the background thread terminates, and the exception will be lost. No additional event handlers will be called.

## Related topics

<dl> <dt>

[C++ Event Sinks Sample](c---event-sinks-sample.md)
</dt> <dt>

[General Threading Considerations](general-threading-considerations.md)
</dt> <dt>

[Managed Library Threading Considerations](managed-library-threading-considerations.md)
</dt> </dl>

 

 




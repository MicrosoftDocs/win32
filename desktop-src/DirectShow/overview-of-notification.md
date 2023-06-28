---
description: Overview of Event Notification
ms.assetid: c8b960db-fb8b-4c32-99c3-9d83432574cc
title: Overview of Event Notification
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Overview of Event Notification

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

A filter notifies the Filter Graph Manager about an event by posting an event notification. The event could be something expected, such as the end of a stream, or it could represent an error, such as a failure to render a stream. The Filter Graph Manager handles some filter events by itself, and it leaves others for the application to handle. If the Filter Graph Manager does not handle a filter event, it places the event notification into a queue. The filter graph can also queue its own event notifications for the application.

An application retrieves events from the queue and responds to them based on the type of event. Event notification in DirectShow is therefore similar to the Microsoft Windows message queuing scheme. An application can also cancel the Filter Graph Manager's default behavior for a given event type. The Filter Graph Manager then puts those events directly into the queue for the application to handle.

This mechanism enables

-   The Filter Graph Manager to communicate with the application.
-   Filters to communicate with both the application and the Filter Graph Manager.
-   The application to determine its degree of involvement in handling events.

 

 




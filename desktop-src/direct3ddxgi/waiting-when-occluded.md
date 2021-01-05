---
description: Apps can wait on an event when rendering to the screen is unnecessary (that is, while they are occluded).
ms.assetid: B9EC23C9-A311-4BD9-BBE8-908A1334A541
title: Waiting on an event when rendering is unnecessary
ms.topic: article
ms.date: 05/31/2018
---

# Waiting on an event when rendering is unnecessary

Apps can wait on an event when rendering to the screen is unnecessary (that is, while they are occluded). When the Desktop Window Manager (DWM) or an app is occluded, no rendering is necessary and the operating system can stay in lower power states for longer periods of time. This saves power and extends battery life.

An app can wait on an event when:

-   All the monitors are off.
-   The session that the app runs in is disconnected.
-   The app runs in full screen exclusively on a single monitor configuration.
-   The app runs on a different desktop than the active desktop and does not have permission to render on the active desktop.

The operating system triggers the event when the app is able to render again. The event is not cleared during a driver upgrade, or timeout detection and recovery (TDR) procession, however it is cleared when the new adapter and monitors become active.

If you want your app to be notified about changes of occlusion status, the app must register for these changes. An app can register to be notified about changes of occlusion status through a message to a window or through event signaling. To register to receive notification messages to a window about occlusion status changes, an app calls the [**IDXGIFactory2::RegisterOcclusionStatusWindow**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatuswindow) method. To register to receive notification of occlusion status changes via event signaling, an app calls the [**IDXGIFactory2::RegisterOcclusionStatusEvent**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-registerocclusionstatusevent) method. Both methods return a pointer to a key value that the app can use to unregister the notification. To unregister the notification, the app passes this key value to the [**IDXGIFactory2::UnregisterOcclusionStatus**](/windows/desktop/api/DXGI1_2/nf-dxgi1_2-idxgifactory2-unregisterocclusionstatus) method.

## Related topics

<dl> <dt>

[DXGI 1.2 Improvements](dxgi-1-2-improvements.md)
</dt> </dl>

 

 




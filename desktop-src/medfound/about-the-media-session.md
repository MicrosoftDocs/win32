---
Description: About the Media Session
ms.assetid: 09f50b11-0e0a-42b6-a7bf-bb0135343351
title: About the Media Session
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About the Media Session

The Media Session exposes the [**IMFMediaSession**](/windows/win32/mfidl/nn-mfidl-imfmediasession?branch=master) interface. There are two ways to create the Media Session, depending on whether your application will support protected content:

-   If your application does not support protected content, you can create the Media Session by calling the [**MFCreateMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatemediasession?branch=master). This function creates the Media Session inside the application process.
-   To support protected content, create the Media Session by calling [**MFCreatePMPMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatepmpmediasession?branch=master). This function creates the Media Session inside the Protected Media Path (PMP) process. The application receives a pointer to a proxy object that marshals method calls across the process boundary. Note that the PMP Media Session can be used to play clear content, as well as protected content.

Any application that uses the Media Session will follow these general steps:

1.  Create a topology.
2.  Queue the topology on the Media Session by calling [**IMFMediaSession::SetTopology**](/windows/win32/mfidl/nf-mfidl-imfmediasession-settopology?branch=master).
3.  Control the flow of data by calling [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master), [**IMFMediaSession::Pause**](/windows/win32/mfidl/nf-mfidl-imfmediasession-pause?branch=master), or [**IMFMediaSession::Stop**](/windows/win32/mfidl/nf-mfidl-imfmediasession-stop?branch=master).
4.  Before the application exits, call [**IMFMediaSession::Close**](/windows/win32/mfidl/nf-mfidl-imfmediasession-close?branch=master) to close the Media Session.
5.  Shut down any media sources that the application created, by calling [**IMFMediaSource::Shutdown**](/windows/win32/mfidl/nf-mfidl-imfmediasource-shutdown?branch=master).
6.  Shut down the Media Session by calling [**IMFMediaSession::Shutdown**](/windows/win32/mfidl/nf-mfidl-imfmediasession-shutdown?branch=master).

When using the Media Session, the application should not directly start, pause, or stop the media source. All state changes must be initiated by calling [**IMFMediaSession**](/windows/win32/mfidl/nn-mfidl-imfmediasession?branch=master) methods. State changes in the media source are handled by the Media Session.

Many other details will depend on the specific functionality of your application.

## Protected Content

To play protected content, you must create the Media Session inside the protected media path (PMP), by calling [**MFCreatePMPMediaSession**](/windows/win32/mfidl/nf-mfidl-mfcreatepmpmediasession?branch=master). This function creates an instance of the Media Session inside the PMP and returns a pointer to a proxy object that marshals interfaces across the process boundary.

In most respects, using the Media Session inside the PMP is transparent to the application. However, the application might need to invoke certain actions that enable the user to play the content. For example, the user might need to obtain a DRM license. Media Foundation defines a generic mechanism for these actions using the [**IMFContentEnabler**](/windows/win32/mfidl/nn-mfidl-imfcontentenabler?branch=master) interface.

For more information, see the following topics:

-   [Protected Media Path](protected-media-path.md)
-   [How to Play Protected Media Files](how-to-play-protected-media-files.md)

## Presentation Clock

The Media Session manages all aspects of the presentation clock:

-   Creating the presentation clock.

-   Selecting the time source.

-   Notifying the media sinks about the clock

-   Starting, stopping, and pausing the clock as necessary.

-   Shutting down the clock.

To get a pointer to the presentation clock, call [**IMFMediaSession::GetClock**](/windows/win32/mfidl/nf-mfidl-imfmediasession-getclock?branch=master) on the Media Session. The presentation clock does not return a valid time until the Media Session sends the [MESessionTopologyStatus](mesessiontopologystatus.md) event with the MF\_TOPOSTATUS\_READY flag. Until then, **GetClock** returns MF\_E\_CLOCK\_NO\_TIME\_SOURCE.

An application that uses the Media Session should never start, stop, or pause the presentation clock; change the clock rate; or shut down the clock.

When the application calls [**IMFMediaSession::Start**](/windows/win32/mfidl/nf-mfidl-imfmediasession-start?branch=master), the Media Session starts the presentation clock with a starting time equal to the starting position specified in the **Start** method. For more information about the Media Session, see [Media Session](media-session.md).

## Related topics

<dl> <dt>

[Media Session](media-session.md)
</dt> </dl>

 

 




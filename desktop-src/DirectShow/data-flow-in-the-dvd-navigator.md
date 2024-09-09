---
description: Data Flow in the DVD Navigator
ms.assetid: 14f9cfa3-5ef6-419c-9196-2e4060549c03
title: Data Flow in the DVD Navigator
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Data Flow in the DVD Navigator

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The DVD Navigator has methods to stop and pause playback. These methods are similar — but not identical — to the **Stop** and **Pause** methods in [**IMediaControl**](/windows/desktop/api/Control/nn-control-imediacontrol). Here is the difference between them:

-   The **IDvdControl2** methods change what the DVD Navigator reads from the disk. They do not change the state of the graph.
-   The **IMediaControl** methods change the state of the graph. They do not change what the DVD Navigator reads from the disk. (There is one important exception, explained in the next section, related to the **Stop** method.)

For example, [**IDvdControl2::Pause**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-pause) method issues the Annex J "Pause\_On" command, but does not pause the filter graph. The [**IMediaControl::Pause**](/windows/desktop/api/Control/nf-control-imediacontrol-pause) method, on the other hand, pauses the graph but does not issue any DVD command.

In general, use the **IMediaControl::Pause** and **Stop** methods instead of the corresponding **IDvdControl2** methods. The **IMediaControl** methods have very small latencies, whereas the **IDvdControl2** methods can have up to two seconds of latency.

Stopping Playback

The behavior of [**IMediaControl::Stop**](/windows/desktop/api/Control/nf-control-imediacontrol-stop) depends on a flag that you can set with the [**IDvdControl2::SetOption**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-setoption) method.

-   If the DVD\_ResetOnStop flag is **FALSE**, **IMediaControl::Stop** stops the graph, but does not change the DVD Navigator's domain. When you call run again, playback resumes from the current position.
-   If DVD\_ResetOnStop is **TRUE**, **IMediaControl::Stop** causes the DVD Navigator to reset. When you call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run) again, the DVD Navigator plays from the First Play domain, as if you were inserting the DVD for the first time.

The DVD\_ResetOnStop flag is **TRUE** by default, for compatibility with older applications. Generally, however, you should override the default and set the flag to **FALSE**. The reason is that certain events can cause the graph to stop during playback. For example, if the display resolution changes, the filter graph stops, reconnects the video renderer, and restarts. If DVD\_ResetOnStop is **TRUE**, playback will restart from the beginning of the disc. That is probably not what the user expects.

At the beginning of your application, therefore, call **SetOption** with DVD\_ResetOnStop set to **FALSE**. If you want to stop playback and have it resume from the same location, call **IMediaControl::Stop** or **IMediaControl::Pause**. If you want to stop playback and reset the disk, call **SetOption** with DVD\_ResetOnStop equal to **TRUE**; then call **IMediaControl::Stop**; finally, call **SetOption** again and reset DVD\_ResetOnStop to **FALSE**.

Pausing Playback

If you give the DVD Navigator a command while the graph is paused, the command may not complete until the graph runs again. In some situations, this can cause a deadlock in your application. There are two rules you should follow to avoid deadlocks:

-   While paused, do not issue more than one asynchronous DVD command.
-   While paused, do not block the application's UI thread or the thread that changes the state of the graph.

The second rule is worth examining in more detail. Here are some specific scenarios that may cause a deadlock:

-   **Scenario**: While paused, the application issues a DVD command with the blocking flag. This can cause a deadlock if the thread that issues the DVD command is the same thread that issues the run command. The DVD command blocks until the graph runs, but the graph cannot run until the command completes.

    **Recommendation**: Issue the DVD command on a separate worker thread, or don't use the blocking flag.

-   **Scenario**: While paused, the application issues a DVD command, then calls [**IDvdCmd::WaitForEnd**](/windows/desktop/api/Strmif/nf-strmif-idvdcmd-waitforend) on the command object. This situation is equivalent to the previous example. If you call **Wait** from the UI thread, the UI thread cannot run the graph until the **Wait** method unblocks, but the **Wait** method will not unblock until the graph runs.

    **Recommendation**: Call **Wait** on a worker thread.

-   **Scenario**: While the graph is running, the application issues a DVD command with the blocking flag, and then calls pause from another thread. This is a possible race condition because the graph may pause before the command is issued. If one of the two threads is the UI thread, you may cause a deadlock similar to the previous two examples. This example illustrates the importance of writing thread-safe code if your application uses multiple threads.

    **Recommendation**: If you use worker threads, make sure your code is thread-safe.

-   **Scenario**: While paused, the application disables the run command from the UI, and then issues an asynchronous DVD command. This case is not strictly a deadlock, because the application thread is still running. However, the user is now prevented from running the graph, and therefore the command will never complete.

    **Recommendation**: When pausing, always leave the run command enabled.

Seeking a DVD to a Specified Time

To accurately seek to a specified time on a disc, call [**IMediaControl::Run**](/windows/desktop/api/Control/nf-control-imediacontrol-run). Then call [**IDvdControl2::PlayAtTime**](/windows/desktop/api/Strmif/nf-strmif-idvdcontrol2-playattime), specifying the time and setting *dwFlags* to DVD\_CMD\_FLAG\_Flush.

## Related topics

<dl> <dt>

[DVD Applications](dvd-applications.md)
</dt> </dl>

 

 




---
description: Playback Controls in TopoEdit
ms.assetid: 36ebfa9e-7092-4a93-b633-8eefef8ac9e6
title: Playback Controls in TopoEdit
ms.topic: article
ms.date: 05/31/2018
---

# Playback Controls in TopoEdit

After a topology is resolved, it is queued on the Media Session for playback. TopoEdit provides transport control for changing the state of topology on the Media Session.

The following table shows the menu/toolbar command and the equivalent Media Foundation method for each operation.



| Menu/Toolbar Command                                                                                                                                                                                                                          | Media Foundation Method                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------|
| On the **Controls** menu, click **Play**.\[newline\] -or-\[newline\] click the **play** button on the toolbar (shown in the following image).\[newline\]![screen shot of the play button](images/536e8908-ef44-4d25-98f1-c06b5ef37591.jpg)    | [**IMFMediaSession::Start**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-start) |
| On the **Controls** menu, click **Stop**.\[newline\] -or-\[newline\] click the **stop** button on the toolbar (shown in the following image).\[newline\]![screen shot of the stop button](images/f74657f8-12b3-414a-a1f1-39b7ae2b20f1.jpg)    | [**IMFMediaSession::Stop**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-stop)   |
| On the **Controls** menu, click **Pause**.\[newline\] -or-\[newline\] click the **pause** button on the toolbar (shown in the following image).\[newline\]![screen shot of the pause button](images/156351f1-7215-4062-b4a1-0a0aaa79d205.jpg) | [**IMFMediaSession::Pause**](/windows/desktop/api/mfidl/nf-mfidl-imfmediasession-pause) |



 

For information about controlling the playback programmatically by using Media Foundation APIs, see [How to Control Presentation States](how-to-control-presentation-states.md).

## Seeking

If the topology is seekable, you can seek by using the seek bar (shown in the following image) to specify a place in the topology's timeline to begin playback.

![screen shot of the seek bar](images/95a4e3ef-8489-4e26-9f02-436f81d8a96e.jpg)

> [!Note]  
> If the media source is seekable, the Stop command also seeks the topology back to the start of the stream.

 

## Changing the Playback Rate

If the underlying media source for the topology supports multiple playback rates, you can use the rate bar to change the playback rate. To fast-forward a topology on the Media Session, increase the rate by dragging the slider to the right, as shown in the following image.

![screen shot of the rate bar](images/6e094ecf-c87f-4f27-bca7-a53cc790f5c2.jpg)

> [!Note]  
> In this version, TopoEdit only supports positive rates. Reverse playback is not supported.

 

For information about changing the playback rate programmatically by using Media Foundation APIs, see [About Rate Control](about-rate-control.md).

## Related topics

<dl> <dt>

[TopoEdit Menus](topoedit-menus.md)
</dt> <dt>

[TopoEdit Toolbar](topoedit-toolbar.md)
</dt> <dt>

[TopoEdit](topoedit.md)
</dt> </dl>

 

 




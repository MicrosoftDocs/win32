---
description: Managing Video Editing Projects
ms.assetid: f8d74807-562f-429b-93a1-e65d0f15163b
title: Managing Video Editing Projects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Managing Video Editing Projects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](/windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

The following tips will help you to manage projects in [DirectShow Editing Services](directshow-editing-services.md).

Changes to the Timeline

-   If you change the timeline after you build the filter graph, call [**IRenderEngine::ConnectFrontEnd**](irenderengine-connectfrontend.md) again to rebuild the front end. Usually, this does not affect the rest of the graph. Occasionally, however, the render engine needs to delete the entire graph before it rebuilds the front end. (For example, this happens if you add or remove a group.) The **ConnectFrontEnd** method returns S\_WARN\_OUTPUTRESET to signal that it deleted the graph. If this happens, your application must rebuild the rendering section of the graph.
-   To remove all objects completely from the timeline, call the [**IAMTimeline::ClearAllGroups**](iamtimeline-clearallgroups.md) method.

**Cleanup**

-   When you are finished using a render engine, call the [**IRenderEngine::ScrapIt**](irenderengine-scrapit.md) method. As with any COM object, be sure to release every interface pointer when you are finished using it.
-   The render engine does not keep a reference count on the timeline. Do not release the timeline before you are done using it, and always call **ScrapIt** on the render engine first.
-   If you release all references to a timeline, do not use any of the objects in that timeline, even if you are holding reference counts on them.

**Multiple Timeline Instances**

-   Do not move timeline objects between timelines. Every object in a timeline must be created by that timeline. The timeline holds an internal cache with information about the objects that it creates; moving timeline objects can disrupt the cache.
-   Never use the same instance of a render engine with more than one timeline. The render engine holds a cache with information about the timeline. Multiple timelines will disrupt the cache and cause unpredictable results. If you need two active timelines, make separate instances of render engines for each timeline.
-   A timeline can use more than one render engine, but not at the same time. Delete the old render engine before using another render engine. (You would typically do this when you switch from using the basic render engine for preview to the smart render engine for file writing.)

**Persistence**

-   The filter graph is not persistent when you save the project to an XML file. Therefore, you lose any information relating to smart recompression, compression format, or compression parameters. It is up to the application to restore these parameters after it loads a project.

## Related topics

<dl> <dt>

[Using DirectShow Editing Services](using-directshow-editing-services.md)
</dt> </dl>

 

 




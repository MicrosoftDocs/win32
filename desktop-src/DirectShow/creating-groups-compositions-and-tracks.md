---
description: Creating Groups Compositions and Tracks
ms.assetid: c3bef3cd-5e3c-42c5-850f-b4cb00c414bd
title: Creating Groups Compositions and Tracks
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Creating Groups Compositions and Tracks

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

Groups, compositions, and tracks are the intermediate layers between the timeline and the source clips. They are distinguished by the type of object they can contain.

-   Tracks contain source objects.
-   Compositions contain tracks and other compositions, but not source objects.
-   Groups are top-level compositions. Groups contain compositions and tracks, but compositions cannot contain groups.
-   A *virtual track* is any object that can reside inside a composition or a group. This includes tracks and compositions.

These objects expose the following interfaces:



| Interface                                                  | Exposed By           |
|------------------------------------------------------------|----------------------|
| [**IAMTimelineTrack**](iamtimelinetrack.md)               | Tracks               |
| [**IAMTimelineVirtualTrack**](iamtimelinevirtualtrack.md) | Tracks, Compositions |
| [**IAMTimelineComp**](iamtimelinecomp.md)                 | Compositions, Groups |
| [**IAMTimelineGroup**](iamtimelinegroup.md)               | Groups               |



 

These interfaces contain the methods for adding objects to the timeline.

-   [**IAMTimeline::AddGroup**](iamtimeline-addgroup.md): Inserts a group into the timeline.
-   [**IAMTimelineComp::VTrackInsBefore**](iamtimelinecomp-vtrackinsbefore.md): Inserts a virtual track into a composition or group.
-   [**IAMTimelineTrack::SrcAdd**](iamtimelinetrack-srcadd.md): Inserts a source into a track.

For example, the following code inserts a new track into a group. As shown in the previous table, a group is considered a kind of composition, and a track is a kind of virtual track. Therefore, to insert the track into the group, you must query the group for its **IAMTimelineComp** interface and call the **IAMTimelineComp::VTrackInsBefore** method.


```C++
IAMTimelineGroup    *pGroup;
// Create a new group (not shown). 

IAMTimelineComp     *pComp = NULL;
IAMTimelineObj      *pTrackObj = NULL;

pTL->CreateEmptyNode(&pTrackObj, TIMELINE_MAJOR_TYPE_TRACK);
pGroup->QueryInterface(IID_IAMTimelineComp, (void **)&pComp);
pComp->VTrackInsBefore(pTrackObj, 0);
```



The second parameter to **VTrackInsBefore** specifies the priority of the virtual track. Priority levels start at zero. If you specify the value –1, the virtual track is inserted at the end of the priority list. If you specify a value where there is already a virtual track, everything from that point on moves down the list by one priority level. Do not insert a virtual track at a priority greater than the number of virtual tracks, because it will cause undefined behavior.

To delete an object permanently from the timeline, call [**IAMTimelineObj::RemoveAll**](iamtimelineobj-removeall.md) on the object. This method removes the object and all its children. To remove an object for the purpose of reinserting it elsewhere in the timeline, call [**IAMTimelineObj::Remove**](iamtimelineobj-remove.md) instead. Unlike **RemoveAll**, this method does not delete the object's children. To remove everything from the timeline, call [**IAMTimeline::ClearAllGroups**](iamtimeline-clearallgroups.md).

## Related topics

<dl> <dt>

[Constructing a Timeline](constructing-a-timeline.md)
</dt> </dl>

 

 




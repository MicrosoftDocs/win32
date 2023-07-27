---
description: Adding Effect and Transition Objects
ms.assetid: fe82392f-33e2-432a-a6e3-710e475547b3
title: Adding Effect and Transition Objects
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Adding Effect and Transition Objects

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

\[This API is not supported and may be altered or unavailable in the future.\]

In DES, an effect or transition is represented with two objects:

-   A *timeline object* represents the effect or transition within the timeline. For effects, the timeline object supports the [**IAMTimelineEffect**](iamtimelineeffect.md) interface. For transitions, it supports the [**IAMTimelineTrans**](iamtimelinetrans.md) interface. Both types support the [**IAMTimelineObj**](iamtimelineobj.md) interface.
-   The *subobject* is an object that implements the data processing for the effect or transition. The timeline object holds a pointer to the subobject.

To add an effect or transition, perform the following steps.

**1. Create the Timeline Object**

To create the timeline object, call the [**IAMTimeline::CreateEmptyNode**](iamtimeline-createemptynode.md) method. Set the type equal to **TIMELINE\_MAJOR\_TYPE\_EFFECT** for an effect, or **TIMELINE\_MAJOR\_TYPE\_TRANSITION** for a transition.

The following example creates a transition object:


```C++
IAMTimelineObj *pTransObj = NULL;
pTimeline->CreateEmptyNode(&pTransObj, TIMELINE_MAJOR_TYPE_TRANSITION);
```



**2. Specify the Subobject**

The timeline object acts as a wrapper for another object, called the *subobject*, which does the real work. The subobject implements a data transform that produces the desired effect or transition. For a list of transitions and effects supplied with DES, see [Transitions and Effects](transitions-and-effects.md).

To set the subobject, call the [**IAMTimelineObj::SetSubObjectGUID**](iamtimelineobj-setsubobjectguid.md) method on the timeline object, passing it the class identifier (CLSID) of the subobject. DirectShow provides an enumerator for video effects and video transitions, which you can use to obtain the CLSID. For more information, see [Enumerating Effects and Transitions](enumerating-effects-and-transitions.md).

The following example sets the [SMPTE Wipe Transition](smpte-wipe-transition.md) as the subobject :


```C++
hr = pTransObj->SetSubObjectGUID(CLSID_DxtJpeg);  // SMPTE Wipe
```



**3. Set the Start and Stop Times**

To set the start and stop times, call the [**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md) method. These times are relative to the start time of the parent object. Effects can overlap within the same object, but transitions cannot.

The following example sets the start time to 5 seconds and the stop time to 10 seconds:


```C++
const REFERENCE_TIME ONE_SECOND = 10000000
hr = pTransObj->SetStartStop(5 * ONE_SECOND, 10 * ONE_SECOND);
```



When a transition is rendered, the progress of the transition at each frame is calculated based on a **Progress** property, which is normalized to a range of 0.0 to 1.0. DES uses the start time of each frame to calculate the progress value. This means if the transition stop time is equal to the source stop time, the **Progress** value will never reach exactly 1.0, because the start time of the last frame is slightly than the stop time. To make the transition reach 1.0, set the transition stop time to be at least one frame earlier than the source stop time.

**4. Insert the Object into the Timeline**

To insert the object into the timeline, call one of the following methods on the parent, depending on the object type:

-   Effects: [**IAMTimelineEffectable::EffectInsBefore**](iamtimelineeffectable-effectinsbefore.md)
-   Transitions: [**IAMTimelineTransable::TransAdd**](iamtimelinetransable-transadd.md)

In the [**IAMTimelineEffectable::EffectInsBefore**](iamtimelineeffectable-effectinsbefore.md) method, you must specify the priority of the effect. When effects overlap on the same object, they are applied in order of priority. The Volume Envelope audio effect is an exception; see the [Volume Envelope Effect](volume-envelope-effect.md) reference for details. Within a composition, all audio tracks are mixed before the audio effects for that composition are applied.

Because transitions cannot overlap on the same object, they do not have a priority value.

The following example adds the transition object to a track:


```C++
IAMTimelineTransable *pTransable = NULL;
hr = pTrack->QueryInterface(IID_IAMTimelineTransable, (void **)&pTransable);
hr = pTransable->TransAdd(pTransObj);  
pTransable->Release();
```



The example queries the track object for the [**IAMTimelineTransable**](iamtimelinetransable.md) interface before calling AddTrans.

**5. Set Properties**

Many effects and transitions support custom properties. For information, see [Setting Properties on Effects and Transitions](setting-properties-on-effects-and-transitions.md).

Example

The following code example adds a [SMPTE Wipe Transition](smpte-wipe-transition.md) to a track. It assumes that the track object already exists in the timeline.


```C++
IAMTimeline *pTL;
IAMTimelineTrack *pTrack;

// Create timeline with track (not shown).

// Create the transition object. 
IAMTimelineObj *pTransObj = NULL;
hr = pTL->CreateEmptyNode(&pTransObj, TIMELINE_MAJOR_TYPE_TRANSITION);

// Set the subobject. 
hr = pTransObj->SetSubObjectGUID(CLSID_DxtJpeg);  // SMPTE Wipe

// Set the start and stop times. 
hr = pTransObj->SetStartStop(50000000, 100000000);

// Insert the transition object into the timeline. 
IAMTimelineTransable *pTransable = NULL;
hr = pTrack->QueryInterface(IID_IAMTimelineTransable, (void **)&pTransable);
hr = pTransable->TransAdd(pTransObj);  
pTransable->Release();
pTransObj->Release();
```



## Related topics

<dl> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 




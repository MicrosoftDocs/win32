---
description: This interface is used to control animation functionality, connecting animation sets with the transformation frames that are being animated.
ms.assetid: a485e4d2-82e1-45db-8496-dd743904c34d
title: ID3DXAnimationController interface (D3dx9anim.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXAnimationController
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXAnimationController interface

This interface is used to control animation functionality, connecting animation sets with the transformation frames that are being animated. The interface has methods to mix multiple animations and to modify blending parameters over time to enable smooth transitions and other effects.

## Members

The **ID3DXAnimationController** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXAnimationController** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXAnimationController** interface has these methods.



| Method                                                                                   | Description                                                                                                                                             |
|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvanceTime**](id3dxanimationcontroller--advancetime.md)                             | Animates the mesh and advances the global animation time by a specified amount.<br/>                                                              |
| [**CloneAnimationController**](id3dxanimationcontroller--cloneanimationcontroller.md)   | Clones, or copies, an animation controller.<br/>                                                                                                  |
| [**GetAnimationSet**](id3dxanimationcontroller--getanimationset.md)                     | Gets an animation set.<br/>                                                                                                                       |
| [**GetAnimationSetByName**](id3dxanimationcontroller--getanimationsetbyname.md)         | Gets an animation set, given its name.<br/>                                                                                                       |
| [**GetCurrentPriorityBlend**](id3dxanimationcontroller--getcurrentpriorityblend.md)     | Returns an event handle to a priority blend event that is currently running.<br/>                                                                 |
| [**GetCurrentTrackEvent**](id3dxanimationcontroller--getcurrenttrackevent.md)           | Returns an event handle to the event currently running on the specified animation track.<br/>                                                     |
| [**GetEventDesc**](id3dxanimationcontroller--geteventdesc.md)                           | Gets a description of a specified animation event.<br/>                                                                                           |
| [**GetMaxNumAnimationOutputs**](id3dxanimationcontroller--getmaxnumanimationoutputs.md) | Get the maximum number of animation outputs the animation controller can support.<br/>                                                            |
| [**GetMaxNumAnimationSets**](id3dxanimationcontroller--getmaxnumanimationsets.md)       | Gets the maximum number of animation sets the animation controller can support.<br/>                                                              |
| [**GetMaxNumEvents**](id3dxanimationcontroller--getmaxnumevents.md)                     | Gets the maximum number of events the animation controller can support.<br/>                                                                      |
| [**GetMaxNumTracks**](id3dxanimationcontroller--getmaxnumtracks.md)                     | Gets the maximum number of tracks in the animation controller.<br/>                                                                               |
| [**GetNumAnimationSets**](id3dxanimationcontroller--getnumanimationsets.md)             | Returns the number of animation sets currently registered in the animation controller.<br/>                                                       |
| [**GetPriorityBlend**](id3dxanimationcontroller--getpriorityblend.md)                   | Gets the current priority blending weight used by the animation controller.<br/>                                                                  |
| [**GetTime**](id3dxanimationcontroller--gettime.md)                                     | Gets the global animation time.<br/>                                                                                                              |
| [**GetTrackAnimationSet**](id3dxanimationcontroller--gettrackanimationset.md)           | Gets the animation set for the given track.<br/>                                                                                                  |
| [**GetTrackDesc**](id3dxanimationcontroller--gettrackdesc.md)                           | Gets the track description.<br/>                                                                                                                  |
| [**GetUpcomingPriorityBlend**](id3dxanimationcontroller--getupcomingpriorityblend.md)   | Returns an event handle to the next priority blend event scheduled to occur after a specified event.<br/>                                         |
| [**GetUpcomingTrackEvent**](id3dxanimationcontroller--getupcomingtrackevent.md)         | Returns an event handle to the next event scheduled to occur after a specified event on an animation track.<br/>                                  |
| [**KeyPriorityBlend**](id3dxanimationcontroller--keypriorityblend.md)                   | Sets blending event keys for the specified animation track.<br/>                                                                                  |
| [**KeyTrackEnable**](id3dxanimationcontroller--keytrackenable.md)                       | Sets an event key that enables or disables an animation track.<br/>                                                                               |
| [**KeyTrackPosition**](id3dxanimationcontroller--keytrackposition.md)                   | Sets an event key that changes the local time of an animation track.<br/>                                                                         |
| [**KeyTrackSpeed**](id3dxanimationcontroller--keytrackspeed.md)                         | Sets an event key that changes the rate of play of an animation track.<br/>                                                                       |
| [**KeyTrackWeight**](id3dxanimationcontroller--keytrackweight.md)                       | Sets an event key that changes the weight of an animation track. The weight is used as a multiplier when combining multiple tracks together.<br/> |
| [**RegisterAnimationOutput**](id3dxanimationcontroller--registeranimationoutput.md)     | Adds an animation output to the animation controller and registers pointers for scale, rotate, and translate (SRT) transformations.<br/>          |
| [**RegisterAnimationSet**](id3dxanimationcontroller--registeranimationset.md)           | Adds an animation set to the animation controller.<br/>                                                                                           |
| [**ResetTime**](id3dxanimationcontroller--resettime.md)                                 | Resets the global animation time to zero. Any pending events will retain their original schedules, but in the new timeframe.<br/>                 |
| [**SetPriorityBlend**](id3dxanimationcontroller--setpriorityblend.md)                   | Sets the priority blending weight used by the animation controller.<br/>                                                                          |
| [**SetTrackAnimationSet**](id3dxanimationcontroller--settrackanimationset.md)           | Applies the animation set to the specified track.<br/>                                                                                            |
| [**SetTrackDesc**](id3dxanimationcontroller--settrackdesc.md)                           | Sets the track description.<br/>                                                                                                                  |
| [**SetTrackEnable**](id3dxanimationcontroller--settrackenable.md)                       | Enables or disables a track in the animation controller.<br/>                                                                                     |
| [**SetTrackPosition**](id3dxanimationcontroller--settrackposition.md)                   | Sets the track to the specified local animation time.<br/>                                                                                        |
| [**SetTrackPriority**](id3dxanimationcontroller--settrackpriority.md)                   | Sets the priority blending weight for the specified animation track.<br/>                                                                         |
| [**SetTrackSpeed**](id3dxanimationcontroller--settrackspeed.md)                         | Sets the track speed. The track speed is similar to a multiplier that is used to speed up or slow down the playback of the track.<br/>            |
| [**SetTrackWeight**](id3dxanimationcontroller--settrackweight.md)                       | Sets the track weight. The weight is used to determine how to blend multiple tracks together.<br/>                                                |
| [**UnkeyAllPriorityBlends**](id3dxanimationcontroller--unkeyallpriorityblends.md)       | Removes all scheduled priority blend events from the animation controller.<br/>                                                                   |
| [**UnkeyAllTrackEvents**](id3dxanimationcontroller--unkeyalltrackevents.md)             | Removes all events from a specified animation track.<br/>                                                                                         |
| [**UnkeyEvent**](id3dxanimationcontroller--unkeyevent.md)                               | Removes a specified event from an animation track, preventing the execution of the event.<br/>                                                    |
| [**UnregisterAnimationSet**](id3dxanimationcontroller--unregisteranimationset.md)       | Removes an animation set from the animation controller.<br/>                                                                                      |
| [**ValidateEvent**](id3dxanimationcontroller--validateevent.md)                         | Checks whether a specified event handle is valid and the animation event has not yet completed.<br/>                                              |



 

## Remarks

Create an animation controller object with [**D3DXCreateAnimationController**](d3dxcreateanimationcontroller.md).

The LPD3DXANIMATIONCONTROLLER type is defined as a pointer to the **ID3DXAnimationController** interface.


```
typedef interface ID3DXAnimationController ID3DXAnimationController;
typedef interface ID3DXAnimationController *LPD3DXANIMATIONCONTROLLER;
```



The D3DXEVENTHANDLE type is defined as an event handle to animation controller events.


```
typedef DWORD D3DXEVENTHANDLE;
```



The LPD3DXEVENTHANDLE type is defined as a pointer to an event handle to animation controller events.


```
typedef D3DXEVENTHANDLE *LPD3DXEVENTHANDLE;
```



## Requirements



| Requirement | Value |
|--------------------|----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3dx9anim.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>   |



## See also

<dl> <dt>

[D3DX Interfaces](dx9-graphics-reference-d3dx-interfaces.md)
</dt> </dl>

 

 

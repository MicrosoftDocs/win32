---
description: The IAMTimeline interface provides methods for manipulating the timeline, the central object in Microsoft DirectShow Editing Services (DES).
ms.assetid: 6750efa0-946c-4ad3-b0df-de55872b94c3
title: IAMTimeline interface (Qedit.h)
ms.topic: reference
ms.date: 4/26/2023
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IAMTimeline
api_type: 
- COM
api_location: 
- strmiids.lib
- strmiids.dll
ms.custom: UpdateFrequency5
---

# IAMTimeline interface

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `IAMTimeline` interface provides methods for manipulating the timeline, the central object in Microsoft [DirectShow Editing Services](directshow-editing-services.md) (DES). A timeline is a collection of time-ordered elements, such as video clips, audio clips, effects, and transitions between clips. The render engine uses the timeline to create a filter graph, from which the application can generate the rendered output.

`IAMTimeline` performs three basic services. It

-   Creates the objects in the timeline.
-   Acts as a container for those objects.
-   Sets and retrieves general parameters of the timeline.

To create the timeline object, call **CoCreateInstance** with the class identifier CLSID\_AMTimeline.

## Members

The **IAMTimeline** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IAMTimeline** also has these types of members:

-   [Methods](#methods)

### Methods

The **IAMTimeline** interface has these methods.



| Method                                                             | Description                                                                                                                       |
|:-------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| [**AddGroup**](iamtimeline-addgroup.md)                           | Adds a group to the timeline.<br/>                                                                                          |
| [**ClearAllGroups**](iamtimeline-clearallgroups.md)               | Removes all groups from the timeline, along with all objects contained in those groups.<br/>                                |
| [**CreateEmptyNode**](iamtimeline-createemptynode.md)             | Creates a new timeline object.<br/>                                                                                         |
| [**EffectsEnabled**](iamtimeline-effectsenabled.md)               | Determines whether effects are enabled.<br/>                                                                                |
| [**EnableEffects**](iamtimeline-enableeffects.md)                 | Enables or disables all effects in the timeline.<br/>                                                                       |
| [**EnableTransitions**](iamtimeline-enabletransitions.md)         | Enables or disables all transitions in the timeline.<br/>                                                                   |
| [**GetCountOfType**](iamtimeline-getcountoftype.md)               | Retrieves the number of objects of the specified type that are contained in a specified group and all of its children.<br/> |
| [**GetDefaultEffect**](iamtimeline-getdefaulteffect.md)           | Retrieves the default effect.<br/>                                                                                          |
| [**GetDefaultEffectB**](iamtimeline-getdefaulteffectb.md)         | Retrieves the default effect as a **BSTR** value.<br/>                                                                      |
| [**GetDefaultFPS**](iamtimeline-getdefaultfps.md)                 | Retrieves the default output frame rate, in frames per second.<br/>                                                         |
| [**GetDefaultTransition**](iamtimeline-getdefaulttransition.md)   | Retrieves the default transition.<br/>                                                                                      |
| [**GetDefaultTransitionB**](iamtimeline-getdefaulttransitionb.md) | Retrieves the default transition as a **BSTR** value.<br/>                                                                  |
| [**GetDirtyRange**](iamtimeline-getdirtyrange.md)                 | Not supported.<br/>                                                                                                         |
| [**GetDuration**](iamtimeline-getduration.md)                     | Retrieves the timeline duration.<br/>                                                                                       |
| [**GetDuration2**](iamtimeline-getduration2.md)                   | Retrieves the timeline duration as a **double**.<br/>                                                                       |
| [**GetGroup**](iamtimeline-getgroup.md)                           | Retrieves a specified group.<br/>                                                                                           |
| [**GetGroupCount**](iamtimeline-getgroupcount.md)                 | Retrieves the number of groups that are contained in the timeline.<br/>                                                     |
| [**GetInsertMode**](iamtimeline-getinsertmode.md)                 | Not supported.<br/>                                                                                                         |
| [**IsDirty**](iamtimeline-isdirty.md)                             | Not supported.<br/>                                                                                                         |
| [**RemGroupFromList**](iamtimeline-remgroupfromlist.md)           | Not supported.<br/>                                                                                                         |
| [**SetDefaultEffect**](iamtimeline-setdefaulteffect.md)           | Sets the default effect.<br/>                                                                                               |
| [**SetDefaultEffectB**](iamtimeline-setdefaulteffectb.md)         | Sets the default effect as a **BSTR** value.<br/>                                                                           |
| [**SetDefaultFPS**](iamtimeline-setdefaultfps.md)                 | Sets the default output frame rate, in frames per second.<br/>                                                              |
| [**SetDefaultTransition**](iamtimeline-setdefaulttransition.md)   | Sets the default transition.<br/>                                                                                           |
| [**SetDefaultTransitionB**](iamtimeline-setdefaulttransitionb.md) | Sets the default transition as a BSTR value.<br/>                                                                           |
| [**SetInsertMode**](iamtimeline-setinsertmode.md)                 | Not implemented.<br/>                                                                                                       |
| [**SetInterestRange**](iamtimeline-setinterestrange.md)           | Not implemented.<br/>                                                                                                       |
| [**TransitionsEnabled**](iamtimeline-transitionsenabled.md)       | Determines whether transitions are enabled.<br/>                                                                            |
| [**ValidateSourceNames**](iamtimeline-validatesourcenames.md)     | Validates source names in the timeline.<br/>                                                                                |



 

## Remarks

> [!Note]  
> The header file Qedit.h is not compatible with Direct3D headers later than version 7.

 

> [!Note]  
> To obtain Qedit.h, download the [Microsoft Windows SDK Update for Windows Vista and .NET Framework 3.0](https://msdn.microsoft.com/windowsvista/bb980924.aspx). Qedit.h is not available in the Microsoft Windows SDK for Windows 7 and .NET Framework 3.5 Service Pack 1.

 

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Qedit.h</dt> </dl>      |
| Library<br/> | <dl> <dt>Strmiids.lib</dt> </dl> |



 

 

---
title: Constants (Windows Animation Reference)
description: Reference documentation for constants and enumerations defined by the Windows Animation Manager.
ms.assetid: c590cf68-28ce-4d7d-949d-2683ece3c12d
ms.topic: article
ms.date: 05/31/2018
---

# Constants (Windows Animation Reference)

Reference documentation for constants and enumerations defined by the Windows Animation Manager.

## In this section



| Topic                                                                                                                             | Description                                                                                                                                                                                                                                                                |
|-----------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UI\_ANIMATION\_DIMENSION\_UNKNOWN**](ui-animation-dimension-unknown.md)<br/>                                            | Indicates that the requested dimension cannot be retrieved.<br/>                                                                                                                                                                                                     |
| [**UI\_ANIMATION\_ITERATION\_NONE**](-ui-animation-iteration-none.md)<br/>                                                 | Indicates that this is the initial entry into a given loop.<br/>                                                                                                                                                                                                     |
| [**UI\_ANIMATION\_KEYFRAME\_STORYBOARD\_START**](/previous-versions/windows/desktop/legacy/dd756780(v=vs.85))<br/>                           | Represents the implicit keyframe at the start of every storyboard.<br/>                                                                                                                                                                                              |
| [**UI\_ANIMATION\_REPEAT\_INDEFINITELY**](ui-animation-repeat-indefinitely.md)<br/>                                        | Indicates that the interval between two keyframes in a storyboard should repeat indefinitely until the [**IUIAnimationStoryboard::Conclude**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-conclude) method is called.<br/>                                                            |
| [**UI\_ANIMATION\_REPEAT\_INDEFINITELY\_CONCLUDE\_AT\_END**](ui-animation-repeat-indefinitely-conclude-at-end.md)<br/>     | Indicates that the interval between two keyframes in a storyboard should repeat indefinitely until the keyframe loop terminates on the ending keyframe when the [**IUIAnimationStoryboard::Conclude**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-conclude) method is called.<br/>   |
| [**UI\_ANIMATION\_REPEAT\_INDEFINITELY\_CONCLUDE\_AT\_START**](ui-animation-repeat-indefinitely-conclude-at-start.md)<br/> | Indicates that the interval between two keyframes in a storyboard should repeat indefinitely until the keyframe loop terminates on the starting keyframe when the [**IUIAnimationStoryboard::Conclude**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-conclude) method is called.<br/> |
| [**UI\_ANIMATION\_SECONDS\_EVENTUALLY**](ui-animation-seconds-eventually.md)<br/>                                          | Indicates that Windows Animation can delay the scheduled start of a storyboard for as much time as necessary to avoid scheduling conflicts.<br/>                                                                                                                     |
| [**UI\_ANIMATION\_SECONDS\_INFINITE**](ui-animation-seconds-infinite.md)<br/>                                              | Indicates that there are no scheduled events.<br/>                                                                                                                                                                                                                   |



 

## Related topics

<dl> <dt>

[Windows Animation Reference](windows-animation-reference.md)
</dt> </dl>

 


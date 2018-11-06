---
title: Schedule a Storyboard
description: After a storyboard is created, it is scheduled by the animation manager.
ms.assetid: f3c8fe34-8bca-4421-a390-9e0ba9af27b4
keywords:
- storyboards Windows Animation ,scheduling
ms.topic: article
ms.date: 05/31/2018
---

# Schedule a Storyboard

After a storyboard is created, it is scheduled by the animation manager.

## Overview

By default, each storyboard starts immediately when it is scheduled. This means that when a storyboard starts to animate one or more variables, it may interrupt any other storyboards animating those same variables. However, an application may specify other behaviors by determining the relative priority between storyboards.

After a storyboard has been scheduled, it can no longer be altered. However, after a storyboard has been removed from the schedule, it can be scheduled for play again. Developers should exercise caution when re-using storyboards, as this should only be done where there is no chance that the same storyboard might need to be queued due to a user action when it is already playing or queued in the schedule.

## Example Code

The following example code is taken from MainWindow.cpp in the Windows Animation samples [Application-Driven Animation](application-driven-animation-sample.md) and [Timer-Driven Animation](timer-driven-animation-sample.md). It uses the [**IUIAnimationStoryboard::Schedule**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-schedule) method to schedule the storyboard. This method requires the current time as a parameter.


```
// Get the current time and schedule the storyboard for play

UI_ANIMATION_SECONDS secondsNow;
hr = m_pAnimationTimer->GetTime(
    &secondsNow
    );
if (SUCCEEDED(hr))
{
    hr = pStoryboard->Schedule(
        secondsNow
    );
}
```



## Previous Step

Before starting this step, you should have completed this step: [Create a Storyboard and Add Transitions](updating---timer-driven-animation.md).

## Related topics

<dl> <dt>

[**IUIAnimationStoryboard::Schedule**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-schedule)
</dt> <dt>

[**IUIAnimationTimer::GetTime**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtimer-gettime)
</dt> <dt>

[Storyboard Overview](storyboard-construction.md)
</dt> </dl>

 

 





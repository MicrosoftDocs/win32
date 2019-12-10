---
title: Windows Animation Glossary
description: This glossary contains terms and acronyms of interest to developers using the Windows Animation Manager.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 66e9cfb4-b9ae-4c21-9b1f-532c7d750903
keywords:
- Windows Animation Windows Animation ,glossary
ms.topic: article
ms.date: 05/31/2018
---

# Windows Animation Glossary

This glossary contains terms and acronyms of interest to developers using the Windows Animation Manager.

<dl> <dt>

<span id="uianimation.term.animation"></span><span id="UIANIMATION.TERM.ANIMATION"></span> **animation** 
</dt> <dd>

A sequence of synthetic, successive still images that produces an illusion of movement when played back.

</dd> <dt>

<span id="uianimation.term.animation_manager"></span><span id="UIANIMATION.TERM.ANIMATION_MANAGER"></span> **animation manager** 
</dt> <dd>

A core component of Windows Animation and the central programmatic interface for managing (creating, scheduling, and controlling) animations.

</dd> <dt>

<span id="uianimation.term.animation_timer"></span><span id="UIANIMATION.TERM.ANIMATION_TIMER"></span>**animation timer**
</dt> <dd>

A component to provide timing services that can be used in conjunction with the animation manager. It dynamically throttles the frame rate based on application and system load or in low-power mode. See also: throttling.

</dd> <dt>

<span id="uianimation.term.animation_variable"></span><span id="UIANIMATION.TERM.ANIMATION_VARIABLE"></span> **animation variable** 
</dt> <dd>

A value that can be animated. Animation variables may be used to represent the position, size, rotation, transparency and other qualities of visible objects.

</dd> <dt>

<span id="uianimation.term.cancellation"></span><span id="UIANIMATION.TERM.CANCELLATION"></span>**cancellation**
</dt> <dd>

The process of removing a storyboard from the schedule before it has started playing.

</dd> <dt>

<span id="uianimation.term.compression"></span><span id="UIANIMATION.TERM.COMPRESSION"></span>**compression**
</dt> <dd>

A warping of a storyboard's perception of time. The system increases the rate at which the storyboard progresses by passing input time values that increase faster than the system clock.

</dd> <dt>

<span id="uianimation.term.conclusion"></span><span id="UIANIMATION.TERM.CONCLUSION"></span>**conclusion**
</dt> <dd>

The process of directing a storyboard to exit any indefinite loops. If the loop has begun, the current iteration will complete and the remainder of the storyboard will then play. Otherwise, the looped portion of the storyboard will be skipped entirely.

</dd> <dt>

<span id="uianimation.term.frame"></span><span id="UIANIMATION.TERM.FRAME"></span> **frame** 
</dt> <dd>

A single image in a movie or an animation.

</dd> <dt>

<span id="uianimation.term.frame_rate"></span><span id="UIANIMATION.TERM.FRAME_RATE"></span> **frame rate** 
</dt> <dd>

The number of frames displayed per second. Higher frame rates generally produce smoother movement in the picture.

</dd> <dt>

<span id="uianimation.term.interpolator"></span><span id="UIANIMATION.TERM.INTERPOLATOR"></span>**interpolator**
</dt> <dd>

The programming object that does the mathematical interpolation of the value and velocity of a variable for a transition.

</dd> <dt>

<span id="uianimation.term.keyframe"></span><span id="UIANIMATION.TERM.KEYFRAME"></span>**keyframe**
</dt> <dd>

A moment in time within a storyboard, which can be specified relative to the start of the storyboard, relative to another keyframe, or at the end time of a transition, and used to specify the start and end time of other transitions or a cycle within the storyboard.

</dd> <dt>

<span id="uianimation.term.loop"></span><span id="UIANIMATION.TERM.LOOP"></span>**loop**
</dt> <dd>

A section of a storyboard between two keyframes that is played repeatedly. A loop may play a finite number of times or indefinitely.

</dd> <dt>

<span id="uianimation.term.priority_comparison"></span><span id="UIANIMATION.TERM.PRIORITY_COMPARISON"></span> **priority comparison** 
</dt> <dd>

Client-defined code that compares two storyboards, one already scheduled and the other about to be scheduled, to determine their relative priority. A scheduled storyboard may be trimmed, compressed, canceled, or concluded to enable scheduling of the storyboard with higher priority.

</dd> <dt>

<span id="uianimation.term.storyboard"></span><span id="UIANIMATION.TERM.STORYBOARD"></span> **storyboard** 
</dt> <dd>

A group of animation transitions synchronized relative to one another.

</dd> <dt>

<span id="uianimation.term.tag"></span><span id="UIANIMATION.TERM.TAG"></span> **tag** 
</dt> <dd>

A pair consisting of an integer ID and a COM object used by an application to identify animation variables and storyboards within the scope of a specific animation manager.

</dd> <dt>

<span id="uianimation.term.throttling"></span><span id="UIANIMATION.TERM.THROTTLING"></span> **throttling** 
</dt> <dd>

Dynamically adjusting the frame rate of an animation to meet certain requirements. Throttling helps to ensure that animations are rendered at a consistent frame rate while minimizing the use of system resources for rendering at a rate that is beyond what is needed or useful.

</dd> <dt>

<span id="uianimation.term.tick"></span><span id="UIANIMATION.TERM.TICK"></span> **tick** 
</dt> <dd>

A timer event that typically triggers the rendering of a single frame.

</dd> <dt>

<span id="uianimation.term.transition"></span><span id="UIANIMATION.TERM.TRANSITION"></span> **transition** 
</dt> <dd>

A construct that defines progressive updates for an animation variable over a period of time.

</dd> <dt>

<span id="uianimation.term.trimming"></span><span id="UIANIMATION.TERM.TRIMMING"></span>**trimming**
</dt> <dd>

Preempting a storyboard's control of an animation variable with a higher-priority storyboard. If trimming a storyboard on one or more variables causes the storyboard to end prematurely, it is considered truncated. See also: truncation.

</dd> <dt>

<span id="uianimation.term.truncation"></span><span id="UIANIMATION.TERM.TRUNCATION"></span>**truncation**
</dt> <dd>

Ending a storyboard prematurely by preempting control of one or more of the variables that it animates with one or more higher-priority storyboards. See also: trimming.

</dd> </dl>

 

 





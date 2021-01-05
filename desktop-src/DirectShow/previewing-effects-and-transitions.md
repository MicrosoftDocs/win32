---
description: Previewing Effects and Transitions
ms.assetid: aa13bd57-69c1-462c-86e3-64026a03bfc4
title: Previewing Effects and Transitions
ms.topic: article
ms.date: 05/31/2018
---

# Previewing Effects and Transitions

\[This API is not supported and may be altered or unavailable in the future.\]

Some effects and transitions take a relatively long time to render. During preview this can cause the video to become choppy or out of sync with the audio. You can increase preview speed by disabling effects or transitions:

-   To disable all effects, call [**IAMTimeline::EnableEffects**](iamtimeline-enableeffects.md).
-   To disable all transitions, call [**IAMTimeline::EnableTransitions**](iamtimeline-enabletransitions.md).
-   To disable a particular transition, call [**IAMTimelineTrans::SetCutsOnly**](iamtimelinetrans-setcutsonly.md).

When effects are disabled, they are not rendered during preview. When a transition is disabled, it is rendered as a jump cut. The segue between tracks still occurs, but the visual effect is not rendered.

If an effect or transition cannot be rendered, the render engine substitutes a default effect or transition. Call the [**IAMTimeline::SetDefaultEffect**](iamtimeline-setdefaulteffect.md) method to set the default effect, and the [**IAMTimeline::SetDefaultTransition**](iamtimeline-setdefaulttransition.md) method to set the default transition. If you do not specify a default, or if the one you specify also causes an error, DES uses its own default.

> [!Note]  
> You can also improve preview quality by increasing the amount of frame buffering. See [**IAMTimelineGroup::SetOutputBuffering**](iamtimelinegroup-setoutputbuffering.md).

 

## Related topics

<dl> <dt>

[Working with Effects and Transitions](working-with-effects-and-transitions.md)
</dt> </dl>

 

 




---
title: Create a Storyboard and Add Transitions
description: To create an animation, an application must construct a storyboard.
ms.assetid: e2641c93-e520-4749-a98e-5a58c175fdb9
keywords:
- storyboards Windows Animation ,creating
- storyboards Windows Animation ,adding transitions
- transitions Windows Animation ,creating
- transitions Windows Animation ,adding to storyboard
ms.topic: article
ms.date: 05/31/2018
---

# Create a Storyboard and Add Transitions

To create an animation, an application must construct a storyboard.

## Overview

The general steps for constructing a storyboard are as follows:

1.  Create a storyboard
2.  Create one or more transitions
3.  Add the transitions to the storyboard, specifying which variables they animate

An empty storyboard can be created using the animation manager. The application must populate each storyboard with transitions. Each transition specifies how a single animation variable changes over a given time interval. Transitions can be created using the transition library component included in Windows Animation. Alternately, an application can create its own custom transitions or use a transition library from a third party. When the application adds a transition to a storyboard, it specifies which animation variable the transition will animate.

A storyboard may include transitions on one or more animation variables. More complex storyboards can use keyframes to synchronize the starts or ends of transitions, or to specify portions of the storyboard that should repeat (a fixed number of times or indefinitely).

## Example Code

The following example code is taken from MainWindow.cpp in the Windows Animation sample [Timer-Driven Animation](timer-driven-animation-sample.md); see the CMainWindow::ChangeColor method. This example creates the storyboard (step 1) using the [**IUIAnimationManager::CreateStoryboard**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-createstoryboard) method, creates the transitions (step 2) using the [**IUIAnimationTransitionLibrary::CreateAccelerateDecelerateTransition**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtransitionlibrary-createacceleratedeceleratetransition) method, and adds the transitions to the storyboard (step 3) using the [**IUIAnimationStoryboard::AddTransition**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-addtransition) method.


```C++
const UI_ANIMATION_SECONDS DURATION = 0.5;
const DOUBLE ACCELERATION_RATIO = 0.5;
const DOUBLE DECELERATION_RATIO = 0.5;

// Create a storyboard

IUIAnimationStoryboard *pStoryboard = NULL;
HRESULT hr = m_pAnimationManager->CreateStoryboard(
    &pStoryboard
    );
if (SUCCEEDED(hr))
{
    // Create transitions for the RGB animation variables

    IUIAnimationTransition *pTransitionRed;
    hr = m_pTransitionLibrary->CreateAccelerateDecelerateTransition(
        DURATION,
        red,
        ACCELERATION_RATIO,
        DECELERATION_RATIO,
        &pTransitionRed
        );
    if (SUCCEEDED(hr))
    {
        IUIAnimationTransition *pTransitionGreen;
        hr = m_pTransitionLibrary->CreateAccelerateDecelerateTransition(
            DURATION,
            green,
            ACCELERATION_RATIO,
            DECELERATION_RATIO,
            &pTransitionGreen
            );
        if (SUCCEEDED(hr))
        {
            IUIAnimationTransition *pTransitionBlue;
            hr = m_pTransitionLibrary->CreateAccelerateDecelerateTransition(
                DURATION,
                blue,
                ACCELERATION_RATIO,
                DECELERATION_RATIO,
                &pTransitionBlue
                );
            if (SUCCEEDED(hr))
            {
                // Add transitions to the storyboard

                hr = pStoryboard->AddTransition(
                    m_pAnimationVariableRed,
                    pTransitionRed
                    );
                if (SUCCEEDED(hr))
                {
                    hr = pStoryboard->AddTransition(
                        m_pAnimationVariableGreen,
                        pTransitionGreen
                        );
                    if (SUCCEEDED(hr))
                    {
                        hr = pStoryboard->AddTransition(
                            m_pAnimationVariableBlue,
                            pTransitionBlue
                            );
                        if (SUCCEEDED(hr))
                        {
                            // Get the current time and schedule the storyboard for play

                            ...

}
```



## Previous Step

Before starting this step, you should have completed this step: [Read the Animation Variable Values](updating---application-driven-animation.md).

## Next Step

After completing this step, the next step is: [Schedule a Storyboard](scheduling-a-storyboard.md).

## Related topics

<dl> <dt>

[**IUIAnimationManager::CreateStoryboard**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-createstoryboard)
</dt> <dt>

[**IUIAnimationStoryboard::AddTransition**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationstoryboard-addtransition)
</dt> <dt>

[**IUIAnimationTransitionLibrary::CreateAccelerateDecelerateTransition**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationtransitionlibrary-createacceleratedeceleratetransition)
</dt> <dt>

[Storyboard Overview](storyboard-construction.md)
</dt> </dl>

 

 





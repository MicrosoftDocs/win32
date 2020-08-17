---
title: Create Animation Variables
description: An application must create an animation variable for each visual characteristic that is to be animated using Windows Animation.
ms.assetid: 360aa157-cb50-400a-b373-45885410469d
keywords:
- animation variables Windows Animation ,creating
ms.topic: article
ms.date: 05/31/2018
---

# Create Animation Variables

An application must create an animation variable for each visual characteristic that is to be animated using Windows Animation.

## Overview

Animation variables are created using the animation manager, and the application should retain a reference to each for as long as it is needed. Your application will generally create each animation variable at the same time as the visual object it animates.

When an animation variable is created, its initial value must be specified. Thereafter, its value can only be altered by scheduling storyboards that animate it.

Animation variables are passed as parameters when storyboards are constructed, so the application should not release them until the visual characteristics they represent no longer need to be animated, typically when the associated visual objects are about to be destroyed.

## Example Code

-   [Animating Colors](#animating-colors)
-   [Animating x and y Coordinates](#animating-x-and-y-coordinates)

### Animating Colors

The following example code is taken from MainWindow.cpp in the Windows Animation samples [Application-Driven Animation](application-driven-animation-sample.md) and [Timer-Driven Animation](timer-driven-animation-sample.md). In the example, three animation variables are created using [**CreateAnimationVariable**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-createanimationvariable) to represent background colors. The code also uses the [**SetLowerBound**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setlowerbound) and [**SetUpperBound**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setupperbound) methods to control the value of the animation variable.


```
const DOUBLE INITIAL_RED = COLOR_MAX;
const DOUBLE INITIAL_GREEN = COLOR_MAX;
const DOUBLE INITIAL_BLUE = COLOR_MAX;

HRESULT hr = m_pAnimationManager->CreateAnimationVariable(
    INITIAL_RED,
    &m_pAnimationVariableRed
    );
if (SUCCEEDED(hr))
{
    hr = m_pAnimationVariableRed->SetLowerBound(COLOR_MIN);
    if (SUCCEEDED(hr))
    {
        hr = m_pAnimationVariableRed->SetUpperBound(COLOR_MAX);
        if (SUCCEEDED(hr))
        {
            hr = m_pAnimationManager->CreateAnimationVariable(
                INITIAL_GREEN,
                &m_pAnimationVariableGreen
                );
            if (SUCCEEDED(hr))
            {
                hr = m_pAnimationVariableGreen->SetLowerBound(COLOR_MIN);
                if (SUCCEEDED(hr))
                {
                    hr = m_pAnimationVariableGreen->SetUpperBound(COLOR_MAX);
                    if (SUCCEEDED(hr))
                    {
                        hr = m_pAnimationManager->CreateAnimationVariable(
                            INITIAL_BLUE,
                            &m_pAnimationVariableBlue
                            );
                        if (SUCCEEDED(hr))
                        {
                            hr = m_pAnimationVariableBlue->SetLowerBound(COLOR_MIN);
                            if (SUCCEEDED(hr))
                            {
                                hr = m_pAnimationVariableBlue->SetUpperBound(COLOR_MAX);
                            }
                        }
                    }
                }
            }
        }
    }
}
```



Note the following definitions from MainWindow.h.


```
class CMainWindow
{

    ...

private:

    // Animated Variables

    IUIAnimationVariable *m_pAnimationVariableRed;
    IUIAnimationVariable *m_pAnimationVariableGreen;
    IUIAnimationVariable *m_pAnimationVariableBlue;

    ...

};
```



### Animating x and y Coordinates

The following example code is taken from Thumbnail.cpp in the Windows Animation [Grid Layout Sample](/windows/desktop/UIAnimation/grid-layout-sample); see the CMainWindow::CreateAnimationVariables method. Two animation variables are created to represent the X and Y coordinates of each object.


```C++
// Create the animation variables for the x and y coordinates

hr = m_pAnimationManager->CreateAnimationVariable(
    xInitial,
    &m_pAnimationVariableX
    );

if (SUCCEEDED(hr))
{
    hr = m_pAnimationManager->CreateAnimationVariable(
        yInitial,
        &m_pAnimationVariableY
        );

    ...

}
```



Note the following definitions from Thumbnail.h.


```
class CThumbnail
{
public:

    ...

    // X and Y Animation Variables

    IUIAnimationVariable *m_pAnimationVariableX;
    IUIAnimationVariable *m_pAnimationVariableY;

    ...

};
```



Animation variables are floating-point numbers, but their values can be fetched as integers, too. By default, each value will be rounded to the nearest integer, but it is possible to override the rounding mode used for a variable. The following example code uses the [**SetRoundingMode**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setroundingmode) method to specify that the values should always be rounded down.


```C++
hr = m_pAnimationVariableX->SetRoundingMode(
    UI_ANIMATION_ROUNDING_MODE_FLOOR
    );
if (SUCCEEDED(hr))
{
    hr = m_pAnimationVariableY->SetRoundingMode(
        UI_ANIMATION_ROUNDING_MODE_FLOOR
        );

    ...

}
```



## Previous Step

Before starting this step, you should have completed this step: [Create the Main Animation Objects](adding-animation-to-an-application.md).

## Next Step

After completing this step, the next step is: [Update the Animation Manager and Draw Frames](introducing-windows-animation-manager.md).

## Related topics

<dl> <dt>

[**IUIAnimationManager::CreateAnimationVariable**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationmanager-createanimationvariable)
</dt> <dt>

[**IUIAnimationVariable::SetLowerBound**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setlowerbound)
</dt> <dt>

[**IUIAnimationVariable::SetRoundingMode**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setroundingmode)
</dt> <dt>

[**IUIAnimationVariable::SetUpperBound**](/windows/desktop/api/UIAnimation/nf-uianimation-iuianimationvariable-setupperbound)
</dt> <dt>

[Windows Animation Overview](scenic-animation-api-overview.md)
</dt> </dl>

 

 
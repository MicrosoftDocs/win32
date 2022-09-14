---
title: Sample Render Code
description: Sample Render Code
ms.assetid: 14978cf4-47fa-4b2e-ba51-799be873dc8a
keywords:
- visualizations,sample code
- custom visualizations,sample code
- visualizations,Render function
- custom visualizations,Render function
- Render function,sample code
- samples,Render function for visualizations
ms.topic: article
ms.date: 05/31/2018
---

# Sample Render Code

Here is some sample code that uses the **Render** function to draw a line across the screen. The height of the line is defined by the waveform value.


```C++
STDMETHODIMP CStock::Render(TimedLevel *pLevels, HDC hdc, RECT *prc)
{
    // Create new brushes and pens.
    HBRUSH hNewBrush = ::CreateSolidBrush( 0 );
    // Create a new solid pen the color of the foreground.
    HPEN hNewPen = ::CreatePen( PS_SOLID, 0, m_clrForeground );


    // Add the pen to the device context.
    HPEN hOldPen= static_cast<HPEN>(::SelectObject( hdc, hNewPen ));

    // Fill the background with the black brush.
    ::FillRect( hdc, prc, hNewBrush );

    // Get the y value from the waveform.
    int y = pLevels->waveform[0][0];

    // Draw the line from left to right.
    ::MoveToEx( hdc, prc->left, y, NULL);  
    ::LineTo(hdc, prc->right, y); 

    // Delete your brush.
    if (hNewBrush)
    {
        ::DeleteObject( hNewBrush );
    }
    // Delete your pen.
    if (hNewPen)
    {
        ::SelectObject( hdc, hOldPen );
        ::DeleteObject( hNewPen );
    }

    // You're done for this round.
    return S_OK;
}

```



The **Render** function is where the main work of your code takes place. Every time Windows Media Player takes a snapshot of the audio, it will call this function and your code will run.

This code performs the following tasks. Refer to the Microsoft Windows Platform SDK for 32-bit Windows for more details about specific functions.

## Creating Objects

Usually you will be using the drawing functions that come with the Microsoft Windows Graphical Display Interface (GDI). You need to create pens to draw lines and brushes to fill areas.

A solid black brush is created to fill in the background.

A solid pen is created to draw a line. The color will be the foreground color as defined by the skin that is going to display the visualization.

## Adding the Object to the DC

You need to add the pen to the device context (DC). The DC is the portion of memory that all drawing data and objects are stored in. Essentially the DC is the window traffic manager that keeps track of everything graphical.

You need to *cast* the pen object you created and store it as an old pen. Use this coding technique for all new pens. This technique is required for 32-bit programming.

## Filling in the Background

You now are ready to draw. The **FillRect** function will fill the rectangle of the window, as defined by the parameters of the **Render** function. The rectangle is filled with a black brush.

## Getting Audio Data

Next the code gets some audio data from Windows Media Player. By using the waveform array, you can get the current value of the audio power at the moment the snapshot was taken. In this case, you are taking the audio data of the left channel. The first value in the array is the first 1024th of the audio power snapshot.

This information will be used to display a line whose height will match the audio power snapshot.

## Draw the Line

The line is drawn from left to right using the **MoveToEx** and **LineTo** GDI functions.

First you move the pen to the starting point. In this case, x and y are used to define the left-to-right and top-to-bottom values the user will see on the screen. X is defined by the rectangle prc and specifically by the value of prc->left. Y is defined as the value of the waveform data at that moment.

Then you draw a line to the other side of the window. The point you draw the line to is again an x, y value. X is defined by the rectangle prc, but this time by prc->right. Y is still defined by the waveform data and is the same as the point you started from, because you are drawing a straight line from left to right.

## Clean up Everything

You must delete the objects you create. Specifically you must delete any and all brushes and pens you create. It is good practice to delete pens and brushes when you finish using them.

If you do not delete them before finishing your implementation of the **Render** function, your visualization will crash in a minute or less. You must keep a count of your pens and brushes and destroy every single one. Be especially careful not to create pens inside a code loop.

Use the coding technique given in the example to destroy your pens and brushes.

-   **Important** Destroy your pens and brushes!

When you have finished cleaning up, be sure to return S\_OK so that Windows Media Player knows you are finished drawing. Once you finish, your drawing will be transferred to the window, another snapshot will be taken, **Render** will ask your code to draw again, and so on.

## Related topics

<dl> <dt>

[**Implementing Render**](implementing-render.md)
</dt> </dl>

 

 





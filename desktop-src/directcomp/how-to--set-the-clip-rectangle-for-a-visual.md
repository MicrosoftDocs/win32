---
title: How to clip with a rectangle clip object
description: This topic demonstrates how to use a rectangle clip object to clip a visual or visual tree.
ms.assetid: 377EF49A-F9F2-4A72-9D22-DEC33803AD0D
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to clip with a rectangle clip object

This topic demonstrates how to use a rectangle clip object to clip a visual or visual tree.

The example in this topic defines a rectangular clip that is centered at the mouse location, and applies the clip to a visual that is centered in the client area of the composition target window. This screen shot shows the result of applying the rectangle clip object to the visual.

![result of applying a rectangle clip object to a visual](images/clipwithrectangleclipobject.png)

## What you need to know

### Technologies

-   [DirectComposition](directcomposition-portal.md)
-   [Direct3D 11 Graphics](https://msdn.microsoft.com/library/windows/desktop/ff476080)
-   [DirectX Graphics Infrastructure (DXGI)](https://msdn.microsoft.com/library/windows/desktop/hh404534)

### Prerequisites

-   C/C++
-   Microsoft Win32
-   Component Object Model (COM)

## Instructions

### Step 1: Initialize DirectComposition objects

1.  Create the device object and the composition target object.
2.  Create a visual, set its content, and add it to the visual tree.

For more information, see [How to initialize DirectComposition](initialize-directcomposition.md).

### Step 2: Create the rectangle clip object

Use the [**IDCompositionDevice::CreateRectangleClip**](https://msdn.microsoft.com/en-us/library/Hh437399(v=VS.85).aspx) method to create an instance of the rectangle clip object.


```C++
    HRESULT hr = S_OK;
    
    // Create the rectangle clip object.
    if (m_pClip == NULL)
    {
        hr = m_pDevice->CreateRectangleClip(&amp;m_pClip);
    }
```



### Step 3: Set the properties of the rectangle clip object

Call the methods of the rectangle clip object's [**IDCompositionRectangleClip**](https://msdn.microsoft.com/en-us/library/Hh437434(v=VS.85).aspx) interface to set the properties of the clip rectangle.

The following example defines a clip rectangle that is centered around the current mouse location. The `m_offsetX` and `m_offsetY` member variables contain the values of the OffsetX and OffsetY properties of the visual.


```C++
    if (SUCCEEDED(hr))
    {
        // Get the location of the mouse.
        POINT ptMouse = { };
        GetCursorPos(&amp;ptMouse);
        ScreenToClient(m_hwnd, &amp;ptMouse);

        // Create a 100-by-100 pixel rectangular clip that is 
        // centered at the mouse location, and is mapped to
        // the rectangle of the visual.
        m_pClip->SetLeft((ptMouse.x - m_offsetX) - 50.f);
        m_pClip->SetTop((ptMouse.y - m_offsetY) - 50.f);
        m_pClip->SetRight((ptMouse.x - m_offsetX) + 50.f);
        m_pClip->SetBottom((ptMouse.y - m_offsetY) + 50.f);
    }
```



Note that the [**IDCompositionRectangleClip**](https://msdn.microsoft.com/en-us/library/Hh437434(v=VS.85).aspx) interface includes the following methods for defining a clip rectangle that has rounded corners:

-   [**SetTopLeftRadiusX**](/windows/desktop/api/Dcomp/nf-dcomp-settopleftradiusx)
-   [**SetTopLeftRadiusY**](/windows/desktop/api/Dcomp/nf-dcomp-settopleftradiusy)
-   [**SetTopRightRadiusX**](/windows/desktop/api/Dcomp/nf-dcomp-settoprightradiusx)
-   [**SetTopRightRadiusY**](/windows/desktop/api/Dcomp/nf-dcomp-settoprightradiusy)

### Step 4: Set the Clip property of the visual

Use the [**IDCompositionVisual::SetClip**](https://msdn.microsoft.com/en-us/library/Hh449153(v=VS.85).aspx) method to associate the Clip property of the visual with the rectangle clip object.


```C++
    if (SUCCEEDED(hr))
    {
        // Set the the rectangle clip object as the Clip property 
        // of the visual.
        hr = m_pVisual->SetClip(m_pClip);
    }
```



### Step 5: Commit the composition

Call the [**IDCompositionDevice::Commit**](https://msdn.microsoft.com/en-us/library/Hh437393(v=VS.85).aspx) method to commit the batch of commands to Microsoft DirectComposition for processing. The result of applying the clip rectangle appears in the target window.


```C++
    if (SUCCEEDED(hr))
    {
        // Commit the visual to be composed and displayed.
        hr = m_pDevice->Commit();  
    }
```



### Step 6: Free the DirectComposition objects

Be sure to free the rectangle clip object when you no longer need it, as well as the device object, the composition target object, and any visual objects. The following example calls the application-defined [**SafeRelease**](https://msdn.microsoft.com/library/windows/desktop/dd940435) macro to free the DirectComposition objects.


```C++
    SafeRelease(&amp;m_pClip);
    SafeRelease(&amp;m_pDevice);
    SafeRelease(&amp;m_pD3D11Device);
    SafeRelease(&amp;m_pCompTarget);
    SafeRelease(&amp;m_pVisual);
    SafeRelease(&amp;m_pSurface);
```



## Related topics

<dl> <dt>

[Clipping](clipping.md)
</dt> </dl>

 

 





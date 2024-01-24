---
title: Best practices for DirectComposition
description: This topic describes best practices for using Microsoft DirectComposition and provides links to articles on writing secure C++ code.
ms.assetid: D3A1ECD4-9358-44B9-8A84-7D901219D5CD
keywords:
- best practices for DirectComposition
- recommended practices for DirectComposition
ms.topic: article
ms.date: 05/31/2018
---

# Best practices for DirectComposition

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

This topic describes best practices for using Microsoft DirectComposition.

-   [Best practices](#best-practices-for-directcomposition)
-   [Security considerations](#security-considerations)
-   [Related topics](#related-topics)

## Best practices

The following table presents the practices recommended for working with Microsoft DirectComposition visuals.



| Practice                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| After creating a DirectComposition device, call the [**IDCompositionDevice::CheckDeviceState**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-checkdevicestate) method in response to each [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message to ensure that the device is still valid.<br/> | If the Microsoft DirectX Graphics Infrastructure (DXGI) device is lost, the DirectComposition device associated with the DXGI device is also lost. When it detects a lost device, DirectComposition sends the [**WM\_PAINT**](/windows/desktop/gdi/wm-paint) message to all windows. Calling [**CheckDeviceState**](/windows/win32/api/dcomp/nf-dcomp-idcompositiondevice-checkdevicestate) in response to each **WM\_PAINT** message lets you determine whether the DirectComposition device object is still valid and, if not, take steps to recover content. <br/> For more information, see [Device object](basic-concepts.md).<br/> |
| Create only the number of visuals needed for a composition or animation, and destroy the visuals immediately after DirectComposition finishes using them.<br/>                                                                                            | DirectComposition uses the graphics processing unit (GPU), a resource that your application shares with other applications and the operating system. This practice ensures that all applications and the operating system receive adequate GPU resources.<br/> For more information, see [Visuals](basic-concepts.md).<br/>                                                                                                                                                                                                                                                                     |
| Do not hide visuals by setting opacity to 0%; instead, remove visuals from the visual tree.<br/>                                                                                                                                                          | Setting opacity to 0% requires more system resources than removing them from the visual tree.<br/> For more information, see [Opacity](effects.md) and [Visual tree](basic-concepts.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                      |
| Do not hide a visual by applying an empty (zero sized) clip rectangle to a visual. Instead, remove the visual from the visual tree. <br/>                                                                                                                 | Removing a visual from the visual tree results in better performance than applying an empty clip rectangle.<br/> For more information, see [Clipping](clipping.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Do not apply a clip rectangle to a visual if the clip rectangle is not needed, such as a clip rectangle that includes the entire bitmap content of the visual.<br/>                                                                                       | Unnecessary clip rectangles harm system performance.<br/> For more information, see [Clipping](clipping.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| If you need a large, single-color bitmap, create a smaller bitmap surface and then apply a scale transform instead of creating a full-sized surface. <br/>                                                                                                | Applying a scale transform to a smaller surface uses fewer system resources than a full-size surface.<br/> For more information, see [Bitmap objects](bitmap-surfaces.md) and [Transforms](transforms.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                     |
| Avoid applying 3D transforms to multiple levels of a visual tree, such as to a parent and its descendent(s). <br/>                                                                                                                                        | Applying 3D transforms to multiple levels of a visual tree can produce unintended results because 3D transformations are not multiplied out in the tree. For example, a 90 degree rotation around the y-axis on a child, and a  90 degree rotation around the y-axis on a parent, results in both visuals being rotated away to nothing.<br/> For more information, see [Effects](effects.md).<br/>                                                                                                                                                                                                     |



 

## Security considerations

The following articles provide guidance for writing secure C++ code.

-   [Security Best Practices for C++](/cpp/security/security-best-practices-for-cpp)
-   [Patterns & Practices Security Guidance for Applications](/previous-versions/msp-n-p/ff650760(v=pandp.10))

## Related topics

<dl> <dt>

[How to Use DirectComposition](how-to-use-directcomposition.md)
</dt> </dl>

 


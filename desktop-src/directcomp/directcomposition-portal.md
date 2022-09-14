---
title: DirectComposition
description: This topic explains the purpose of Microsoft DirectComposition, identifies its run-time requirements, and describes the programming background that you need to use Microsoft DirectComposition effectively.
ms.assetid: 40e2d02b-77e8-425f-ac5e-3dcddef08173
keywords:
- DirectComposition
- DirectComposition API
- Microsoft DirectComposition
ms.topic: article
ms.date: 05/31/2018
---

# DirectComposition

> [!NOTE]
> For apps on Windows 10, we recommend using Windows.UI.Composition APIs instead of DirectComposition. For more info, see [Modernize your desktop app using the Visual layer](/windows/uwp/composition/visual-layer-in-desktop-apps).

## Purpose

Microsoft DirectComposition is a Windows component that enables high-performance bitmap composition with transforms, effects, and animations. Application developers can use the DirectComposition API to create visually engaging user interfaces that feature rich and fluid animated transitions from one visual to another.

DirectComposition enables rich and fluid transitions by achieving a high framerate, using graphics hardware, and operating independently of the UI thread. DirectComposition can accept bitmap content drawn by different rendering libraries, including Microsoft DirectX bitmaps, and bitmaps rendered to a window (HWND bitmaps). Also, DirectComposition supports a variety of transformations, such as 2D affine transforms and 3D perspective transforms, as well as basic effects such as clipping and opacity.

DirectComposition is designed to simplify the process of composing [*visuals*](directcomposition-glossary.md) and creating animated transitions. If your application already contains rendering code or already uses the recommended DirectX API, you only need to do a minimal amount of work to use DirectComposition effectively.

## Developer audience

The DirectComposition API is intended for experienced and highly-capable graphics developers who know C/C++, have a solid understanding of the Component Object Model (COM), and are familiar with Windows programming concepts.

## Run-time requirements

DirectComposition was introduced in Windows 8. It is included in 32-bit, 64-bit, and ARM platforms.

## In this section



| Topic                                                                       | Description                                                                                                                                                    |
|-----------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Why use DirectComposition?](why-use-directcomposition-.md)<br/>     | This topic describes the capabilities and benefits of DirectComposition. <br/>                                                                           |
| [How to Use DirectComposition](how-to-use-directcomposition.md)<br/> | This section describes best practices for using the DirectComposition API, and demonstrates how to use the API to accomplish several common tasks. <br/> |
| [DirectComposition concepts](directcomposition-concepts.md)<br/>     | This section provides a conceptual overview of DirectComposition.<br/>                                                                                   |
| [DirectComposition reference](reference.md)<br/>                     | This section provides detailed reference information for the elements that make up the DirectComposition API.<br/>                                       |
| [DirectComposition samples](directcomposition-code-samples.md)<br/>  | The following sample applications show how to use the DirectComposition API and demonstrate its capabilities. <br/>                                      |
| [DirectComposition glossary](directcomposition-glossary.md)<br/>     | This topic defines DirectComposition terms. <br/>                                                                                                        |



 

 

 






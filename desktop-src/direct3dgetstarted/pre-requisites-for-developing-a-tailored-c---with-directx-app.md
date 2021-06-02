---
title: Prerequisites for developing with DirectX
description: When you start to develop a Windows app using DirectX, keep the prerequisites on this page in mind. This includes the technologies you need to know before you dive in.
ms.assetid: 93f566cf-0c16-4487-9d53-dc59746e4d00
keywords:
- DirectX app, prerequisites
- DirectX app, Windows Store app
ms.topic: article
ms.date: 05/31/2018
---

# Prerequisites for developing with DirectX

When you start to develop a Windows app using DirectX, keep the prerequisites on this page in mind. This includes the technologies you need to know before you dive in.

## What should I know to develop a Windows game using DirectX?

Before you start to develop a Windows Store app using DirectX, you need to know how to program in Windows with C++. Windows apps using DirectX are developed at a low level of programming, which means that you will be exposed to many features of the operating system. These include memory and resource management, and the interface for the graphics device itself. If you are new to game or graphics app development, you may find this challenging. But you will also find it rewarding, because learning game development at this level creates far, far greater possibilities for game and graphics app design and development.

You'll also need to understand the basics of 2D and 3D graphics programming and mathematics, because many of the APIs you'll use were developed with these principles in mind. It'll be easier for you to understand their parameters and results if you are familiar with the operations behind them.

At a minimum, you should have a grasp of the following:

-   Windows C/C++ programming. This means that you understand pointers and references, events and callbacks, and perhaps a few of the common libraries like ATL.
-   Win32 programming. You understand how windows are created, and how user interface events are processed. You also understand a little bit about COM and essential Win32 APIs.
-   Linear algebra and trigonometry. While not essential, you'll have an easier time if you are familiar with concepts from these two math disciplines, because they are the foundation of much of 3D graphics programming.
-   Basic graphics terminology and concepts, such as bitmaps, textures, vertices, meshes, and viewports.

## What does DirectX provide me?

DirectX is the primary set of graphics APIs you'll use to develop Windows games. Here are the categories of features that you must become familiar with when you decide how to develop your game.



| Library     | Description                                                                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct3D    | A powerful, performance-oriented, hardware-accelerated set of libraries for rendering 3D graphics.                                              |
| Direct2D    | A set of 2D graphics libraries for hardware-accelerated bitmap and vector 2D drawing.                                                           |
| DirectXMath | A library of common, optimized math operations used in 2D and 3D graphics, such as vector and matrix operations.                                |
| DirectWrite | A library of 2D text rendering and layout APIs. It supports both hardware acceleration and software rasterization.                              |
| XAudio2     | A low-level, cross-platform audio API for Microsoft Windows that provides a signal processing and audio mixing foundation for game development. |
| XInput      | A library that supports various traditional gaming controls, with an emphasis on the Xbox 360 controller model.                                 |



 

## What tools do I need to develop a Windows game with DirectX?

To get started with this tutorial, you need:

-   Windows 8.1 or greater
-   Microsoft Visual Studio 2013 or greater

 

 





---
title: Samples
description: Samples
ms.assetid: b9acb143-1c23-4f6b-8f45-fef812c3b590
keywords:
- Windows Movie Maker,samples
- Movie Maker,samples
- Windows DVD Maker,samples
- DVD Maker,samples
- programming guide,Windows Movie Maker samples
- programming guide,Windows DVD Maker samples
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Samples

The Windows Movie Maker and Windows DVD Maker SDK includes two samples that demonstrate many of the extensibility techniques described in this document. In addition, several of the headers and libraries included with the samples expose the APIs documented in [Windows Movie Maker APIs](windows-movie-maker-apis.md).

Download the samples, headers, libraries, and documentation at the [Windows Movie Maker and Windows DVD Maker SDK page](http://go.microsoft.com/fwlink/p/?linkid=82670) on the Microsoft Download Center.

Following are descriptions of the contents of each directory in the download package.

Documentation

This Help file.

Include

Required C++ header files.

Lib

Libraries that define some of the APIs documented in [Windows Movie Maker APIs](windows-movie-maker-apis.md); use GPUPipelineVC8.lib for Visual Studio 2005 and GPUPipelineVC7.lib for Visual Studio .NET.

Lib\\x64

A 64-bit version of the library GPUPipelineVC8.lib for use with Visual Studio 2005 only. Use this library for building 64-bit effects and transitions.

Media

Sample XML and bitmap files for the sample projects.

A Visual Studio solution (one for Visual Studio 2005 and one for Visual Studio .NET) with the following two sample projects:

**SampleTFX.** One sample effect and one sample transition.

**SampleDVDMenuStyle.** One sample DVD menu style.

In addition to the two project folders, the Common folder contains common.cpp, which defines the [Transform Helper Functions](transform-helper-functions.md).

 

 





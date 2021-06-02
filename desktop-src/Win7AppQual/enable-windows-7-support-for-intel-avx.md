---
description: Enable Windows 7 Support for Intel AVX
ms.assetid: fe19e337-3109-42d6-a704-70662ac7c684
title: Enable Windows 7 Support for Intel AVX
ms.topic: article
ms.date: 05/31/2018
---

# Enable Windows 7 Support for Intel AVX

## Affected Platforms

 **Clients** - Windows 7 SP1  
**Servers** - Windows Server 2008 R2 SP1  


## Feature Impact

 **Severity** - Low  
**Frequency** - Low  





## Description

Intel<sup>?</sup> Advanced Vector Extensions (AVX)<sup>?</sup> is a 256-bit SIMD floating-point vector extension of Intel architecture. It includes extensions to both instruction and register sets.

Microsoft has developed some API enhancements, such as XState functions, that enable applications to access and manipulate extended processor feature information and state, including AVX.

## Usage Scenarios

There are three general levels of potential impact.

**Level 1:** Applications that do not directly use Intel AVX will not see any impact to their functionality even if they call into libraries or use compilers that indirectly use or generate Intel AVX extensions. This represents by far the majority of applications.

**Level 2:** Advanced applications that explicitly use the Intel AVX instruction set will be able to access and change AVX register contents when a hardware exception is raised. A very small number of applications would fall into this category, as it implies an intimate knowledge of the instruction stream executing at the time of the exception, such as applications with sections written in assembly language or those that generate machine code at runtime (for example, managed code runtimes with just-in-time compilation).

**Level 3:** Debugger applications will be able to access and manipulate the AVX state in the application being debugged.

## How to Leverage Feature Capabilities

**Level 1:** No action is necessary for applications to use Intel AVX.

**Level 2:** Applications in this category have the option to access and manipulate AVX state at the time of the exception from within their exception filters. After obtaining the base processor context via GetExceptionInformation, filters should:

 **1.** Check the value of the **CONTEXT\_XSTATE** flag. This flag indicates the presence of at least one XState feature in the context.  
**2.** If this is the case, call **GetXStateFeaturesMask** and test the value of the **XSTATE\_AVX** flag in the returned mask. This indicates the presence of AVX state in the context.  
**3.** Call **LocateXStateFeature** to retrieve the actual location where the AVX state is stored.  

**Level 3:** It is not necessary to update existing debugger applications unless they wish access the Intel AVX registers:

**1.** To determine if AVX is enabled, the debugger should use:

-   GetEnabledXStateFeatures to get a mask of enabled XState features on x86 or x64 processors to determine what features are present and enabled on the system before using an XState processor feature or attempting to manipulate XState contexts

  
**2.** If AVX is present and you wish to retrieve and manipulate the AVX state from the application being debugged (for example, GetThreadContext and SetThreadContext), the debugger should use:

-   InitializeContext Function to Initialize a context structure inside a buffer with the necessary size and alignment
-   CopyContext Function to copy a source context structure (including any XState) onto an initialized destination context structure

  
**3.** To test, set and locate the AVX state within a processor context, the debugger should use:

-   LocateXStateFeature to retrieve a pointer to the processor state for an individual XState feature within a context structure
-   GetXStateFeaturesMask to return the mask of XState features set within a context structure
-   SetXStateFeaturesMask to set the mask of XState features set within a context structure

  


## Links to Other Resources

-   For information about the XState functions in the Windows SDK, see [Debugging Functions](../debug/debugging-functions.md).
-   For an overview of the instructions and capabilities of the Intel AVX, see [Intel AVX: New Frontiers in Performance Improvements and Energy Efficiency](https://software.intel.com/articles/intel-avx-new-frontiers-in-performance-improvements-and-energy-efficiency/).

 

 

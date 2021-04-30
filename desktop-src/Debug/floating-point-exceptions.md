---
description: By default, the system has all FP exceptions turned off.
ms.assetid: efbea036-de9c-4f92-865a-494161da375e
title: Floating-Point Exceptions
ms.topic: article
ms.date: 05/31/2018
---

# Floating-Point Exceptions

By default, the system has all FP exceptions turned off. Therefore, computations result in NAN or INFINITY, rather than an exception. Before you can trap floating-point (FP) exceptions using structured exception handling, you must call the [\_controlfp\_s](/previous-versions/visualstudio/visual-studio-2010/c9676k6h(v=vs.100)) C run-time library function to turn on all possible FP exceptions. To trap only particular exceptions, use only the flags that correspond to the exceptions to be trapped. Note that any handler for FP errors should call [\_clearfp](/cpp/c-runtime-library/reference/clear87-clearfp?view=vs-2019) as its first FP instruction. This function clears floating-point exceptions.

 

 

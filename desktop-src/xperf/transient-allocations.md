---
title: Transient Allocations
description: Transient Allocations
ms.assetid: 5967f082-3c59-4fc2-b4f8-29e88cd74a5d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Transient Allocations

Transient allocations are commonly used, but depending on their number and size can lead to unacceptable peak heap usage or poor data locality resulting in increased execution time.

There are a number of techniques to reduce the number of transient allocations. The simplest of these is to convert small heap allocations that live for the lifetime of a function call to a stack variable. Care must be taken to ensure that this conversion will not lead to excessive stack usage.

A second option is to modify the algorithm or call path so fewer transient allocations are made. Often execution patterns within the process or code base can result in a large number of transient allocations rather than a specific algorithm. How often a call path is executed or incorrect usage assumptions made during development can sometimes lead to a large number of avoidable transient allocations.

 

 





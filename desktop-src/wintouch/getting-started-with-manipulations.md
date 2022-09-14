---
title: Manipulations
description: This section explains object manipulation for Windows Touch.
ms.assetid: 7f905c36-7804-422c-8a60-a281e03c5e15
keywords:
- Windows Touch,manipulations
- manipulations,about
- manipulations,gesture differences
- gestures,manipulation differences
ms.topic: article
ms.date: 05/31/2018
---

# Manipulations

This section explains object manipulation for Windows Touch.

## Manipulation Overview

A convenient way to think about manipulations is to consider them a superset of gestures. What you can do with gestures, you can do with more flexibility and with finer precision by using manipulations. The difference between manipulations and gestures is best demonstrated with a simple example. You can expand an object and at the same time translate it using manipulations; with gestures, you can do only one at a time. This ability to manipulate an object in real time makes applications more intuitive to users by enabling a more realistic experience.

The Manipulation APIs are used to simplify transformation operations on objects for touch-enabled applications. Manipulations are performed in Windows 7 through the manipulations COM object. By using manipulations, developers can more easily support inertia (object physics) and can easily perform transformations on objects in a way that is consistent with other applications. The following sections explain various ways that you can perform manipulations.



| Section                                                                                            | Description                                                                                                                                          |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Adding Manipulation Support to Unmanaged Code](adding-manipulation-support-in-unmanaged-code.md) | Explains how to implement an event sink for the [**\_IManipulationEvents**](/windows/win32/api/manipulations/nn-manipulations-_imanipulationevents) interface and add event handlers to your code. |
| [Advanced Manipulations](advanced-manipulations.md)                                               | Explains how to perform complex manipulations.                                                                                                       |
| [Single Finger Rotation](single-finger-rotation.md)                                               | Explains how to rotate an object by using a pivot point and the manipulation processor.                                                              |



 

## Related topics

<dl> <dt>

[Manipulations and Inertia](manipulation-and-inertia.md)
</dt> </dl>

 

 





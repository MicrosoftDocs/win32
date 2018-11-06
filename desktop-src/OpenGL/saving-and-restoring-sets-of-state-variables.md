---
title: Saving and Restoring Sets of State Variables
description: You can save and restore the values of a collection of state variables on an attribute stack with the glPushAttrib and glPopAttrib functions.
ms.assetid: 339de633-4158-4907-b985-2d75b465fb2a
keywords:
- OpenGL state variables
- saving state variables OpenGL
- restoring state variables OpenGL
ms.topic: article
ms.date: 05/31/2018
---

# Saving and Restoring Sets of State Variables

You can save and restore the values of a collection of state variables on an attribute stack with the [**glPushAttrib**](glpushattrib.md) and [**glPopAttrib**](glpopattrib.md) functions. The attribute stack has a depth of at least 16. To obtain the actual depth, use GL\_MAX\_ATTRIB\_STACK\_DEPTH with [**glGetIntegerv**](glgetintegerv.md). Pushing a full stack or popping an empty one generates an error.

It is generally faster to use **glPushAttrib** and **glPopAttrib** than to get and restore the values yourself. Some values might be pushed and popped in the hardware, and saving and restoring them can be resource-intensive. Also, if you're operating on a remote client, all of the attribute data must be transferred across the network connection and back as it is saved and restored. However, your OpenGL implementation keeps the attribute stack on the server, avoiding unnecessary network delays.

The prototype of **glPushAttrib** is:

**void** **glPushAttrib**(**GLbitfield** *mask* );

Using [**glPushAttrib**](glpushattrib.md) saves all the attributes indicated by bits in *mask* by pushing them onto the attribute stack. For a list of the possible mask bits you can logically OR together to save any combination of attributes, see [Attribute Groups](attribute-groups.md). Each bit corresponds to a collection of individual state variables. For example, GL\_LIGHTING\_BIT refers to all the state variables related to lighting, which include the current material color; the ambient, diffuse, specular, and emitted light; a list of the lights that are enabled; and the directions of the spotlights. When you call [**glPopAttrib**](glpopattrib.md), all those variables are restored. To find out exactly which attributes are saved for particular mask values, see [OpenGL State Variables](opengl-state-variables.md).

 

 





---
title: Precise Capture Control
description: Precise Capture Control
ms.assetid: 497c9d77-f392-4cbb-88f3-8418e1e9fc6b
keywords:
- AVICap callback functions,precise capture control
ms.topic: article
ms.date: 05/31/2018
---

# Precise Capture Control

A capture window can provide the capture-control callback function with precise control over the moments that streaming capture begin and end. The first message sent from the capture driver to the callback procedure sets the *nState* parameter to CONTROLCALLBACK\_PREROLL after allocating all buffers and all other capture preparations are complete. This message gives the application the ability to preroll the video sources. (The callback function specifies *nState* as its second parameter.) The callback function then returns at the exact moment recording is to begin. A return value of **TRUE** from the callback function continues capture. A return value of **FALSE** aborts capture. Once capture begins, the callback function is called frequently with *nState* set to CONTROLCALLBACK\_CAPTURING to allow the application to end capture by returning **FALSE**.

 

 





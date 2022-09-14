---
description: Although a&\#160;recognizer context&\#160;cannot be accessed on two threads simultaneously by the Tablet PC platform, the AdviseInkChange function can be called at any time on any thread.
ms.assetid: 2cd19819-08d0-418d-830b-2288a66ca0d0
title: Recognizer Threading Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Recognizer Threading Considerations

Although a [recognizer context](hrecocontext-handle.md) cannot be accessed on two threads simultaneously by the Tablet PC platform, the [**AdviseInkChange**](/windows/desktop/api/recapis/nf-recapis-adviseinkchange) function can be called at any time on any thread. Because the Tablet PC platform does not ensure that there is only one recognizer context at a time, two separate recognizer contexts in separate threads may simultaneously attempt to access your [recognizer](hrecognizer-handle.md). Therefore, global variables in your recognition engine must be thread-safe.

Word lists are an optional implementation used to increase accuracy. If your recognizer implements word lists, it must be thread-safe. For more information about using word lists, see [Using Application Dictionaries](using-application-dictionaries.md).

For details about other threading considerations, see [Tablet PC Threading Considerations](tablet-pc-threading-considerations.md).

 

 




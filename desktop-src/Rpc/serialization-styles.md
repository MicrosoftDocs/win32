---
title: Serialization Styles
description: There are three styles you can use to manipulate serialization handles.
ms.assetid: 40b609b2-abad-4967-a5d1-948ac26fd65c
ms.topic: article
ms.date: 05/31/2018
---

# Serialization Styles

There are three styles you can use to manipulate serialization handles. These are:

-   [Fixed Buffer Serialization](fixed-buffer-serialization.md)
-   [Dynamic Buffer Serialization](dynamic-buffer-serialization.md)
-   [Incremental Serialization](incremental-serialization.md)

Regardless of the style you use, you must create a serialization handle, serialize the data, and then free the handle. The style is set when your program creates the handle and defines the way a buffer is manipulated. The handle maintains the appropriate context associated with each of the three serialization styles.

 

 





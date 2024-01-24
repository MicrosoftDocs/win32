---
description: You can specify that the driver clip the frames.
ms.assetid: a4f53568-684b-48cf-835b-915cefb45a5d
title: Clipping a Frame
ms.topic: article
ms.date: 05/31/2018
---

# Clipping a Frame

You can specify that the driver clip the frames. (If the other capture filter sections are omitted, this may be the only function of your capture filter). If the **nFrameBytesToCopy** field is not zero (0), its value specifies how many bytes of each frame received to retain. If the field is zero, then the whole frame is retained.

> [!Note]  
> You may clip any frame that passes the other portions of your capture filter by setting **nFrameBytesToCopy**.

 

 

 




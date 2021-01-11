---
description: A Tablet PC pen may have more than one end that can interact with the digitizer.
ms.assetid: c1aa0d65-cfea-4720-ad09-7add724e03c7
title: Multiple Functionality with One Pen
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Functionality with One Pen

A Tablet PC pen may have more than one end that can interact with the digitizer. If both ends of the pen can generate events, one end may be used to lay down ink, select, and point, and the other end may be used for other functions such as erasing.

To implement such functionality, your application must be able to determine which end of the pen is being used and hence when to change the appearance of the cursor. It can do this by looking for the state of the [**Inverted**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkcursor-get_inverted) property on the [**Cursor**](/windows/desktop/api/msinkaut/nn-msinkaut-iinkcursor) object.

For specific details about using the back of the pen for erasing, see [Erasing Ink with the Pen](erasing-ink-with-the-pen.md). In addition, the [Ink Erasing Sample](ink-erasing-sample.md) demonstrates how to use the back of the pen to erase ink.

 

 




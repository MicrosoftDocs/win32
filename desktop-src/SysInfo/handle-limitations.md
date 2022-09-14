---
description: Some objects support only one handle at a time.
ms.assetid: 3eafd0e0-3923-4489-8a0a-63007dd3183a
title: Handle Limitations
ms.topic: article
ms.date: 05/31/2018
---

# Handle Limitations

Some objects support only one handle at a time. The system provides the handle when an application creates the object and invalidates the handle when the application destroys the object. Other objects support multiple handles to a single object. The operating system automatically removes the object from memory after the last handle to the object is closed.

The total number of open handles in the system is limited only by the amount of memory available. Some object types support a limited number of handles per session or per process.

 

 




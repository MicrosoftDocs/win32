---
title: Edit Sessions
description: When a text service must obtain, modify, or set text in a context, it must request an edit session.
ms.assetid: e4115227-1036-4892-986d-dc4cef5b178e
keywords:
- Text Services Framework (TSF),edit session
- TSF (Text Services Framework),edit session
- text services,edit session
- edit session
ms.topic: article
ms.date: 05/31/2018
---

# Edit Sessions

When a text service must obtain, modify, or set text in a context, it must request an *edit session*. When an edit session is requested, the TSF manager negotiates with the owner of the target context for a document lock of the requested type. When the document lock is granted, the TSF manager enables the text service to read and/or write text to or from the context.

 

 





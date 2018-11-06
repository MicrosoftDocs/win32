---
title: About Custom File and Stream Handlers
description: About Custom File and Stream Handlers
ms.assetid: 6a00c8db-3ac6-4826-a373-52b6b7d1652f
keywords:
- Video for Windows (VFW),custom file handlers
- Video for Windows (VFW),custom stream handlers
- Video for Windows (VFW),file handlers
- Video for Windows (VFW), stream handlers
- VFW (Video for Windows),custom file handlers
- VFW (Video for Windows),custom stream handlers
- VFW (Video for Windows),file handlers
- VFW (Video for Windows),stream handlers
ms.topic: article
ms.date: 05/31/2018
---

# About Custom File and Stream Handlers

Your application can use a custom file handler to read from a file or write to a file that is in a nonstandard format. To do this, your application simply uses the name of your file handler when opening the file or allocating the file interface. The AVIFile library then uses the functions from your file handler instead of those from another file handler. The nonstandard format appears as standard AVI data to your application or to any other application using your custom file handler.

Similarly, your application can use a custom stream handler to read a stream that is in a nonstandard format. A stream — whether it constitutes audio, video, MIDI, text, or custom data — is a component of an AVI file. For example, an AVI file that contains a video sequence, an English soundtrack, and a French soundtrack consists of three streams. Your application can specify the streams in an AVI file to process and direct each of those streams to a handler that can optimally process the appropriate type of multimedia data.

> [!Note]  
> You must place custom stream and file handlers in one or more DLLs, separated from main application files.

 

 

 





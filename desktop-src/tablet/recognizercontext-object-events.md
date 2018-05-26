---
Description: The following table describes which threads the RecognizerContext object events can fire on.EventThreadsRecognitionFires on the background recognition thread, or on the thread which calls the RecognizerContext objects Recognize method.RecognitionWithAlternatesFires on the background recognition thread. 
ms.assetid: bcdf33aa-21bc-4218-a0a8-2edfa019f340
title: RecognizerContext Object Events
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RecognizerContext Object Events

The following table describes which threads the [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object events can fire on.



| Event                                                                               | Threads                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Recognition**](inkrecognizercontext-recognition.md)                             | Fires on the background recognition thread, or on the thread which calls the [**RecognizerContext**](/windows/win32/msinkaut/?branch=master) object's [**Recognize**](/windows/win32/msinkaut/?branch=master) method.<br/> |
| [**RecognitionWithAlternates**](inkrecognizercontext-recognitionwithalternates.md) | Fires on the background recognition thread.<br/>                                                                                                                                                               |



 

 

 





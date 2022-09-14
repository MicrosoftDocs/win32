---
description: The following table describes which threads the RecognizerContext object events can fire on.EventThreadsRecognitionFires on the background recognition thread, or on the thread which calls the RecognizerContext object's Recognize method.RecognitionWithAlternatesFires on the background recognition thread.
ms.assetid: bcdf33aa-21bc-4218-a0a8-2edfa019f340
title: RecognizerContext Object Events
ms.topic: article
ms.date: 05/31/2018
---

# RecognizerContext Object Events

The following table describes which threads the [**RecognizerContext**](inkrecognizercontext-class.md) object events can fire on.



| Event                                                                               | Threads                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Recognition**](inkrecognizercontext-recognition.md)                             | Fires on the background recognition thread, or on the thread which calls the [**RecognizerContext**](inkrecognizercontext-class.md) object's [**Recognize**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-recognize) method.<br/> |
| [**RecognitionWithAlternates**](inkrecognizercontext-recognitionwithalternates.md) | Fires on the background recognition thread.<br/>                                                                                                                                                               |



 

 

 





---
description: A handwriting recognition engine, or recognizer, is software that processes ink and converts that ink into text.
ms.assetid: b64f6856-453c-4080-84e0-0a9e69e79de7
title: Using Context to Improve Accuracy
ms.topic: article
ms.date: 05/31/2018
---

# Using Context to Improve Accuracy

A handwriting recognition engine, or recognizer, is software that processes ink and converts that ink into text. A context is relevant, application-specific information that you provide to a recognizer to improve recognition accuracy. In other words, context is any piece of information about input that aids the recognizer in accurately processing the ink in a field.

This section describes the different ways you can take advantage of context in your Tablet PC application, placing emphasis on the preferred programmatic technique for applications that are not ink enabled.

> [!Note]  
> There are places in the Tablet PC Technology sections of the Windows Vista Software Development Kit (SDK) where the term "context" is used in regard to the [**RecognizerContext**](inkrecognizercontext-class.md) object and its [**PrefixText**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_prefixtext) and [**SuffixText**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_suffixtext) properties. Do not confuse these other usages of "context" with the definition in this section.

 

 

 




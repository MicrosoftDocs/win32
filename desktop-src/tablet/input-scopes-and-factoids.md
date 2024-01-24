---
description: Describes how input scopes are used for recognition.
ms.assetid: 9faf6d22-b80d-4020-ac74-ee40b31ae9d4
title: Input Scopes and Factoids
ms.topic: article
ms.date: 05/31/2018
---

# Input Scopes and Factoids

An input scope is a defined set of words, numbers, punctuation, and syntactical orderings that are allowed within a given language model. Input scopes can be used by applications to restrict the language model used by the recognizer to a specific context. For example, an input scope of IS\_EMAIL\_SMTPEMAILADDRESS influences the recognition results by indicating that a specific field is an email address. Thus, the field is likely to contain characters such as "@" and "\_", and it may not contain characters such as "\*" and spaces.

> [!Note]  
> Other Microsoft technologies also use input scopes. This article focuses on using context to improve accuracy of handwriting recognition engines for Tablet PC applications.

 

Previous versions of the Tablet PC Technology API used factoids to define context. For practical purposes, a factoid is the same thing as an input scope. Version one of the Tablet PC SDK platform defined a set of factoid values in the [**Factoid**](factoid-constants.md) object. These values were used to set context and influence recognition results when using the [**RecognizerContext**](inkrecognizercontext-class.md) object for recognition. For recognizers of Latin script starting with Windows XP Tablet PC Edition 2005, you still use the [**Factoid**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid) property of the **RecognizerContext** object to set context, but you should pass in an input scope, phrase list, or handwriting regular expression value instead of one of the version one factoid values. The Microsoft recognizers of East Asian characters do not support using the input scope enumerated values. You should continue to use factoid values for recognizers of East Asian characters.

Input scopes and factoids are restrictions on the word level alternates; the character alternates may be outside the input scope specified even when the **COERCE** flag is set.

When the **COERCE** flag is set with a restrictive factoid, it may happen that the recognizer cannot produce an answer that both matches the ink and satisfies the factoid. Another scenario where recognizer may not produce any satisfactory answer is when the language of the recognizer does not match the language of the ink (for example the US English recognizer and Chinese ink characters).

When the handwriting recognizer cannot recognize the ink for a given word or character, it may either return an empty alternate list or an alternate list where the first choice is code point 0xffff (undefined character). This is especially useful in boxed guide input modes, where each box with ink is expected to have a non-empty list of alternates. The application can then display this undefined character in any manner it chooses (for example as "???").

> [!Note]  
> The factoid values continue to work with recognizers of Latin script for backward compatibility.

 

For more information about factoids, see [Setting Context for Ink-Enabled Controls](setting-context-for-ink-enabled-controls.md).

For information about East Asian factoids, see [Supported Factoids from Version 1](supported-factoids-from-version-1.md).

 

 




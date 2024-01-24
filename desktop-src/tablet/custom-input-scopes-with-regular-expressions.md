---
description: You can define custom input scopes by using language models composed of regular expressions for handwriting and assigning them to fields.For example, if you are creating a database application for warehouse parts and want users to be able to enter part numbers using the Tablet PC Input Panel's writing pad. If the part number syntax consists of three letters followed by four numbers followed by another letter (for example, ABC1234D), the handwriting recognizer would have a difficult time recognizing such input because it is not defined in the language model. There is no predefined factoid that corresponds to such syntax, nor can Microsoft include the syntax for every possible field an application might need. Handwriting regular expressions provide an easy way for applications to define their own language model for a particular special-use field.Note  When working in an ink-enabled application that uses the Factoid property of the RecognizerContext object, you cannot use version 1 factoids in a regular expression.
ms.assetid: 71f80196-0a36-4a14-a115-712bc909f6d7
title: Custom Input Scopes with Regular Expressions
ms.topic: article
ms.date: 05/31/2018
---

# Custom Input Scopes with Regular Expressions

You can define custom input scopes by using language models composed of regular expressions for handwriting and assigning them to fields.

For example, if you are creating a database application for warehouse parts and want users to be able to enter part numbers using the Tablet PC Input Panel's writing pad. If the part number syntax consists of three letters followed by four numbers followed by another letter (for example, ABC1234D), the handwriting recognizer would have a difficult time recognizing such input because it is not defined in the language model. There is no predefined factoid that corresponds to such syntax, nor can Microsoft include the syntax for every possible field an application might need. Handwriting regular expressions provide an easy way for applications to define their own language model for a particular special-use field.

> [!Note]  
> When working in an ink-enabled application that uses the [**Factoid**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_factoid) property of the [**RecognizerContext**](inkrecognizercontext-class.md) object, you cannot use version 1 factoids in a regular expression.

 

 

 




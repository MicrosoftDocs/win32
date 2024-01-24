---
description: All application dictionaries are implemented by using the WordList object.
ms.assetid: 805788ec-1672-462a-b188-c680f56c2641
title: Understanding Word Lists, Recognizer Context, and Factoids
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Word Lists, Recognizer Context, and Factoids

All application dictionaries are implemented by using the [**WordList**](inkwordlist-class.md) object. The [**RecognizerContext**](inkrecognizercontext-class.md) object manages recognition, in part through that object's [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property. The **RecognizerContext** object passes the word list to the recognizer. You may enable an application dictionary in any **RecognizerContext** in your application by setting the **WordList** property of the **RecognizerContext** object. To make the word list available to the entire application, you must set the **WordList** property of every **RecognizerContext** object in the application.

At the recognizer level, all dictionaries except for the system dictionary are implemented as word lists. However, the recognizer can only have one active word list at a time. This means that you cannot have both an application dictionary and the user dictionary active at the same time. On the other hand, the system dictionary is always available, unless a factoid is set that turns the system dictionary off.

The user dictionary is the list of words that the user has added to his or her Tablet PC. If the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property of the [**RecognizerContext**](inkrecognizercontext-class.md) is not set, the **RecognizerContext** passes the user dictionary as a word list to the recognizer. However, if the **WordList** property of the **RecognizerContext** object is set, the word list is passed to the recognizer instead of the user dictionary.

> [!Note]  
> The [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_strokes) property of the [**RecognizerContext**](inkrecognizercontext-class.md) object must be empty before you set the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property. If the **Strokes** property is not empty, an exception is thrown. Words should never be added to a word list after it has been assigned to a **RecognizerContext** object.

 

Setting a factoid on the [**RecognizerContext**](inkrecognizercontext-class.md) object also affects how application dictionaries are used by the recognizer. The factoids that affect the behavior of dictionaries are:

-   **WordList**
-   **SystemDictionary**
-   **None**

By far, the most useful factoid for application dictionaries is the **WordList** factoid. The **WordList** factoid biases the recognizer toward returning only words found in the word list. This factoid turns off all other dictionaries except for the word list. If the **WordList** factoid is set, and no word list is specified in the recognizer context, the user dictionary is used as the word list.

For example, if you are designing an airplane parts application with a field that accepts one of ten names of specialized parts, you may create a word list that contains only these part names. Setting the **WordList** factoid for the field greatly improves recognition for the words entered in that field. The recognizer need not choose between words in the system dictionary and words in the word list.

The **SystemDictionary** factoid enables the system dictionary only. The **None** factoid disables all dictionaries. These two factoids are used to increase recognition accuracy in certain instances. However, because they disable application dictionaries, they are rarely used in conjunction with application dictionaries.

For more information about how factoids affect recognition, see [Using Context to Improve Accuracy](using-context-to-improve-accuracy.md).

For more information about the **SystemDictionary** and **None** factoids, see [Supported Factoids from Version 1](supported-factoids-from-version-1.md).

 

 




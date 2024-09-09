---
description: To use an application dictionary with the Tablet PC API, you must first create a file with the list of words for your application dictionary.
ms.assetid: 6abadad1-262b-4536-8846-1c06226dc18a
title: Using Application Dictionaries with the Tablet PC Platform APIs
ms.topic: article
ms.date: 05/31/2018
---

# Using Application Dictionaries with the Tablet PC Platform APIs

To use an application dictionary with the Tablet PC API, you must first create a file with the list of words for your application dictionary.

The easiest solution for this is to use a text file that contains a list of the words. When your application loads, it reads the text file and creates a [**WordList**](inkwordlist-class.md) object from the list of words in the file. For each [**RecognizerContext**](inkrecognizercontext-class.md) associated with the application dictionary, set the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property of the **RecognizerContext** object to the word list in the text file.

The following example illustrates how to create a [**WordList**](inkwordlist-class.md) object from a [StringCollection](/dotnet/api/system.collections.specialized.stringcollection?view=netcore-3.1&preserve-view=true) collection. This example assumes that you have already loaded the list of words from disk and created a StringCollection collection from these words.


```C++
using System.Collections.Specialized;
using Microsoft.Ink;
//...
RecognizerContext theRecognizerContext;
StringCollection theUserDictionary;
//... 
// Initialize theRecognizerContext and theUserDictionary objects here.
//...
WordList theUserWordList = new WordList();
foreach (string s in theUserDictionary)
{
    theUserWordList.Add(s);
}
theRecognizerContext.WordList = theUserWordList;
```



> [!Note]  
> The [**Strokes**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_strokes) property of the [**RecognizerContext**](inkrecognizercontext-class.md) object must be empty before you set the [**WordList**](inkwordlist-class.md) property. If the [**Strokes**](/previous-versions/windows/desktop/legacy/ms703293(v=vs.85)) property is not empty, an exception is thrown. In addition, words should never be added to a word list after it has been assigned to a **RecognizerContext** object. Words that are added to the word list after it is assigned to the **RecognizerContext** object are not updated in the recognizer. To update the word list you must reassign the **WordList** object to the [**WordList**](/windows/desktop/api/msinkaut/nf-msinkaut-iinkrecognizercontext-get_wordlist) property of the **RecognizerContext** object.

 

For maximum recognition accuracy, combine factoids with your application dictionary in an advantageous relationship. For more information about the relationship between factoids and application dictionaries, see [Understanding Word Lists, Recognizer Context, and Factoids](understanding-wordlists--the-recognizercontext--and-factoids.md).

For an example of using application dictionaries with the [InkEdit](inkedit-control-reference.md) control, see [Using an Application Dictionary with InkEdit](using-an-application-dictionary-with-inkedit.md).

 

 

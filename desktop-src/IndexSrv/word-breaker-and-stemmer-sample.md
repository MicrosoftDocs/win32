---
title: Word Breaker and Stemmer Sample
description: Word Breaker and Stemmer Sample
ms.assetid: ba252bb4-18bf-4837-9c11-b4a2c76b9964
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Word Breaker and Stemmer Sample

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The lrsample sample includes an example [**IWordBreaker**](iwordbreaker.md) implementation, an example [**IStemmer**](istemmer.md) implementation, and the DLL entry points and exports for the component. The word breaker implementation parses Unicode text based on the occurrence of white space and punctuation. The stemmer implementation uses a small, static custom dictionary to look up and generate inflected forms for words. The sample words are English words and their inflected forms.

The language resource code sample is located in *mssdk*\\samples\\winbase\\indexing\\lrsample (where *mssdk* is the directory where the Platform SDK is installed).

**To build the sample**

1.  Set the Lib environment variable to *drive*:\\*mssdk*\\Lib;%Lib% and the Include environment variable to *drive*:\\*mssdk*\\Include;%Include% (where *drive* is the drive on which you installed the Platform SDK).
2.  Open a command prompt window, and then change the directory to the source path of the sample.
3.  At the command prompt, type **nmake** to build the language resource DLL.

**To register the sample**

1.  Copy the language resource DLL, the lrsample.dll file, to your installation directory (for example, *drive*:\\MyDLLs).
2.  At the command prompt, type **regsvr32.exe** *drive***:\\MyDLLs\\lrsample.dll** to self-register the filter.

The word breaker and stemmer are available when Indexing Service starts.

-   The word breaker is registered under class ID d225281a-7ca9-4a46-ae7d-c63a9d4815d4.
-   The stemmer is registered under class ID 0a275611-aa4d-4b39-8290-4baf77703f55.

    The class IDs for these and other word breakers and stemmers are located in the following registry location:

    hklm\\system\\currentcontrolset\\control\\contentindex\\language

    The samples are registered under the English language and the "English\_Sample" sublanguage.

### Programmer's Notes

The lrsample sample demonstrates the basic structure of a word breaker and stemmer. It minimally implements the methods of the [**IWordBreaker**](iwordbreaker.md) and [**IStemmer**](istemmer.md) interfaces.

The following table shows source files for the lrsample sample and provides a short description for each file.



| File         | Description                                                                                                                                                                                                                            |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lrsample.cxx | C++ source file that contains the [**IWordBreaker**](iwordbreaker.md) interface implementation (**CSampleWordBreaker**), the [**IStemmer**](istemmer.md) interface implementation (**CSampleStemmer**), and the DLL export functions |
| Lrsample.hxx | C++ header file that contains the class definitions for **CSampleWordBreaker**, **CSampleStemmer**, and **CLanguageResrouceSampleCF**, the class factory for the sample                                                                |
| Langreg.hxx  | C++ header file that contains utilities for registering language resources                                                                                                                                                             |
| Lrsample.def | Definition file that contains definitions for DLL export functions                                                                                                                                                                     |
| Minici.hxx   | C++ header file that contains utility functions for the sample                                                                                                                                                                         |



 

**CSampleWordBreaker** is the class implementation of the [**IWordBreaker**](iwordbreaker.md) interface. It implements a private method, **CSampleWordBreaker::Tokenize**, in addition to implementations for the public interface methods. **CSampleWordBreaker::BreakText** reads text from the text source, **TEXT\_SOURCE**, and calls the **Tokenize** method on the contents of the text buffer. **CSampleWordBreaker::Tokenize** breaks text based on the accuracy of white space and word separators for this locale, as determined by a call to **GetStringTypeW** in the Microsoft Win32 APIs. **CSampleWordBreaker::Tokenize** also removes punctuation and makes the appropriate calls methods of the **WordSink** object.

**CSampleStemmer** is the class implementation of the [**IStemmer**](istemmer.md) interface. **CSampleStemmer::GenerateWordForms** takes input words and generates alternative, inflected, word forms for that word based on the contents of a small, custom dictionary contained in the aStemForms\[\] array. This stemmer implementation does not perform any morphological analysis in determining inflected forms for a word. The aStemForms\[\] array contains English words and their inflected forms. You can modify the array for words and alternative forms for any other inflected language. The custom dictionary is implemented as a static array in this sample to illustrate basic stemmer functionality. You should not expand or use this dictionary implementation in a production environment.

### Error Handling

Error handling in the language resource sample is rudimentary. The sample handles only the most obvious error conditions. If you use the language resource as a basis for your own word breaker or stemmer, you must determine the additional error conditions that you must detect and handle.

 

 





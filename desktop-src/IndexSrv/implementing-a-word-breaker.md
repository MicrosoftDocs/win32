---
title: Implementing a Word Breaker
description: Implementing a Word Breaker
ms.assetid: c257db30-821a-44c0-8896-890090c9aedf
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing a Word Breaker

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Word breakers for Indexing Service implement the [**IWordBreaker**](iwordbreaker.md) interface. The [**BreakText**](iwordbreaker-breaktext.md) method performs all text processing and parsing. To implement a word breaker component, you must have language heuristics for your language. This includes information about syntax and morphology. You may also need a list of words to exclude or include. You build the file of noise words for your language locale from the list of excluded words. For more information about linguistic considerations and how these considerations affect word breaker implementations, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

The main function of the [**BreakText**](iwordbreaker-breaktext.md) method is to process text continuously from the [text source](text-source.md) until all the text is processed, or until the word breaker encounters an error. While in this data processing loop, the **BreakText** method calls parsing and utility methods that perform specific tasks for that process. For example, the German word breaker may handle compound words, whereas the French word breaker may process [diacritics](diacritics.md) or [clitics](clitics.md). The specific functions that the word breaker performs and the strategy that it employs in performing these tasks depend entirely on the requirements for that language.

When breaking text, word breakers identify "alternative" forms for words that may have multiple representations. No semantic relationship is implied between the generated words. In fact, the original word may not be included among the list of alternatives. The alternative forms are saved in the same position in the index as the original word to indicate that they are identical.

When a document is included in the index, each word is assigned an integer value that represents the *offset*, or the distance of the word from the beginning of a document. The relative distance between words in a query is compared against the offsets stored in the full-text index. The query "Where is Kyle's document" matches any document with "Where" at offset *n*, "is" at *n*+1, "Kyle's" at *n*+2, and "document" at *n*+3. "Where is Kyle's document filed in the data-base?" is represented as:



|                  |               |                                   |                     |                  |                |                |                                          |
|------------------|---------------|-----------------------------------|---------------------|------------------|----------------|----------------|------------------------------------------|
| Where<br/> | is<br/> | Kyle<br/> Kyle's<br/> | document<br/> | filed<br/> | in <br/> | the<br/> | database<br/> data base<br/> |



 

In this example, the word breaker stores alternative forms for "Kyle" ("Kyle's") and "database" ("data base") in the index. The word breaker generates and stores alternative words during the index creation process under the following conditions:

-   If an alternative word is likely to appear as a single word in a query
-   If a stemmer is not likely to derive the original word from the alternative

Generating alternative word forms increases the number of ways that queries represent and match a sentence:

1.  Where is Kyle document filed in the database
2.  Where is Kyle's document filed in the database
3.  Where is Kyle document filed in the data base
4.  Where is Kyle's document filed in the data base

### WordSink and PhraseSink

Word breakers use the [**WordSink**](iwordsink.md) and [**PhraseSink**](/windows/win32/Indexsrv/nn-indexsrv-iphrasesink?branch=master) objects to collect and store all words and phrases that they extract from text. A word breaker stores words in a form that is as close as possible to the original word form in the document. The **PhraseSink** stores phrases at query time. Phrases improve the relevance of query results because longer sequences of words are rarer and provide greater distinction than smaller phrases. When Indexing Service places a phrase in the **PhraseSink** at query time, it creates an instance of the word breaker to break the phrase into words. Indexing Service then evaluates the phrase by checking whether the words in the phrase occur adjacent to one another in the index. For example, if "ABCD" occurs in the index at positions *x*, *x*+1, *x*+2, and *x*+3, the phrase match will occur if any adjacent substring of "ABCD" is submitted in a query. This strategy is effective for character-based word breakers that split phrases and long words during index creation and that generate phrases during query time.

### Breaks

Breaks are the spaces between words. White space, punctuation, formatting, or just the nature of the language itself can cause breaks. There are four different types of breaks that Indexing Service uses: end of word (EOW), end of sentence (EOS), end of paragraph (EOP) and end of chapter (EOC). The EOW break is the default break. After each token, each break indicates a different semantic distance between the words on either side. Words separated by EOW have the tightest semantic link, followed by EOS, EOP, and EOC. Multiple calls to [**PutBreak**](iwordsink-putbreak.md) are cumulative, and are analogous to inserting null words or sentences.

### Scalability

The way the word breaker responds to simultaneous calls is largely determined by your choice of threading model. Indexing Service is a single-threaded application. For word breakers to work in a single-threaded environment, word breakers must be written using a "free" or "both" threading model. Word breakers must not register with COM by using the "apartment" threading model.

It is recommended that word breakers avoid global states and store data in the instance for the word breaker. The only content that should be stored in the word breaker implementation is the query flag, *fQuery*, and *MaxTokenSize*.

### Performance

Word breakers should be no more than two times slower than the benchmark established by the English word breaker. The English word breaker currently breaks approximately 1.1 million characters per second on a computer with the following hardware specifications:

-   Single processor
-   Pentium III, 400 megahertz (MHz)
-   256 megabytes (MB) of RAM

Word breaker performance should also improve with increased hardware capability.

### Security

Word breakers for Indexing Service run in the Local System security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer. Word breakers cannot assume that the text passed to the [**BreakText**](iwordbreaker-breaktext.md) method is well formed.

For more information about troubleshooting word breakers, see [Troubleshooting Language Resources](troubleshooting-language-resources.md).

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> <dt>

[Troubleshooting Language Resources](troubleshooting-language-resources.md)
</dt> </dl>

 

 






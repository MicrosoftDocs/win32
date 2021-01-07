---
description: Microsoft provides word breakers and stemmers for a number of languages. This topic describes how to implement, and use custom word breakers and stemmers for languages, and locales beyond those provided by Microsoft.
ms.assetid: 47768691-7071-440e-bfbf-975713880c00
title: Implementing a Word Breaker and Stemmer
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a Word Breaker and Stemmer

Microsoft provides word breakers and stemmers for a number of languages. This topic describes how to implement, and use custom word breakers and stemmers for languages, and locales beyond those provided by Microsoft.

> [!Note]
> As of July 2018 a security change was made to Windows Server 2019 that prevents DLLs without a Microsoft signature from being loaded by SearchIndexer.exe. As a result Windows Server 2019 no longer supports non-Microsoft signed custom word breakers. 

This topic is organized as follows:

-   [Registering a Language Resource DLL](#registering-a-language-resource-dll)
-   [Registering a Language](#registering-a-language-resource-dll)
-   [Implementing a Word Beaker](#implementing-a-word-beaker)
    -   [WordSink and PhraseSink](#wordsink-and-phrasesink)
    -   [Breaks](#breaks)
    -   [Scalability, Performancy, and Security](#scalability-performancy-and-security)
-   [Implementing a Stemmer](#implementing-a-stemmer)
    -   [Scalability, Performancy, and Security](#scalability-performancy-and-security)
-   [Related topics](#related-topics)

## Registering a Language Resource DLL

Each language resource DLL must implement and export the following entry points. The DLL can be registered to be in any folder.

-   DllMain is the standard entry point to DLL.
-   DllRegisterServer registers the DLL in the registry, such as `regsvr32.exe %SystemRoot%\MyFolder\wordbreaker.dll`
-   DllCanUnloadNow enables clients to call this entry point through Component Object Model (COM) to determine whether it is possible to unload the language resource DLL.
-   DllUnRegisterServer removes the DLL from the registry.

## Registering a Language

The registry contains language-specific entries for the language being indexed, and these entries control the parts of the indexing and query processes that are language specific. These registry entries can be found under the following registry key.

```
HKEY_LOCAL_MACHINE
   SYSTEM
      CurrentControlSet
         ContentIndex
            Control
               Language
                  
```

## Implementing a Word Beaker

Word breakers implement [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker). The [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) method performs all text processing and parsing. To implement a word breaker component, you must have language heuristics for your language. This includes information about syntax and morphology. You may also need a list of words to exclude or include. You build the file of noise words for your language locale from the list of excluded words. For more information about linguistic considerations and how these considerations affect word breaker implementations, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

The main purpose of [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) is to process text continuously from the [**TEXT\_SOURCE**](/windows/win32/api/indexsrv/ns-indexsrv-text_source) until all the text is processed, or until the word breaker encounters an error. While in this data processing loop, **IWordBreaker::BreakText** calls parsing and utility methods that perform specific tasks for that process. For example, the German word breaker may handle compound words, whereas the French word breaker may process [diacritics](surface-form-normalization.md) or [clitics](surface-form-normalization.md). The specific functions that the word breaker performs and the strategy that it uses in performing these tasks depend entirely on the requirements for that language.

When breaking text, word breakers identify "alternative" forms for words that may have multiple representations. No semantic relationship is implied between the generated words. In fact, the original word may not be included among the list of alternatives. The alternative forms are saved in the same position in the index as the original word to indicate that they are identical.

When a document is included in the index, each word is assigned an integer value that represents the offset, or the distance of the word from the beginning of a document. The relative distance between words in a query is compared against the offsets stored in the full-text index. The query "Where is Kyle's document" matches any document with "Where" at offset n, "is" at n+1, "Kyle's" at n+2, and "document" at n+3. "Where is Kyle's document filed in the data-base?" is represented as:



|       |     |                        |          |       |     |     |                               |
|-------|-----|------------------------|----------|-------|-----|-----|-------------------------------|
| Where | is  | Kyle Kyle's<br/> | document | filed | in  | the | database data base<br/> |



 

In this example, the word breaker stores alternative forms for "Kyle" ("Kyle's") and "database" ("data base") in the index. The word breaker generates and stores alternative words during the index creation process under the following conditions:

-   If an alternative word is likely to appear as a single word in a query
-   If a stemmer is not likely to derive the original word from the alternative

Generating alternative word forms increases the number of ways that queries represent and match a sentence, as shown in the following variations:

1.  Where is Kyle document filed in the database
2.  Where is Kyle's document filed in the database
3.  Where is Kyle document filed in the data base
4.  Where is Kyle's document filed in the data base

### WordSink and PhraseSink

Word breakers use the [**IWordSink**](iwordsink.md) and [**IPhraseSink**](/windows/win32/api/indexsrv/nn-indexsrv-iphrasesink) objects to collect and store all words and phrases that they extract from text. A word breaker stores words in a form that is as close as possible to the original word form in the document. **IPhraseSink** stores phrases at query time. Phrases improve the relevance of query results because longer sequences of words are rarer and provide greater distinction than smaller phrases. When the indexer places a phrase in the **IPhraseSink** at query time, it creates an instance of the word breaker to break the phrase into words. The indexer then evaluates the phrase by checking whether the words in the phrase occur adjacent to one another in the index. For example, if "ABCD" occurs in the index at positions *x*, *x*+1, *x*+2, and *x*+3, the phrase match will occur if any adjacent substring of "ABCD" is submitted in a query. This strategy is effective for character-based word breakers that split phrases and long words during index creation and that generate phrases during query time.

### Breaks

Breaks are the spaces between words. White space, punctuation, formatting, or just the nature of the language itself can cause breaks. There are four different types of breaks that the indexer uses: end of word (EOW), end of sentence (EOS), end of paragraph (EOP) and end of chapter (EOC). The EOW break is the default break. After each token, each break indicates a different semantic distance between the words on either side. Words separated by EOW have the tightest semantic link, followed by EOS, EOP, and EOC. Multiple calls to [**IWordSink::PutBreak**](iwordsink-putbreak.md) are cumulative, and are analogous to inserting null words or sentences.

### Scalability, Performancy, and Security

The way the word breaker responds to simultaneous calls is largely determined by your choice of threading model. The indexer is a single-threaded application. For word breakers to work in a single-threaded environment, word breakers must be written using a "free" or "both" threading model. Word breakers must not register with COM by using the "apartment" threading model.

We recommend that word breakers avoid global states and store data in the instance for the word breaker. The only content that should be stored in the word breaker implementation are for the parameters *fQuery* and *ulMaxTokenSize*. Word breakers should be no more than two times slower than the benchmark established by the English word breaker. Word breaker performance should also improve with increased hardware capability.

Word breakers for the indexer run in the Local System security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer. Word breakers cannot assume that the text passed to the [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) method is well formed. For more information about troubleshooting word breakers, see [Troubleshooting Language Resources and Best Practices](troubleshooting-language-resources.md).

## Implementing a Stemmer

Stemmers implement the [**IStemmer**](/windows/desktop/api/Indexsrv/nn-indexsrv-istemmer) interface. The [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) method generates a list of inflected word forms for a particular input word. To implement a stemmer component, you must have language heuristics for your language. This includes information about morphology. You may also need a list of words to exclude or include. For more information about linguistic considerations and how these considerations affect stemmer implementations, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

We recommend that stemmers should not generate the genitive, or possessive, case for words. For example, "David" is not generated as an alternative form for "David's." The word breaker generates both "David" and "David's" when it parses "David's."

The stemmer uses the [IWordFormSink](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordformsink) object to gather the list of alternative words. [**IWordFormSink::PutWord**](iwordformsink-putword.md) generates the final word from the stemmer. In all cases, this final word is the same as the input word from [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms). For example, given the word "swim," the stemmer generates the following word forms: "swimming," "swimmer," "swims," "swam," and "swum," through calls to [**IWordFormSink::PutAltWord**](iwordformsink-putphrase.md). The stemmer generates "swim" through **IWordFormSink::PutWord**.

### Scalability, Performancy, and Security

Stemmers, like word breakers, must use a "free" threading model and register with COM with their threading model set to "free" or "both." Windows Search calls separate instances of the stemmer from different threads at the same time. Stemmers should therefore have minimal instance data.

Stemmer accuracy has a significant impact on query relevance. If the stemmer stems the text incorrectly, queries may return unpredictable and inaccurate results. Stemmers must handle hundreds of queries per second without negatively affecting query performance. Stemmer performance should improve with increased hardware capability. For information about troubleshooting stemmers, see [Troubleshooting Language Resources and Best Practices](troubleshooting-language-resources.md).

Stemmers for Windows Search run in the Local Security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer.

## Related topics

<dl> <dt>

[Extending Language Resources](extending-language-resources-in-windows-search.md)
</dt> <dt>

[Understanding Language Resource Components](understanding-language-resource-components.md)
</dt> <dt>

[Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md)
</dt> <dt>

[Troubleshooting Language Resources and Best Practices](troubleshooting-language-resources.md)
</dt> </dl>

 

 

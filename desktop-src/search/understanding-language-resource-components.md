---
description: Language resources consist of word breakers and stemmers that extend index building and querying capabilities to new languages and locales.
ms.assetid: 7963805e-e279-42cf-ba95-f81a7de8e68e
title: Understanding Language Resource Components
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Language Resource Components

Language resources consist of word breakers and stemmers that extend index building and querying capabilities to new languages and locales. Word breakers are used during both index creation and querying. Stemmers are used only for querying. Windows Search uses language resource DLLs to bind to [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker) and [**IStemmer**](/windows/desktop/api/Indexsrv/nn-indexsrv-istemmer) implementations for a specific language locale.

This topic is organized as follows:

-   [About Language Resources](#about-language-resources)
-   [Word Breaking](#word-breaking)
-   [Stemming](#stemming)
-   [Normalization](#normalization)
-   [Noise Words](#noise-words)
-   [Related topics](#related-topics)

## About Language Resources

Windows Search uses a filter (an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface) and [**ILoadFilter**](/windows/desktop/api/filtereg/nn-filtereg-iloadfilter) to access a document in its native format. The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) component extracts text content, properties, and formatting from the document. The [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) identifies the locale of the document that it is filtering. The indexing component invokes the appropriate word breaker for that locale. If none is available, the indexing component invokes the neutral word breaker. The word breaker receives, from an [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter), an input stream of Unicode characters that the word breaker parses to produce individual words and phrases. The word breaker also normalizes date and time formats. The indexer normalizes the words produced by the word breaker by converting the words to all uppercase letters. The indexer saves the uppercase words to the full-text index, with the exception of noise words identified for that locale.

The following table lists the actions and corresponding results for the sentence "Figure 1 illustrates the role of language resources for Windows Search during the index creation process."



| Action                  | Resulting text                                                                                                               |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------|
| Original text           | Figure 1 illustrates the role of language resources for Windows Search during the index creation process.                    |
| Filtering               | Figure 1 illustrates the role of language resources for Windows Search during the index creation process.                    |
| Word breaking           | Figure, 1, illustrates, the, role, of, language, resources, for, Windows, Search, during, the, index, creation, process, EOS |
| Normalization           | FIGURE, 1, ILLUSTRATES, THE, ROLE, OF, LANGUAGE, RESOURCES, WINDOWS, SEARCH, DURING, THE, INDEX, CREATION, PROCESS           |
| Noise word removal      | FIGURE, ILLUSTRATES, ROLE, LANGUAGE, RESOURCES, WINDOWS, SEARCH, DURING, INDEX, CREATION, PROCESS                            |
| Save to full-text index | FIGURE, ILLUSTRATES, ROLE, LANGUAGE, RESOURCES, WINDOWS, SEARCH, DURING, INDEX, CREATION, PROCESS                            |



 

Word breakers and stemmers are used to expand [FREETEXT](-search-sql-freetext.md) queries at query time. The locale of the query is the default locale unless a language code identifier (LCID) is passed as a query parameter. The query component invokes the appropriate word breaker on the query terms listed in the [WHERE](-search-sql-where.md) clause of the query. For example, if the WHERE clause of the query contains "FREETEXT (apples, oranges, and pears)," the word breaker receives the text, "apples, oranges, and pears." If the query WHERE clause uses the [CONTAINS](-search-sql-contains.md) full-text predicate, the text output from the word breaker is normalized. Otherwise, the query component passes each word identified by the word breaker to the appropriate stemmer for that language and locale. The stemmer generates a list of alternative, or inflected, forms for that word. The query component normalizes the expanded list of query terms and removes noise words.

The following table lists the actions and corresponding results for the query "apples, oranges, and pears."



| Action                       | Resulting text                                            |
|------------------------------|-----------------------------------------------------------|
| Original text                | apples, oranges, and pears                                |
| Word breaking                | apples, oranges, and, pears, EOS                          |
| Stemming                     | apple, apples, orange, orangey, oranges, and, pear, pears |
| Normalization                | APPLE, APPLES, ORANGE, ORANGEY, ORANGES, AND, PEAR, PEARS |
| Noise word removal           | APPLE, APPLES, ORANGE, ORANGEY, ORANGES, PEAR, PEARS      |
| Expanded list of query terms | APPLE, APPLES, ORANGE, ORANGEY, ORANGES, PEAR, PEARS      |



 

The expanded query terms increase the likelihood that the query will find documents that match the intent of the original query. Text that the word breaker or stemmer generates at query time is not stored on disk.

## Word Breaking

Word breaking is the separation of text into individual text tokens, or words. Many languages, especially those with Roman alphabets, have an array of word separators (such as white space) and punctuation that are used to discern words, phrases, and sentences. Word breakers must rely on accurate language heuristics to provide reliable and accurate results. Word breaking is more complex for character-based systems of writing or script-based alphabets, where the meaning of individual characters is determined from context. For more information about linguistic considerations that may affect your word breaker implementation, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

## Stemming

Windows Search applies stemmers exclusively at query time to generate additional word forms for terms in [FREETEXT](-search-sql-freetext.md) and property queries. Stemmers perform morphological analysis and apply grammatical rules to generate a list of alternative, or inflected, forms for words. Alternative forms often have the same stem or base form. By generating the inflected forms for a word, Indexing Service returns query results that are statistically more relevant to a query. For example, a full-text query for "swim meet" matches documents that contain "swim, swim's, swims, swims', swimming, swam, swum" or "meet, meet's, meets, meets', meeting, met" and combinations of these terms.

Some languages require that inflected terms be generated at both index time and query time for both standard and variant inflections. In this case, stemming happens in the word breaker component, with minimal stemming work in the actual stemmer. For example, the Japanese word breaker performs stemming during both index creation and querying to enable a query to find different inflected forms of the search terms.

## Normalization

Documents of all languages are stored in a single index. Although words and linguistic rules differ dramatically, there are some considerations, such as numbers, dates, and times, that are handled consistently across all word breakers. For more information about normalization considerations that may affect your word breaker implementation, see [Surface Form Normalization](surface-form-normalization.md).

## Noise Words

Noise words, also known as stop words, are words that are not significant indicators for content. Indexing Service removes noise words from query terms and from content that is included in the full-text index. An *offset* is the occurrence of a word in a document or in a list of query terms. The offset of noise words in a document or query is recorded as blank. Removing noise words improves query performance by avoiding unnecessary index growth. It also improves the relevance of query results. You can configure Windows Search to use noise word lists for specific languages. These lists are used when a word breaker is invoked for that language. For example, "the" in the English language occurs so often that it has little value as a unique key. "The" is in the noise word list, is not written to the content index, and, if queried for, returns no results.

Noise words act as placeholders in phrase queries. A document that contains the text "wag the dog" is stored in the index with "wag" at occurrence 1 and "dog" at occurrence 3. The phrase query "wag dog" does not match, but the phrase query "wag a dog" does, because the occurrence information matches. The phrase "wag purple dog" does not match because "purple" is not found in the index at occurrence 2. However, a query for "wag the dog" returns documents that contain "wag purple dog" because there is no way to efficiently determine whether the document had a non-noise word between "wag" and "dog."

## Related topics

<dl> <dt>

[Extending Language Resources](extending-language-resources-in-windows-search.md)
</dt> <dt>

[Implementing a Word Breaker and Stemmer](implementing-a-word-breaker-and-stemmer.md)
</dt> <dt>

[Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md)
</dt> <dt>

[Troubleshooting Language Resources and Best Practices](troubleshooting-language-resources.md)
</dt> </dl>

 

 

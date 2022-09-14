---
description: This topic describes stemming considerations for agglutinative languages and Unicode surrogate pairs, and for using surrogate pairs to extend the Unicode character set to accommodate different character sets.
ms.assetid: 7104b2da-2ece-46ce-b4ca-6c24dc4d6677
title: Miscellaneous Linguistic and Unicode Considerations
ms.topic: article
ms.date: 05/31/2018
---

# Miscellaneous Linguistic and Unicode Considerations

This topic describes stemming considerations for agglutinative languages and Unicode surrogate pairs, and for using surrogate pairs to extend the Unicode character set to accommodate different character sets. This topic also describes how word breakers identify phrases in text and handle nonbreaking spaces, and how word breakers and stemmers handle numbers and dates, compound words, compound phrases, special words and characters, acronyms and abbreviations, and capitalization.

This topic is organized as follows:

-   [Phrase Identification](#phrase-identification)
-   [Agglutinative Languages](#agglutinative-languages)
-   [Numbers, Times, and Dates](#numbers-times-and-dates)
-   [Compound Words](#compound-words)
-   [Compound Phrases](#compound-phrases)
-   [Special Characters and Words](#special-characters-and-words)
-   [Acronyms and Abbreviations](#acronyms-and-abbreviations)
-   [Capitalization](#capitalization)
-   [Nonbreaking Spaces](#nonbreaking-spaces)
-   [Surrogate Pairs](#surrogate-pairs)

## Phrase Identification

Phrases are a word or a group of words that are modified by one or more others. Phrases are difficult to identify consistently because the same modifier may be used in more than one phrase with the same noun. For example, "new house," "House of Parliament," "new House of Parliament."

Windows Search uses phrases most often at query time. Phrases in query text receive higher weight than individual words. From the previous example, a document containing "House of Parliament" is ranked higher than one containing "House" and "Parliament" at different points in the document. We recommend that word breakers generate a phrase at query time if the phrase is likely to match at least one document.

## Agglutinative Languages

Agglutinative languages form words through the combination of smaller morphemes to express compound ideas. Each of these morphemes generally has one meaning or function and retains its original form and meaning during the combination process. For languages that have agglutinative morphology, such as Turkish, Finnish, Hungarian, or Korean, it is possible to produce thousands of forms for a given root word.

The following table shows a list of inflected forms for the Finnish word "talo" ("house").



| Word      | Translation   |
|-----------|---------------|
| Talo      | House         |
| Taloni    | My house      |
| Talossa   | In the house  |
| Talossani | In my house   |
| Taloja    | Houses        |
| Taloissa  | In the houses |



 

Inflected languages, such as English, French, and Latin, have a very small number of possible word forms for one root word. In inflected languages, morphemes influence one another when binding. Most changes in inflection are present in the stem or word ending. In contrast to agglutinative languages, inflected languages tend to have different functions for a single morpheme. For example, a morpheme can determine both number and case.

Stemmers for agglutinative languages must weigh the trade-off between performance and accuracy to generate only a subset of the number of possible word forms.

## Numbers, Times, and Dates

Word breakers must use a common format for representing numbers, times, and dates to facilitate consistent querying.

When you create a word breaker, we recommend that the word breaker normalize numbers to a canonical representation by using the pattern "NN*dd*D*cc*", where NN is the literal sequence "NN", *dd* is the integer portion of the number, D is the literal "D", and *cc* is the fractional portion of the number. Word breakers do not restrict the number of digits for either the integer or the fraction portion of the number. We recommend that word breakers recognize numerical patterns that are delimited by both periods (.) and commas (,). For example, Windows Search represents both "1,000.2" and "1.000,2" as "NN1000D2."

Choose one format for both word breaker and stemmer. Single-byte Arabic numerals are normalized such that a query containing any of these forms matches documents with the other forms.

When you create a word breaker, we recommend that the word breaker present all times as a 24-hour representation using the pattern "TT*hhmmss*," where TT is the literal prefix "TT", *hh* is the hours, *mm* is the minutes, and *ss* is the seconds. Windows Search does not match additional units of time, such as milliseconds. Parsing A.M. and P.M. patterns is optional.

When you create a word breaker, we recommend that the word breaker generate dates in the canonical format of "DD*yyyymmdd*", where DD is the literal "DD", *yyyy* is the years, *mm* is the months, and *dd* is the days. We also recommend that word breakers store two-digit years in both twentieth-century and twenty-first-century formats. For example, word breakers represent "2.2.99" as "DD19990202" and "DD20990202". At query time, Windows Search derives the date by using Windows application programming interfaces (APIs) to determine the crossover date for the server to display the correct format, 19*XX* or 20*XX*.

## Compound Words

In some languages, such as German, nouns are compounded from simpler nouns. These compound nouns are too specific in meaning for reasonable query recall. For example, without decomposition, a query for "Versicherung" ("insurance") does not match "Lebensversicherungsgesellschaft" ("life-insurance salesman"). In cases such as this, we recommend that word breakers break these compound words into base components during both index creation and query time. The German word breaker breaks "Lebensversicherungsgesellschaft" into the component words "Leben," "Versicherung," and "Gesellschaft." It applies the same decomposition at query time, along with optional stemming for each of the resultant terms.

## Compound Phrases

Some languages, such as Korean, contain complex phrases that can be broken in a number of different ways. A Korean phrase consists of *content words*, such as nouns, pronouns, verbs, and adjectives, followed by *functional words*. Functional words are found in post-positions and endings. Post-positions indicate the functional role of the noun or pronoun in a sentence; endings indicate the functional role of the verb or adjective.

One phrase can have the several analyses, and each analysis can consist of several content words. The word breaker must employ language-specific heuristics to determine, from context, how much weight to give to different analyses. The word breaker may determine which decomposition to use based on the number of resulting component words. Some word breakers may favor short sequences of longer terms, whereas other word breakers may favor long sequences of smaller words.

Another consideration is that in Korean, nouns and pronouns can be the stored in the index without their corresponding functional words. Korean is an agglutinative language and combines numerous word endings with verbs and adjectives to form countless inflected forms. Verbs and adjectives identified in phrases are saved with their endings in the index, but the word breaker does not generate new forms.

## Special Characters and Words

Special characters are characters such as "," "©," and "™". These characters are rarely used in queries. Word breakers should strip special characters during index creation and at query time.

We recommend that word breakers recognize special words, such as "C++," "C\#," ".NET," grades, and musical notation. Word breakers can use a language heuristic to identify a pattern for special words. Word breakers can also use a custom dictionary that contains recognized special words.

## Acronyms and Abbreviations

Acronyms and abbreviations must be considered when you implement a word breaker. In many languages, individual letters of acronyms are separated by periods. Occasionally, words that are not recognized acronyms or abbreviations are abbreviated. For example, "United States of America" may be abbreviated as either "USA" or "U.S.A." Word breakers included with Windows Search usually identify single-letter words as noise words and treat those words as placeholders during query time. During query time, a word breaker that is not aware of common acronyms, or that does not recognize abbreviations, converts the abbreviation "U.S.A." into "U", "S", and "A". This decomposition does not provide enough information to match words in the full-text index because all the query terms are noise words. When you create a word breaker, we recommend that the word breaker remove the periods that separate the letters of acronyms. In the example, "U.S.A." is stored as "USA" and a query term that contains "U.S.A." actually queries for "USA." If a word breaker processes an abbreviation, the period in that abbreviation is not treated as an EOS break. Because of this, a word breaker might not correctly identify an EOS break if the abbreviation is at the end of the sentence.

## Capitalization

Windows Search does not currently preserve capitalization when it saves words to the full-text index. Word breakers and stemmers should not modify the case for words.

## Nonbreaking Spaces

When you create a word breaker, we recommend that you ensure that the word breaker treats nonbreaking spaces as word separators. It is also recommended that the word breaker generate alternative forms of the word, with and without nonbreaking spaces. Some characters, such as underscores, are special characters that are treated as nonbreaking characters because of the sources of the text in which they are found. For example, source code or file names may include underscores as nonbreaking characters.

## Surrogate Pairs

Surrogate pairs are character representations in source code that represent a single character that consists of a sequence of two Unicode values. In a coded pair, the first value is a high surrogate and the second is a low surrogate. A high surrogate is a character in the range U+D800 through U+DBFF. A low surrogate is a character in the range U+DC00 through U+DFFF. Surrogate pairs extend the character set beyond the Unicode character. We recommend that a word breaker should use the following rules when handling surrogate pairs:

-   A high surrogate must precede a low surrogate.
-   A low surrogate must follow a high surrogate.
-   A high or low surrogate without a corresponding value for its other half has no meaning.

Word breakers must consider any pairs and generate the pairs as such in the index. For more information, see [Surrogates and Supplementary Characters](/windows/desktop/Intl/surrogates-and-supplementary-characters).

 

 

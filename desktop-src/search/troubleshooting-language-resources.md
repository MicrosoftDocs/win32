---
description: This topic provides best practices and suggestions for validating and troubleshooting your IWordBreaker and IStemmer implementations.
ms.assetid: b0e199b9-8d81-4445-92f7-de9b8a00a9cb
title: Troubleshooting Language Resources and Best Practices
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Language Resources and Best Practices

This topic provides best practices and suggestions for validating and troubleshooting your [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker) and [**IStemmer**](/windows/desktop/api/Indexsrv/nn-indexsrv-istemmer) implementations.

This topic is organized as follows:

-   [Best Practices](#best-practices)
-   [Testing Stemmer Consistency](#testing-stemmer-consistency)
-   [Testing for Invalid Input in the Stemmer](#testing-for-invalid-input-in-the-stemmer)
-   [Testing Word Breaker Consistency](#testing-word-breaker-consistency)
-   [Testing for Invalid Input in the Word Breaker](#testing-for-invalid-input-in-the-word-breaker)

### Best Practices

-   Ensure that the threading model for language resources is set to "both" in the registry.
-   Where possible, put language data in a resource in your DLL rather than in a separate file. This makes the DLL easier to install and more secure. Additionally, putting language data in a resource will result in improved performance for that language resource component.
-   Minimize the system resources that language resource components use. For example, if each instance of a language resource object needs read-only access to a lexicon, consider sharing the lexicon across all instances.
-   Consider using the neutral word breaker to handle text that is not in the language or locale for your word breaker implementation. This will help ensure that text is processed consistently across all languages.
-   Check all return codes and return them from functions like [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) and [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext). If indexing fails, it is important to pass the error so that the user is notified which documents were indexed.

### Testing Stemmer Consistency

We recommend that you monitor the performance of an [**IStemmer**](/windows/desktop/api/Indexsrv/nn-indexsrv-istemmer) implementation for consistency under the following conditions:

-   The stemmer performs consistently across multiple calls to [**IStemmer::Init**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-init). The stemmer reinitializes with the same parameters as in the previous initialization, without releasing the parameters.
-   Given the same test corpus, and repetitions of the same query, [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) produces the identical output and makes identical calls to the methods of the [**IWordFormSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordformsink) object.

### Testing for Invalid Input in the Stemmer

We recommend that you monitor how the [**IStemmer**](/windows/desktop/api/Indexsrv/nn-indexsrv-istemmer) methods handle all errors related to invalid parameters. In addition, we recommend that you ensure that the stemmer methods do not raise unhandled exceptions. The stemmer should handle the following errors:

-   Call to [**IStemmer::Init**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-init) with *pfLicense* set to **NULL**. Init fails and does not result in an access violation.
-   Call to [**IStemmer::GetLicenseToUse**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-getlicensetouse) with the *ppwcsLicense* parameter set to **NULL**. **IStemmer::GetLicenseToUse** does not result in an access violation.
-   Call to [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) with the *pwcInBuf* parameter set to **NULL**. **IStemmer::GenerateWordForms** fails (returns E\_FAIL) and does not result in an access violation.
-   Call to [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) with the *cwc* parameter equal to 0. **IStemmer::GenerateWordForms** returns successfully (returns S\_OK) and does not result in an access violation.
-   Call to [**IStemmer::GenerateWordForms**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-generatewordforms) with the *pwcInBuf* parameter set to **NULL** and the *cwc* parameter equal to 0. **IStemmer::GenerateWordForms** fails (returns E\_FAIL) and does not result in an access violation.

### Testing Word Breaker Consistency

We recommend that you ensure that the [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker) implementation performs consistently under the following conditions:

-   Word breaker performs consistently across multiple calls to its [**IWordBreaker::Init**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-init) method. The word breaker reinitializes with the same parameters as in the previous initialization, without releasing the parameters.
-   Given the same test corpus, and repetitions of the same query, the [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) method produces the identical output and makes identical calls to the methods of the [**IWordSink**](iwordsink.md) and [**IPhraseSink**](/windows/win32/api/indexsrv/nn-indexsrv-iphrasesink) objects.

### Testing for Invalid Input in the Word Breaker

We recommend that you ensure that the [**IWordBreaker**](/windows/desktop/api/Indexsrv/nn-indexsrv-iwordbreaker) methods handle all errors related to invalid parameters. In addition, we recommend that you ensure that the word breaker methods do not raise unhandled exceptions. The word breaker should perform the following functions and handle the following errors:

-   Call to [**IWordBreaker::Init**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-init) must return either LANGUAGE\_E\_DATABASE\_NOT\_FOUND or S\_OK.
-   Call to [**IWordBreaker::Init**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-init) successfully initializes the *pfLicense* parameter to **FALSE** and calls [**IStemmer::GetLicenseToUse**](/windows/desktop/api/Indexsrv/nf-indexsrv-istemmer-getlicensetouse) and does not result in an access violation.
-   Word breaker does not read past the end of the *awcBuffer* parameter in the [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) method.
-   Call to [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) with the *pwcInBuf* set to **NULL**. **IWordBreaker::BreakText** fails (returns E\_FAIL) and does not result in an access violation.
-   Call to [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) with the *cwc* parameter equal to 0. **IWordBreaker::BreakText** returns successfully (returns S\_OK) and does not result in an access violation.
-   Call to the [**IWordBreaker::BreakText**](/windows/desktop/api/Indexsrv/nf-indexsrv-iwordbreaker-breaktext) method with the *pwcInBuf* parameter set to **NULL** and the *cwc* parameter equal to 0. **IWordBreaker::BreakText** fails (returns E\_FAIL) and does not result in an access violation.
-   Phrases generated during index creation contain the same number of words.
-   Phrases are generated during index creation through successive calls to the [**IWordFormSink::PutWord**](iwordsink-putword.md) and [**IWordFormSink::PutAltWord**](iwordsink-putaltword.md) methods. The word breaker uses only the [**IPhraseSink**](/windows/win32/api/indexsrv/nn-indexsrv-iphrasesink) object during query time.

## Related topics

<dl> <dt>

[Extending Language Resources](extending-language-resources-in-windows-search.md)
</dt> <dt>

[Understanding Language Resource Components](understanding-language-resource-components.md)
</dt> <dt>

[Implementing a Word Breaker and Stemmer](implementing-a-word-breaker-and-stemmer.md)
</dt> <dt>

[Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md)
</dt> </dl>

 

 

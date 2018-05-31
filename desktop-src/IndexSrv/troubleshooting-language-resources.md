---
title: Troubleshooting Language Resources
description: Troubleshooting Language Resources
ms.assetid: 7d6bf4c6-e0b2-4e9b-a5aa-06b1f617127d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting Language Resources

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section contains tips and suggestions to help you validate your [**IStemmer**](istemmer.md) and [**IWordBreaker**](iwordbreaker.md) implementations and ensure that they meet the requirements for Indexing Service.

-   [General Recommendations](#general-recommendations)
-   [Testing Stemmer Consistency](#testing-stemmer-consistency)
-   [Testing for Invalid Input in the Stemmer](#testing-for-invalid-input-in-the-stemmer)
-   [Testing Word Breaker Consistency](#testing-word-breaker-consistency)
-   [Testing for Invalid Input in the Word Breaker](#testing-for-invalid-input-in-the-word-breaker)

### General Recommendations

-   Ensure that the threading model for language resources is set to "both" in the registry.
-   Where possible, put language data in a resource in your DLL rather than in a separate file. This makes the DLL easier to install and make secure. Additionally, putting language data in a resource will result in improved performance for that language resource component.
-   Minimize the system resources that language resource components use. For example, if each instance of a language resource objects needs read-only access to a lexicon, consider sharing the lexicon across all instances.
-   Consider using the neutral word breaker to handle text that is not in the language or locale for your word breaker implementation. This will help ensure that text is processed consistently across all languages. The [Word Breaker and Stemmer Sample](word-breaker-and-stemmer-sample.md) provides a sample implementation of a language neutral word breaker.
-   Check all return codes and return them from functions like [**GenerateWordForms**](istemmer-generatewordforms.md) and [**BreakText**](iwordbreaker-breaktext.md). If indexing fails it is important to pass the error so the user is notified as to which documents were indexed.

### Testing Stemmer Consistency

It is recommended that you monitor the performance of an [**IStemmer**](istemmer.md) implementation for consistency under the following conditions:

-   The stemmer performs consistently across multiple calls to its [**Init**](istemmer-init.md) method. The stemmer reinitializes with the same parameters as in the previous initialization, without releasing the parameters.
-   Given the same test corpus, and repetitions of the same query, the [**GenerateWordForms**](istemmer-generatewordforms.md) method produces the identical output and makes identical calls to the methods of the [**WordFormSink**](iwordformsink.md) object.

### Testing for Invalid Input in the Stemmer

It is recommended that you monitor how the [**IStemmer**](istemmer.md) methods handle all errors related to invalid parameters. In addition, it is recommended that you ensure that the stemmer methods do not raise nonhandled exceptions. The stemmer should handle the following errors:

-   Call to the [**Init**](istemmer-init.md) method with *pfLicense* set to **NULL**. **Init** fails and does not result in an access violation.
-   Call to the [**GetLicenseToUse**](istemmer-getlicensetouse.md) method with the *\*\*ppwcsLicense* parameter set to **NULL**. **GetLicenseToUse** does not result in an access violation.
-   Call to the [**GenerateWordForms**](istemmer-generatewordforms.md) method with the *pwcInBuf* set to **NULL**. **GenerateWordForms** fails (return E\_FAIL) and does not result in an access violation.
-   Call to the [**GenerateWordForms**](istemmer-generatewordforms.md) method with the *cwc* equal to 0. **GenerateWordForms** returns successfully (return S\_OK) and does not result in an access violation.
-   Call to the [**GenerateWordForms**](istemmer-generatewordforms.md) method with the *pwcInBuf* set to **NULL** and the *cwc* equal to 0. **GenerateWordForms** fails (return E\_FAIL) and does not result in an access violation.

### Testing Word Breaker Consistency

It is recommended that you ensure that the [**IWordBreaker**](iwordbreaker.md) implementation performs consistently under the following conditions:

-   Word breaker performs consistently across multiple calls to its [**Init**](iwordbreaker-init.md) method. The word breaker reinitializes with the same parameters as in the previous initialization, without releasing the parameters.
-   Given the same test corpus, and repetitions of the same query, the [**IWordBreaker::BreakText**](iwordbreaker-breaktext.md) method produces the identical output and makes identical calls to the methods of the [**WordSink**](iwordsink.md) and [**PhraseSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iphrasesink) objects.

### Testing for Invalid Input in the Word Breaker

It is recommended that you ensure that the [**IWordBreaker**](iwordbreaker.md) methods handle all errors related to invalid parameters. In addition, it is recommended that you ensure that the word breaker methods do not raise nonhandled exceptions. The word breaker should perform the following functions and handle the following errors:

-   Call to [**IWordBreaker::Init**](iwordbreaker-init.md) must return either LANGUAGE\_E\_DATABASE\_NOT\_FOUND or S\_OK.
-   Call to[**IWordBreaker::Init**](iwordbreaker-init.md) successfully initializes the *\*pfLicense* parameter to **FALSE** and calls [**GetLicenseToUse**](iwordbreaker-getlicensetouse.md). **GetLicenseToUse** does not result in an access violation.
-   Word breaker does not read past the end of the *awcBuffer* parameter in the [**IWordBreaker::BreakText**](iwordbreaker-breaktext.md) method.
-   Call to the [**BreakText**](iwordbreaker-breaktext.md) method with the *pwcInBuf* set to **NULL**. **BreakText** fails (return E\_FAIL) and does not result in an access violation.
-   Call to the [**BreakText**](iwordbreaker-breaktext.md) method with the *cwc* equal to 0. **BreakText** returns successfully (return S\_OK) and does not result in an access violation.
-   Call to the [**BreakText**](iwordbreaker-breaktext.md) method with the *pwcInBuf* set to **NULL** and the *cwc* equal to 0. **BreakText** fails (return E\_FAIL) and does not result in an access violation.
-   Phrases generated during index creation contain the same number of words.
-   Phrases are generated during index creation through successive calls to the [**PutWord**](iwordsink-putword.md) and [**PutAltWord**](iwordsink-putaltword.md) methods in the [**WordSink**](iwordsink.md) object. The word breaker uses only the [**PhraseSink**](/windows/desktop/api/Indexsrv/nn-indexsrv-iphrasesink) object during query time.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 





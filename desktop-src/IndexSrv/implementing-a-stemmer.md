---
title: Implementing a Stemmer
description: Implementing a Stemmer
ms.assetid: d8ace103-a4ca-424f-9358-cd5fc6263a87
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Implementing a Stemmer

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Stemmers for Indexing Service implement the **IStemmer** interface. The **GenerateWordForms** method generates a list of inflected word forms for a given input word. To implement a stemmer component, you must have language heuristics for your language. This includes information about morphology. You may also need a list of words to exclude or include.

For more information about linguistic considerations and how these considerations affect stemmer implementations, see [Linguistic and Unicode Considerations](linguistic-and-unicode-considerations.md).

It is recommended that stemmers not generate the genitive, or possessive, case for words. For example, "David" is not generated as an alternative form for "David's." The word breaker generates both "David" and "David's" when it parses "David's."

The stemmer uses the **WordFormSink** object to gather the list of alternative words. The **PutWord** method generates the final word from the stemmer. In all cases, this final word is the same as the input word from **IStemmer::GenerateWordForms**. For example, given the word "swim," the stemmer generates the following word forms: "swimming," "swimmer," "swims," "swam," and "swum," through calls to the **PutAltWord** method. The stemmer generates "swim" through the **PutWord** method.

### Scalability

Stemmers, like word breakers, must use a "free" threading model and register with COM with their threading model set to "free" or "both." Indexing Service calls separate instances of the stemmer from different threads at the same time. Stemmers should therefore have minimal instance data.

### Performance

Stemmer accuracy has a significant impact on query relevance. If the stemmer stems the text incorrectly, queries may return unpredictable and inaccurate results. Stemmers must handle hundreds of queries per second without negatively affecting query performance. Stemmer performance should improve with increased hardware capability.

For more information about troubleshooting stemmers, see [Troubleshooting Language Resources](troubleshooting-language-resources.md).

### Security

Stemmers for Indexing Service run in the Local Security context. They should be written to manage buffers and to stack correctly. All string copies must have explicit checks to guard against buffer overruns. You should always verify the allocated size of the buffer and test the size of the data against the size of the buffer.

## Related topics

<dl> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> <dt>

[Troubleshooting Language Resources](troubleshooting-language-resources.md)
</dt> </dl>

 

 





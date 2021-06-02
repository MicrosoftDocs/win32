---
description: IInkAnalyzer::SearchWithLanguageId method - Provides a fuzzy, case-insensitive phrase based search for analyzed writing strokes and analyzed drawing strokes that have recognized types.
ms.assetid: dfd481f9-38fd-433f-b1fc-697c735c13da
title: IInkAnalyzer::SearchWithLanguageId method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalyzer.SearchWithLanguageId
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalyzer::SearchWithLanguageId method

Provides a fuzzy, case-insensitive phrase based search for analyzed writing strokes and analyzed drawing strokes that have recognized types.

## Syntax


```C++
HRESULT SearchWithLanguageId(
  [in]      BSTR  bstrPhraseToMatch,
  [in]      LONG  lSearchStringLanguageId,
  [in, out] ULONG *pulSearchResultCount,
  [out]     ULONG **ppulStrokeCountPerResult,
  [in, out] ULONG *pulStrokeIdsCount,
  [out]     ULONG **ppulStrokeIds
);
```



## Parameters

<dl> <dt>

*bstrPhraseToMatch* \[in\]
</dt> <dd>

The phrase that will be found in the alternates for the currently analyzed strokes.

</dd> <dt>

*lSearchStringLanguageId* \[in\]
</dt> <dd>

The LCID associated with the string that is passed. Used to convert the case internally to support case insensitive comparisons.

</dd> <dt>

*pulSearchResultCount* \[in, out\]
</dt> <dd>

The maximum number of results returned from the search.

</dd> <dt>

*ppulStrokeCountPerResult* \[out\]
</dt> <dd>

Pointer to an array of the number of strokes in each search result.

</dd> <dt>

*pulStrokeIdsCount* \[in, out\]
</dt> <dd>

The number of stroke IDs in *ppulStrokeIds*.

</dd> <dt>

*ppulStrokeIds* \[out\]
</dt> <dd>

Pointer to an array of stroke IDs representing a set of sets of strokes.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

This search finds multi-word and single word substrings. Both alternate recognition results and alternate segmentations are searched.

All incoming strings will be converted to a single casing for comparison utilizing the LCID of the current thread to do this conversion to respect cultural case conventions.

The string passed is treated as a phrase. Words and characters must appear in the alterantes for the strokes in the order specified. The first and last words of the phrase may be matched as substrings (the first word appearing at the end of an alternate and the last word appearing at the begginging of one), but any other words (those inside of the phrase) must appear as whole words.

If the string passed in has no whitespace in between characters, the substring may be found anywhere inside of a single word in an alternate.

Only the presence or absence of whitespace between characters changes the results of search. Whitespace that is not surrounded by characters is ignored. The type of the whitespace is ignored (a tab or a space between characters will give the same result). The amount of whitespace does not matter - one space or two spaces in between characters will give the same result.

Search does not generate PopulateContextNode events. Only the strokes that have already been populated will be searched.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalyzer**](iinkanalyzer.md)
</dt> </dl>

 

 





---
Description: Retrieves the identifiers for the locales that this IInkAnalysisRecognizer supports.
ms.assetid: 14c91ad0-f49e-43e7-848c-abc96b0dffa8
title: IInkAnalysisRecognizerGetLanguages method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IInkAnalysisRecognizer::GetLanguages method

Retrieves the identifiers for the locales that this [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) supports.

## Syntax


```C++
HRESULT GetLanguages(
  [in, out] ULONG *pulLanguagesCount,
  [out]     ULONG **ppulLanguages
);
```



## Parameters

<dl> <dt>

*pulLanguagesCount* \[in, out\]
</dt> <dd>

The number of identifiers in *ppulLanguages*.

</dd> <dt>

*ppulLanguages* \[out\]
</dt> <dd>

A pointer to the identifiers for the locales that this [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md) supports.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> \[!Caution\]  
> To avoid a memory leak, use [**CoTaskMemFree**](https://msdn.microsoft.com/library/windows/desktop/ms680722) to release the memory from \**ppulLanguages* when you no longer need the information.

 

This method returns an empty array for object and gesture recognizers.

For more information about language identifiers, see [Language Identifier Constants and Strings](https://msdn.microsoft.com/library/windows/desktop/dd318693).

## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                                                 |
| Minimum supported server<br/> | None supported<br/>                                                                                     |
| Header<br/>                   | <dl> <dt>IACom.h (also requires IACom\_i.c)</dt> </dl> |
| DLL<br/>                      | <dl> <dt>IACom.dll</dt> </dl>                          |



## See also

<dl> <dt>

[**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md)
</dt> <dt>

[Ink Analysis Reference](ink-analysis-reference.md)
</dt> </dl>

 

 





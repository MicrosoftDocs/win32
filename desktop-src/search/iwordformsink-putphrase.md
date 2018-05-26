---
Description: Puts an alternative form of a word in the IWordFormSink object.
ms.assetid: 4F6A3E88-A17C-4CA3-849D-FF0DC06D5DC3
title: IWordFormSinkPutAltWord method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IWordFormSink::PutAltWord method

Puts an alternative form of a word in the [**IWordFormSink**](/windows/win32/Indexsrv/nn-indexsrv-iwordformsink?branch=master) object.

## Syntax


```C++
HRESULT PutAltWord(
  [in] const WCHAR *pwcInBuf ,
  [in]       ULONG cwc
);
```



## Parameters

<dl> <dt>

*pwcInBuf* \[in\]
</dt> <dd>

A pointer to a buffer that contains an alternative form of a word.

</dd> <dt>

*cwc* \[in\]
</dt> <dd>

The number of characters in *pwcInBuf*.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                              | Description                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | The operation was completed successfully. <br/>                                                                                             |
| <dl> <dt>**LANGUAGE\_S\_LARGE\_WORD** </dt> </dl> | Value of *cwc* is larger than the value for *ulMaxTokenSize* that is specified in [**IStemmer::Init**](search._search_istemmer_init). <br/> |



 

## Remarks

This method is called from the [**GenerateWordForms**](search._search_istemmer_generatewordforms) method of the [**IStemmer**](search._search_istemmer) implementation. All alternative forms for a word, except the last, are put in the [**IWordFormSink**](/windows/win32/Indexsrv/nn-indexsrv-iwordformsink?branch=master) object by calling **IWordFormSink::PutAltWord**. The final alternative form of a word, which is always the original form of the word, is handled by calling [**IWordFormSink::PutWord**](iwordformsink-putword.md).

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Search.h</dt> </dl> |



## See also

<dl> <dt>

[**IWordFormSink**](/windows/win32/Indexsrv/nn-indexsrv-iwordformsink?branch=master)
</dt> </dl>

 

 





---
description: Retrieves the vendor name of the IInkAnalysisRecognizer.
ms.assetid: 62ff209e-2a34-4c04-90a0-661d06898298
title: IInkAnalysisRecognizer::GetVendor method (IACom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IInkAnalysisRecognizer.GetVendor
api_type: 
- COM
api_location: 
- IACom.dll
---

# IInkAnalysisRecognizer::GetVendor method

Retrieves the vendor name of the [**IInkAnalysisRecognizer**](iinkanalysisrecognizer.md).

## Syntax


```C++
HRESULT GetVendor(
  [out] BSTR *pbstrVendor
);
```



## Parameters

<dl> <dt>

*pbstrVendor* \[out\]
</dt> <dd>

The name of the vendor.

</dd> </dl>

## Return value

For a description of the return values, see [Classes and Interfaces - Ink Analysis](classes-and-interfaces---ink-analysis.md).

## Remarks

> [!Caution]  
> To avoid a memory leak, call [**SysFreeString**](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) on \**pbstrVendor* when you no longer need to use the string.

 

## Requirements



| Requirement | Value |
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

 


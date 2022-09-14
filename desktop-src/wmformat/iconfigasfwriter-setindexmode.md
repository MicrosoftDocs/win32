---
title: IConfigAsfWriter SetIndexMode method
description: The SetIndexMode method enables the application to control whether the file will be temporally indexed.
ms.assetid: 104e29f4-a1e5-4e26-a9ef-52ef52d6f5b2
keywords:
- SetIndexMode method windows Media Format
- SetIndexMode method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , SetIndexMode method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.SetIndexMode
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::SetIndexMode method

The **SetIndexMode** method enables the application to control whether the file will be temporally indexed.

## Syntax


```C++
HRESULT SetIndexMode(
  [in] BOOL bIndexFile
);
```



## Parameters

<dl> <dt>

*bIndexFile* \[in\]
</dt> <dd>

Variable of type **BOOL**; **TRUE** specifies that the file will be temporally indexed.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

By default, the [WM ASF Writer](wm-asf-writer-filter.md) creates temporally indexed ASF files. It performs the indexing when the graph stops. You can disable this behavior if you want to do your own frame-based indexing as a post-processing step. To create a frame-indexed file, call **SetIndexMode**(FALSE), create the file, and then use the Windows Media Format SDK methods directly to create a frame-based index for the file.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

 
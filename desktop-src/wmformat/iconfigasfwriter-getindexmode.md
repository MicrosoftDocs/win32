---
title: IConfigAsfWriter GetIndexMode method
description: The GetIndexMode method retrieves the current temporal index mode.
ms.assetid: beb874ea-d0d5-4323-a817-47984911da4c
keywords:
- GetIndexMode method windows Media Format
- GetIndexMode method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , GetIndexMode method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.GetIndexMode
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::GetIndexMode method

The **GetIndexMode** method retrieves the current temporal index mode.

## Syntax


```C++
HRESULT GetIndexMode(
  [out] BOOL *pbIndexFile
);
```



## Parameters

<dl> <dt>

*pbIndexFile* \[out\]
</dt> <dd>

Pointer to a variable of type **BOOL** that receives the temporal index mode setting. A value of **TRUE** indicates that the WM ASF Writer is configured to write temporally indexed files.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

Use this method to determine whether the [WM ASF Writer](wm-asf-writer-filter.md) is currently configured to write temporally indexed ASF files. For more information on temporally indexed and frame-indexed files, see the Remarks for [**IConfigAsfWriter::SetIndexMode**](iconfigasfwriter-setindexmode.md).

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

 
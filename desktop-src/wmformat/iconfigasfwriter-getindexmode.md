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
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter::GetIndexMode method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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

 

 
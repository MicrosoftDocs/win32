---
title: IConfigAsfWriter2 GetParam method
description: The GetParam method retrieves the current value of the specified filter configuration parameter.
ms.assetid: 81d915a1-6190-46e3-a5cb-7f5fc242b8dd
keywords:
- GetParam method windows Media Format
- GetParam method windows Media Format , IConfigAsfWriter2 interface
- IConfigAsfWriter2 interface windows Media Format , GetParam method
topic_type:
- apiref
api_name:
- IConfigAsfWriter2.GetParam
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter2::GetParam method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetParam** method retrieves the current value of the specified filter configuration parameter.

## Syntax


```C++
HRESULT GetParam(
  [in]  DWORD dwParam,
  [out] DWORD *pdwParam1,
  [out] DWORD *pdwParam2
);
```



## Parameters

<dl> <dt>

*dwParam* \[in\]
</dt> <dd>

Specifies the parameter to retrieve. It must be a value defined in the [\_AM\_ASFWRITERCONFIG\_PARAM](/previous-versions/windows/desktop/legacy/dd758054(v=vs.85)) enumeration.

</dd> <dt>

*pdwParam1* \[out\]
</dt> <dd>

Pointer to a variable that retrieves the value of the parameter specified in *dwParam*.

</dd> <dt>

*pdwParam2* \[out\]
</dt> <dd>

Not used, must be zero.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## See also

<dl> <dt>

[**IConfigAsfWriter2 Interface**](/previous-versions/windows/desktop/legacy/dd743206(v=vs.85))
</dt> <dt>

[**IConfigAsfWriter2::SetParam**](iconfigasfwriter2-setparam.md)
</dt> </dl>

 

 
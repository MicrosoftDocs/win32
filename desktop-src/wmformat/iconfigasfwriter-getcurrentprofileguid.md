---
title: IConfigAsfWriter GetCurrentProfileGuid method
description: The GetCurrentProfileGuid method retrieves the current Windows Media system profile GUID.
ms.assetid: e7a2ecc0-48d4-446c-852a-0d7677cbbe71
keywords:
- GetCurrentProfileGuid method windows Media Format
- GetCurrentProfileGuid method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , GetCurrentProfileGuid method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.GetCurrentProfileGuid
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter::GetCurrentProfileGuid method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetCurrentProfileGuid** method retrieves the current Windows Media system profile GUID.

## Syntax


```C++
HRESULT GetCurrentProfileGuid(
  [out] GUID *pProfileGuid
);
```



## Parameters

<dl> <dt>

*pProfileGuid* \[out\]
</dt> <dd>

Pointer to a variable of type **GUID** that identifies the current system profile being used by the filter.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

This method is not used with custom profiles (including all profiles that include streams that use the Windows Media Audio and Video codecs) because all such profiles are created by applications and have no GUID identifier. If no system profile is loaded, *pProfileGuid* will be set to **NULL**.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

 
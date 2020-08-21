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
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::GetCurrentProfileGuid method

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

 

 
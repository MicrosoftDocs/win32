---
title: IConfigAsfWriter GetCurrentProfileId method
description: The GetCurrentProfileId method retrieves the current profile ID. (For Windows Media Format 4.0 profiles only.).
ms.assetid: a5162bb1-5fcb-449e-b8d3-624b863e656d
keywords:
- GetCurrentProfileId method windows Media Format
- GetCurrentProfileId method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , GetCurrentProfileId method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.GetCurrentProfileId
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# IConfigAsfWriter::GetCurrentProfileId method

The **GetCurrentProfileId** method retrieves the current profile ID. (For Windows Media Format 4.0 profiles only.)

## Syntax


```C++
HRESULT GetCurrentProfileId(
  [out] DWORD *pdwProfileId
);
```



## Parameters

<dl> <dt>

*pdwProfileId* \[out\]
</dt> <dd>

Pointer to a variable of type **DWORD** that receives the current profile ID.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

This method is now obsolete because it assumes version 4.0 Windows Media Format SDK profiles. Use [**IConfigAsfWriter::GetCurrentProfile**](iconfigasfwriter-getcurrentprofile.md) or [**IConfigAsfWriter::GetCurrentProfileGuid**](iconfigasfwriter-getcurrentprofileguid.md) instead to correctly identify a profile for version 7.0 and later.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

 
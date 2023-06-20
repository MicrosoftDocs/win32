---
title: IConfigAsfWriter GetCurrentProfile method
description: The GetCurrentProfile method retrieves the application-defined profile.
ms.assetid: 7f6e7085-982b-4234-b890-950efdcdb559
keywords:
- GetCurrentProfile method windows Media Format
- GetCurrentProfile method windows Media Format , IConfigAsfWriter interface
- IConfigAsfWriter interface windows Media Format , GetCurrentProfile method
topic_type:
- apiref
api_name:
- IConfigAsfWriter.GetCurrentProfile
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
api_location: 
ms.custom: UpdateFrequency5
---

# IConfigAsfWriter::GetCurrentProfile method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetCurrentProfile** method retrieves the application-defined profile.

## Syntax


```C++
HRESULT GetCurrentProfile(
  [out] IWMProfile **ppProfile
);
```



## Parameters

<dl> <dt>

*ppProfile* \[out\]
</dt> <dd>

Address of a pointer that receives the [**IWMProfile**](iwmprofile.md) interface of the application-defined profile.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.

## Remarks

If the method succeeds, the **IWMProfile** pointer that it returns has an outstanding reference count. Be sure to release the interface when you are finished using it.

## See also

<dl> <dt>

[**IConfigAsfWriter Interface**](/previous-versions/windows/desktop/legacy/dd743205(v=vs.85))
</dt> </dl>

 

 
---
title: IWMDRMLicense GetInclusionList method (Wmdrmsdk.h)
description: The GetInclusionList method retrieves the entire inclusion list for the current license or license chain.
ms.assetid: a3cb70c5-7d20-413c-aeb8-66c9233b384e
keywords:
- GetInclusionList method windows Media Format
- GetInclusionList method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetInclusionList method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetInclusionList
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicense::GetInclusionList method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetInclusionList** method retrieves the entire inclusion list for the current license or license chain.

## Syntax


```C++
HRESULT GetInclusionList(
  [out] GUID  **ppGuids,
  [out] DWORD *pcGuids
);
```



## Parameters

<dl> <dt>

*ppGuids* \[out\]
</dt> <dd>

Receives an array of GUIDs identifying the included technologies.

</dd> <dt>

*pcGuids* \[out\]
</dt> <dd>

Receives the number of elements in the *ppGuids* array. The array is allocated by using **CoTaskMemAlloc**. When finished with the list, release the memory by calling **CoTaskMemFree**.

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

The license issuer can specify other protection systems to which the encrypted content may be converted. The list of GUIDs retrieved by this method identifies the allowed protection systems. When you enter into a license agreement with Microsoft to get the stub library, you will receive a list of currently supported protection systems and the GUIDs used to identify them.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**Explicit Authorization and Inclusion Lists**](explicit-authorization-and-inclusion-lists.md)
</dt> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 






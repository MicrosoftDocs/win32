---
title: IWMDRMLicense GetLicense method (Wmdrmsdk.h)
description: The GetLicense method retrieves the license as XML or XMR data.
ms.assetid: 63317841-fd13-4e83-8b99-e3cab1405050
keywords:
- GetLicense method windows Media Format
- GetLicense method windows Media Format , IWMDRMLicense interface
- IWMDRMLicense interface windows Media Format , GetLicense method
topic_type:
- apiref
api_name:
- IWMDRMLicense.GetLicense
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicense::GetLicense method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetLicense** method retrieves the license as XML or XMR data.

## Syntax


```C++
HRESULT GetLicense(
  [out] BYTE  **ppbLicense,
  [out] DWORD *pcbLicense,
  [out] DWORD *pdwLicenseType
);
```



## Parameters

<dl> <dt>

*ppbLicense* \[out\]
</dt> <dd>

Receives the license.

</dd> <dt>

*pcbLicense* \[out\]
</dt> <dd>

Receives the size of the license.

</dd> <dt>

*pdwLicenseType* \[out\]
</dt> <dd>

Receives the type of the license returned. This value is set to one of the constants in the following table.



| Constant                  | Description                            |
|---------------------------|----------------------------------------|
| WMDRM\_LICENSE\_TYPE\_XML | Retrieved license is formatted as XML. |
| WMDRM\_LICENSE\_TYPE\_XMR | Retrieved license is formatted as XMR. |



 

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                          | Description                      |
|--------------------------------------------------------------------------------------|----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | The method succeeded.<br/> |



 

## Remarks

None.

## Requirements



| Requirement | Value |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Wmdrmsdk.h</dt> </dl>   |
| Library<br/> | <dl> <dt>Wmdrmsdk.lib</dt> </dl> |



## See also

<dl> <dt>

[**GetLicenseProperty**](iwmdrmlicense-getlicenseproperty.md)
</dt> <dt>

[**IWMDRMLicense Interface**](iwmdrmlicense.md)
</dt> </dl>

 

 






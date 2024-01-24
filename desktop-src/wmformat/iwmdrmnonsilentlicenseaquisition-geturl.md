---
title: IWMDRMNonSilentLicenseAquisition GetURL method (Wmdrmsdk.h)
description: The GetURL method retrieves the URL to which the license challenge should be posted.
ms.assetid: f65f1984-74bc-4cd0-957e-930aa6a6f6a5
keywords:
- GetURL method windows Media Format
- GetURL method windows Media Format , IWMDRMNonSilentLicenseAquisition interface
- IWMDRMNonSilentLicenseAquisition interface windows Media Format , GetURL method
topic_type:
- apiref
api_name:
- IWMDRMNonSilentLicenseAquisition.GetURL
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMNonSilentLicenseAquisition::GetURL method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetURL** method retrieves the URL to which the license challenge should be posted.

## Syntax


```C++
HRESULT GetURL(
  [out] BSTR *pbstrURL
);
```



## Parameters

<dl> <dt>

*pbstrURL* \[out\]
</dt> <dd>

Address of a variable that receives the URL.

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

[**IWMDRMNonSilentLicenseAquisition Interface**](iwmdrmnonsilentlicenseaquisition.md)
</dt> </dl>

 

 






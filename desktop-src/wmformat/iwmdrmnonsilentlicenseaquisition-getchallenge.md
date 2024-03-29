---
title: IWMDRMNonSilentLicenseAquisition GetChallenge method (Wmdrmsdk.h)
description: The GetChallenge method retrieves the license challenge that should be posted to the license server.
ms.assetid: f2ff8484-8fe2-4c74-82c1-9bc14f8197e0
keywords:
- GetChallenge method windows Media Format
- GetChallenge method windows Media Format , IWMDRMNonSilentLicenseAquisition interface
- IWMDRMNonSilentLicenseAquisition interface windows Media Format , GetChallenge method
topic_type:
- apiref
api_name:
- IWMDRMNonSilentLicenseAquisition.GetChallenge
api_location:
- Wmdrmsdk.lib
- Wmdrmsdk.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMNonSilentLicenseAquisition::GetChallenge method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetChallenge** method retrieves the license challenge that should be posted to the license server.

## Syntax


```C++
HRESULT GetChallenge(
  [out] BSTR *pbstrChallenge
);
```



## Parameters

<dl> <dt>

*pbstrChallenge* \[out\]
</dt> <dd>

Address of a variable that receives the license challenge.

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

 

 






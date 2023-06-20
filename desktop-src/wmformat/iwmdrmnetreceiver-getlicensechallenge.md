---
title: IWMDRMNetReceiver GetLicenseChallenge method (Wmdrmsdk.h)
description: The GetLicenseChallenge method generates a Windows Media DRM for Network Devices license challenge that can be sent to a transmitter when requesting protected content.
ms.assetid: c13b9e9e-b076-411b-a106-b602544faaba
keywords:
- GetLicenseChallenge method windows Media Format
- GetLicenseChallenge method windows Media Format , IWMDRMNetReceiver interface
- IWMDRMNetReceiver interface windows Media Format , GetLicenseChallenge method
topic_type:
- apiref
api_name:
- IWMDRMNetReceiver.GetLicenseChallenge
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMNetReceiver::GetLicenseChallenge method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetLicenseChallenge** method generates a Windows Media DRM for Network Devices license challenge that can be sent to a transmitter when requesting protected content.

## Syntax


```C++
HRESULT GetLicenseChallenge(
  [in]  BSTR  bstrAction,
  [out] BYTE  **ppbLicenseChallenge,
  [out] DWORD *pcbLicenseChallenge
);
```



## Parameters

<dl> <dt>

*bstrAction* \[in\]
</dt> <dd>

Action for which to generate the challenge.

</dd> <dt>

*ppbLicenseChallenge* \[out\]
</dt> <dd>

Address of a pointer that is set to the address of the generated challenge. When finished with this data, you must release the memory by calling **CoTaskMemFree**.

</dd> <dt>

*pcbLicenseChallenge* \[out\]
</dt> <dd>

Address of a variable that receives the size of the license challenge in bytes.

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
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdrmsdk.h</dt> </dl> |



## See also

<dl> <dt>

[**IWMDRMNetReceiver Interface**](iwmdrmnetreceiver.md)
</dt> <dt>

[**IWMDRMNetReceiver::ProcessLicenseResponse**](iwmdrmnetreceiver-processlicenseresponse.md)
</dt> </dl>

 

 






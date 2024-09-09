---
title: IWMDRMIndividualizationStatus GetStatus method (Wmdrmsdk.h)
description: The GetStatus method retrieves detailed information about individualization progress.
ms.assetid: 8985f3cc-006d-4fd5-b218-d3af3473b8e3
keywords:
- GetStatus method windows Media Format
- GetStatus method windows Media Format , IWMDRMIndividualizationStatus interface
- IWMDRMIndividualizationStatus interface windows Media Format , GetStatus method
topic_type:
- apiref
api_name:
- IWMDRMIndividualizationStatus.GetStatus
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMIndividualizationStatus::GetStatus method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **GetStatus** method retrieves detailed information about individualization progress.

## Syntax


```C++
HRESULT GetStatus(
  [out] WM_INDIVIDUALIZE_STATUS *pStatus
);
```



## Parameters

<dl> <dt>

*pStatus* \[out\]
</dt> <dd>

Receives a [**WM\_INDIVIDUALIZE\_STATUS**](drmwm-individualize-status.md) structure containing detailed information about the status of the individualization attempt.

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

[**IWMDRMIndividualizationStatus Interface**](iwmdrmindividualizationstatus.md)
</dt> </dl>

 

 






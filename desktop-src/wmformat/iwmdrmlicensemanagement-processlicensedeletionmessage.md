---
title: IWMDRMLicenseManagement ProcessLicenseDeletionMessage method (Wmdrmsdk.h)
description: The ProcessLicenseDeletion method deletes a license that was imported for content originally protected with another content protection system.
ms.assetid: 478dd156-feb8-4eda-9d3a-35db3e65c227
keywords:
- ProcessLicenseDeletionMessage method windows Media Format
- ProcessLicenseDeletionMessage method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , ProcessLicenseDeletionMessage method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.ProcessLicenseDeletionMessage
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMDRMLicenseManagement::ProcessLicenseDeletionMessage method

\[The feature associated with this page, [Windows Media Format 11 SDK](/windows/win32/wmformat/windows-media-format-11-sdk), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader) and [Sink Writer](/windows/win32/medfound/sink-writer). **Source Reader** and **Sink Writer** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** and **Sink Writer** instead of **Windows Media Format 11 SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **ProcessLicenseDeletion** method deletes a license that was imported for content originally protected with another content protection system.

## Syntax


```C++
HRESULT ProcessLicenseDeletionMessage(
  [in] BSTR bstrDeletionMessage
);
```



## Parameters

<dl> <dt>

*bstrDeletionMessage* \[in\]
</dt> <dd>

Message identifying the license to delete.

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

[**IWMDRMLicenseManagement Interface**](iwmdrmlicensemanagement.md)
</dt> </dl>

 

 






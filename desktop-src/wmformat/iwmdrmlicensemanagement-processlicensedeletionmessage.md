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
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::ProcessLicenseDeletionMessage method

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

 

 






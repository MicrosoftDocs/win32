---
title: IWMDRMLicenseManagement CreateLicenseRevocationChallenge method (Wmdrmsdk.h)
description: The CreateLicenseRevocationChallenge method generates a license revocation challenge.
ms.assetid: 31fcf7a7-1af8-4474-abac-eddb1070975b
keywords:
- CreateLicenseRevocationChallenge method windows Media Format
- CreateLicenseRevocationChallenge method windows Media Format , IWMDRMLicenseManagement interface
- IWMDRMLicenseManagement interface windows Media Format , CreateLicenseRevocationChallenge method
topic_type:
- apiref
api_name:
- IWMDRMLicenseManagement.CreateLicenseRevocationChallenge
api_location:
- Wmdrmsdk.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMDRMLicenseManagement::CreateLicenseRevocationChallenge method

The **CreateLicenseRevocationChallenge** method generates a license revocation challenge.

## Syntax


```C++
HRESULT CreateLicenseRevocationChallenge(
  [in]  BYTE  *pbMachineID,
  [in]  DWORD cbMachineID,
  [in]  BYTE  *pbChallenge,
  [in]  DWORD cbChallenge,
  [out] BYTE  **ppbChallengeOutput,
  [out] DWORD *pcbChallengeOutput
);
```



## Parameters

<dl> <dt>

*pbMachineID* \[in\]
</dt> <dd>

User-specified machine identifier. This value is used to query for a license on the server and must conform to whatever format the license server uses.

</dd> <dt>

*cbMachineID* \[in\]
</dt> <dd>

Size, in bytes, of the machine identifier.

</dd> <dt>

*pbChallenge* \[in\]
</dt> <dd>

User-specified challenge data. This data, in addition to the machine identifier, is used to query the license server for licenses to be revoked.

</dd> <dt>

*cbChallenge* \[in\]
</dt> <dd>

Size, in bytes, of the challenge data.

</dd> <dt>

*ppbChallengeOutput* \[out\]
</dt> <dd>

Address of a pointer that receives the address of the challenge output. This buffer is the data that is sent to the license revocation service. When finished with this data, you must release the memory by calling **CoTaskMemFree**.

</dd> <dt>

*pcbChallengeOutput* \[out\]
</dt> <dd>

Address of a variable that receives the size of the allocated challenge output data, in bytes.

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

 

 






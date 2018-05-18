---
title: ISCPSecureQuery GetRights method
description: The GetRights method retrieves rights information for the current piece of content. Rights are file-specific.
ms.assetid: '3d9991f4-ce20-45c4-a408-d7a846b019ef'
keywords: ["GetRights method windows Media Device Manager", "GetRights method windows Media Device Manager , ISCPSecureQuery interface", "ISCPSecureQuery interface windows Media Device Manager , GetRights method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery.GetRights
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery::GetRights method

The **GetRights** method retrieves rights information for the current piece of content. Rights are file-specific.

## Syntax


```C++
HRESULT GetRights(
  [in]      BYTE                *pData,
  [in]      DWORD               dwSize,
  [in]      BYTE                *pbSPSessionKey,
  [in]      DWORD               dwSessionKeyLen,
  [in]      IMDSPStorageGlobals *pStgGlobals,
  [out]     PWMDMRIGHTS         *ppRights,
  [out]     UINT                *pnRightsCount,
  [in, out] BYTE                abMac
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to data requested by [**GetDataDemands**](iscpsecurequery-getdatademands.md). This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

Number of bytes of data in the *pData* buffer. This parameter must be included in the input message authentication code.

</dd> <dt>

*pbSPSessionKey* \[in\]
</dt> <dd>

Pointer to an array of bytes containing the session key for securing communication with the service provider to which *pStgGlobals* points. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSessionKeyLen* \[in\]
</dt> <dd>

Length of the byte array to which *pbSPSessionKey* points. This parameter must be included in the input message authentication code.

</dd> <dt>

*pStgGlobals* \[in\]
</dt> <dd>

Pointer to an [**IWMDMStorageGlobals**](iwmdmstorageglobals.md) interface on the root storage of the media or device to or from which the file is being transferred.

</dd> <dt>

*ppRights* \[out\]
</dt> <dd>

Pointer to an array of [**WMDMRIGHTS**](wmdmrights.md) structures containing the rights information for this object. The array is allocated by this method and must be freed using **CoTaskMemFree**. This parameter is included in the output message authentication code.

</dd> <dt>

*pnRightsCount* \[out\]
</dt> <dd>

Number of **WMDMRIGHTS** structures in the *ppRights* array. This parameter is included in the output message authentication code.

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                     | Description                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_CALL\_OUT\_OF\_SEQUENCE**</dt> </dl> | This method was called out of sequence. **GetDataDemands** and then [**ExamineData**](iscpsecurequery-examinedata.md) must be called first, in that order.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl>      | The message authentication code is not valid.<br/>                                                                                                               |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>                | The caller does not have the rights required to perform the requested operation.<br/>                                                                            |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | A parameter is invalid or is a **NULL** pointer.<br/>                                                                                                            |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | An unspecified error occurred.<br/>                                                                                                                              |



 

## Remarks

This method must not be called until **GetDataDemands** and then **ExamineData** have been called, in that order.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> <dt>

[**IWMDMStorageGlobals Interface**](iwmdmstorageglobals.md)
</dt> <dt>

[**WMDMRIGHTS**](wmdmrights.md)
</dt> </dl>

 

 






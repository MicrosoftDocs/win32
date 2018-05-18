---
title: ISCPSecureQuery3 GetRightsOnClearChannel method
description: The GetRightsOnClearChannel method retrieves rights information for the current piece of content on a clear channel.
ms.assetid: 'ab64b790-848a-4c7f-9bf9-4a9b40bcc9cb'
keywords: ["GetRightsOnClearChannel method windows Media Device Manager", "GetRightsOnClearChannel method windows Media Device Manager , ISCPSecureQuery3 interface", "ISCPSecureQuery3 interface windows Media Device Manager , GetRightsOnClearChannel method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery3.GetRightsOnClearChannel
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery3::GetRightsOnClearChannel method

The **GetRightsOnClearChannel** method retrieves rights information for the current piece of content on a clear channel.

## Syntax


```C++
HRESULT GetRightsOnClearChannel(
  [in]  BYTE                *pData,
  [in]  DWORD               dwSize,
  [in]  BYTE                *pbSPSessionKey,
  [in]  DWORD               dwSessionKeyLen,
  [in]  IMDSPStorageGlobals *pStgGlobals,
  [in]  IWMDMProgress3      *pProgressCallback,
  [out] PWMDMRIGHTS         *ppRights,
  [out] UINT                *pnRightsCount
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to data object.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

Number of bytes of data in the *pData* buffer.

</dd> <dt>

*pbSPSessionKey* \[in\]
</dt> <dd>

Pointer to an array of bytes containing the session key for securing communication with the service provider to which *pStgGlobals* points.

</dd> <dt>

*dwSessionKeyLen* \[in\]
</dt> <dd>

Length of the byte array to which *pbSPSessionKey* points.

</dd> <dt>

*pStgGlobals* \[in\]
</dt> <dd>

Pointer to an [**IWMDMStorageGlobals**](iwmdmstorageglobals.md) interface on the root storage of the media or device to or from which the file is being transferred.

</dd> <dt>

*pProgressCallback* \[in\]
</dt> <dd>

Pointer to an [**IWMDMProgress3**](iwmdmprogress3.md) interface.

</dd> <dt>

*ppRights* \[out\]
</dt> <dd>

Pointer to an array of [**WMDMRIGHTS**](wmdmrights.md) structures containing the rights information for this object. The array is allocated by this method and must be freed using **CoTaskMemFree**.

</dd> <dt>

*pnRightsCount* \[out\]
</dt> <dd>

Number of **WMDMRIGHTS** structures in the *ppRights* array.

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If the method fails, it returns an **HRESULT** error code.



| Return code                                                                                                     | Description                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_CALL\_OUT\_OF\_SEQUENCE**</dt> </dl> | This method was called out of sequence. [**ISCPSecureQuery::GetDataDemands**](iscpsecurequery-getdatademands.md) and then [**ISCPSecureQuery::ExamineData**](iscpsecurequery-examinedata.md)must be called, in that order.<br/> |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl>      | The message authentication code is not valid.<br/>                                                                                                                                                                                |
| <dl> <dt>**WMDM\_E\_NORIGHTS**</dt> </dl>                | The caller does not have the rights required to perform the requested operation.<br/>                                                                                                                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | A parameter is invalid or is a **NULL** pointer.<br/>                                                                                                                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | An unspecified error occurred.<br/>                                                                                                                                                                                               |



 

## Remarks

This method is identical to **ISCPSecureQuery::GetRights** except that the parameters passed to this method are not encrypted. Consequently this method is more efficient.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery::GetRights**](iscpsecurequery-getrights.md)
</dt> <dt>

[**ISCPSecureQuery3 Interface**](iscpsecurequery3.md)
</dt> <dt>

[**IWMDMStorageGlobals Interface**](iwmdmstorageglobals.md)
</dt> <dt>

[**WMDMRIGHTS**](wmdmrights.md)
</dt> </dl>

 

 






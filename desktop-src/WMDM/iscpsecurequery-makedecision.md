---
title: ISCPSecureQuery MakeDecision method
description: The MakeDecision method determines whether access to the content is allowed. If access is allowed, this method returns the interface that will be used to access the content.
ms.assetid: 'cbcc8999-d7e4-4b67-a5ba-dd850ff7a07a'
keywords: ["MakeDecision method windows Media Device Manager", "MakeDecision method windows Media Device Manager , ISCPSecureQuery interface", "ISCPSecureQuery interface windows Media Device Manager , MakeDecision method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery.MakeDecision
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery::MakeDecision method

The **MakeDecision** method determines whether access to the content is allowed. If access is allowed, this method returns the interface that will be used to access the content.

## Syntax


```C++
HRESULT MakeDecision(
  [in]      UINT                fuFlags,
  [in]      BYTE                *pData,
  [in]      DWORD               dwSize,
  [in]      DWORD               dwAppSec,
  [in]      BYTE                *pbSPSessionKey,
  [in]      DWORD               dwSessionKeyLen,
  [in]      IMDSPStorageGlobals *pStorageGlobals,
  [out]     ISCPSecureExchange  **ppExchange,
  [in, out] BYTE                abMac
);
```



## Parameters

<dl> <dt>

*fuFlags* \[in\]
</dt> <dd>

Flags describing the data offered to the secure content provider for making decisions. This parameter must be included in the input message authentication code. The following flags can be present.



| Flag                              | Description                                                                                                                                                                                                                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WMDM\_SCP\_DECIDE\_DATA           | The *pData* parameter points to data to be examined.                                                                                                                                                                                                                                                  |
| WMDM\_MODE\_TRANSFER\_PROTECTED   | The output object data from the [**ISCPSecureExchange**](iscpsecureexchange.md) interface must be protected. If Windows Media Device Manager sets neither or both mode flags, DRM decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected. |
| WMDM\_MODE\_TRANSFER\_UNPROTECTED | The output object data from the **ISCPSecureExchange** interface must be unprotected. If Windows Media Device Manager sets neither or both mode flags, DRM decides whether the output object data from the **ISCPSecureExchange** interface must be protected or unprotected.                         |



 

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to a data object containing the data to be examined. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

**DWORD** that contains the length, in bytes, of the data to be examined. This parameter must be included in the input message authentication code.

</dd> <dt>

*dwAppSec* \[in\]
</dt> <dd>

**DWORD** that indicates the current level of security of Windows Media Device Manager. This is the smaller of the current security levels of the application and the target service provider. This parameter must be included in the input message authentication code.

</dd> <dt>

*pbSPSessionKey* \[in\]
</dt> <dd>

Pointer to an array of bytes containing the session key for securing communication with the service provider to which *pStgGlobals* points. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSessionKeyLen* \[in\]
</dt> <dd>

Length of the byte array to which *pbSPSessionKey* points. This parameter must be included in the input message authentication code.

</dd> <dt>

*pStorageGlobals* \[in\]
</dt> <dd>

Pointer to the [**IWMDMStorageGlobals**](iwmdmstorageglobals.md) interface on the root storage of the media or device to or from which the file is being transferred. This parameter must be included in the input message authentication code.

</dd> <dt>

*ppExchange* \[out\]
</dt> <dd>

Pointer to an exchange object that receives the exchange interface.

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                     | Description                                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_CALL\_OUT\_OF\_SEQUENCE**</dt> </dl> | This method was called out of sequence.<br/>                                                                                                                                                                                                                   |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl>      | The message authentication code is not valid.<br/>                                                                                                                                                                                                             |
| <dl> <dt>**WMDM\_E\_MOREDATA**</dt> </dl>                | Windows Media Device Manager must call this method again with another packet of data. The size of the packet is determined by the *pdwMinDecisionData* parameter in the [**ISCPSecureQuery::GetDataDemands**](iscpsecurequery-getdatademands.md) method.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                         | The caller does not have the rights required to perform the requested transfer.<br/>                                                                                                                                                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | A parameter is invalid or is a **NULL** pointer.<br/>                                                                                                                                                                                                          |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | An unspecified error occurred.<br/>                                                                                                                                                                                                                            |



 

## Remarks

This method is called after the [**ISCPSecureQuery::ExamineData**](iscpsecurequery-examinedata.md) method, and makes the final decision whether access to the content is allowed.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureExchange Interface**](iscpsecureexchange.md)
</dt> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> <dt>

[**ISCPSecureQuery2::MakeDecision2**](iscpsecurequery2-makedecision2.md)
</dt> <dt>

[**IWMDMStorageGlobals Interface**](iwmdmstorageglobals.md)
</dt> </dl>

 

 






---
title: ISCPSecureQuery ExamineData method
description: The ExamineData method determines rights and responsibility for the content by examining data that Windows Media Device Manager passes to this method.
ms.assetid: 'e12d8b55-5600-4178-8b2b-8afe8ade6818'
keywords: ["ExamineData method windows Media Device Manager", "ExamineData method windows Media Device Manager , ISCPSecureQuery interface", "ISCPSecureQuery interface windows Media Device Manager , ExamineData method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery.ExamineData
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery::ExamineData method

The **ExamineData** method determines rights and responsibility for the content by examining data that Windows Media Device Manager passes to this method.

## Syntax


```C++
HRESULT ExamineData(
  [in]      UINT   fuFlags,
  [in]      LPWSTR pwszExtension,
  [in]      BYTE   *pData,
  [in]      DWORD  dwSize,
  [in, out] BYTE   abMac
);
```



## Parameters

<dl> <dt>

*fuFlags* \[in\]
</dt> <dd>

Flags describing the data offered to the secure content provider to make decisions. The following flags can be present.



| Flag                     | Description                                          |
|--------------------------|------------------------------------------------------|
| WMDM\_SCP\_EXAMINE\_DATA | The *pData* parameter points to data to be examined. |



 

</dd> <dt>

*pwszExtension* \[in\]
</dt> <dd>

Pointer to the file name extension to be examined if the secure content provider asks for an extension in the [**GetDataDemands**](iscpsecurequery-getdatademands.md) call.

</dd> <dt>

*pData* \[in\]
</dt> <dd>

Pointer to the data at the beginning of the file to be examined. This parameter must be included in the input message authentication code and must be encrypted.

</dd> <dt>

*dwSize* \[in\]
</dt> <dd>

**DWORD** that contains the length, in bytes, of the data to be examined. This parameter must be included in the input message authentication code.

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

The method returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                                                     | Description                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                            | The method succeeded. The secure content provider is responsible for this content.<br/>                                                                                                                |
| <dl> <dt>**WMDM\_E\_CALL\_OUT\_OF\_SEQUENCE**</dt> </dl> | This method was called out of sequence. **GetDataDemands** must be called first.<br/>                                                                                                                  |
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl>      | The message authentication code is not valid.<br/>                                                                                                                                                     |
| <dl> <dt>**WMDM\_E\_MOREDATA**</dt> </dl>                | Windows Media Device Manager must call this method again with another packet of data. The size of the packet is determined by the *pdwMinExamineData* parameter in the **GetDataDemands** method.<br/> |
| <dl> <dt>**S\_FALSE**</dt> </dl>                         | The secure content provider is not responsible for this content. Terminate interaction with the secure content provider.<br/>                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                    | A parameter is invalid or is a **NULL** pointer.<br/>                                                                                                                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>                          | An unspecified error occurred.<br/>                                                                                                                                                                    |



 

## Remarks

This method is called after the **GetDataDemands** method. The secure content provider uses the information passed in this method to determine whether it is responsible for the content. The *fuFlags* parameter is consulted to determine which data has been presented for examination. The *pData* parameter points to the beginning of the rights and responsibility data. The *dwSize* parameter contains the length, in bytes, of the rights and responsibility data.

If the WMDM\_SCP\_EXAMINE\_DATA flag is set, then the *pDataBuffer* parameter contains *dwDataLength* of bytes for the secure content provider to examine.

If this method does not return S\_OK or WMDM\_E\_MOREDATA, then Windows Media Device Manager does not make any further calls to this secure content provider.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> </dl>

 

 






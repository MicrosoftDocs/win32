---
title: ISCPSecureQuery GetDataDemands method
description: The GetDataDemands method reports which data the secure content provider needs to determine the rights and responsibility for a specified piece of content.
ms.assetid: 'c4ed4da1-9378-4c35-8f03-b028e37c1707'
keywords: ["GetDataDemands method windows Media Device Manager", "GetDataDemands method windows Media Device Manager , ISCPSecureQuery interface", "ISCPSecureQuery interface windows Media Device Manager , GetDataDemands method"]
topic_type:
- apiref
api_name:
- ISCPSecureQuery.GetDataDemands
api_location:
- mssachlp.lib
- mssachlp.dll
api_type:
- COM
---

# ISCPSecureQuery::GetDataDemands method

The **GetDataDemands** method reports which data the secure content provider needs to determine the rights and responsibility for a specified piece of content.

## Syntax


```C++
HRESULT GetDataDemands(
  [out]     UINT  *pfuFlags,
  [out]     DWORD *pdwMinRightsData,
  [out]     DWORD *pdwMinExamineData,
  [out]     DWORD *pdwMinDecideData,
  [in, out] BYTE  abMac
);
```



## Parameters

<dl> <dt>

*pfuFlags* \[out\]
</dt> <dd>

Flags describing the data required by the secure content provider to make decisions. This parameter is included in the output message authentication code. At least one of the following flags must be used.



| Flag                           | Description                                                                                                                      |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| WMDM\_SCP\_RIGHTS\_DATA        | The secure content provider needs data to determine rights for the content.                                                      |
| WMDM\_SCP\_EXAMINE\_DATA       | The secure content provider needs data to determine whether it is responsible for the content.                                   |
| WMDM\_SCP\_DECIDE\_DATA        | The secure content provider needs data to determine whether to allow the content to be downloaded.                               |
| WMDM\_SCP\_EXAMINE\_EXTENSION  | The secure content provider needs to examine the file name extension to determine whether to allow the content to be downloaded. |
| WMDM\_SCP\_PROTECTED\_OUTPUT   | The secure content provider needs protected output.                                                                              |
| WMDM\_SCP\_UNPROTECTED\_OUTPUT | The secure content provider needs unprotected output.                                                                            |



 

</dd> <dt>

*pdwMinRightsData* \[out\]
</dt> <dd>

Pointer to a **DWORD** specifying the minimum amount of data needed to determine rights for this content. This parameter is included in the output message authentication code.

</dd> <dt>

*pdwMinExamineData* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the minimum number of bytes of data that the secure content provider needs to determine whether it is responsible for the content. This parameter is included in the output message authentication code.

</dd> <dt>

*pdwMinDecideData* \[out\]
</dt> <dd>

Pointer to a **DWORD** containing the minimum number of bytes of data that the secure content provider needs to determine whether to allow the content to be downloaded. This parameter is included in the output message authentication code.

</dd> <dt>

*abMac* \[in, out\]
</dt> <dd>

Array of eight bytes containing the message authentication code for the parameter data of this method. (WMDM\_MAC\_LENGTH is defined as 8.)

</dd> </dl>

## Return value

If the method succeeds, it returns S\_OK. If it fails, it returns an **HRESULT** error code.



| Return code                                                                                                | Description                                               |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>**WMDM\_E\_MAC\_CHECK\_FAILED**</dt> </dl> | The message authentication code is not valid.<br/>  |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | A parameter is an invalid or **NULL** pointer.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | An unspecified error occurred.<br/>                 |



 

## Remarks

This method must be called before any of the other methods of **ISCPSecureQuery** are called.

This method is called after any certificate exchanges have been successfully finished. The secure content provider fills in the parameters with the flags and data that describe its requirements for making decisions about the content.

If the secure content provider sets the WMDM\_SCP\_RIGHTS\_DATA flag, then Windows Media Device Manager sends the amount of data specified in *pdwMinRightsData* by calling [**ISCPSecureQuery::GetRights**](iscpsecurequery-getrights.md).

If the secure content provider sets the WMDM\_SCP\_EXAMINE\_DATA flag, then Windows Media Device Manager sends the amount of data specified in *pdwMinExamineData* by calling [**ISCPSecureQuery::ExamineData**](iscpsecurequery-examinedata.md).

If the secure content provider sets the WMDM\_SCP\_DECIDE\_DATA flag, then Windows Media Device Manager sends the amount of data specified in *pdwMinDecideData* by calling [**ISCPSecureQuery::MakeDecision**](iscpsecurequery-makedecision.md).

If no examine flags are set, Windows Media Device Manager does not make any more calls. If no decide flags are set, Windows Media Device Manager still calls [**ISCPSecureQuery::ExamineData**](iscpsecurequery-examinedata.md).

If this method does not return S\_OK, then Windows Media Device Manager does not make any further calls to this secure content provider.

## Requirements



|                    |                                                                                         |
|--------------------|-----------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>WMSCP.idl</dt> </dl>    |
| Library<br/> | <dl> <dt>Mssachlp.lib</dt> </dl> |



## See also

<dl> <dt>

[**ISCPSecureQuery Interface**](iscpsecurequery.md)
</dt> </dl>

 

 






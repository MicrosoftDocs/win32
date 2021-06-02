---
description: Estimates the risk of executing unknown code when a handler is called on a given file. This risk is based on an understanding of the handler and the code content of the file.
title: EstimateFileRiskLevel function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EstimateFileRiskLevel
api_type: 
- DllExport
api_location: 
- Winshfhc.dll
ms.assetid: 33a5589a-201b-4d94-afbf-5965a39e2748

---

# EstimateFileRiskLevel function

\[This function is available on Windows XP with Service Pack 2 (SP2) through Windows Vista. It might be altered or unavailable in subsequent versions of Windows. Client applications instead should use [**IAttachmentExecute**](/windows/desktop/api/shobjidl_core/nn-shobjidl_core-iattachmentexecute) to present a user environment that provides safe download and exchange of files through email and messaging attachments.\]

Estimates the risk of executing unknown code when a handler is called on a given file. This risk is based on an understanding of the handler and the code content of the file.

## Syntax


```C++
HRESULT EstimateFileRiskLevel(
  _In_  LPCWSTR         pszFilePath,
  _In_  LPCWSTR         pszExt,
  _In_  LPCWSTR         pszHandler,
  _Out_ FILE_RISK_LEVEL *pfrlEstimate
);
```



## Parameters

<dl> <dt>

*pszFilePath* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a null-terminated string that contains the path of the file that is being checked against the handler.

</dd> <dt>

*pszExt* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a null-terminated string that contains the extension of the file that is being checked, either with or without its leading period. For instance, ".txt" or "txt".

</dd> <dt>

*pszHandler* \[in\]
</dt> <dd>

Type: **LPCWSTR**

A pointer to a null-terminated string that contains the path of the handler for the file.

</dd> <dt>

*pfrlEstimate* \[out\]
</dt> <dd>

Type: **FILE\_RISK\_LEVEL\***

When this function returns successfully, contains a pointer to one of the following values that state the estimated risk.

<dt>

<span id="FRL_NO_OPINION"></span><span id="frl_no_opinion"></span>

<span id="FRL_NO_OPINION"></span><span id="frl_no_opinion"></span>**FRL\_NO\_OPINION** (0)


</dt> <dd>

The format of the file is not identified or the handler is not identified. Insufficient information available for a meaningful answer.

</dd> <dt>

<span id="FRL_LOW"></span><span id="frl_low"></span>

<span id="FRL_LOW"></span><span id="frl_low"></span>**FRL\_LOW** (1)


</dt> <dd>

The format of the file is completely understood, the handler is known, and there is high confidence that no extraneous code will be executed.

</dd> <dt>

<span id="FRL_MODERATE"></span><span id="frl_moderate"></span>

<span id="FRL_MODERATE"></span><span id="frl_moderate"></span>**FRL\_MODERATE** (2)


</dt> <dd>

The format of the file is identified, but it is not sufficiently understood to label as either a high or low risk.

</dd> <dt>

<span id="FRL_HIGH"></span><span id="frl_high"></span>

<span id="FRL_HIGH"></span><span id="frl_high"></span>**FRL\_HIGH** (3)


</dt> <dd>

The file format is understood and elevated risk factors have been identified.

</dd> <dt>

<span id="FRL_BLOCK"></span><span id="frl_block"></span>

<span id="FRL_BLOCK"></span><span id="frl_block"></span>**FRL\_BLOCK** (4)


</dt> <dd>

The file format is specifically blocked for this handler.

</dd> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This function is not declared in a public header or included in a library file. To use it you must load it directly from Winshfhc.dll by ordinal 101.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| DLL<br/>                      | <dl> <dt>Winshfhc.dll (version 5.1 or later)</dt> </dl> |



 

 





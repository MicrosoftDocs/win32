---
title: WSMan.GetErrorMessage method (WSManDisp.h)
description: Returns a formatted string that contains the text of an error number.
ms.assetid: 5f0a5259-8356-4406-8612-34f4921184f0
ms.tgt_platform: multiple
keywords:
- GetErrorMessage method Windows Remote Management
- GetErrorMessage method Windows Remote Management , WSMan object
- WSMan object Windows Remote Management , GetErrorMessage method
topic_type:
- apiref
api_name:
- WSMan.GetErrorMessage
api_location:
- WSMAuto.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# WSMan.GetErrorMessage method

Returns a formatted string that contains the text of an error number. This method performs the same operation as the **Winrm** command-line **winrm helpmsg** *decimal or hexadecimal error number*.

## Syntax


```VB
WSMan.GetErrorMessage( _
  ByVal errorNumber, _
  ByRef errorMessage _
)
```



## Parameters

<dl> <dt>

*errorNumber* \[in\]
</dt> <dd>

An error message number in decimal or hexadecimal from WinRM, WinHTTP, or other operating system components.

</dd> <dt>

*errorMessage* \[out\]
</dt> <dd>

An error message string formatted like messages returned from the **Winrm** command.

</dd> </dl>

## Remarks

The corresponding C++ method is [**IWSManEx::GetErrorMessage**](/windows/desktop/api/WSManDisp/nf-wsmandisp-iwsmanex-geterrormessage).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Header<br/>                   | <dl> <dt>WSManDisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>WSManDisp.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>WSManDisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WSMAuto.dll</dt> </dl>   |



## See also

<dl> <dt>

[**WSMan**](wsman.md)
</dt> </dl>

 

 






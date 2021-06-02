---
title: INapSoHProcessor GetNumberOfAttributes method (NapProtocol.h)
description: Retrieves the total number of attributes in the SoH.
ms.assetid: ee0b1857-65a7-47bb-ae91-c939344a24d0
keywords:
- GetNumberOfAttributes method NAP
- GetNumberOfAttributes method NAP , INapSoHProcessor interface
- INapSoHProcessor interface NAP , GetNumberOfAttributes method
topic_type:
- apiref
api_name:
- INapSoHProcessor.GetNumberOfAttributes
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHProcessor::GetNumberOfAttributes method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHProcessor::GetNumberOfAttributes** method retrieves the total number of attributes in the SoH.

## Syntax


```C++
HRESULT GetNumberOfAttributes(
  [out] UINT16 *attributeCount
);
```



## Parameters

<dl> <dt>

*attributeCount* \[out\]
</dt> <dd>

A pointer to the returned attribute count.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>NapProtocol.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>NapProtocol.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Qutil.dll</dt> </dl>       |



## See also

<dl> <dt>

[**INapSoHProcessor**](inapsohprocessor.md)
</dt> </dl>

 

 






---
title: INapSoHProcessor FindNextAttribute method (NapProtocol.h)
description: Finds the location (index) of the next attribute of the type indicated by SoHAttributeType.
ms.assetid: 0ff94a32-ece8-4a89-9ee9-93c5e14dfb6c
keywords:
- FindNextAttribute method NAP
- FindNextAttribute method NAP , INapSoHProcessor interface
- INapSoHProcessor interface NAP , FindNextAttribute method
topic_type:
- apiref
api_name:
- INapSoHProcessor.FindNextAttribute
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHProcessor::FindNextAttribute method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHProcessor::FindNextAttribute** method finds the location (index) of the next attribute of the type indicated by *SoHAttributeType*.

## Syntax


```C++
HRESULT FindNextAttribute(
  [in]  UINT16           fromLocation,
  [in]  SoHAttributeType type,
  [out] UINT16           *attributeLocation
);
```



## Parameters

<dl> <dt>

*fromLocation* \[in\]
</dt> <dd>

The starting location (index) in the Statement of Health (SoH) packet to begin the attribute search. This value must be in the range of 0 to (**numAttrib** - 1) where **numAttrib** is retrieved using [**INapSoHProcessor::GetNumberOfAttributes**](inapsohprocessor-getnumberofattributes-method.md).

> [!Note]  
> The SoH packet uses 0-based attribute indices.

 

</dd> <dt>

*type* \[in\]
</dt> <dd>

An [**SoHAttributeType**](sohattributetype-enum.md) structure that contains the attribute type to locate.

</dd> <dt>

*attributeLocation* \[out\]
</dt> <dd>

A pointer that contains the location (index) in the SoH packet of the first attribute of type *SoHAttributeType* from the index *fromLocation*.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                            | Description                                                        |
|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>                  | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl>        | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>         | System resource limit, could not perform the operation.<br/> |
| <dl> <dt>**ERROR\_FILE\_NOT\_FOUND**</dt> </dl> | Attribute not found.<br/>                                    |



 

## Remarks

The **FindNextAttribute** method searches for attributes of type *SoHAttributeType* from the index specified by *fromLocation* and higher until a match is found. If no match is found, **ERROR\_FILE\_NOT\_FOUND** is returned.

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

 

 






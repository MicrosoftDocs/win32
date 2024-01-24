---
title: INapSoHConstructor AppendAttribute method (NapProtocol.h)
description: Adds a TLV to the end of the SoH buffer.
ms.assetid: 5706ceaa-757f-49d2-90e0-011415853875
keywords:
- AppendAttribute method NAP
- AppendAttribute method NAP , INapSoHConstructor interface
- INapSoHConstructor interface NAP , AppendAttribute method
topic_type:
- apiref
api_name:
- INapSoHConstructor.AppendAttribute
api_location:
- qutil.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# INapSoHConstructor::AppendAttribute method

> [!Note]  
> The Network Access Protection platform is not available starting with Windows 10

 

The **INapSoHConstructor::AppendAttribute** method adds a TLV to the end of the SoH buffer.

## Syntax


```C++
HRESULT AppendAttribute(
  [in]       SoHAttributeType  type,
  [in] const SoHAttributeValue *value
);
```



## Parameters

<dl> <dt>

*type* \[in\]
</dt> <dd>

A [**SoHAttributeType**](sohattributetype-enum.md) enumeration that indicates the attribute type of the new TLV.

</dd> <dt>

*value* \[in\]
</dt> <dd>

A pointer to an [**SoHAttributeValue**](sohattributevalue-union.md) structure that contains the value for the new TLV.

</dd> </dl>

## Return value

Other COM-specific error codes also may be returned.



| Return code                                                                                     | Description                                                        |
|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <dl> <dt>**S\_OK** </dt> </dl>           | Operation succeeded.<br/>                                    |
| <dl> <dt>**E\_ACCESSDENIED** </dt> </dl> | Permissions error, access denied.<br/>                       |
| <dl> <dt>**E\_OUTOFMEMORY** </dt> </dl>  | System resource limit, could not perform the operation.<br/> |



 

## Remarks

The [**sohAttributeTypeSystemHealthId**](sohattributetype-enum.md) TLV must not be added using this function. It is added as the first TLV by [**INapSoHConstructor::Initialize**](inapsohconstructor-initialize-method.md) to newly constructed SOH packets.

When appending an attribute which will be consumed by the Nap System, it should not be encrypted or modified in any manner. If the HealthEntity requires encryption/integrity checking (MACs) of private information, it should be included only in the [**sohAttributeTypeVendorSpecific**](sohattributetype-enum.md) attribute.

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

[**INapSoHConstructor**](inapsohconstructor.md)
</dt> </dl>

 

 






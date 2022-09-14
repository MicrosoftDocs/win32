---
description: The Get method retrieves the value of a given stream quality property.
ms.assetid: a8b5b8c7-47c9-4561-be96-af8416d854dc
title: ITStreamQualityControl::Get method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITStreamQualityControl::Get method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Get** method retrieves the value of a given [**stream quality property**](streamqualityproperty.md).

## Syntax


```C++
HRESULT Get(
  [in]  StreamQualityProperty Property,
  [out] long                  *plValue,
  [out] TAPIControlFlags      *plFlags
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

Member of the [**StreamQualityProperty**](streamqualityproperty.md) enum.

</dd> <dt>

*plValue* \[out\]
</dt> <dd>

Value of the input *Property*.

</dd> <dt>

*plFlags* \[out\]
</dt> <dd>

Value of the [**TAPIControlFlags**](tapicontrolflags.md) enum indicating how the *Property* value is controlled.

</dd> </dl>

## Return value

This method can return one of these values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Method succeeded.<br/>                                    |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Insufficient memory exists to perform the operation.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|--------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.1<br/>                                                         |
| Header<br/>       | <dl> <dt>Ipmsp.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>  |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITStreamQualityControl**](itstreamqualitycontrol.md)
</dt> <dt>

[**TAPIControlFlags**](tapicontrolflags.md)
</dt> <dt>

[**StreamQualityProperty**](streamqualityproperty.md)
</dt> </dl>

 

 





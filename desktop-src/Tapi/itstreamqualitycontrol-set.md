---
description: The Set method sets the value of a given stream quality property.
ms.assetid: 57029d1c-ac63-45c0-9d07-43c7b46a27b1
title: ITStreamQualityControl::Set method (Ipmsp.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITStreamQualityControl::Set method

\[ This method is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **Set** method sets the value of a given [**stream quality property**](streamqualityproperty.md).

## Syntax


```C++
HRESULT Set(
  [in] StreamQualityProperty Property,
  [in] long                  lValue,
  [in] TAPIControlFlags      lFlags
);
```



## Parameters

<dl> <dt>

*Property* \[in\]
</dt> <dd>

Member of the [**StreamQualityProperty**](streamqualityproperty.md) enum.

</dd> <dt>

*lValue* \[in\]
</dt> <dd>

Desired value for the input *Property*.

</dd> <dt>

*lFlags* \[in\]
</dt> <dd>

Value of the [**TAPIControlFlags**](tapicontrolflags.md) enum indicating how the *Property* value is to be controlled.

</dd> </dl>

## Return value

This method can return one of these values.



| Value                                                                                         | Meaning                                                         |
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

 

 





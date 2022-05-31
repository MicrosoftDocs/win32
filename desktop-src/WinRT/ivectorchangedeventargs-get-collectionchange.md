---
description: Describes the **IVectorChangedEventArgs::get_CollectionChange** method, and documents its syntax, parameters, return value, and requirements.
ms.assetid: 213f4794-b972-44e3-a400-8a24b1583ddd
title: IVectorChangedEventArgs::get_CollectionChange method (IVectorChangedEventArgs.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IVectorChangedEventArgs.get_CollectionChange
api_type: 
- COM
api_location: 
- IVectorChangedEventArgs.h
---

# IVectorChangedEventArgs::get\_CollectionChange method

Gets the type of change that occurred in the vector.

## Syntax


```C++
HRESULT get_CollectionChange(
  [out, retval] CollectionChange *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

Type: **CollectionChange\***

A value from the [**CollectionChange**](/uwp/api/Windows.Foundation.Collections.CollectionChange) enumeration that describes the change.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Header<br/>                   | <dl> <dt>IVectorChangedEventArgs.h</dt> </dl> |



## See also

<dl> <dt>

[**IVectorChangedEventArgs**](ivectorchangedeventargs.md)
</dt> </dl>

 

 

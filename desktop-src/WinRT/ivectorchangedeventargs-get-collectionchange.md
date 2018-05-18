---
Description: 'Gets the type of change that occurred in the vector.'
ms.assetid: '213f4794-b972-44e3-a400-8a24b1583ddd'
title: 'IVectorChangedEventArgs::get\_CollectionChange method'
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

A value from the [**CollectionChange**](w_found_coll.collectionchange) enumeration that describes the change.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                       |
| Header<br/>                   | <dl> <dt>IVectorChangedEventArgs.h</dt> </dl> |



## See also

<dl> <dt>

[**IVectorChangedEventArgs**](ivectorchangedeventargs.md)
</dt> </dl>

 

 





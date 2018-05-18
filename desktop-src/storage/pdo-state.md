---
title: PDO\_STATE enumeration
description: This enumeration describes the states of Physical Device Objects (PDOs).
ms.assetid: '006e2cef-4e49-4819-bfce-d9bf5983643e'
keywords: ["PDO_STATE enumeration Storage Devices"]
topic_type:
- apiref
api_name:
- PDO_STATE
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
---

# PDO\_STATE enumeration

This enumeration describes the states of Physical Device Objects (PDOs).

## Syntax


```C++
typedef enum _PDO_STATE { 
  PDO_STATE_UNDEFINED    = 0,
  PDO_STATE_STARTED      = 1,
  PDO_STATE_NOT_STARTED  = 2
} PDO_STATE;
```



## Constants

<dl> <dt>

<span id="PDO_STATE_UNDEFINED"></span><span id="pdo_state_undefined"></span>**PDO\_STATE\_UNDEFINED**
</dt> <dd>

This value indicates that the PDO state is undefined.

</dd> <dt>

<span id="PDO_STATE_STARTED"></span><span id="pdo_state_started"></span>**PDO\_STATE\_STARTED**
</dt> <dd>

This value indicates that the PDO is started.

</dd> <dt>

<span id="PDO_STATE_NOT_STARTED"></span><span id="pdo_state_not_started"></span>**PDO\_STATE\_NOT\_STARTED**
</dt> <dd>

This value indicates that the PDO is not started.

</dd> </dl>

## Remarks

## Requirements



|                   |                                                                                                                  |
|-------------------|------------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PDO_STATE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






---
description: The TAPI LINE\_ADDRESSSTATE message is sent when the status of an address changes on a line that is currently open by the application. The application can invoke lineGetAddressStatus to determine the current status of the address.
ms.assetid: af211fa1-79f8-49ac-a1d8-b62981f50519
title: LINE_ADDRESSSTATE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_ADDRESSSTATE message

The TAPI **LINE\_ADDRESSSTATE** message is sent when the status of an address changes on a line that is currently open by the application. The application can invoke [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus) to determine the current status of the address.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the line device.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The address identifier of the address that changed status.

</dd> <dt>

*dwParam2* 
</dt> <dd>

The address state that changed. Can be one or more of the [**LINEADDRESSSTATE\_ constants**](lineaddressstate--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Return value

No return value.

## Remarks

The **LINE\_ADDRESSSTATE** message is sent to any application that has opened the line device and that has enabled this message. The sending of this message for the various status items can be controlled and queried using [**lineGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linegetstatusmessages) and [**lineSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linesetstatusmessages). By default, address status reporting is disabled.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.0 or later<br/>                                             |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)
</dt> <dt>

[**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)
</dt> <dt>

[**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus)
</dt> <dt>

[**lineGetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linegetstatusmessages)
</dt> <dt>

[**lineSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linesetstatusmessages)
</dt> </dl>

 

 





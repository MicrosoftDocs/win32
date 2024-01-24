---
description: UdpIp_Fail class - This class is the event type class for TCP/IP failure events. The following syntax is simplified from MOF code.
ms.assetid: 552e63ef-70e4-4bc4-be33-bd77bd5acd61
title: UdpIp_Fail class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- UdpIp_Fail
- UdpIp_Fail.Proto
- UdpIp_Fail.FailureCode
api_type: 
- NA
api_location: 
---

# UdpIp\_Fail class

This class is the event type class for TCP/IP failure events.

The following syntax is simplified from MOF code.

## Syntax

``` syntax
[EventType{17}, EventTypeName{"Fail"}]
class UdpIp_Fail : UdpIp
{
  uint16 Proto;
  uint16 FailureCode;
};
```

## Members

The **UdpIp\_Fail** class has these types of members:

-   [Properties](#properties)

### Properties

The **UdpIp\_Fail** class has these properties.

<dl> <dt>

**FailureCode**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reason for the failure. Can be one of the following codes:

<dl> <dt>

<span id="ERROR_INSUFFICIENT_RESOURCES"></span><span id="error_insufficient_resources"></span>**ERROR\_INSUFFICIENT\_RESOURCES** (1)
</dt> <dt>

<span id="ERROR_TOO_MANY_ADDRESSES"></span><span id="error_too_many_addresses"></span>**ERROR\_TOO\_MANY\_ADDRESSES** (2)
</dt> <dt>

<span id="ERROR_ADDRESS_EXISTS"></span><span id="error_address_exists"></span>**ERROR\_ADDRESS\_EXISTS** (3)
</dt> <dt>

<span id="ERROR_INVALID_ADDRESS"></span><span id="error_invalid_address"></span>**ERROR\_INVALID\_ADDRESS** (4)
</dt> <dt>

<span id="ERROR_OTHER"></span><span id="error_other"></span>**ERROR\_OTHER** (5)
</dt> <dt>

<span id="ERROR_TIMEWAIT_ADDRESS_EXIST"></span><span id="error_timewait_address_exist"></span>**ERROR\_TIMEWAIT\_ADDRESS\_EXIST** (6)
</dt> </dl>

</dd> <dt>

**Proto**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the protocol. Can be one of the following values:



| Value                                                                                                                                                                                                  | Meaning                                                            |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| <span id="AF_INET"></span><span id="af_inet"></span><dl> <dt>**AF\_INET**</dt> <dt>2</dt> </dl>     | The Internet Protocol version 4 (IPv4) address family.<br/>  |
| <span id="AF_INET6"></span><span id="af_inet6"></span><dl> <dt>**AF\_INET6**</dt> <dt>23</dt> </dl> | The Internet Protocol version 6 (IPv6) address family..<br/> |



 

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[**UdpIp**](udpip.md)
</dt> </dl>

 

 





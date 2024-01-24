---
description: The following table describes IP\_DSCP\_TRAFFIC\_TYPE Socket Options.
ms.assetid: 0042B53F-B84E-453A-8E18-87052280DAD5
title: IP_DSCP_TRAFFIC_TYPE
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IP_DSCP_TRAFFIC_TYPE
api_type: 
- HeaderDef
api_location: 
- N/A
---

# IP\_DSCP\_TRAFFIC\_TYPE

The following table describes IP\_DSCP\_TRAFFIC\_TYPE Socket Options.

<dl> <dt><span id="IP_DSCP_TRAFFIC_TYPE"></span><span id="ip_dscp_traffic_type"></span>**IP\_DSCP\_TRAFFIC\_TYPE**</dt> <dd> <dl> <dt> 

| Option              | Get | Set | Optval Type | Description                                                                                                                                                                                                                                                                                                                                      |
|---------------------|-----|-----|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DSCP\_TRAFFIC\_TYPE | Yes | Yes | DWORD       | By setting this value to values defined in **DSCP\_TRAFFIC\_TYPE**, an application will be able to ask its network packets to be treated according to the type of service being requested. Similarly calls to [**getsockopt**](/windows/desktop/api/winsock/nf-winsock-getsockopt) can be used to obtain the current setting for the type of traffic requested on the given socket |



 


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|----------------------------------|--------------------------------------------------------------------------------|
| End of client support<br/> | Windows 10<br/>                                                          |
| End of server support<br/> | Windows Server 2016<br/>                                                 |
| Header<br/>                | <dl> <dt>N/A</dt> </dl> |



 

 





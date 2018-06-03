---
title: RequestResponse method of the Microsoft\_IPMI class
description: Sends a request for data from an IPMI provider to the IPMI driver.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e0adbc24-2aa5-48c9-b2da-7ba328da8cb9
ms.prod: windows-server-dev
ms.technology:
- intelligent-platform-management-interface
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- IPMI driver WS-Management
- RequestResponse method
- RequestResponse method, Microsoft_IPMI class
- Microsoft_IPMI class, RequestResponse method
topic_type:
- apiref
api_name:
- Microsoft_IPMI.RequestResponse
api_location:
- IpmiDrv.sys
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RequestResponse method of the Microsoft\_IPMI class

Sends a request for data from an IPMI provider to the IPMI driver.

## Syntax


```mof
void RequestResponse(
  [in]  uint8  Command,
  [out] uint8  CompletionCode,
  [in]  uint8  Lun,
  [in]  uint8  NetworkFunction,
  [in]  uint8  RequestData[],
  [out] uint32 ResponseDataSize,
  [in]  uint32 RequestDataSize,
  [in]  uint8  ResponderAddress,
  [out] uint8  ResponseData
);
```



## Parameters

<dl> <dt>

*Command* \[in\]
</dt> <dd>

IPMI request command.

</dd> <dt>

*CompletionCode* \[out\]
</dt> <dd>

Completion code for the status of the request response.

<dt>

0 (0x0)
</dt> <dd>

Command completed normally.

</dd> <dt>

192 (0xC0)
</dt> <dd>

Node busy.

</dd> <dt>

193 (0xC1)
</dt> <dd>

The command is not valid.

</dd> <dt>

194 (0xC2)
</dt> <dd>

The command is not valid for given LUN.

</dd> <dt>

195 (0xC3)
</dt> <dd>

Time-out while processing command.

</dd> <dt>

196 (0xC4)
</dt> <dd>

Out of space.

</dd> <dt>

197 (0xC5)
</dt> <dd>

Reservation canceled or reservation ID is not valid.

</dd> <dt>

198 (0xC6)
</dt> <dd>

Request data truncated.

</dd> <dt>

199 (0xC7)
</dt> <dd>

Request data length is not valid.

</dd> <dt>

200 (0xC8)
</dt> <dd>Request data field length limit exceeded.</dd> <dt>

201 (0xC9)
</dt> <dd>

Parameter out of range.

</dd> <dt>

206 (0xCE)
</dt> <dd>

Cannot return number of requested data bytes.

</dd> <dt>

203 (0xCB)
</dt> <dd>

Requested sensor, data, or record not present.

</dd> <dt>

204 (0xCC)
</dt> <dd>

Data field in request is not valid.

</dd> <dt>

205 (0xCD)
</dt> <dd>

Command illegal for specified sensor or record type.

</dd> <dt>

206 (0xCE)
</dt> <dd>

Command response could not be provided.

</dd> <dt>

207 (0xCF)
</dt> <dd>

Cannot execute duplicated request.

</dd> <dt>

208 (0xD0)
</dt> <dd>

Command response could not be provided. SDR repository in update mode.

</dd> <dt>

209 (0xD1)
</dt> <dd>

Command response could not be provided. Device in firmware update mode.

</dd> <dt>

210 (0xD2)
</dt> <dd>

Command response could not be provided. BMC initialization in progress.

</dd> <dt>

211 (0xD3)
</dt> <dd>

Destination unavailable.

</dd> <dt>

212 (0xD4)
</dt> <dd>

Cannot execute command. Insufficient privilege level.

</dd> <dt>

213 (0xD5)
</dt> <dd>

Cannot execute command. Command, or request parameters, not supported in present state.

</dd> <dt>

1 126
</dt> <dd>

Unspecified error.

</dd> <dt>

128 190
</dt> <dd>

Device-specific (OEM) completion codes.

</dd> <dt>

214 255
</dt> <dd>

Standard command-specific codes. reserved.

</dd> </dl> </dd> <dt>

*Lun* \[in\]
</dt> <dd>

Logical unit number to which IPMI request is sent.

</dd> <dt>

*NetworkFunction* \[in\]
</dt> <dd>

Network function for the IPMI request.

</dd> <dt>

*RequestData* \[in\]
</dt> <dd>

Byte array containing IPMI request data.

</dd> <dt>

*ResponseDataSize* \[out\]
</dt> <dd>

Number of bytes for IPMI response data. Completion code is included in this size.

</dd> <dt>

*RequestDataSize* \[in\]
</dt> <dd>

Number of bytes in *RequestData*.

</dd> <dt>

*ResponderAddress* \[in\]
</dt> <dd>

Responder address to which IPMI request is sent.

</dd> <dt>

*ResponseData* \[out\]
</dt> <dd>

IPMI response data. Completion code is present in response data.

</dd> </dl>

## Return value

This method does not return a value.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\wmi<br/>                                                                   |
| DLL<br/>                      | <dl> <dt>IpmiDrv.sys</dt> </dl> |



## See also

<dl> <dt>

[**Microsoft\_IPMI**](microsoft-ipmi.md)
</dt> <dt>

[IPMI Provider](ipmi-provider.md)
</dt> </dl>

 

 






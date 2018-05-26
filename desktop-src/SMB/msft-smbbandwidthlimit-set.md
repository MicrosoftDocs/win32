---
title: Set method of the MSFT\_SmbBandwidthLimit class
description: Specifies the bandwidth limit for SMB traffic of the specified category.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E4103594-B5A6-4722-85DE-C3DF3571E078
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method SMB
- Set method SMB , MSFT_SmbBandwidthLimit class
- MSFT_SmbBandwidthLimit class SMB , Set method
topic_type:
- apiref
api_name:
- MSFT_SmbBandwidthLimit.Set
api_location:
- SmbWmiV2.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the MSFT\_SmbBandwidthLimit class

Specifies the bandwidth limit for SMB traffic of the specified category.

## Syntax


```mof
uint32 Set(
  [in]  uint32                 Category,
  [in]  uint64                 BytesPerSecond,
  [out] MSFT_SmbBandwidthLimit Output[]
);
```



## Parameters

<dl> <dt>

*Category* \[in\]
</dt> <dd>

The category that specifies the type of SMB traffic to throttle.

<dt>

"0"
</dt> <dd>

Regular Hyper-V over SMB traffic.

</dd> <dt>

"1"
</dt> <dd>

Live migration traffic.

</dd> <dt>

"2"
</dt> <dd>

All other traffic.

</dd> </dl> </dd> <dt>

*BytesPerSecond* \[in\]
</dt> <dd>

The bandwidth limit in bytes per second.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Receives an instance of the updated [**MSFT\_SmbBandwidthLimit**](msft-smbbandwidthlimit.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                       |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Smb<br/>                                                |
| MOF<br/>                      | <dl> <dt>SmbWmiV2.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SmbWmiV2.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SmbBandwidthLimit**](msft-smbbandwidthlimit.md)
</dt> </dl>

 

 






---
title: GetSupportedStripeLengthRange method of the MSISCSITARGET\_StorageCapabilities class
description: Retrieves the supported range of extent stripe lengths for systems that support a range of lengths.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6f2bf3a9-b506-4858-b761-dae22ee466ec
ms.prod: windows-server-dev
ms.technology:
- iscsi-target
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetSupportedStripeLengthRange method iSCSI Software Target API
- GetSupportedStripeLengthRange method iSCSI Software Target API , MSISCSITARGET_StorageCapabilities class
- MSISCSITARGET_StorageCapabilities class iSCSI Software Target API , GetSupportedStripeLengthRange method
topic_type:
- apiref
api_name:
- MSISCSITARGET_StorageCapabilities.GetSupportedStripeLengthRange
api_location:
- SmIScsiTargetProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetSupportedStripeLengthRange method of the MSISCSITARGET\_StorageCapabilities class

Retrieves the supported range of extent stripe lengths for systems that support a range of lengths. Retrieved values can change after the call due to requests from other clients.

Different implementations can support either the [**GetSupportedStripeLengths**](getsupportedstripelengths-msiscsitarget-storagecapabilities.md) or the **GetSupportedStripeLengthRange** method. If the system only supports discrete values, then this method returns **Use GetSupportedStripeLengths instead** (3) .

This method is inherited from the **CIM\_StorageCapabilities** class.

## Syntax


```mof
uint32 GetSupportedStripeLengthRange(
  [out] uint16 MinimumStripeLength,
  [out] uint16 MaximumStripeLength,
  [out] uint32 StripeLengthDivisor
);
```



## Parameters

<dl> <dt>

*MinimumStripeLength* \[out\]
</dt> <dd>

On return, indicates the minimum extent stripe length for a volume or pool in bytes.

</dd> <dt>

*MaximumStripeLength* \[out\]
</dt> <dd>

On return, indicates the maximum extent stripe length for a volume or pool in bytes.

</dd> <dt>

*StripeLengthDivisor* \[out\]
</dt> <dd>

On return, indicates the size in bytes of an incremental unit of stripe length. The user data stripe length for a volume or pool must be an even multiple of this value.

</dd> </dl>

## Return value

<dl> <dt>

**Method completed OK** (0)
</dt> <dt>

**Method not supported** (1)
</dt> <dt>

**Choices not available for this capability** (2)
</dt> <dt>

**Use GetSupportedStripeLengths instead** (3)
</dt> </dl>

## Requirements



|                                     |                                                                                                  |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                                |
| Namespace<br/>                | Root\\CIMv2\\Storage\\iScsiTarget<br/>                                                     |
| MOF<br/>                      | <dl> <dt>Smiscsitarget.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>SmIScsiTargetProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSISCSITARGET\_StorageCapabilities**](msiscsitarget-storagecapabilities.md)
</dt> <dt>

[**GetSupportedStripeLengths**](getsupportedstripelengths-msiscsitarget-storagecapabilities.md)
</dt> </dl>

 

 






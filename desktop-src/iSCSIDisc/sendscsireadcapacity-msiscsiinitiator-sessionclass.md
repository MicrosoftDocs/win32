---
Description: TheSendScsiReadCapacitymethod sends the SCSI Read Capacity command to the specified Logical Unit Number (LUN).
ms.assetid: 0686a59d-d097-4cf2-98ce-b803403ec465
title: SendScsiReadCapacity method of the MSIscsiInitiator\_SessionClass class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SendScsiReadCapacity method of the MSIscsiInitiator\_SessionClass class

The**SendScsiReadCapacity**method sends the SCSI Read Capacity command to the specified Logical Unit Number (LUN).

## Syntax


```mof
uint32 SendScsiReadCapacity(
  [in]  uint64 Lun,
  [out] uint8  ScsiStatus,
  [out] uint8  ResponseBuffer[],
  [out] uint8  SenseBuffer[]
);
```



## Parameters

<dl> <dt>

*Lun* \[in\]
</dt> <dd>

The LUN to query for SCSI inquiry data.

</dd> <dt>

*ScsiStatus* \[out\]
</dt> <dd>

The execution status of the CDB.

</dd> <dt>

*ResponseBuffer* \[out\]
</dt> <dd>

A buffer containing the inquiry data.

</dd> <dt>

*SenseBuffer* \[out\]
</dt> <dd>

A buffer containing the sense data.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Namespace<br/>                | Root\\WMI<br/>                                                                    |
| MOF<br/>                      | <dl> <dt>Iscsidsc.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSIscsiInitiator\_SessionClass**](msiscsiinitiator-sessionclass.md)
</dt> </dl>

 

 





---
Description: 'The SendScsiInquiry method sends SCSI inquiry command to the specified Logical Unit Number (LUN).'
ms.assetid: '30f3e173-93a3-485d-a48a-68ec5790efdb'
title: 'SendScsiInquiry method of the MSIscsiInitiator\_SessionClass class'
---

# SendScsiInquiry method of the MSIscsiInitiator\_SessionClass class

The [**SendScsiInquiry**](sendscsiinquiry.md) method sends SCSI inquiry command to the specified Logical Unit Number (LUN).

## Syntax


```mof
uint32 SendScsiInquiry(
  [in]  uint64 Lun,
  [in]  uint8  EvpdCmddt,
  [in]  uint8  PageCode,
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

*EvpdCmddt* \[in\]
</dt> <dd>

The values to assign to the EVP (Enable Vital Product data) and CmdDt (Command Support Data) bits in the INQUERY command. Bits 0 (EVP) and 1 (CmdDt) of the *EvpdCmddt* parameter are inserted into bits 0 and 1, respectively, of the second byte of the Command Descriptor Block (CDB) of the INQUIRY command.

</dd> <dt>

*PageCode* \[in\]
</dt> <dd>

The page code, which is inserted into the third byte of the CDB of the INQUERY command.

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

 

 





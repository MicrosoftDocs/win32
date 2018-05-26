---
Description: The SendScsiReportLuns method sends the Report LUN command to the target associated with the specified session.
ms.assetid: a928d44d-3da3-44ef-ac6c-0fd1a669fa17
title: SendScsiReportLuns method of the MSIscsiInitiator\_SessionClass class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SendScsiReportLuns method of the MSIscsiInitiator\_SessionClass class

The [**SendScsiReportLuns**](/windows/previous-versions/Iscsidsc/nf-iscsidsc-sendscsireportluns?branch=master) method sends the Report LUN command to the target associated with the specified session.

## Syntax


```mof
uint32 SendScsiReportLuns(
  [out] uint8 ScsiStatus,
  [out] uint8 ResponseBuffer[],
  [out] uint8 SenseBuffer[]
);
```



## Parameters

<dl> <dt>

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

 

 





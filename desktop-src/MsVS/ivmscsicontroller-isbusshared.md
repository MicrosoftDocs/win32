---
title: IVMSCSIController IsBusShared property
description: The IsBusShared property indicates whether the SCSI controller is on a shared SCSI bus.
ms.assetid: '39a153fc-60cc-4a3d-adb8-93485d11710c'
keywords: ["IsBusShared property Virtual Server", "IsBusShared property Virtual Server , IVMSCSIController interface", "IVMSCSIController interface Virtual Server , IsBusShared property", "IsBusShared property Virtual Server , VMSCSIController interface", "VMSCSIController interface Virtual Server , IsBusShared property"]
topic_type:
- apiref
api_name:
- IVMSCSIController.IsBusShared
- IVMSCSIController.get_IsBusShared
- VMSCSIController.IsBusShared
api_location:
- VsComInterfaces.h
api_type:
- COM
---

# IVMSCSIController::IsBusShared property

The **IsBusShared** property indicates whether the SCSI controller is on a shared SCSI bus.

This property is read-only.

## Syntax


```C++
HRESULT get_IsBusShared(
  [out] VARIANT_BOOL *isBusShared
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>VMSCSIController.IsBusShared( _
  ByRef isBusShared _
)</code></pre></td>
</tr>
</tbody>
</table>



## Property value

Contains **vbTrue** if the SCSI controller is on a shared SCSI bus.

This property value is read-only.

## Error codes



| Name                                                                                          | Meaning                                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>              | The operation was successful.<br/>                                |
| <dl> <dt>E\_POINTER</dt> </dl>         | The *isBusShared* parameter is **NULL**.<br/>                     |
| <dl> <dt>VM\_E\_VM\_UNKNOWN</dt> </dl> | The virtual machine for this SCSI controller does not exist.<br/> |
| <dl> <dt>DISP\_E\_EXCEPTION</dt> </dl> | An unexpected error has occurred.<br/>                            |



## Requirements



|                     |                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------|
| Product<br/>  | Microsoft Virtual Server 2005 onWindows Server 2003<br/>                                    |
| Download<br/> | Microsoft Virtual Server 2005 R2 SP1 Update onWindows Server 2008orWindows Server 2003<br/> |
| Header<br/>   | <dl> <dt>VsComInterfaces.h</dt> </dl>      |



## See also

<dl> <dt>

[**IVMSCSIController**](ivmscsicontroller.md)
</dt> </dl>

 

 






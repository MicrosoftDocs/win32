---
description: Define the set of actions for the IOCTL\_STORAGE\_MANAGE\_DATA\_SET\_ATTRIBUTES control code.
ms.assetid: ff688c9a-8669-4699-aab9-1e2e3a5c7fca
title: DEVICE_DATA_MANAGEMENT_SET_ACTION (WinIoCtl.h)
ms.topic: reference
ms.date: 05/31/2018
---

# DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION

The following constant values are the set of possible values for the **DEVICE\_DATA\_MANAGEMENT\_SET\_ACTION** type, which is defined as type **DWORD**.

<dl> <dt>

<span id="DeviceDsmAction_None"></span><span id="devicedsmaction_none"></span><span id="DEVICEDSMACTION_NONE"></span>**DeviceDsmAction\_None**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



No action is performed.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Trim"></span><span id="devicedsmaction_trim"></span><span id="DEVICEDSMACTION_TRIM"></span>**DeviceDsmAction\_Trim**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



A trim action is performed.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Notification"></span><span id="devicedsmaction_notification"></span><span id="DEVICEDSMACTION_NOTIFICATION"></span>**DeviceDsmAction\_Notification**
</dt> <dd> <dl> <dt>

2 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000002)
</dt> <dt>



A notification action is performed. The parameters are in a [**DEVICE\_DSM\_NOTIFICATION\_PARAMETERS**](/windows/desktop/api/WinIoCtl/ns-winioctl-device_dsm_notification_parameters) structure. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_OffloadRead"></span><span id="devicedsmaction_offloadread"></span><span id="DEVICEDSMACTION_OFFLOADREAD"></span>**DeviceDsmAction\_OffloadRead**
</dt> <dd> <dl> <dt>

3 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000003)
</dt> <dt>



An offload read action is performed. The parameters are in a [**DEVICE\_DSM\_OFFLOAD\_READ\_PARAMETERS**](/windows/desktop/api/WinIoCtl/ns-winioctl-device_dsm_offload_read_parameters) structure. The output is in a [**STORAGE\_OFFLOAD\_READ\_OUTPUT**](/windows/desktop/api/WinIoCtl/ns-winioctl-storage_offload_read_output) structure. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_OffloadWrite"></span><span id="devicedsmaction_offloadwrite"></span><span id="DEVICEDSMACTION_OFFLOADWRITE"></span>**DeviceDsmAction\_OffloadWrite**
</dt> <dd> <dl> <dt>

4
</dt> <dt>



An offload write action is performed. The parameters are in a [**DEVICE\_DSM\_OFFLOAD\_WRITE\_PARAMETERS**](/windows/desktop/api/WinIoCtl/ns-winioctl-device_dsm_offload_write_parameters) structure. The output is in a [**STORAGE\_OFFLOAD\_WRITE\_OUTPUT**](/windows/desktop/api/WinIoCtl/ns-winioctl-storage_offload_write_output) structure.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Allocation"></span><span id="devicedsmaction_allocation"></span><span id="DEVICEDSMACTION_ALLOCATION"></span>**DeviceDsmAction\_Allocation**
</dt> <dd> <dl> <dt>

5 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000005)
</dt> <dt>



An allocation bitmap is returned for the first data set range passed in. The output is in a [**DEVICE\_DATA\_SET\_LB\_PROVISIONING\_STATE**](/windows/desktop/api/WinIoCtl/ns-winioctl-device_data_set_lb_provisioning_state) structure. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Repair"></span><span id="devicedsmaction_repair"></span><span id="DEVICEDSMACTION_REPAIR"></span>**DeviceDsmAction\_Repair**
</dt> <dd> <dl> <dt>

6 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000006)
</dt> <dt>



A repair action is performed. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Scrub"></span><span id="devicedsmaction_scrub"></span><span id="DEVICEDSMACTION_SCRUB"></span>**DeviceDsmAction\_Scrub**
</dt> <dd> <dl> <dt>

7 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000007)
</dt> <dt>



A scrub action is performed. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> <dt>

<span id="DeviceDsmAction_Resiliency"></span><span id="devicedsmaction_resiliency"></span><span id="DEVICEDSMACTION_RESILIENCY"></span>**DeviceDsmAction\_Resiliency**
</dt> <dd> <dl> <dt>

8 \| **DeviceDsmActionFlag\_NonDestructive** (0x80000008)
</dt> <dt>



A resiliency action is performed. The **DeviceDsmActionFlag\_NonDestructive** (0x80000000) is a bit flag to indicate to the driver stack that this operation is non-destructive.

**Windows 7 and Windows Server 2008 R2:** This value is not supported before Windows 8 and Windows Server 2012.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                                      |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                         |
| Header<br/>                   | <dl> <dt>WinIoCtl.h (include Windows.h)</dt> </dl> |



 

 





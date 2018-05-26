---
title: Ntddstor.h
description: This section contains reference topics for the Ntddstor.h header.
ms.assetid: 3A20AC4A-CE9E-4A75-883E-69A2D920C9AD
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ntddstor.h

This section contains reference topics for the Ntddstor.h header.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Data Set Management Structures](data-set-management-structures.md)<br/></td>

</tr>
<tr class="even">
<td>[Storage Firmware Update I/O Control Codes](storage-firmware-update-i-o-control-codes.md)<br/></td>
<td>The storage firmware update IOCTLs are used to update the storage firmware on a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[Storage Firmware Update Structures](storage-firmware-update-structures.md)<br/></td>
<td>This section describes structures that are associated with storage firmware update.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_COPY_OFFLOAD_DESCRIPTOR</strong>](device-copy-offload-descriptor.md)<br/></td>
<td>Used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to describe the copy offload capabilities of a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEVICE_LB_PROVISIONING_DESCRIPTOR</strong>](device-lb-provisioning-descriptor.md)<br/></td>
<td>The [<strong>DEVICE_LB_PROVISIONING_DESCRIPTOR</strong>](device-lb-provisioning-descriptor.md) structure is one of the query result structures returned from an [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request. This structure contains the thin provisioning capabilities for a storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_MEDIA_INFO</strong>](device-media-info.md)<br/></td>
<td>A storage class driver returns an array of [<strong>DEVICE_MEDIA_INFO</strong>](device-media-info.md) structures, embedded in a [<strong>GET_MEDIA_TYPES</strong>](get-media-types.md) structure, in response to an [<strong>IOCTL_STORAGE_GET_MEDIA_TYPES_EX</strong>](ioctl-storage-get-media-types-ex.md) device-control request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEVICE_POWER_DESCRIPTOR</strong>](device-power-descriptor.md)<br/></td>
<td>Used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) control code to describes the power capabilities of a storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_SEEK_PENALTY_DESCRIPTOR</strong>](device-seek-penalty-descriptor.md)<br/></td>
<td>The DEVICE_SEEK_PENALTY_DESCRIPTOR structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the seek penalty descriptor data for a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>DEVICE_TRIM_DESCRIPTOR</strong>](device-trim-descriptor.md)<br/></td>
<td>The DEVICE_TRIM_DESCRIPTOR structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the trim descriptor data for a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>DEVICE_WRITE_AGGREGATION_DESCRIPTOR</strong>](device-write-aggregation-descriptor.md)<br/></td>
<td>Reserved for system use.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_BREAK_RESERVATION</strong>](ioctl-storage-break-reservation.md)<br/></td>
<td>Breaks a disk reservation. In a multi-initiator (&quot;clustered&quot;) system, a single computer can reserve a disk resource, so that no other computer can access the disk. If the computer does not or cannot free the resource in a timely fashion, a means is needed to remove the reservation of the disk by force.<br/> One means of forcing the system to free a reserved disk resource is to reset the bus. In fact, for storage devices whose bus adapters are managed by the SCSI port driver, the IOCTL_STORAGE_BREAK_RESERVATION request is equivalent to [<strong>IOCTL_STORAGE_RESET_BUS</strong>](ioctl-storage-reset-bus.md), which simply does a reset of the bus, freeing all of its reserved resources.<br/> For storage devices whose bus adapters are managed by the STOR port driver, this I/O control code offers a better technique of breaking a disk reservation. That technique is called a &quot;hierarchical reset.&quot; Upon receiving an IOCTL_STORAGE_BREAK_RESERVATION request, the STOR port driver first attempts to remove the reserve on the logical unit by resetting the logical unit itself. If that fails, the STOR port driver attempts to reset the target device that is the parent of the logical unit. Only when resetting the target device fails will the port driver reset the bus.<br/> Resetting the bus clears all device reservations and transfer speed settings, which must then be renegotiated. Because this is a time-consuming operation, IOCTL_STORAGE_BREAK_RESERVATION is always to be preferred to a simple bus reset. <br/> The caller requires only read access to issue a bus reset. <br/> The <strong>SrbStatus</strong> flag of pending SRBs is set to SRB_STATUS_BUS_RESET. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_CHECK_VERIFY</strong>](ioctl-storage-check-verify.md)<br/></td>
<td>Determines whether the media has changed on a removable-media device that the caller has opened for read or write access. If read or write access to the device is not necessary, the caller can improve performance by opening the device with FILE_READ_ATTRIBUTES and issuing an[<strong>IOCTL_STORAGE_CHECK_VERIFY2</strong>](ioctl-storage-check-verify2.md) request instead. <br/> For more information, see [Supporting Removable Media](https://msdn.microsoft.com/library/windows/hardware/ff563916).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_CHECK_VERIFY2</strong>](ioctl-storage-check-verify2.md)<br/></td>
<td>Determines whether the media has changed on a removable-media device - the caller has opened with FILE_READ_ATTRIBUTES. Because no file system is mounted when a device is opened in this way, this request can be processed much more quickly than an IOCTL_STORAGE_CHECK_VERIFY request.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_DEVICE_POWER_CAP</strong>](ioctl-storage-device-power-cap.md)<br/></td>
<td>A driver can use <strong>IOCTL_STORAGE_DEVICE_POWER_CAP</strong> to specify a maximum operational power consumption level for a storage device. The OS will do it's best to transition the device to a power state that will not exceed the given maximum. However, this depends on what the device supports. The actual maximum may be less than or greater than the desired maximum.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_EJECT_MEDIA</strong>](ioctl-storage-eject-media.md)<br/></td>
<td>Causes the device to eject the media if the device supports ejection capabilities.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_EJECTION_CONTROL</strong>](ioctl-storage-ejection-control.md)<br/></td>
<td>Locks the device to prevent removal of the media. If the driver can prevent the media from being removed while the drive is in use, the driver disables or enables the mechanism that ejects media, thereby locking the drive. A caller must open the device with FILE_READ_ATTRIBUTES to send this request. <br/> Unlike [<strong>IOCTL_STORAGE_MEDIA_REMOVAL</strong>](ioctl-storage-media-removal.md), the driver tracks [<strong>IOCTL_STORAGE_EJECTION_CONTROL</strong>](ioctl-storage-ejection-control.md) requests by caller and ignores unlock requests for which it has not received a lock request from the same caller, thereby preventing other callers from unlocking the drive.<br/> A driver for a removable-media device - can support this IOCTL must do the following:<br/>
<ol>
<li>Keep a lock count, tagged by caller, in the device object extension.<br/></li>
<li>Keep the lock count per physical device.<br/></li>
<li>When called with this IOCTL, if the flag to prevent removing the media is set, increment the count; if the flag is clear and the driver has previously received a lock request from the same caller, decrement the count.<br/></li>
<li>Prevent removal of the media unless all lock counts are zero.<br/></li>
</ol>
Under normal circumstances, the caller who locked the device using IOCTL_STORAGE_EJECTION_CONTROL, unlocks the device by sending IOCTL_STORAGE_EJECTION_CONTROL again with <strong>Irp-&gt;AssociatedIrp.SystemBuffer</strong> set to a boolean value of <strong>FALSE</strong>. However, sometimes the caller fails to unlock the device properly. <br/> To ensure that media removal locks are released properly, the class driver keeps track of callers who lock the media with IOCTL_STORAGE_EJECTION_CONTROL. If the caller terminates without unlocking the device, the class driver unlocks the device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_FIND_NEW_DEVICES</strong>](ioctl-storage-find-new-devices.md)<br/></td>
<td>Determines whether another device that the driver supports has been connected to the I/O bus, either since the system was booted or since the driver last processed this request. <br/> This IOCTL is obsolete in the Plug and Play environment. Plug and Play class drivers handle this request by calling [<strong>IoInvalidateDeviceRelations</strong>](https://msdn.microsoft.com/library/windows/hardware/ff549353) with the device relations type <strong>BusRelations</strong>. If a new device is found, the class driver's <em>AddDevice</em> routine will be called. <br/> Legacy class drivers can continue to handle this IOCTL without modifications. If a new device is found, the driver sets up any necessary system objects and resources to handle I/O requests for its new device. It also initializes the device on receipt of this request dynamically, that is, without requiring the machine to be rebooted. Such a driver is assumed to support devices connected on a dynamically configurable I/O bus.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_GET_DEVICE_NUMBER</strong>](ioctl-storage-get-device-number.md)<br/></td>
<td>Returns a [<strong>STORAGE_DEVICE_NUMBER</strong>](storage-device-number.md) structure that contains the FILE_DEVICE_<em>XXX</em> type, device number, and, for a partitionable device, the partition number assigned to a device by the driver when the device is started. This request is usually issued by a fault-tolerant disk driver. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_GET_HOTPLUG_INFO</strong>](ioctl-storage-get-hotplug-info.md)<br/></td>
<td>Retrieves the hotplug configuration of the specified device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</strong>](ioctl-storage-get-lb-provisioning-map-resources.md)<br/></td>
<td>The [<strong>IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</strong>](ioctl-storage-get-lb-provisioning-map-resources.md) request is sent to the storage class driver to determine available and used mapping resources on a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_GET_MEDIA_SERIAL_NUMBER</strong>](ioctl-storage-get-media-serial-number.md)<br/></td>
<td>Queries the USB generic parent driver for the serial number of a USB device. If a USB device has a CSM-1 content security interface, a USB client driver can query for its serial number using this request. USB client drivers that help implement a digital rights management (DRM) system can use this information to ensure that only legitimate customers have access to digitized intellectual property. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_GET_MEDIA_TYPES</strong>](ioctl-storage-get-media-types.md)<br/></td>
<td>Returns information about the geometry of floppy drives.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_GET_MEDIA_TYPES_EX</strong>](ioctl-storage-get-media-types-ex.md)<br/></td>
<td>Returns information about the types of media supported by a device. A storage class driver must handle this IOCTL to control devices to be accessed by the removable storage manager (RSM) either as stand-alone devices or as data transfer elements (drives) in a media library or changer device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS</strong>](ioctl-storage-get-physical-element-status.md)<br/></td>
<td>The [<strong>IOCTL_STORAGE_GET_PHYSICAL_ELEMENT_STATUS</strong>](ioctl-storage-get-physical-element-status.md) control code queries for and returns the physical element status from a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_LOAD_MEDIA</strong>](ioctl-storage-load-media.md)<br/></td>
<td>Causes media to be loaded in a device that the caller has opened for read or write access. If read or write access to the device is not necessary, the caller can improve performance by opening the device with FILE_READ_ATTRIBUTES and issuing an [<strong>IOCTL_STORAGE_LOAD_MEDIA2</strong>](ioctl-storage-load-media2.md) request instead. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_LOAD_MEDIA2</strong>](ioctl-storage-load-media2.md)<br/></td>
<td>Causes media to be loaded in a device that the caller has opened with FILE_READ_ATTRIBUTES. Because no file system is mounted when a device is opened in this way, this request can be processed much more quickly than an [<strong>IOCTL_STORAGE_LOAD_MEDIA</strong>](ioctl-storage-load-media.md) request.<br/> Input, output, and I/O status block values for IOCTL_STORAGE_LOAD_MEDIA2 are identical to those for IOCTL_STORAGE_LOAD_MEDIA.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</strong>](ioctl-storage-manage-data-set-attributes.md)<br/></td>
<td>This [<strong>IOCTL_STORAGE_MANAGE_DATA_SET_ATTRIBUTES</strong>](ioctl-storage-manage-data-set-attributes.md) request is used to send a manage data set attributes request to a storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_MCN_CONTROL</strong>](ioctl-storage-mcn-control.md)<br/></td>
<td>Temporarily enables or disables delivery of the custom PnP events GUID_IO_MEDIA_ARRIVAL and GUID_IO_MEDIA_REMOVAL on a removable-media device. This, in turn, enables or disables media change detection (AutoPlay) for the device if the caller has opened the device with FILE_READ_ATTRIBUTES access and if the device has AutoPlay enabled in the registry. The caller must not open the device for read or write access or the IOCTL operation will fail. This IOCTL has no effect on the AutoPlay setting in the registry.<br/> A driver for such a removable-media device must do the following:<br/>
<ol>
<li>Keep a count of disable requests, per physical device, in the device object extension.<br/></li>
<li>When called with this IOCTL, if the flag to disable media change detection is set, increment the count; if the flag is clear, decrement the count.<br/></li>
<li>Set the media change event for the device when the media state is changed only if the disable request count is zero.<br/></li>
</ol>
When the IRP_MJ_DEVICE_CONTROL IRP that contains this IOCTL is passed to the SCSI class driver, the <strong>FileObject</strong> member of the current [<strong>IO_STACK_LOCATION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff550659) must point to a valid file object. The SCSI class driver requires a file object for cases where a user-mode application that is disabling or enabling AutoPlay terminates unexpectedly. In such cases, the SCSI class driver uses the file object to reenable media change detection. Because the file object is necessary for proper clean-up, the SCSI class driver will cause the IRP to fail with an error message of STATUS_INVALID_PARAMETER if the <strong>FileObject</strong> member of IO_STACK_LOCATION does not point to a valid file object. If a user-mode application opens the device, then the I/O manager initializes this member, but kernel-mode driver writers should not assume that <strong>FileObject</strong> will be properly initialized when the IRP is generated by a user-mode application. If, for instance, a user-mode application mistakenly opens the device for either read or write access before sending the IOCTL, then the device control IRP will be routed through the file system, preventing the SCSI class driver and the device driver from directly accessing the device's file object. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_MEDIA_REMOVAL</strong>](ioctl-storage-media-removal.md)<br/></td>
<td>Locks the device to prevent removal of the media. If the driver can prevent the media from being removed while the drive is in use, it disables or enables the mechanism that ejects media on a device - the caller has opened for read or write access.<br/> Unlike [<strong>IOCTL_STORAGE_EJECTION_CONTROL</strong>](ioctl-storage-ejection-control.md), for which the driver tracks requests by caller, the driver ignores IOCTL_STORAGE_MEDIA_REMOVAL unlock requests only if its lock count is already zero, thereby allowing any caller to unlock the drive.<br/> A driver for such a removable-media device that can support this IOCTL must do the following:<br/>
<ol>
<li>Keep a lock count in the device object extension.<br/></li>
<li>Keep the lock count per physical device.<br/></li>
<li>When called with this IOCTL, if the flag to prevent removing the media is set, increment the count; if the flag is clear, decrement the count.<br/></li>
<li>Prevent removal of the media unless all lock counts are zero.<br/></li>
</ol></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_PERSISTENT_RESERVE_IN</strong>](ioctl-storage-persistent-reserve-in.md)<br/></td>
<td>The generic storage class driver (<em>classpnp.sys</em>) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve In commands. The behavior of the storage device when a Persistent Reserve In command is received is described in the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification. The IOCTL interface requires the caller to have read access to the physical device for Persistent Reserve In commands. User-mode applications, services, and kernel-mode drivers can use this IOCTL to control persistent reservations. If called from a driver, this IOCTL must be called from a thread running at IRQL &lt; DISPATCH_LEVEL. This IOCTL is defined with FILE_READ_ACCESS, requiring a device handle to have read permissions to issue the Persistent Reserve In command.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</strong>](ioctl-storage-persistent-reserve-out.md)<br/></td>
<td>The generic storage class driver (<em>classpnp.sys</em>) exposes an I/O control (IOCTL) interface for issuing Persistent Reserve Out commands. The behavior of the storage device when a Persistent Reserve Out command is received is described in the [SCSI Primary Commands - 2 (SPC-2)](http://go.microsoft.com/fwlink/p/?linkid=153142) specification. The IOCTL interface requires the caller to have read/write access to the physical device for Persistent Reserve Out commands. User-mode applications, services, and kernel-mode drivers can use this IOCTL to control persistent reservations. If called from a driver, this IOCTL must be called from a thread running at IRQL &lt; DISPATCH_LEVEL. This IOCTL is defined with FILE_READ_ACCESS and FILE_WRITE_ACCESS, requiring a device handle to have both read and write permissions to issue the Persistent Reserve Out command.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_PREDICT_FAILURE</strong>](ioctl-storage-predict-failure.md)<br/></td>
<td>Polls for a prediction of device failure. This request works with the IDE disk drives that support self-monitoring analysis and reporting technology (SMART). If the drive is a SCSI drive, the class driver attempts to verify if the SCSI disk supports the equivalent IDE SMART technology by check the inquiry information on the Information Exception Control Page, X3T10/94-190 Rev 4. <br/> If the device supports prediction failure, the disk class driver queries the device for failure prediction status and reports the results. If the disk class driver assigns a nonzero value to the <strong>PredictFailure</strong> member of [<strong>STORAGE_PREDICT_FAILURE</strong>](storage-predict-failure.md) in the output buffer at <strong>Irp-&gt;AssociatedIrp.SystemBuffer</strong>, the disk has bad sectors and is predicting a failure. The storage stack returns 512 bytes of vendor-specific information about the failure prediction in the <strong>VendorSpecific</strong> member of STORAGE_PREDICT_FAILURE. <br/> If the <strong>PredictFailure</strong> member contains a value of zero, the disk is not predicting a failure.<br/> If the device does not support failure prediction, IOCTL_STORAGE_PREDICT_FAILURE fails with a status of STATUS_INVALID_DEVICE_REQUEST, and the data in the output buffer is undefined<br/> Other means of checking for disk failure include monitoring the event log and registering to receive a WMI event with WMI_STORAGE_PREDICT_FAILURE_EVENT_GUID. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_PROTOCOL_COMMAND</strong>](ioctl-storage-protocol-command.md)<br/></td>
<td>A driver can use <strong>IOCTL_STORAGE_PROTOCOL_COMMAND</strong> to pass vendor-specific commands to a storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md)<br/></td>
<td>A driver can use <strong>IOCTL_STORAGE_QUERY_PROPERTY</strong> to return properties of a storage device or adapter. The request indicates the kind of information to retrieve, such as inquiry data for a device or capabilities and limitations of an adapter. <strong>IOCTL_STORAGE_QUERY_PROPERTY</strong> can also be used to determine whether the port driver supports a particular property or which fields in the property descriptor can be modified with a subsequent change-property request. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_READ_CAPACITY</strong>](ioctl-storage-read-capacity.md)<br/></td>
<td>The <strong>IOCTL_STORAGE_READ_CAPACITY</strong> request returns the read capacity information for the target storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_REINITIALIZE_MEDIA</strong>](ioctl-storage-reinitialize-media.md)<br/></td>
<td>A driver can use the <strong>IOCTL_STORAGE_REINITIALIZE_MEDIA</strong> control code to reinitialize/erase a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_RELEASE</strong>](ioctl-storage-release.md)<br/></td>
<td>Releases a device previously reserved for the exclusive use of the caller on a bus that supports multiple initiators and the concept of reserving a device, such as a SCSI bus.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_RESERVE</strong>](ioctl-storage-reserve.md)<br/></td>
<td>Claims a device for the exclusive use of the caller on a bus that supports multiple initiators and the concept of reserving a device, such as a SCSI bus.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_RESET_BUS</strong>](ioctl-storage-reset-bus.md)<br/></td>
<td>Resets an I/O bus and, indirectly, each device on the bus. Resetting the bus clears all device reservations and transfer speed settings, which must then be renegotiated, making it a time-consuming operation that should be used very rarely. The caller requires only read access to issue a bus reset. <br/> The <strong>SrbStatus</strong> flag of pending SRBs is set to SRB_STATUS_BUS_RESET. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_RESET_DEVICE</strong>](ioctl-storage-reset-device.md)<br/></td>
<td>If possible, resets a non-SCSI storage device without affecting other devices on the bus. Device reset for SCSI devices is not supported. The caller requires only read access to issue a device reset and, to comply, the device must be capable of responding to I/O requests. If the device reset succeeds, pending I/O requests are canceled. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_STORAGE_SET_HOTPLUG_INFO</strong>](ioctl-storage-set-hotplug-info.md)<br/></td>
<td>Sets the hotplug configuration of the specified device. This request takes a [<strong>STORAGE_HOTPLUG_INFO</strong>](storage-hotplug-info.md) structure as input. The <strong>DeviceHotplug</strong> member of the STORAGE_HOTPLUG_INFO structure determines what action is taken. If the value of that member is nonzero, the value for the device's removal policy in the registry is set to <strong>ExpectSurpriseRemoval</strong> and all levels of caching are disabled. If the value of <strong>DeviceHotplug</strong> is zero, the removal policy is set to <strong>ExpectOrderlyRemoval</strong>, and caching might be selectively enabled. <br/></td>
</tr>
<tr class="even">
<td>[<strong>IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</strong>](ioctl-storage-set-temperature-threshold.md)<br/></td>
<td>A driver can use <strong>IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</strong> to set the temperature threshold of a storage device (when supported by the hardware). <br/></td>
</tr>
<tr class="odd">
<td>[<strong>MP_STORAGE_DIAGNOSTIC_LEVEL</strong>](mp-storage-diagnostic-level.md)<br/></td>
<td>The [<strong>MP_STORAGE_DIAGNOSTIC_LEVEL</strong>](mp-storage-diagnostic-level.md) enumeration allows the caller to control what kinds of data the provider should return.<br/></td>
</tr>
<tr class="even">
<td>[<strong>MP_STORAGE_DIAGNOSTIC_TARGET_TYPE</strong>](mp-storage-diagnostic-target-type.md)<br/></td>
<td>The [<strong>MP_STORAGE_DIAGNOSTIC_TARGET_TYPE</strong>](mp-storage-diagnostic-target-type.md) enumeration specifies the target type of a storage diagnostic.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PERSISTENT_RESERVE_COMMAND</strong>](persistent-reserve-command.md)<br/></td>
<td>The PERSISTENT_RESERVE_COMMAND structure is used together with the [<strong>IOCTL_STORAGE_PERSISTENT_RESERVE_IN</strong>](ioctl-storage-persistent-reserve-in.md) and [<strong>IOCTL_STORAGE_PERSISTENT_RESERVE_OUT</strong>](ioctl-storage-persistent-reserve-out.md) requests to obtain and control information about persistent reservations and reservation keys that are active within a device server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PRI_REGISTRATION_LIST</strong>](pri-registration-list.md)<br/></td>
<td>The PRI_REGISTRATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_KEYS.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PRI_RESERVATION_DESCRIPTOR</strong>](pri-reservation-descriptor.md)<br/></td>
<td>The PRI_RESERVATION_DESCRIPTOR structure is used to construct the [<strong>PRI_RESERVATION_LIST</strong>](pri-reservation-list.md) structure that is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PRI_RESERVATION_LIST</strong>](pri-reservation-list.md)<br/></td>
<td>The PRI_RESERVATION_LIST structure is returned in response to a Persistent Reserve In command with ServiceAction = RESERVATION_ACTION_READ_RESERVATIONS.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PRO_PARAMETER_LIST</strong>](pro-parameter-list.md)<br/></td>
<td>The PRO_PARAMETER_LIST structure is sent in a Persistent Reserve Out command to a device server.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR</strong>](storage-access-alignment-descriptor.md)<br/></td>
<td>The STORAGE_ACCESS_ALIGNMENT_DESCRIPTOR structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the storage access alignment descriptor data for a device. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_ADAPTER_DESCRIPTOR</strong>](storage-adapter-descriptor.md)<br/></td>
<td>The [<strong>STORAGE_ADAPTER_DESCRIPTOR</strong>](storage-adapter-descriptor.md) structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the storage adapter descriptor data for a device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_ASSOCIATION_TYPE</strong>](storage-association-type.md)<br/></td>
<td>The STORAGE_ASSOCIATION_TYPE enumeration indicates whether a storage descriptor identifies a device or a port.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_BREAK_RESERVATION_REQUEST</strong>](storage-break-reservation-request.md)<br/></td>
<td>The STORAGE_BREAK_RESERVATION_REQUEST structure is used in conjunction with the [<strong>IOCTL_STORAGE_BREAK_RESERVATION</strong>](ioctl-storage-break-reservation.md) request to free a disk resource that was previously reserved. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_BUS_RESET_REQUEST</strong>](storage-bus-reset-request.md)<br/></td>
<td>The STORAGE_BUS_RESET_REQUEST structure is used in conjunction with the [<strong>IOCTL_STORAGE_RESET_BUS</strong>](ioctl-storage-reset-bus.md) request to specify the path of the bus to be reset.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_BUS_TYPE</strong>](storage-bus-type.md)<br/></td>
<td>The STORAGE_BUS_TYPE enumeration provides a symbolic means of representing storage bus types.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_COMPONENT_HEALTH_STATUS</strong>](storage-component-health-status.md)<br/></td>
<td>Indicates the health status of a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_CRYPTO_ALGORITHM_ID</strong>](storage-crypto-algorithm-id.md)<br/></td>
<td>The <strong>STORAGE_CRYPTO_ALGORITHM_ID</strong> enum provides an output buffer for <strong>StorageAdapterCryptoProperty</strong> and <strong>PropertyStandardQuery</strong>.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_CRYPTO_CAPABILITY</strong>](storage-crypto-capability.md)<br/></td>
<td>Reserved for system use.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_CRYPTO_DESCRIPTOR</strong>](storage-crypto-descriptor.md)<br/></td>
<td>Reserved for system use.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_CRYPTO_KEY_SIZE</strong>](storage-crypto-key-size.md)<br/></td>
<td>The <strong>STORAGE_CRYPTO_KEY_SIZE</strong> enum returns the Size of the key in bits.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DESCRIPTOR_HEADER</strong>](storage-descriptor-header.md)<br/></td>
<td>The STORAGE_DESCRIPTOR_HEADER structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the properties of a storage device or adapter. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR</strong>](storage-device-attributes-descriptor.md)<br/></td>
<td>The STORAGE_DEVICE_ATTRIBUTES_DESCRIPTOR structure is used to retrieve the attributes information for a device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DEVICE_DESCRIPTOR</strong>](storage-device-descriptor.md)<br/></td>
<td>The [<strong>STORAGE_DEVICE_DESCRIPTOR</strong>](storage-device-descriptor.md) structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the storage device descriptor data for a device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DEVICE_FORM_FACTOR</strong>](storage-device-form-factor.md)<br/></td>
<td>Indicates the form factor of a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DEVICE_ID_DESCRIPTOR</strong>](storage-device-id-descriptor.md)<br/></td>
<td>The [<strong>STORAGE_DEVICE_ID_DESCRIPTOR</strong>](storage-device-id-descriptor.md) structure is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the device ID descriptor data for a device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DEVICE_IO_CAPABILITY_DESCRIPTOR</strong>](storage-device-io-capability-descriptor.md)<br/></td>
<td>The output buffer for the StorageDeviceIoCapabilityProperty as defined in [<strong>STORAGE_PROPERTY_ID</strong>](storage-property-id.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DEVICE_NUMBER</strong>](storage-device-number.md)<br/></td>
<td>The STORAGE_DEVICE_NUMBER structure is used in conjunction with the [<strong>IOCTL_STORAGE_GET_DEVICE_NUMBER</strong>](ioctl-storage-get-device-number.md) request to retrieve the FILE_DEVICE_<em>XXX</em> device type, the device number, and, for a device that can be partitioned, the partition number assigned to a device by the driver when the device is started. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DEVICE_POWER_CAP</strong>](storage-device-power-cap.md)<br/></td>
<td>This structure is used as an input and output buffer for the [<strong>IOCTL_STORAGE_DEVICE_POWER_CAP</strong>](ioctl-storage-device-power-cap.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DEVICE_POWER_CAP_UNITS</strong>](storage-device-power-cap-units.md)<br/></td>
<td>The units of the maximum power threshold.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DEVICE_RESILIENCY_DESCRIPTOR</strong>](storage-device-resiliency-descriptor.md)<br/></td>
<td>Reserved for system use.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DIAGNOSTIC_DATA</strong>](storage-diagnostic-data.md)<br/></td>
<td>Describes diagnostic data about the storage driver stack. The <strong>STORAGE_DIAGNOSTIC_DATA</strong> structure is provided in the output buffer of an [<strong>IOCTL_STORAGE_DIAGNOSTIC</strong>](storage-ioctl_storage_diagnostic) request.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DIAGNOSTIC_LEVEL</strong>](storage-diagnostic-level.md)<br/></td>
<td>The [<strong>STORAGE_DIAGNOSTIC_LEVEL</strong>](storage-diagnostic-level.md) enumeration specifies the target type of a storage diagnostic.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DIAGNOSTIC_MP_REQUEST</strong>](storage-diagnostic-mp-request.md)<br/></td>
<td>Describes a diagnostic request to Miniport. The <strong>STORAGE_DIAGNOSTIC_MP_REQUEST</strong> structure is provided in the input/output buffer of an [<strong>IOCTL_SCSI_MINIPORT_DIAGNOSTIC</strong>](ioctl-scsi-miniport-diagnostic.md) request.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_DIAGNOSTIC_REQUEST</strong>](storage-diagnostic-request.md)<br/></td>
<td>Describes a diagnostic request about the storage driver stack. The <strong>STORAGE_DIAGNOSTIC_REQUEST</strong> structure is provided in the input buffer of an [<strong>IOCTL_STORAGE_DIAGNOSTIC</strong>](storage-ioctl_storage_diagnostic) request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_DIAGNOSTIC_TARGET_TYPE</strong>](storage-diagnostic-target-type.md)<br/></td>
<td>The [<strong>STORAGE_DIAGNOSTIC_TARGET_TYPE</strong>](storage-diagnostic-target-type.md) enumeration specifies the target type of a storage diagnostic.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_HOTPLUG_INFO</strong>](storage-hotplug-info.md)<br/></td>
<td>The STORAGE_HOTPLUG_INFO structure provides hotplug information for a device. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_IDENTIFIER</strong>](storage-identifier.md)<br/></td>
<td>The STORAGE_IDENTIFIER structure represents a SCSI identification descriptor.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_IDENTIFIER_CODE_SET</strong>](storage-identifier-code-set.md)<br/></td>
<td>The STORAGE_IDENTIFIER_CODE_SET enumeration specifies the code set used by a SCSI identification descriptor ([<strong>STORAGE_IDENTIFIER</strong>](storage-identifier.md)) to identify a logical unit.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_IDENTIFIER_TYPE</strong>](storage-identifier-type.md)<br/></td>
<td>The STORAGE_IDENTIFIER_TYPE enumeration specifies the type of storage identifier.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_LB_PROVISIONING_MAP_RESOURCES</strong>](storage-lb-provisioning-map-resources.md)<br/></td>
<td>The [<strong>STORAGE_LB_PROVISIONING_MAP_RESOURCES</strong>](storage-lb-provisioning-map-resources.md) structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an [<strong>IOCTL_STORAGE_GET_LB_PROVISIONING_MAP_RESOURCES</strong>](ioctl-storage-get-lb-provisioning-map-resources.md) request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_MEDIA_TYPE</strong>](storage-media-type.md)<br/></td>
<td>The STORAGE_MEDIA_TYPE enumeration is used in conjunction with the [<strong>IOCTL_STORAGE_GET_MEDIA_TYPES_EX</strong>](ioctl-storage-get-media-types-ex.md) request to query the class driver for the types of media that a device supports.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_MEDIUM_PRODUCT_TYPE_DESCRIPTOR</strong>](storage-medium-product-type-descriptor.md)<br/></td>
<td>Used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to describe the product type of a storage device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_MINIPORT_DESCRIPTOR</strong>](storage-miniport-descriptor.md)<br/></td>
<td>Reserved for system use.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PHYSICAL_ADAPTER_DATA</strong>](storage-physical-adapter-data.md)<br/></td>
<td>Specifies the physical device data of a storage adapter.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PHYSICAL_DEVICE_DATA</strong>](storage-physical-device-data.md)<br/></td>
<td>Specifies the physical device data of a storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PHYSICAL_NODE_DATA</strong>](storage-physical-node-data.md)<br/></td>
<td>Specifies the physical device data of a storage node.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PHYSICAL_TOPOLOGY_DESCRIPTOR</strong>](storage-physical-topology-descriptor.md)<br/></td>
<td>Describes the physical topology of storage in a system.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PORT_CODE_SET</strong>](storage-port-code-set.md)<br/></td>
<td>Reserved for system use. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PREDICT_FAILURE</strong>](storage-predict-failure.md)<br/></td>
<td>The STORAGE_PREDICT_FAILURE structure is used in conjunction with [<strong>IOCTL_STORAGE_PREDICT_FAILURE</strong>](ioctl-storage-predict-failure.md) to report whether a device is currently predicting a failure.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PROPERTY_ID</strong>](storage-property-id.md)<br/></td>
<td>This enumeration is used in the [<strong>STORAGE_PROPERTY_QUERY</strong>](storage-property-query.md) structure in conjunction with [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) to retrieve information about a storage device or adapter. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PROPERTY_QUERY</strong>](storage-property-query.md)<br/></td>
<td>This structure is used in conjunction with [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) to retrieve the properties of a storage device or adapter. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PROTOCOL_ATA_DATA_TYPE</strong>](storage-protocol-ata-data-type.md)<br/></td>
<td>The ATA protocol data type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PROTOCOL_COMMAND</strong>](storage-protocol-command.md)<br/></td>
<td>This structure is used as an input buffer when using the pass-through mechanism to issue a vendor-specific command to a storage device (via [<strong>IOCTL_STORAGE_PROTOCOL_COMMAND</strong>](ioctl-storage-protocol-command.md)).<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PROTOCOL_DATA_DESCRIPTOR</strong>](storage-protocol-data-descriptor.md)<br/></td>
<td>This structure is used in conjunction with [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) to return protocol-specific data from a storage device or adapter. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PROTOCOL_NVME_DATA_TYPE</strong>](storage-protocol-nvme-data-type.md)<br/></td>
<td>Describes the type of NVMe protocol-specific data that's to be queried during an [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PROTOCOL_SPECIFIC_DATA</strong>](storage-protocol-specific-data.md)<br/></td>
<td>Describes protocol-specific device data, provided in the input and output buffer of an [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_PROTOCOL_TYPE</strong>](storage-protocol-type.md)<br/></td>
<td>This enumeration is used to define the different storage command protocols that are used between software and hardware.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_PROTOCOL_UFS_DATA_TYPE</strong>](storage-protocol-ufs-data-type.md)<br/></td>
<td>The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff560590) request.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_QUERY_TYPE</strong>](storage-query-type.md)<br/></td>
<td>The STORAGE_QUERY_TYPE enumeration is used in conjunction with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve the properties of a storage device or adapter.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_READ_CAPACITY</strong>](storage-read-capacity.md)<br/></td>
<td>The <strong>STORAGE_READ_CAPACITY</strong> contains the disk read capacity information returned from a [<strong>IOCTL_STORAGE_READ_CAPACITIY</strong>](ioctl-storage-read-capacity.md) request. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_SPEC_VERSION</strong>](storage-spec-version.md)<br/></td>
<td>Indicates the specification of the storage device.<br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_TEMPERATURE_DATA_DESCRIPTOR</strong>](storage-temperature-data-descriptor.md)<br/></td>
<td>This structure is used in conjunction with [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) to return temperature data from a storage device or adapter. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_TEMPERATURE_INFO</strong>](storage-temperature-info.md)<br/></td>
<td>Describes device temperature data. Returned as part of [<strong>STORAGE_TEMPERATURE_DATA_DESCRIPTOR</strong>](storage-temperature-data-descriptor.md) when querying for temperature data with an [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request. <br/></td>
</tr>
<tr class="even">
<td>[<strong>STORAGE_TEMPERATURE_THRESHOLD</strong>](storage-temperature-threshold.md)<br/></td>
<td>This structure is used to set the over or under temperature threshold of a storage device (via [<strong>IOCTL_STORAGE_SET_TEMPERATURE_THRESHOLD</strong>](ioctl-storage-set-temperature-threshold.md)).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_WRITE_CACHE_PROPERTY</strong>](storage-write-cache-property.md)<br/></td>
<td>The STORAGE_WRITE_CACHE_PROPERTY structure is used with the [<strong>IOCTL_STORAGE_QUERY_PROPERTY</strong>](ioctl-storage-query-property.md) request to retrieve information about a device's write cache property.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WRITE_CACHE_CHANGE</strong>](write-cache-change.md)<br/></td>
<td>The WRITE_CACHE_CHANGE enumeration indicates whether the write cache features of a device are changeable or not.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WRITE_CACHE_ENABLE</strong>](write-cache-enable.md)<br/></td>
<td>The WRITE_CACHE_ENABLE enumeration indicates whether the write cache is enabled or disabled.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WRITE_CACHE_TYPE</strong>](write-cache-type.md)<br/></td>
<td>The WRITE_CACHE_TYPE enumeration specifies the cache type.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WRITE_THROUGH</strong>](write-through.md)<br/></td>
<td>The WRITE_THROUGH enumeration specifies whether a storage device supports write-through caching.<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Ntddstor.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






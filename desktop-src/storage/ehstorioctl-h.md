---
title: Ehstorioctl.h
description: This section contains reference topics for the Ehstorioctl.h header.
ms.assetid: 38A7A3A3-2343-49FA-BD8F-911CC2D7CF5B
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ehstorioctl.h

This section contains reference topics for the Ehstorioctl.h header.

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
<td>[Storage Silo Driver Structures](storage-silo-driver-structures.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>ACT_AUTHZ_STATE</strong>](act-authz-state.md)<br/></td>
<td>This structure describes the Addressable Command Target (ACT) authorization state.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ENUM_PDO_ENTRY</strong>](enum-pdo-entry.md)<br/></td>
<td>This structure describes a single entry in a result set of Physical Device Objects (PDOs) that are enumerated with [<strong>IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</strong>](ioctl-ehstor-device-enumerate-pdos.md).<br/></td>
</tr>
<tr class="even">
<td>[<strong>ENUM_PDO_RESULTS</strong>](enum-pdo-results.md)<br/></td>
<td>This structure describes a result set of Physical Device Objects (PDOs) that are enumerated with [<strong>IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</strong>](ioctl-ehstor-device-enumerate-pdos.md).<br/></td>
</tr>
<tr class="odd">
<td>[<strong>IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS</strong>](ioctl-ehstor-device-enumerate-pdos.md)<br/></td>
<td>This IOCTL returns a result set containing the enumeration of all active storage Physical Device Objects (PDOs) associated with the given Addressable Command Target (ACT). The client may first probe for the required buffer size by issuing this IOCTL in the following manner:<br/> <span data-codelanguage=""></span>
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>DeviceIoControl(
    hDevice,
    IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS,
    &amp;pdoType,
    sizeof(PDO_TYPE),
    NULL,
    0,
    &amp;dwBytesRequired,
    NULL );</code></pre></td>
</tr>
</tbody>
</table>

<p>With the output buffer parameter set to <strong>NULL</strong>, the I/O manager clears the IRP_INPUT_OPERATION bit in the IRP flags. Upon detecting this, the storage silo driver can safely set IoStatus.Information to the required buffer size, thus indicating it to the client.</p>
<p>This only works because STATUS_BUFFER_OVERFLOW (0x80000005) is an NT_WARNING() value for which I/O manager copies IoStatus.Information into the lpBytesReturned parameter, returning that value to the client.</p>
<p>Caution is required here because IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS is defined with METHOD_BUFFERED, therefore I/O manager will attempt to copy this number of bytes into the output buffer.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_GET_AUTHZ_STATE</strong>](ioctl-ehstor-device-get-authz-state.md)</p></td>
<td><p>This IOCTL is used to inform the owning driver for the IEEE 1667 device PDOs that the authorization state has changed. The owning driver may choose to change the state of the disk PDO in response to this IOCTL. In the case of <em>EhStorClass.sys</em>, the disk PDO is added or removed based on the authorization value in the input buffer of this IOCTL. Typically this IOCTL is issued by a UMDF authentication silo driver, such as the password or certificate driver, immediately following a successful silo operation which has changed the authentication state of the silo.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE</strong>](ioctl-ehstor-device-get-queue-state.md)</p></td>
<td><p>The [<strong>IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE</strong>](ioctl-ehstor-device-get-queue-state.md) request is sent by silo drivers and applications to determine the state of a storage device queue. IO requests in the storage device queue are held when the device is temporarily unauthorized. A storage device may become temporarily unauthorized in low power states or when there is a policy that requires locking Enhanced Storage devices such as when the user session is locked.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_QUERY_PROPERTIES</strong>](ioctl-ehstor-device-query-properties.md)</p></td>
<td><p>A silo driver sends this IOCTL to the storage device stack to query for storage device properties. The Enhanced Storage Class Driver (EHSTOR) will handle the request and return the available properties.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_SET_AUTHZ_STATE</strong>](ioctl-ehstor-device-set-authz-state.md)</p></td>
<td><p>This IOCTL is used to inform the owning driver for the IEEE 1667 device PDOs that the authorization state has changed. The owning driver may choose to change the state of the disk PDO in response to this IOCTL. In the case of <em>EhStorClass.sys</em>, the disk PDO is added or removed based on the authorization value in the input buffer of this IOCTL. Typically this IOCTL is issued by a UMDF authentication silo driver, such as the password or certificate driver, immediately following a successful silo operation which has changed the authentication state of the silo.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE</strong>](ioctl-ehstor-device-set-queue-state.md)</p></td>
<td><p>The [<strong>IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE</strong>](ioctl-ehstor-device-set-queue-state.md) request is sent by silo drivers and applications to change the state of a storage device queue. IO requests in the storage device queue are held when the device is temporarily unauthorized.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_EHSTOR_DEVICE_SILO_COMMAND</strong>](ioctl-ehstor-device-silo-command.md)</p></td>
<td><p>This IOCTL issues a silo command to the targeted silo on the device. Both input and output data are structured according to the definition of silo commands, as found in the IEEE 1667 specification document.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ</strong>](ioctl-ehstor-driver-perform-authz.md)</p></td>
<td><p>[<strong>IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ</strong>](ioctl-ehstor-driver-perform-authz.md) is sent by the Enhanced Storage Class Driver (EHSTOR) to the silo driver to initiate on-demand authentication or deauthentication.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES</strong>](ioctl-ehstor-driver-report-capabilities.md)</p></td>
<td><p>This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of the silo driver's capabilities. The silo driver sends this IOCTL with a [<strong>SILO_DRIVER_CAPABILITES</strong>](act-authz-state.md) structure that indicates whether authentication and banding are supported along with a list of EHSTOR IOCTLs it will handle.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE</strong>](ioctl-ehstor-driver-update-lba-filter-table.md)</p></td>
<td><p>This IOCTL is used to inform the enhanced storage (EHSTOR) class driver of changes to the LBA filter table. Bands managed by the silo driver are composed of LBA ranges. The silo driver notifies the EHSTOR class driver of updates to the set of bands it controls with this IOCTL.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>LBA_FILTER_TABLE</strong>](lba-filter-table.md)</p></td>
<td><p>The [<strong>LBA_FILTER_TABLE</strong>](lba-filter-table.md) structure contains the LBA ranges whose access is controlled by a silo driver. The LBA filter entries in the table define bands on a storage device that are managed by a silo driver. A silo drivers send the LBA filter table to the enhanced storage class driver in an [<strong>IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE</strong>](ioctl-ehstor-driver-update-lba-filter-table.md) request.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>LBA_FILTER_TABLE_ENTRY</strong>](lba-filter-table-entry.md)</p></td>
<td><p>The [<strong>LBA_FILTER_TABLE_ENTRY</strong>](lba-filter-table-entry.md) structure contains an individual LBA range for the [<strong>LBA_FILTER_TABLE</strong>](lba-filter-table.md) sent in an [<strong>IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE</strong>](ioctl-ehstor-driver-update-lba-filter-table.md) request.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PDO_CAPS</strong>](pdo-caps.md)</p></td>
<td><p>This enumeration describes the capabilities of Physical Device Objects (PDOs).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PDO_STATE</strong>](pdo-state.md)</p></td>
<td><p>This enumeration describes the states of Physical Device Objects (PDOs).</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PDO_TYPE</strong>](pdo-type.md)</p></td>
<td><p>This enumeration describes the types of Physical Device Objects (PDOs).</p></td>
</tr>
<tr class="even">
<td><p>[<strong>SILO_COMMAND</strong>](silo-command.md)</p></td>
<td><p>This structure describes a storage silo driver command.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>SILO_DRIVER_CAPABILITIES</strong>](silo-driver-capabilities.md)</p></td>
<td><p>This structure is used to specify the capabilities and support for IOCTL redirection of a storage silo driver. [<strong>SILO_DRIVER_CAPABILITIES</strong>](silo-driver-capabilities.md) is included in the system buffer of an [<strong>IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES</strong>](ioctl-ehstor-driver-report-capabilities.md) request.</p></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Ehstorioctl.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






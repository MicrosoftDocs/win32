---
title: Ntddscsi.h
description: This section contains reference topics for the Ntddscsi.h header.
ms.assetid: 8D862CBC-875E-4CA2-8714-6B9A02D870B0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ntddscsi.h

This section contains reference topics for the Ntddscsi.h header.

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
<td>[IDE I/O Control Codes](ide-i-o-control-codes.md)<br/></td>

</tr>
<tr class="even">
<td>[MPIO I/O Control Codes](mpio-i-o-control-codes.md)<br/></td>

</tr>
<tr class="odd">
<td>[NV Cache Manager I/O Control Codes](nv-cache-manager-i-o-control-codes.md)<br/></td>

</tr>
<tr class="even">
<td>[NV Cache Manager Structures](nv-cache-manager-structures.md)<br/></td>

</tr>
<tr class="odd">
<td>[SCSI Port I/O Control Codes](scsi-port-i-o-control-codes.md)<br/></td>

</tr>
<tr class="even">
<td>[Virtual Miniport I/O Control Codes](virtual-miniport-i-o-control-codes.md)<br/></td>

</tr>
<tr class="odd">
<td>[<strong>ATA_PASS_THROUGH_EX</strong>](ata-pass-through-ex.md)<br/></td>
<td>The ATA_PASS_THROUGH_EX structure is used in conjunction with an [<strong>IOCTL_ATA_PASS_THROUGH</strong>](ioctl-ata-pass-through.md) request to instruct the port driver to send an embedded ATA command to the target device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>ATA_PASS_THROUGH_DIRECT</strong>](ata-pass-through-direct.md)<br/></td>
<td>The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an [<strong>IOCTL_ATA_PASS_THROUGH_DIRECT</strong>](ioctl-ata-pass-through-direct.md) request to instruct the port driver to send an embedded ATA command to the target device. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>HYBRID_INFORMATION</strong>](hybrid-information.md)<br/></td>
<td>The <strong>HYBRID_INFORMATION</strong> structure contains hybrid disk capability information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>IO_SCSI_CAPABILITIES</strong>](io-scsi-capabilities.md)<br/></td>
<td>The IO_SCSI_CAPABILITIES structure is used in conjunction with the [<strong>IOCTL_SCSI_GET_CAPABILITIES</strong>](ioctl-scsi-get-capabilities.md) request to retrieve the capabilities and limitations of the underlying SCSI host adapter.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MPIO_PASS_THROUGH_PATH</strong>](mpio-pass-through-path.md)<br/></td>
<td>The <strong>MPIO_PASS_THROUGH_PATH</strong> structure is used together with an [<strong>IOCTL_MPIO_PASS_THROUGH_PATH</strong>](ioctl-mpio-pass-through-path.md) request to instruct the port driver to send an embedded SCSI command to the target device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MPIO_PASS_THROUGH_PATH_EX</strong>](mpio-pass-through-path-ex.md)<br/></td>
<td>The <strong>MPIO_PASS_THROUGH_PATH_EX</strong> structure is used together with an [<strong>IOCTL_MPIO_PASS_THROUGH_PATH_EX</strong>](ioctl-mpio-pass-through-path-ex.md) request to instruct the port driver to send an embedded SCSI command to the target device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>MPIO_PASS_THROUGH_PATH_DIRECT</strong>](mpio-pass-through-path-direct.md)<br/></td>
<td>The <strong>MPIO_PASS_THROUGH_PATH_DIRECT</strong> structure is used together with an [<strong>IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT</strong>](ioctl-mpio-pass-through-path-direct.md) request to instruct the port driver to send an embedded SCSI command to the target device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>MPIO_PASS_THROUGH_PATH_DIRECT_EX</strong>](mpio-pass-through-path-direct-ex.md)<br/></td>
<td>The <strong>MPIO_PASS_THROUGH_PATH_DIRECT_EX</strong> structure is used together with an [<strong>IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX</strong>](ioctl-mpio-pass-through-path-direct-ex.md) request to instruct the port driver to send an embedded SCSI command to the target device.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCSI_ADAPTER_BUS_INFO</strong>](scsi-adapter-bus-info.md)<br/></td>
<td>The SCSI_ADAPTER_BUS_INFO structure is used in conjunction with the [<strong>IOCTL_SCSI_GET_INQUIRY_DATA</strong>](ioctl-scsi-get-inquiry-data.md) request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCSI_ADDRESS</strong>](scsi-address.md)<br/></td>
<td>The SCSI_ADDRESS structure is used in conjunction with the [<strong>IOCTL_SCSI_GET_ADDRESS</strong>](ioctl-scsi-get-address.md) request to retrieve the address information, such as the target ID (TID) and the logical unit number (LUN) of a particular SCSI target. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCSI_BUS_DATA</strong>](scsi-bus-data.md)<br/></td>
<td>The SCSI_BUS_DATA structure is used in conjunction with the [<strong>IOCTL_SCSI_GET_INQUIRY_DATA</strong>](ioctl-scsi-get-inquiry-data.md) request and the [<strong>SCSI_ADAPTER_BUS_INFO</strong>](scsi-adapter-bus-info.md) structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCSI_INQUIRY_DATA</strong>](scsi-inquiry-data.md)<br/></td>
<td>The SCSI_INQUIRY_DATA structure is used in conjunction with the [<strong>IOCTL_SCSI_GET_INQUIRY_DATA</strong>](ioctl-scsi-get-inquiry-data.md) request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCSI_PASS_THROUGH</strong>](scsi-pass-through.md)<br/></td>
<td>The SCSI_PASS_THROUGH structure is used in conjunction with an [<strong>IOCTL_SCSI_PASS_THROUGH</strong>](ioctl-scsi-pass-through.md) request to instruct the port driver to send an embedded SCSI command to the target device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>SCSI_PASS_THROUGH_EX</strong>](scsi-pass-through-ex.md)<br/></td>
<td>The <strong>SCSI_PASS_THROUGH_EX</strong> structure is used in conjunction with an <strong>IOCTL_SCSI_PASS_THROUGH_EX</strong> request to instruct the port driver to send an embedded SCSI command to the target device. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SCSI_PASS_THROUGH_DIRECT</strong>](scsi-pass-through-direct.md)<br/></td>
<td>The <strong>SCSI_PASS_THROUGH_DIRECT</strong> structure is used in conjunction with an [<strong>IOCTL_SCSI_PASS_THROUGH_DIRECT</strong>](ioctl-scsi-pass-through-direct.md) request to instruct the port driver to send an embedded SCSI command to the target device. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCSI_PASS_THROUGH_DIRECT_EX</strong>](scsi-pass-through-direct-ex.md)<br/></td>
<td>The <strong>SCSI_PASS_THROUGH_DIRECT_EX</strong> structure is used in conjunction with an [<strong>IOCTL_SCSI_PASS_THROUGH_DIRECT_EX</strong>](ioctl-scsi-pass-through-direct-ex.md) request to instruct the port driver to send an embedded SCSI command to the target device. <br/></td>
</tr>
<tr class="odd">
<td>[<strong>SRB_IO_CONTROL</strong>](srb-io-control.md)<br/></td>
<td><blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Ntddscsi.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






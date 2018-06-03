---
title: Srb.h
description: This section contains reference topics for the Srb.h header.
ms.assetid: F09EA208-818D-4EE5-9691-D7C0D17511AA
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Srb.h

This section contains reference topics for the Srb.h header.

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
<td>[<strong>ACCESS_RANGE</strong>](access-range.md)<br/></td>
<td>An ACCESS_RANGE describes a memory or I/O port range used by an HBA.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>_HW_INITIALIZATION_DATA</strong>](hw-initialization-data--scsi-.md)<br/></td>
<td>Each SCSI miniport driver's [<strong>DriverEntry</strong>](https://msdn.microsoft.com/library/windows/hardware/ff544113) routine must initialize with zeros and, then, fill in the relevant HW_INITIALIZATION_DATA (SCSI) information for the OS-specific port driver.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_INITIALIZE</em>](phw-initialize.md)<br/></td>
<td>The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. <br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_STARTIO</em>](phw-startio.md)<br/></td>
<td>The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. <br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_INTERRUPT</em>](phw-interrupt.md)<br/></td>
<td>The PHW_INTERRUPT routine prototype declares the miniport driver's interrupt handler routine. <br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_TIMER</em>](phw-timer.md)<br/></td>
<td>The PHW_TIMER routine prototype declares a SCSI miniport driver's timer routine.<br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_DMA_STARTED</em>](phw-dma-started.md)<br/></td>
<td>The PHW_DMA_STARTED routine prototype declares a SCSI miniport driver routine that starts DMA for subordinate DMA device. <br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_FIND_ADAPTER</em>](phw-find-adapter.md)<br/></td>
<td>The PHW_FIND_ADAPTER prototype declares a routine that uses supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter. <br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_RESET_BUS</em>](phw-reset-bus.md)<br/></td>
<td>The PHW_RESET_BUS prototype declares a routine that resets the indicated SCSI bus.<br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_ADAPTER_STATE</em>](phw-adapter-state.md)<br/></td>
<td>The PHW_INITIALIZE routine prototype declares a routine that saves or restores the state of the miniport driver's HBA. <br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_ADAPTER_CONTROL</em>](phw-adapter-control.md)<br/></td>
<td>The PHW_INITIALIZE routine prototype declares a routine that initializes the miniport driver after a reboot or power failure occurs. <br/></td>
</tr>
<tr class="even">
<td>[<strong>_PORT_CONFIGURATION_INFORMATION</strong>](port-configuration-information--scsi-.md)<br/></td>
<td>PORT_CONFIGURATION_INFORMATION (SCSI) contains configuration information for an HBA. The OS-specific port driver allocates and initializes this structure, supplies as much HBA-specific configuration information as possible, and passes the structure to the miniport driver's <em>HwScsiFindAdapter</em> routine. The port driver gets some of the information for this structure from the miniport driver's HW_INITIALIZATION_DATA structure. The miniport driver's <em>HwScsiFindAdapter</em> routine is responsible for determining whether the miniport driver can support the HBA and, if so, for filling in the pertinent remaining information in the PORT_CONFIGURATION_INFORMATION structure.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>STORAGE_REQUEST_BLOCK</strong>](storage-request-block.md)<br/></td>
<td>The <strong>STORAGE_REQUEST_BLOCK</strong> is the extended format SCSI Request Block (SRB) structure. The structure provides for the addition of extended data associated with an SRB function.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>SCSI_WMI_REQUEST_BLOCK</strong>](scsi-wmi-request-block.md)<br/></td>
<td>This structure is a special version of a [<strong>SCSI_REQUEST_BLOCK</strong>](scsi-request-block.md) for use with WMI commands. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>ScsiPortMoveMemory</strong>](scsiportmovememory.md)<br/></td>
<td>The <strong>ScsiPortMoveMemory</strong> routine copies data from one location to another.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>ScsiPortQuerySystemTime</strong>](scsiportquerysystemtime.md)<br/></td>
<td>The <strong>ScsiPortQuerySystemTime</strong> routine obtains the current system time.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Srb.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






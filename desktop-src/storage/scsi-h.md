---
title: Scsi.h
description: This section contains reference topics for the Scsi.h header.
ms.assetid: '8D862CBC-875E-4CA2-8714-6B9A02D870B0'
---

# Scsi.h

This section contains reference topics for the Scsi.h header.

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
<td>[SCSI Port Library Routines](scsi-port-library-routines.md)<br/></td>

</tr>
<tr class="even">
<td>[<strong>BLOCK_DEVICE_RANGE_DESCRIPTOR</strong>](block-device-range-descriptor.md)<br/></td>
<td>The <strong>BLOCK_DEVICE_RANGE_DESCRIPTOR</strong> structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>BLOCK_DEVICE_TOKEN_DESCRIPTOR</strong>](block-device-token-descriptor.md)<br/></td>
<td><strong>BLOCK_DEVICE_TOKEN_DESCRIPTOR</strong> contains the token returned from a the POPULATE TOKEN command for an offload read data operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>PHW_ADAPTER_CONTROL</strong>](hwscsiadaptercontrol.md)<br/></td>
<td>A miniport driver's <strong>HwScsiAdapterControl</strong> routine is called to perform synchronous operations to control the state or behavior of an HBA, such as stopping or restarting the HBA for power management.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PHW_ADAPTER_STATE</strong>](hwscsiadapterstate.md)<br/></td>
<td>The <em>HwScsiAdapterState</em> routine saves or restores the state of the miniport driver's HBA. <br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PHW_INTERRUPT</strong>](hwscsidisableinterruptscallback.md)<br/></td>
<td><em>HwScsiDisableInterruptsCallback</em> is called after a miniport driver's <em>HwScsiEnableInterruptsCallback</em> routine calls <strong>ScsiPortNotification</strong> with the <em>NotificationType</em><strong>CallDisableInterrupts</strong>. Miniport drivers of HBAs that require interrupt processing that takes more than 50 microseconds in the ISR should have a pair of <em>HwScsi..InterruptsCallback</em> routines.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PHW_DMA_STARTED</strong>](hwscsidmastarted.md)<br/></td>
<td>If the HBA is a subordinate DMA device, the miniport driver's <em>HwScsiDmaStarted</em> routine is called after the operating system-specific port driver has set up the system DMA controller for a DMA transfer.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<strong>PHW_INTERRUPT</strong>](hwscsienableinterruptscallback.md)<br/></td>
<td><em>HwScsiEnableInterruptsCallback</em> is called after a miniport driver's <em>HwScsiInterrupt</em> routine disables interrupts on the HBA and calls <strong>ScsiPortNotification</strong> with the <em>NotificationType</em><strong>CallEnableInterrupts</strong>. Miniport drivers of HBAs that require interrupt processing that takes more than 50 microseconds in the ISR should have a pair of <em>HwScsi..InterruptsCallback</em> routines.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<em>PHW_FIND_ADAPTER</em>](hwscsifindadapter.md)<br/></td>
<td><em>HwScsiFindAdapter</em> uses supplied configuration information to determine whether it supports a particular HBA and, if so, returns information about its HBA in the given <em>ConfigInfo</em> buffer.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_INITIALIZE</em>](hwscsiinitialize.md)<br/></td>
<td><em>HwScsiInitialize</em> initializes the HBA after a reboot or a power failure occurs.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PHW_INTERRUPT</strong>](hwscsiinterrupt.md)<br/></td>
<td><em>HwScsiInterrupt</em> is called when the HBA generates an interrupt. Miniport drivers of HBAs that do not generate interrupts do not have this routine.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_RESET_BUS</em>](hwscsiresetbus.md)<br/></td>
<td><em>HwScsiResetBus</em> resets a given SCSI bus.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>PHW_STARTIO</strong>](hwscsistartio.md)<br/></td>
<td>All miniport drivers must have a <em>HwScsiStartIo</em> routine. The operating system-specific port driver calls <em>HwScsiStartIo</em> first with each incoming I/O request for a target on a SCSI bus.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PHW_TIMER</em>](hwscsitimer.md)<br/></td>
<td><em>HwScsiTimer</em> is called after the interval specified when the miniport driver called <strong>ScsiPortNotification</strong> with the <strong>RequestTimerCall</strong><em>NotificationType</em> value.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<em>PSCSIWMI_EXECUTE_METHOD</em>](hwscsiwmiexecutemethod.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiExecuteMethod</strong> routine is called to execute a method associated with a data block. This routine is optional.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PSCSIWMI_FUNCTION_CONTROL</em>](hwscsiwmifunctioncontrol.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiFunctionControl</strong> routine is called to enable or disable notification of events. It is also called to enable or disable data collection for data blocks that the miniport driver designated as expensive to collect. This routine is optional.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<em>PSCSIWMI_QUERY_DATABLOCK</em>](hwscsiwmiquerydatablock.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiQueryDataBlock</strong> routine is called to obtain either a single instance or all instances of a data block. This routine is required.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PSCSIWMI_QUERY_REGINFO</em>](hwscsiwmiqueryreginfo.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiQueryReginfo</strong> routine is called to obtain information about the data and event blocks to be registered on behalf of the miniport driver by the SCSI port driver. This routine is required.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<em>PSCSIWMI_SET_DATABLOCK</em>](hwscsiwmisetdatablock.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiSetDataBlock</strong> routine is called to change all data items in a single instance of a data block. This routine is optional.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>[<em>PSCSIWMI_SET_DATAITEM</em>](hwscsiwmisetdataitem.md)<br/></td>
<td>A miniport driver's <strong>HwScsiWmiSetDataItem</strong> routine is called to change a single data item in an instance of a data block. This routine is optional.<br/>
<blockquote>
[!Note]<br />
The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>[<strong>INQUIRYDATA</strong>](inquirydata.md)<br/></td>
<td>The INQUIRYDATA structure is used in conjunction with the [<strong>TapeMiniExtensionInit</strong>](tapeminiextensioninit.md) and [<strong>TapeMiniVerifyInquiry</strong>](tapeminiverifyinquiry.md) routines to report SCSI inquiry data associated with a tape device. <br/></td>
</tr>
<tr class="even">
<td>[<strong>POPULATE_TOKEN_HEADER</strong>](populate-token-header.md)<br/></td>
<td>A populate token parameter list starts with a <strong>POPULATE_TOKEN_HEADER</strong> structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>RECEIVE_TOKEN_INFORMATION_HEADER</strong>](receive-token-information-header.md)<br/></td>
<td>The <strong>RECEIVE_TOKEN_INFORMATION_HEADER</strong> structure contains information returned as status from an offload data transfer operation.<br/></td>
</tr>
<tr class="even">
<td>[<strong>RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</strong>](receive-token-information-response-header.md)<br/></td>
<td>A token, created as a representation of data (ROD), for an offload read data operation is returned in a <strong>RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER</strong> structure.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>TRACK_INFORMATION2</strong>](track-information2.md)<br/></td>
<td>The TRACK_INFORMATION2 structure is used to report track information.<br/></td>
</tr>
<tr class="even">
<td>[<strong>VPD_THIRD_PARTY_COPY_PAGE</strong>](vpd-third-party-copy-page.md)<br/></td>
<td>The <strong>VPD_THIRD_PARTY_COPY_PAGE</strong> structure defines the vital product data (VPD) page for offload data transfer operations.<br/></td>
</tr>
<tr class="odd">
<td>[<strong>WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR</strong>](windows-block-device-token-limits-descriptor.md)<br/></td>
<td>The <strong>WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR</strong> structure is the third party copy descriptor for Windows systems.<br/></td>
</tr>
<tr class="even">
<td>[<strong>WRITE_USING_TOKEN_HEADER</strong>](write-using-token-header.md)<br/></td>
<td>The <strong>WRITE_USING_TOKEN_HEADER</strong> structure describes the destination data locations for an offload write data operation. <br/></td>
</tr>
</tbody>
</table>



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Scsi.h%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






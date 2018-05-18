---
title: RECEIVE\_TOKEN\_INFORMATION\_HEADER structure
description: The RECEIVE\_TOKEN\_INFORMATION\_HEADER structure contains information returned as status from an offload data transfer operation.
ms.assetid: '3D8BF059-2063-499E-B287-41EE184A2264'
keywords: ["RECEIVE_TOKEN_INFORMATION_HEADER structure Storage Devices", "PRECEIVE_TOKEN_INFORMATION_HEADER structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- RECEIVE_TOKEN_INFORMATION_HEADER
api_location:
- scsi.h
api_type:
- HeaderDef
---

# RECEIVE\_TOKEN\_INFORMATION\_HEADER structure

The **RECEIVE\_TOKEN\_INFORMATION\_HEADER** structure contains information returned as status from an offload data transfer operation.

## Syntax


```C++
typedef struct _RECEIVE_TOKEN_INFORMATION_HEADER {
  UCHAR AvailableData[4];
  UCHAR ResponseToServiceAction  :5;
  UCHAR Reserved1  :3;
  UCHAR OperationStatus  :7;
  UCHAR Reserved2   :1;
  UCHAR OperationCounter[2];
  UCHAR EstimatedStatusUpdateDelay[4];
  UCHAR CompletionStatus;
  UCHAR SenseDataFieldLength;
  UCHAR SenseDataLength;
  UCHAR TransferCountUnits;
  UCHAR TransferCount[8];
  UCHAR SegmentsProcessed[2];
  UCHAR Reserved3[6];
  UCHAR SenseData[ANYSIZE_ARRAY];
} RECEIVE_TOKEN_INFORMATION_HEADER, *PRECEIVE_TOKEN_INFORMATION_HEADER;
```



## Members

<dl> <dt>

**AvailableData**
</dt> <dd>

The amount of data available in the **SenseData** array and any additional result information.

</dd> <dt>

**ResponseToServiceAction**
</dt> <dd>

A response code indicating which command action the response is for. The service action codes are the following.



| Value                                                                                                                                                                                                                     | Meaning                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <span id="SERVICE_ACTION_POPULATE_TOKEN"></span><span id="service_action_populate_token"></span><dl> <dt>**SERVICE\_ACTION\_POPULATE\_TOKEN**</dt> </dl>           | The response information is for a POPULATE TOKEN command.<br/>    |
| <span id="SERVICE_ACTION_WRITE_USING_TOKEN"></span><span id="service_action_write_using_token"></span><dl> <dt>**SERVICE\_ACTION\_WRITE\_USING\_TOKEN**</dt> </dl> | The response information is for a WRITE USING TOKEN command.<br/> |



 

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**OperationStatus**
</dt> <dd>

The current status of the copy operation. The status can be one of the following values.



| Value                                                                           | Meaning                                                                                                             |
|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>0x01</dt> </dl> | The operation completed successfully.<br/>                                                                    |
| <dl> <dt>0x02</dt> </dl> | The operation completed unsuccessfully.<br/>                                                                  |
| <dl> <dt>0x04</dt> </dl> | The operation completed successfully but the copy initiator should verify that all data was transferred.<br/> |
| <dl> <dt>0x10</dt> </dl> | The operation is in progress. Foreground or background operation state is unknown.<br/>                       |
| <dl> <dt>0x11</dt> </dl> | The operation is in progress in the foreground.<br/>                                                          |
| <dl> <dt>0x12</dt> </dl> | The operation is in progress in the background.<br/>                                                          |
| <dl> <dt>0x60</dt> </dl> | The operation was terminated. Possibly by an existing resource reservation.<br/>                              |



 

</dd> <dt>

**Reserved2** 
</dt> <dd>

Reserved.

</dd> <dt>

**OperationCounter**
</dt> <dd>

The number of commands processed for the current copy operation.

</dd> <dt>

**EstimatedStatusUpdateDelay**
</dt> <dd>

The recommended time, in milliseconds, to wait before sending the next RECEIVE COPY STATUS command for updated information about the current copy operation.

</dd> <dt>

**CompletionStatus**
</dt> <dd>

SCSI status code for the copy command operation.

</dd> <dt>

**SenseDataFieldLength**
</dt> <dd>

The length, in bytes, of the entire data area available for sense data. This value is always &gt;= **SenseDataLength**.

</dd> <dt>

**SenseDataLength**
</dt> <dd>

The length, in bytes, of the data in **SenseData**.

</dd> <dt>

**TransferCountUnits**
</dt> <dd>

The byte units applied to *TransferCount*. Each unit expansion is a exponent in base 2. The multiplier value of **TRANSFER\_COUNT\_UNITS\_KIBIBYTES**, for example, is 1024 and not 1000. The defined units are the following.



| Value                                                                                                                                                                                                                           | Meaning                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| <span id="TRANSFER_COUNT_UNITS_BYTES"></span><span id="transfer_count_units_bytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_BYTES**</dt> </dl>                          | Transfer count is in bytes.<br/>                                              |
| <span id="TRANSFER_COUNT_UNITS_KIBIBYTES"></span><span id="transfer_count_units_kibibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_KIBIBYTES**</dt> </dl>              | Transfer count is in kilobytes.<br/>                                          |
| <span id="TRANSFER_COUNT_UNITS_MEBIBYTES"></span><span id="transfer_count_units_mebibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_MEBIBYTES**</dt> </dl>              | Transfer count is in megabytes.<br/>                                          |
| <span id="TRANSFER_COUNT_UNITS_GIBIBYTES"></span><span id="transfer_count_units_gibibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_GIBIBYTES**</dt> </dl>              | Transfer count is in gigabytes.<br/>                                          |
| <span id="TRANSFER_COUNT_UNITS_TEBIBYTES"></span><span id="transfer_count_units_tebibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_TEBIBYTES**</dt> </dl>              | Transfer count is in terabytes.<br/>                                          |
| <span id="TRANSFER_COUNT_UNITS_PEBIBYTES"></span><span id="transfer_count_units_pebibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_PEBIBYTES**</dt> </dl>              | Transfer count is in petabytes.<br/>                                          |
| <span id="TRANSFER_COUNT_UNITS_EXBIBYTES"></span><span id="transfer_count_units_exbibytes"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_EXBIBYTES**</dt> </dl>              | Transfer count is in exabytes.<br/>                                           |
| <span id="TRANSFER_COUNT_UNITS_NUMBER_BLOCKS"></span><span id="transfer_count_units_number_blocks"></span><dl> <dt>**TRANSFER\_COUNT\_UNITS\_NUMBER\_BLOCKS**</dt> </dl> | Transfer count is not an exponent, but in units of logical block length.<br/> |



 

</dd> <dt>

**TransferCount**
</dt> <dd>

The length of data transferred in the operation. The unit type in **TransferCountUnits** is applied to this value to give the total byte count.

</dd> <dt>

**SegmentsProcessed**
</dt> <dd>

The number of segments processed for the data transfer operation. Segments are copy length units used internally by a storage device's copy provider. On Windowssystems, this value is reserved and applications must ignore this member.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**SenseData**
</dt> <dd>

Sense data returned for the copy operation.

</dd> </dl>

## Remarks

If **RECEIVE\_TOKEN\_INFORMATION\_HEADER** is for a POPULATE TOKEN command operation, and the command completed successfully, a [**RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER**](receive-token-information-response-header.md) structure will also be present after **SenseData** at an offset of **SenseDataFieldLength** from the beginning of the **SenseData** array. The **RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER** structure will contain the token created as a representation of data (ROD) for the range parameters sent with the command.

All multibyte values are in big endian format. Prior to evaluation, these values must be converted to match the endian format of the current platform.

## Requirements



|                    |                                                                                                                               |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                                 |
| Header<br/>  | <dl> <dt>Scsi.h (include Scsi.h, Minitape.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**RECEIVE\_TOKEN\_INFORMATION\_RESPONSE\_HEADER**](receive-token-information-response-header.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RECEIVE_TOKEN_INFORMATION_HEADER%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







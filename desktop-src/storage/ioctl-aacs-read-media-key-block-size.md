---
title: IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK\_SIZE control code
description: Queries the logical unit for the size of the buffer that is required to hold the Advanced Access Control System (AACS) Media Key Block (MKB).
ms.assetid: 2b8e5461-c935-46d8-afe3-c82a7566a4c7
keywords:
- IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE
api_location:
- Ntddcdvd.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK\_SIZE control code

Queries the logical unit for the size of the buffer that is required to hold the Advanced Access Control System (AACS) Media Key Block (MKB).

## Input Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains the AACS\_LAYER\_NUMBER number of the layer. The AACS\_LAYER\_NUMBER is an unsigned long integer value in the range 0 to 255 inclusive that specifies the layer of the media to which a command applies.

`typedef ULONG AACS_LAYER_NUMBER, *PAACS_LAYER_NUMBER;`

## Input Buffer Length

**Parameters.DeviceIoControl.InputBufferLength** in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= **sizeof**(AACS\_LAYER\_NUMBER).

## Output Buffer

The buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains a ULONG that holds the size in bytes of the full AACS MKB for this media.

## Output Buffer Length

Use this value to determine the size of the buffer to allocate for [**IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK**](ioctl-aacs-read-media-key-block.md). The size is always a multiple of 32,768 (0x8000).

## Status block

The **Information** field is set to the number of bytes transferred. The **Status** field is set to STATUS\_SUCCESS if the operation succeeds. The following failure codes are common with this operation:

<dl> <dt>

<span id="STATUS_COPY_PROTECTION_FAILURE_or_STG_E_STATUS_COPY_PROTECTION_FAILURE"></span><span id="status_copy_protection_failure_or_stg_e_status_copy_protection_failure"></span><span id="STATUS_COPY_PROTECTION_FAILURE_OR_STG_E_STATUS_COPY_PROTECTION_FAILURE"></span>STATUS\_COPY\_PROTECTION\_FAILURE or STG\_E\_STATUS\_COPY\_PROTECTION\_FAILURE
</dt> <dd>

Failure of one of the copy protection mechanisms.

</dd> <dt>

<span id="STATUS_CSS_AUTHENTICATION_FAILURE_or_STG_E_CSS_AUTHENTICATION_FAILURE"></span><span id="status_css_authentication_failure_or_stg_e_css_authentication_failure"></span><span id="STATUS_CSS_AUTHENTICATION_FAILURE_OR_STG_E_CSS_AUTHENTICATION_FAILURE"></span>STATUS\_CSS\_AUTHENTICATION\_FAILURE or STG\_E\_CSS\_AUTHENTICATION\_FAILURE
</dt> <dd>

The authentication process has failed.

</dd> <dt>

<span id="STATUS_CSS_KEY_NOT_PRESENT_or_STG_E_CSS_KEY_NOT_PRESENT"></span><span id="status_css_key_not_present_or_stg_e_css_key_not_present"></span><span id="STATUS_CSS_KEY_NOT_PRESENT_OR_STG_E_CSS_KEY_NOT_PRESENT"></span>STATUS\_CSS\_KEY\_NOT\_PRESENT or STG\_E\_CSS\_KEY\_NOT\_PRESENT
</dt> <dd>

No AACS protection exists for this media.

</dd> <dt>

<span id="STATUS_CSS_KEY_NOT_ESTABLISHED_or_STG_E_CSS_KEY_NOT_ESTABLISHED"></span><span id="status_css_key_not_established_or_stg_e_css_key_not_established"></span><span id="STATUS_CSS_KEY_NOT_ESTABLISHED_OR_STG_E_CSS_KEY_NOT_ESTABLISHED"></span>STATUS\_CSS\_KEY\_NOT\_ESTABLISHED or STG\_E\_CSS\_KEY\_NOT\_ESTABLISHED
</dt> <dd>

The AGID for AACS has not been established.

</dd> </dl>

## Remarks

The IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK\_SIZE request will not work if the media in the logical unit is not AACS protected.

The IOCTL\_AACS\_READ\_MEDIA\_KEY\_BLOCK\_SIZE request corresponds to one of the steps of the Advanced Access Content System (AACS) authentication algorithm (AACS-Auth). For a complete description of AACS-Auth, see the *Advanced Access Content System, Introduction and Common Cryptographic Elements* specification that is published by Advanced Access Content System Licensing Administrator (AACS LA).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Ntddcdvd.h (include Ntddcdvd.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






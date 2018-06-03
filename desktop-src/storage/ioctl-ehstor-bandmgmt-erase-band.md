---
title: IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND control code
description: The IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND request will cryptographically erase and reset the authentication key of a band. The remaining configuration of the band is left unmodified.
ms.assetid: E7DE8E55-B753-42AF-B25F-F806EE37DCF1
keywords:
- IOCTL_EHSTOR_BANDMGMT_ERASE_BAND control code Storage Devices
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_ERASE_BAND
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND control code

The **IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND** request will cryptographically erase and reset the authentication key of a band. The remaining configuration of the band is left unmodified.

## Input Buffer

The input buffer at *Irp-&gt;AssociatedIrp.SystemBuffer* must contain an [**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md) and possibly an **AUTH\_KEY** structure.

If the **NewAuthKeyOffset** member of [**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md) is set to **EHSTOR\_BANDMGR\_NO\_KEY**, the input data in the system buffer need not include an **AUTH\_KEY** structure.

## Input Buffer Length

*Parameters.DeviceIoControl.InputBufferLength* indicates the size, in bytes, of the buffer, which must be at least **sizeof** (ERASE\_BAND\_PARAMETERS) + **sizeof**(AUTH\_KEY).

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                     | Description                                                                             |
|----------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                  | The band was successfully deleted.                                                      |
| STATUS\_INVALID\_DEVICE\_REQUEST | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE    | The input buffer size is incorrect.                                                     |
| STATUS\_INVALID\_PARAMETER       | Information in the input buffer is invalid.                                             |
| STATUS\_ACCESS\_DENIED           | The erase authentication key is not a default key and the band cannot be erased.        |
| STATUS\_NOT\_FOUND               | The band was not found for the selection criteria provided.                             |
| STATUS\_IO\_DEVICE\_ERROR        | Communication failed. The storage device might be incompatible with security protocols. |



 

## Remarks

A current erase authentication key is not provided in an **IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND** request. The erase authentication key for the storage device is previously configured.

No method is provided in Windows to change the erase authentication key for a storage device. Provided that the correct parameters are given as input in the system buffer, this request should succeed. If the erase authentication key was changed outside of Windows, such as in a dual-boot environment with a different operating system, this request may fail.

When a band is erased with **IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND**, the only prior properties that remain are band start and band size. The previous media encryption key is removed and a new key is generated. Locking is set to **PERSISTANT\_UNLOCK** for both reading and writing. Security metadata previously set is erased. The new authentication key specified in [**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md) is set unless use of the default key is indicated.

To prevent other applications from taking control of a band and erase by using the default key, a new authentication key should be included with the **IOCTL\_EHSTOR\_BANDMGMT\_ERASE\_BAND** request.

The changes made to the band table by this request are committed to the device atomically before the IOCTL request completes. Therefore, it is guaranteed that the band is modified with all of its properties set or no properties set at all should a system or power failure occur.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**ERASE\_BAND\_PARAMETERS**](erase-band-parameters.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_DELETE\_BAND**](ioctl-ehstor-bandmgmt-delete-band.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_ERASE_BAND%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







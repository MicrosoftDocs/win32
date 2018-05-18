---
title: IOCTL\_EHSTOR\_BANDMGMT\_REVERT control code
description: This IOCTL\_EHSTOR\_BANDMGMT\_REVERT request is sent to deactivate the security features and band management on a storage device. The request includes revert options and the authentication key.
ms.assetid: '981655A8-B6DC-4720-8D2E-B42AA0859FB2'
keywords: ["IOCTL_EHSTOR_BANDMGMT_REVERT control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_BANDMGMT_REVERT
api_location:
- EhStorBandMgmt.h
api_type:
- HeaderDef
---

# IOCTL\_EHSTOR\_BANDMGMT\_REVERT control code

This **IOCTL\_EHSTOR\_BANDMGMT\_REVERT** request is sent to deactivate the security features and band management on a storage device. The request includes revert options and the authentication key.

## Input Buffer

The input buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** contains an **ACTIVATE\_REVERT\_PARAMETERS** structure. **ACTIVATE\_REVERT\_PARAMETERS** is declared in *ehstorbandmgmt.h* as the following.


```
typedef struct _ACTIVATE_REVERT_PARAMETERS
{
    ULONG           StructSize;
    ULONG           Flags;
    ULONG           AuthKeyOffset;
} ACTIVATE_REVERT_PARAMETERS;
```



<dl> <dt>

<span id="StructSize"></span><span id="structsize"></span><span id="STRUCTSIZE"></span>StructSize
</dt> <dd>

The size of the structure. This is set to **sizeof**(ACTIVATE\_REVERT\_PARAMETERS).

</dd> <dt>

<span id="Flags"></span><span id="flags"></span><span id="FLAGS"></span>Flags
</dt> <dd>

A bitmask of deactivation flags. This is a bitwise OR value of the following.



| Flag                  | Description                                                |
|-----------------------|------------------------------------------------------------|
| REVERT\_PSID\_AUTHKEY | The authentication key at **AuthKeyOffset** is a PSID key. |



 

</dd> <dt>

<span id="AuthKeyOffset"></span><span id="authkeyoffset"></span><span id="AUTHKEYOFFSET"></span>AuthKeyOffset
</dt> <dd>

The offset from the beginning of the system buffer to the location of an **AUTH\_KEY** structure.

</dd> </dl>

Following **ACTIVATE\_REVERT\_PARAMETERS** in the system buffer is an **AUTH\_KEY** structure. This holds the key data bytes for the authentication key. **AUTH\_KEY** is declared in *ehstorbandmgmt.h* as the following.


```
typedef struct _AUTH_KEY
{
    ULONG   KeySize;
    UCHAR   Key[ANYSIZE_ARRAY];
} AUTH_KEY;
```



<dl> <dt>

<span id="KeySize"></span><span id="keysize"></span><span id="KEYSIZE"></span>KeySize
</dt> <dd>

The size of the key, in bytes, of the key data at **Key**. If **KeySize** is set to 0, a default key is used.

</dd> <dt>

<span id="Key"></span><span id="key"></span><span id="KEY"></span>Key
</dt> <dd>

A variable length byte array that contains the key data.

</dd> </dl>

## Input Buffer Length

The length of an **ACTIVATE\_REVERT\_PARAMETERS** structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

One of the following values can be returned in the **Status** field.



| Status Value                         | Description                                                                             |
|--------------------------------------|-----------------------------------------------------------------------------------------|
| STATUS\_SUCCESS                      | Security features on the storage device were deactivated.                               |
| STATUS\_INVALID\_DEVICE\_REQUEST     | The storage device does not support band management.                                    |
| STATUS\_INVALID\_BUFFER\_SIZE        | The input buffer size is invalid.                                                       |
| STATUS\_INVALID\_PARAMETER           | Information in the input buffer is invalid.                                             |
| STATUS\_ACCESS\_DENIED               | The authentication key is invalid. Deactivation is denied.                              |
| STATUS\_DEVICE\_CONFIGURATION\_ERROR | The system cannot configure the device in a supported mode.                             |
| STATUS\_IO\_DEVICE\_ERROR            | Communication failed. The storage device might be incompatible with security protocols. |
| STATUS\_INVALID\_DEVICE\_STATE       | The storage device is not activated.                                                    |



 

## Remarks

On successful return from an **IOCTL\_EHSTOR\_BANDMGMT\_REVERT** request, the storage device will return to an inactive security state and all band management IOCTLs, except for [**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md) and [**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md), become unavailable.

## Requirements



|                    |                                                                                                                        |
|--------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                           |
| Header<br/>  | <dl> <dt>EhStorBandMgmt.h (include EhStorBandMgmt.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_ACTIVATE**](ioctl-ehstor-bandmgmt-activate.md)
</dt> <dt>

[**IOCTL\_EHSTOR\_BANDMGMT\_QUERY\_CAPABILITIES**](ioctl-ehstor-bandmgmt-query-capabilities.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_BANDMGMT_REVERT%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







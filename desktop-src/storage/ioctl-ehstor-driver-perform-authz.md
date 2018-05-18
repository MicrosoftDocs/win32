---
title: IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ control code
description: IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ is sent by the Enhanced Storage Class Driver (EHSTOR) to the silo driver to initiate on-demand authentication or deauthentication.
ms.assetid: '689EE1EB-820A-4873-92C5-08F5F1873825'
keywords: ["IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ control code Storage Devices"]
topic_type:
- apiref
api_name:
- IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ
api_location:
- EhStorIoctl.h
api_type:
- HeaderDef
---

# IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ control code

**IOCTL\_EHSTOR\_DRIVER\_PERFORM\_AUTHZ** is sent by the Enhanced Storage Class Driver (EHSTOR) to the silo driver to initiate on-demand authentication or deauthentication.

## Input Buffer

The input buffer at **Irp-&gt;AssociatedIrp.SystemBuffer** must contain an **AUTHZ\_STATE** structure that indicates the type of authentication operation to perform. **AUTHZ\_STATE** is declared in *ehstorioctl.h* as the following.


```
typedef struct _AUTHZ_STATE
{
    ULONG AuthzState;
} AUTHZ_STATE;
```



The value of **AuthzState** specifies the authentication operation. This is one of the following.



| Value                             | Description                                                              |
|-----------------------------------|--------------------------------------------------------------------------|
| 0                                 | Perform on-demand deauthentication.                                      |
| AUTHZSTATE\_AUTHENTICATE          | Perform on-demand authentication.                                        |
| AUTHZSTATE\_CLEAR\_AUTHKEY\_CACHE | Perform on-demand deauthentication and clear cached authentication keys. |



 

## Input Buffer Length

The length of an **AUTHZ\_STATE** structure.

## Output Buffer

None.

## Output Buffer Length

None.

## Status block

STATUS\_SUCCESS is returned in the **Status** field by the silo driver if the authentication state is changed. Otherwise, STATUS\_UNSUCCESSFUL is returned.

## Remarks

This IOCTL is sent by EHSTOR to a silo driver that supports on-demand authentication. The silo driver notifies EHSTOR of this capability in a prior [**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md) request with the **CAP\_ON\_DEMAND\_AUTHENTICATION** flag set in the **Capabilities** member of [**SILO\_DRIVER\_CAPABILITES**](act-authz-state.md).

In response to this IOCTL, the silo driver performs authentication or deauthentication for the device. For banded devices, the silo driver will, depending on the specified operation in the system buffer, unlock or lock as many bands as possible for reads and writes.

If the silo driver fails to perform the requested operation, it will not change the authentication state of a device.

If the **AuthzState** member of **AUTHZ\_STATE** is set to **AUTHZSTATE\_CLEAR\_AUTHKEY\_CACHE**, then the silo driver clears its authentication key cache in addition to deauthenticating. **AUTHZSTATE\_CLEAR\_AUTHKEY\_CACHE** is set when the system is shutting down or hibernating. This prevents the presence of the key cache in the hibernation file.

If a device supports multiple silos, authentication by each silo is exclusive. An authentication operation by one silo driver does not affect the authentication state set by another silo driver.

## Requirements



|                    |                                                                                                                  |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8<br/>                                                                     |
| Header<br/>  | <dl> <dt>EhStorIoctl.h (include EhStorIoctl.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_EHSTOR\_DRIVER\_REPORT\_CAPABILITIES**](ioctl-ehstor-driver-report-capabilities.md)
</dt> <dt>

[**SILO\_DRIVER\_CAPABILITES**](act-authz-state.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ%20control%20code%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







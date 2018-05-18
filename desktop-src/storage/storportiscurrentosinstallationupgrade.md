---
title: StorPortIsCurrentOsInstallationUpgrade routine
description: The StorPortIsCurrentOsInstallationUpgrade routine checks if the current installation of Windows is an upgrade from a previous version or not.
ms.assetid: '68D944D9-1A52-4FB0-B2D7-9680AB1EDABB'
keywords: ["StorPortIsCurrentOsInstallationUpgrade routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortIsCurrentOsInstallationUpgrade
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortIsCurrentOsInstallationUpgrade routine

The **StorPortIsCurrentOsInstallationUpgrade** routine checks if the current installation of Windows is an upgrade from a previous version or not.

## Syntax


```C++
ULONG StorPortIsCurrentOsInstallationUpgrade(
  _In_  PVOID   HwDeviceExtension,
  _Out_ BOOLEAN *Upgraded
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Upgraded* \[out\]
</dt> <dd>

The value pointed to by *Upgraded* is set to **TRUE** if the current operating system installation was upgraded from a previous version. Otherwise, it is set to **FALSE**.

</dd> </dl>

## Return value

The **StorPortIsCurrentOsInstallationUpgrade** routine returns one of these status codes:



| Return code                                                                                                     | Description                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | An upgrade status is returned in the value pointed to by the *Upgraded* parameter.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The pointer value in *Upgraded* is NULL.<br/>                                           |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>      | The current IRQL &gt; PASSIVE\_LEVEL.<br/>                                              |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.1.<br/>                                                                                      |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |
| IRQL<br/>            | IRQL == PASSIVE\_LEVEL<br/>                                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortIsCurrentOsInstallationUpgrade%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






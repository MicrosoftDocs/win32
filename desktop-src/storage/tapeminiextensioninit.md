---
title: TAPE\_EXTENSION\_INIT\_ROUTINE routine
description: ExtensionInit initializes an optional, driver-specific context area. This routine is called by TapeClassInitialize when the tape miniclass driver is loaded. This routine is optional.
ms.assetid: 4837b9c2-a3c1-4574-8f5b-4bf7c7d037a0
keywords:
- ( TAPE_EXTENSION_INIT_ROUTINE) routine Storage Devices
- TAPE_EXTENSION_INIT_ROUTINE
topic_type:
- apiref
api_name:
- ( TAPE_EXTENSION_INIT_ROUTINE)
api_location:
- minitape.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# TAPE\_EXTENSION\_INIT\_ROUTINE routine

*ExtensionInit* initializes an optional, driver-specific context area. This routine is called by [**TapeClassInitialize**](tapeclassinitialize.md) when the tape miniclass driver is loaded. This routine is optional.

## Syntax


```C++
TAPE_EXTENSION_INIT_ROUTINE (*TAPE_EXTENSION_INIT_ROUTINE);

VOID (*TAPE_EXTENSION_INIT_ROUTINE)(
  _In_ PVOID                   MinitapeExtension,
  _In_ PINQUIRYDATA            InquiryData,
  _In_ PMODE_CAPABILITIES_PAGE ModeCapabilitiesPage
)
{ ... }
```



## Parameters

<dl> <dt>

*MinitapeExtension* \[in\]
</dt> <dd>

Pointer to a buffer of the size requested by the tape miniclass driver when it initialized.

</dd> <dt>

*InquiryData* \[in\]
</dt> <dd>

Pointer to the SCSI inquiry data for the tape device.

</dd> <dt>

*ModeCapabilitiesPage* \[in\]
</dt> <dd>

Pointer to a buffer that contains low-level information for the tape device. The format of this page is defined by the QIC 157 standard and is subject to change. This is **NULL** if the device does not support a mode capabilities page.

</dd> </dl>

## Return value

None

## Remarks

A tape miniclass driver requests a minitape extension by specifying a nonzero value for **MinitapeExtensionSize** in the [**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md) structure it passes to [**TapeClassInitialize**](tapeclassinitialize.md) from its **DriverEntry** routine. A miniclass driver defines the structure and contents of the minitape extension and typically uses it to store inquiry data for the devices it supports.

The tape class driver allocates the minitape extension and supplies it subsequently in calls to to the tape miniclass driver's routines that handle the device-specific aspects of device-control requests and to the miniclass driver's optional [**TapeMiniTapeError**](tapeminitapeerror.md) routine.

*ExtensionInit* initializes the minitape extension, and the miniclass driver uses this area to maintain run-time state for its device. The tape class driver passes *InquiryData* and a *ModeCapabilitiesPage* to this routine because those structures contain information that a tape miniclass driver might want to store in the minitape extension.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**DriverEntry of Tape Miniclass Driver**](driverentry-of-tape-miniclass-driver.md)
</dt> <dt>

[**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md)
</dt> <dt>

[**TapeClassInitialize**](tapeclassinitialize.md)
</dt> <dt>

[**TAPE\_STATUS**](tape-status.md)
</dt> <dt>

[**TapeMiniTapeError**](tapeminitapeerror.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_EXTENSION_INIT_ROUTINE%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







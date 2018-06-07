---
title: TAPE\_INIT\_DATA\_EX structure
description: TAPE\_INIT\_DATA\_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass DriverEntry routine passes this information to the tape class driver to complete miniclass driver initialization.
ms.assetid: 438c736e-c9be-4a75-a062-4614ea7fe028
keywords:
- TAPE_INIT_DATA_EX structure Storage Devices
- PTAPE_INIT_DATA_EX structure pointer Storage Devices
topic_type:
- apiref
api_name:
- TAPE_INIT_DATA_EX
api_location:
- minitape.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# TAPE\_INIT\_DATA\_EX structure

TAPE\_INIT\_DATA\_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass **DriverEntry** routine passes this information to the tape class driver to complete miniclass driver initialization.

## Syntax


```C++
typedef struct _TAPE_INIT_DATA_EX {
  ULONG                        InitDataSize;
  TAPE_VERIFY_INQUIRY_ROUTINE  VerifyInquiry;
  BOOLEAN                      QueryModeCapabilitiesPage;
  ULONG                        MinitapeExtensionSize;
  TAPE_EXTENSION_INIT_ROUTINE  ExtensionInit;
  ULONG                        DefaultTimeOutValue;
  TAPE_ERROR_ROUTINE           TapeError;
  ULONG                        CommandExtensionSize;
  TAPE_PROCESS_COMMAND_ROUTINE CreatePartition;
  TAPE_PROCESS_COMMAND_ROUTINE Erase;
  TAPE_PROCESS_COMMAND_ROUTINE GetDriveParameters;
  TAPE_PROCESS_COMMAND_ROUTINE GetMediaParameters;
  TAPE_PROCESS_COMMAND_ROUTINE GetPosition;
  TAPE_PROCESS_COMMAND_ROUTINE GetStatus;
  TAPE_PROCESS_COMMAND_ROUTINE Prepare;
  TAPE_PROCESS_COMMAND_ROUTINE SetDriveParameters;
  TAPE_PROCESS_COMMAND_ROUTINE SetMediaParameters;
  TAPE_PROCESS_COMMAND_ROUTINE SetPosition;
  TAPE_PROCESS_COMMAND_ROUTINE WriteMarks;
  TAPE_PROCESS_COMMAND_ROUTINE PreProcessReadWrite;
  TAPE_PROCESS_COMMAND_ROUTINE TapeGetMediaTypes;
  ULONG                        MediaTypesSupported;
  TAPE_PROCESS_COMMAND_ROUTINE TapeWMIOperations;
  ULONG                        Reserved[2];
} TAPE_INIT_DATA_EX, *PTAPE_INIT_DATA_EX;
```



## Members

<dl> <dt>

**InitDataSize**
</dt> <dd> <dl> <dt>


</dt> <dt>

drivers can be as seamless as possible.
</dt> </dl> </dd> <dt>

**VerifyInquiry**
</dt> <dd>

Specifies the entry point of the tape miniclass driver's [**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md) routine, which determines whether the driver supports a given device. This routine is required.

</dd> <dt>

**QueryModeCapabilitiesPage**
</dt> <dd>

Directs the tape class driver when **TRUE** to pass a mode capabilities page to the tape miniclass driver's [**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md) and [**TapeMiniExtensionInit**](tapeminiextensioninit.md) routines.

</dd> <dt>

**MinitapeExtensionSize**
</dt> <dd>

Specifies the size, in bytes, of a driver-specific context area. If this member is nonzero, **ExtensionInit** must not be **NULL**. This value is optional and must be set to zero if not used.

</dd> <dt>

**ExtensionInit**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniExtensionInit**](tapeminiextensioninit.md) routine, which initializes an optional minitape extension, if any. If **MiniTapeExtensionSize** is zero, **ExtensionInit** must be **NULL**.

</dd> <dt>

**DefaultTimeOutValue**
</dt> <dd>

Specifies the number of seconds that the tape class driver waits for an SRB request before canceling it. If this value is zero, the tape class driver sets an appropriate default value. The tape class driver always uses the default time-out value for read and write requests. The routines contained in the TAPE\_INIT\_DATA\_EX structure can override the default time-out value for device control requests by setting **TimeOutValue** in an SRB.

</dd> <dt>

**TapeError**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniTapeError**](tapeminitapeerror.md) routine, which augments the error-handling activities of the tape class driver. This routine is optional. If one is not used, **TapeError** must be set to **NULL**.

</dd> <dt>

**CommandExtensionSize**
</dt> <dd>

Specifies the size, in bytes, of a command extension to be allocated before the start of each tape command. A tape miniclass driver uses the command extension to store context during the processing of tape commands. Its size and internal structure are defined by the tape miniclass driver. A command extension is optional. If one is not used, **CommandExtensionSize** must be set to zero.

</dd> <dt>

**CreatePartition**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniCreatePartition**](tapeminicreatepartition.md) routine, which creates a partition on a tape. This routine is required.

</dd> <dt>

**Erase**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniErase**](https://msdn.microsoft.com/library/windows/hardware/ff567933) routine, which erases a tape. This routine is required.

</dd> <dt>

**GetDriveParameters**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniGetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567936) routine, which handles requests to get drive parameters. This routine is required.

</dd> <dt>

**GetMediaParameters**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniGetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567937) routine, which handles requests to get media parameters. This routine is required.

</dd> <dt>

**GetPosition**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniGetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567946) routine, which handles requests to get the position of a tape. This routine is required.

</dd> <dt>

**GetStatus**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff567949) routine, which handles requests for status. This routine is required.

</dd> <dt>

**Prepare**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniPrepare**](https://msdn.microsoft.com/library/windows/hardware/ff567950) routine, which prepares a tape device. This routine is required.

</dd> <dt>

**SetDriveParameters**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniSetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567952) routine, which sets drive parameters. This routine is required.

</dd> <dt>

**SetMediaParameters**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniSetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567953) routine, which sets media parameters. This routine is required.

</dd> <dt>

**SetPosition**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniSetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567954) routine, which positions a tape. This routine is required.

</dd> <dt>

**WriteMarks**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniWriteMarks**](https://msdn.microsoft.com/library/windows/hardware/ff567958) routine, which writes marks to tape. This routine is required.

</dd> <dt>

**PreProcessReadWrite**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniPreProcessReadWrite**](https://msdn.microsoft.com/library/windows/hardware/ff567951) routine, which executes device-specific operations before all reads and writes. This routine is optional and is not needed by most drivers. If one is not used, **PreProcessReadWrite** must be **NULL**.

</dd> <dt>

**TapeGetMediaTypes**
</dt> <dd>

Pointer to the tape miniclass driver's [**TapeMiniGetMediaTypes**](https://msdn.microsoft.com/library/windows/hardware/ff567939) routine, which gets a description of each media type supported by a tape device. This routine is required.

</dd> <dt>

**MediaTypesSupported**
</dt> <dd>

Indicates the number of media types supported by the device.

</dd> <dt>

**TapeWMIOperations**
</dt> <dd>

Pointer to the [*TapeMiniWMIControl*](https://msdn.microsoft.com/library/windows/hardware/ff567957) routine.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

A tape miniclass driver's **DriverEntry** routine calls [**TapeClassZeroMemory**](tapeclasszeromemory.md) to clear TAPE\_INIT\_DATA\_EX, fills in the required members and any appropriate optional members, and [**TapeClassInitialize**](tapeclassinitialize.md) with a pointer to this structure.

The names of the tape miniclass driver routines indicated in the member descriptions of this structure are just placeholder names. The prototype for these routines is declared in *newtape.h* as follows:


```
typedef
TAPE_STATUS
(*TAPE_PROCESS_COMMAND_ROUTINE)(
  IN OUT PVOID  MinitapeExtension,
  IN OUT PVOID  CommandExtension,
  IN OUT PVOID  CommandParameters,
  IN OUT PSCSI_REQUEST_BLOCK  Srb,
  IN ULONG  CallNumber,
  IN TAPE_STATUS  StatusOfLastCommand,
  IN OUT PULONG  RetryFlags
  );
```



The meaning of this prototype's parameters are different for each miniclass driver routine. For detailed information about how these parameters are used see the descriptions for each individual miniclass driver routine.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



## See also

<dl> <dt>

[**DriverEntry of Tape Miniclass Driver**](driverentry-of-tape-miniclass-driver.md)
</dt> <dt>

[**TapeClassInitialize**](tapeclassinitialize.md)
</dt> <dt>

[**TapeClassZeroMemory**](tapeclasszeromemory.md)
</dt> <dt>

[**TapeMiniCreatePartition**](tapeminicreatepartition.md)
</dt> <dt>

[**TapeMiniErase**](https://msdn.microsoft.com/library/windows/hardware/ff567933)
</dt> <dt>

[**TapeMiniExtensionInit**](tapeminiextensioninit.md)
</dt> <dt>

[**TapeMiniGetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567936)
</dt> <dt>

[**TapeMiniGetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567937)
</dt> <dt>

[**TapeMiniGetMediaTypes**](https://msdn.microsoft.com/library/windows/hardware/ff567939)
</dt> <dt>

[**TapeMiniGetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567946)
</dt> <dt>

[**TapeMiniGetStatus**](https://msdn.microsoft.com/library/windows/hardware/ff567949)
</dt> <dt>

[**TapeMiniPrepare**](https://msdn.microsoft.com/library/windows/hardware/ff567950)
</dt> <dt>

[**TapeMiniSetDriveParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567952)
</dt> <dt>

[**TapeMiniSetMediaParameters**](https://msdn.microsoft.com/library/windows/hardware/ff567953)
</dt> <dt>

[**TapeMiniSetPosition**](https://msdn.microsoft.com/library/windows/hardware/ff567954)
</dt> <dt>

[**TapeMiniTapeError**](tapeminitapeerror.md)
</dt> <dt>

[**TapeMiniVerifyInquiry**](tapeminiverifyinquiry.md)
</dt> <dt>

[**TapeMiniWriteMarks**](https://msdn.microsoft.com/library/windows/hardware/ff567958)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_INIT_DATA_EX%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







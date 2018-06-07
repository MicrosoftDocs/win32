---
title: TAPE\_INIT\_DATA structure
description: TAPE\_INIT\_DATA is used only by legacy tape miniclass drivers. Use TAPE\_INIT\_DATA\_EX instead.
ms.assetid: 11f5201b-ddd3-43ad-9746-a1a9885c99b1
keywords:
- TAPE_INIT_DATA structure Storage Devices
topic_type:
- apiref
api_name:
- TAPE_INIT_DATA
api_location:
- Minitape.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# TAPE\_INIT\_DATA structure

TAPE\_INIT\_DATA is used only by legacy tape miniclass drivers. Use [**TAPE\_INIT\_DATA\_EX**](tape-init-data-ex.md) instead.

## Remarks

TAPE\_INIT\_DATA is defined as follows.


```
typedef struct _TAPE_INIT_DATA { 
  TAPE_VERIFY_INQUIRY_ROUTINE     VerifyInquiry;   
  BOOLEAN                         QueryModeCapabilitiesPage; 
  ULONG                           MinitapeExtensionSize; 
  TAPE_EXTENSION_INIT_ROUTINE     ExtensionInit;          /* OPTIONAL */
  ULONG                           DefaultTimeOutValue;    /* OPTIONAL */
  TAPE_ERROR_ROUTINE              TapeError;              /* OPTIONAL */
  ULONG                           CommandExtensionSize; 
  TAPE_PROCESS_COMMAND_ROUTINE    CreatePartition; 
  TAPE_PROCESS_COMMAND_ROUTINE    Erase; 
  TAPE_PROCESS_COMMAND_ROUTINE    GetDriveParameters; 
  TAPE_PROCESS_COMMAND_ROUTINE    GetMediaParameters; 
  TAPE_PROCESS_COMMAND_ROUTINE    GetPosition; 
  TAPE_PROCESS_COMMAND_ROUTINE    GetStatus; 
  TAPE_PROCESS_COMMAND_ROUTINE    Prepare; 
  TAPE_PROCESS_COMMAND_ROUTINE    SetDriveParameters; 
  TAPE_PROCESS_COMMAND_ROUTINE    SetMediaParameters; 
  TAPE_PROCESS_COMMAND_ROUTINE    SetPosition; 
  TAPE_PROCESS_COMMAND_ROUTINE    WriteMarks; 
  TAPE_PROCESS_COMMAND_ROUTINE    PreProcessReadWrite; 
} TAPE_INIT_DATA, *PTAPE_INIT_DATA;
```



## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TAPE_INIT_DATA%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






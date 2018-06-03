---
title: PHW\_FIND\_ADAPTER callback function
description: The PHW\_FIND\_ADAPTER prototype declares a routine that uses supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.
ms.assetid: 265dce25-cecb-4bd1-8f5f-1646779da296
keywords:
- ( PHW_FIND_ADAPTER) callback function Storage Devices
topic_type:
- apiref
api_name:
- ( PHW_FIND_ADAPTER)
api_location:
- srb.h
api_type:
- UserDefined
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PHW\_FIND\_ADAPTER callback function

The PHW\_FIND\_ADAPTER prototype declares a routine that uses supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.

## Syntax


```C++
typedef ULONG (*PHW_FIND_ADAPTER)(
  _In_    PVOID                           DeviceExtension ,
  _In_    PVOID                           HwContext ,
  _In_    PVOID                           BusInformation,
  _In_    PCHAR                           ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
  _Out_   PBOOLEAN                        Again
);
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Pointer to the miniport driver's per-HBA storage area.

</dd> <dt>

*HwContext* \[in\]
</dt> <dd>

Reserved member when used by one of the Storport driver's miniport drivers. With SCSI miniport drivers this member points to a context value. For a description of the meaning of this member for a SCSI miniport driver, see [*HwScsiFindAdapter*](hwscsifindadapter.md).

</dd> <dt>

*BusInformation* \[in\]
</dt> <dd>

Reserved member when used by one of the Storport driver's miniport drivers. With SCSI miniport drivers this member points to bus-type-specific information that the OS-specific port driver has gathered. For a complete description of the meaning of this member for a SCSI miniport driver, see [*HwScsiFindAdapter*](hwscsifindadapter.md).

</dd> <dt>

*ArgumentString* \[in\]
</dt> <dd>

Reserved member when used by one of the Storport driver's miniport drivers. With SCSI miniport drivers this member points to a null-terminated ASCII string that contains device information such as a base parameter or an interrupt level from the registry. For a complete description of the meaning of this member for a SCSI miniport driver, see [*HwScsiFindAdapter*](hwscsifindadapter.md).

</dd> <dt>

*ConfigInfo* \[in, out\]
</dt> <dd> <dl> <dt>

Points to a PORT\_CONFIGURATION\_INFORMATION structure that the miniport driver uses during initialization. 
</dt> <dt>

For more information about how a SCSI miniport driver uses this member, see the description of the *ConfigId* member of the [**PORT\_CONFIGURATION\_INFORMATION (SCSI)**](port-configuration-information--scsi-.md) structure.
</dt> <dt>

For more information about how this member is used by a miniport driver that works with the StorPort driver, see the description of the *PortConfiguration* member of the [**PORT\_CONFIGURATION\_INFORMATION (STORPORT)**](port-configuration-information--storport-.md) structure.
</dt> </dl> </dd> <dt>

*Again* \[out\]
</dt> <dd>

Reserved member when used by one of the Storport driver's miniport drivers. With SCSI miniport drivers this member points to a BOOLEAN variable that informs the port driver whether it should call this routine again. For more information about the meaning of this member for a SCSI miniport driver, see [*HwScsiFindAdapter*](hwscsifindadapter.md).

</dd> </dl>

## Return value

The routine declared by this prototype must return one of the following status values:



| Return code                                                                                            | Description                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SP\_RETURN\_FOUND**</dt> </dl>       | Indicates a supported HBA was found and that the HBA-relevant configuration information was successfully determined and set in the PORT\_CONFIGURATION\_INFORMATION structure.<br/>         |
| <dl> <dt>**SP\_RETURN\_ERROR**</dt> </dl>       | Indicates an HBA was found but there was error obtaining the configuration information. If possible, such an error should be logged with [**ScsiPortLogError**](scsiportlogerror.md).<br/> |
| <dl> <dt>**SP\_RETURN\_BAD\_CONFIG**</dt> </dl> | Indicates the supplied configuration information was invalid for the adapter.<br/>                                                                                                          |
| <dl> <dt>**SP\_RETURN\_NOT\_FOUND**</dt> </dl>  | Indicates no supported HBA was found for the supplied configuration information.<br/>                                                                                                       |



 

## Remarks

This declaration is used by both SCSI and StorPort miniport drivers.

For more information about the SCSI miniport driver's version of the routine associated with this declaration, see [*HwScsiFindAdapter*](hwscsifindadapter.md).

For more information about the Storport driver's version of the routine associated with this declaration, see [**HwStorFindAdapter**](hwstorfindadapter.md).

## Requirements



|                            |                                                                                                                             |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                                          |
| Header<br/>          | <dl> <dt>Srb.h (include Storport.h, Srb.h, or Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[*HwScsiFindAdapter*](hwscsifindadapter.md)
</dt> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PHW_FIND_ADAPTER%20callback%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: VirtualHwStorFindAdapter routine
description: The Storport virtual miniport uses configuration information supplied to the VirtualHwStorFindAdapter routine to further initialize itself.
ms.assetid: 55c16545-194e-4d23-b2e6-26821180eafa
keywords:
- VirtualHwStorFindAdapter routine Storage Devices
- VIRTUAL_HW_FIND_ADAPTER
topic_type:
- apiref
api_name:
- VirtualHwStorFindAdapter
api_location:
- Storport.h
api_type:
- UserDefined
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# VirtualHwStorFindAdapter routine

The Storport virtual miniport uses configuration information supplied to the **VirtualHwStorFindAdapter** routine to further initialize itself.

## Syntax


```C++
VIRTUAL_HW_FIND_ADAPTER VirtualHwStorFindAdapter;

ULONG VirtualHwStorFindAdapter(
   IN PVOID                               DeviceExtension,
   IN PVOID                               HwContext,
   IN PVOID                               BusInformation,
   IN PVOID                               LowerDevice,
   IN PCHAR                               ArgumentString,
   IN OUT PPORT_CONFIGURATION_INFORMATION ConfigInfo,
   OUT PBOOLEAN                           Again
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* 
</dt> <dd>

A pointer to the miniport driver's per-adapter non-paged storage area. The operating system-specific port driver allocates memory for and initializes this extension with zeros before it calls the miniport's **VirtualHwStorFindAdapter** routine.

</dd> <dt>

*HwContext* 
</dt> <dd>

A pointer to the PDO in the device stack. The HBA itself is the FDO. The PDO might belong to the Pci.sys driver if the miniport driver controls physical hardware. But in the case of a virtual miniport driver, the PDO belongs to the PnP manager.

</dd> <dt>

*BusInformation* 
</dt> <dd>

A pointer to the miniport's functional device object (FDO).

</dd> <dt>

*LowerDevice* 
</dt> <dd>

A pointer to the device object controlled by the miniport's FDO.

</dd> <dt>

*ArgumentString* 
</dt> <dd>

A pointer to a null-terminated ASCII string. This string, if supplied, contains device information from the registry such as a base parameter.

</dd> <dt>

*ConfigInfo* 
</dt> <dd>

A pointer to a [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure. The port driver initializes this structure with any known configuration information, such as values that the miniport driver's [**DriverEntry**](https://msdn.microsoft.com/library/windows/hardware/ff544113) set in the [**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md). **VirtualHwStorFindAdapter** must use any supplied information to determine if the virtual HBA it describes is one that the miniport driver supports. If so, **VirtualHwStorFindAdapter** initializes and configures that HBA and fills in any missing configuration information. If possible, a miniport driver should have default configuration values for each type of HBA that it supports, in the event that the operating system-dependent port driver cannot supply additional configuration information that was not provided by the miniport driver's **DriverEntry** routine.

</dd> <dt>

*Again* 
</dt> <dd>

Not used.

</dd> </dl>

## Return value

**VirtualHwStorFindAdapter** must return one of the following status values:



| Return code                                                                                            | Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SP\_RETURN\_FOUND**</dt> </dl>       | Indicates that a supported HBA was found and that the HBA-relevant configuration information was determined successfully and set in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure.<br/> |
| <dl> <dt>**SP\_RETURN\_ERROR**</dt> </dl>       | Indicates that an HBA was found, but an error occurred when it obtained the configuration information. If possible, such an error should be logged with [**ScsiPortLogError**](scsiportlogerror.md).<br/>                                    |
| <dl> <dt>**SP\_RETURN\_BAD\_CONFIG**</dt> </dl> | Indicates that the supplied configuration information was invalid for the adapter.<br/>                                                                                                                                                       |
| <dl> <dt>**SP\_RETURN\_NOT\_FOUND**</dt> </dl>  | Indicates that no supported HBA was found for the supplied configuration information.<br/>                                                                                                                                                    |



 

## Remarks

The **VirtualDevice** field in the configuration information structure must be set to **TRUE**. Other fields can be set as needed.

The port driver calls the Storport virtual miniport's **VirtualHwStorFindAdapter** at PASSIVE\_LEVEL.

The name **VirtualHwStorFindAdapter** is placeholder text for the actual routine name. The actual prototype of this routine is defined in Srb.h as follows:


```
typedef
ULONG
VIRTUAL_HW_FIND_ADAPTER (
  _In_ PVOID  DeviceExtension,
  _In_ PVOID  HwContext,
  _In_ PVOID  BusInformation,
  _In_ PVOID  LowerDevice,
  _In_ PCHAR  ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION  ConfigInfo,
  _Out_ PBOOLEAN Again
  );
```



## Examples

To define an **VirtualHwStorFindAdapter** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **VirtualHwStorFindAdapter** callback routine that is named *MyVirtualHwFindAdapter*, use the **VIRTUAL\_HW\_FIND\_ADAPTER** type as shown in this code example:


```
VIRTUAL_HW_FIND_ADAPTER MyVirtualHwFindAdapter;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
ULONG
MyVirtualHwFindAdapter (
  _In_ PVOID  DeviceExtension,
  _In_ PVOID  HwContext,
  _In_ PVOID  BusInformation,
  _In_ PVOID  LowerDevice,
  _In_ PCHAR  ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION  ConfigInfo,
  _Out_ PBOOLEAN Again
  );
  {
      ...
  }
```



The **VIRTUAL\_HW\_FIND\_ADAPTER** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **VIRTUAL\_HW\_FIND\_ADAPTER** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**HwStorFindAdapter**](hwstorfindadapter.md)
</dt> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> <dt>

[**ScsiPortLogError**](scsiportlogerror.md)
</dt> <dt>

[**VIRTUAL\_HW\_INITIALIZATION\_DATA**](virtual-hw-initialization-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20VirtualHwStorFindAdapter%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







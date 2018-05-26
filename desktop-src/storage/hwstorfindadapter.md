---
title: HW\_FIND\_ADAPTER routine
description: The HwStorFindAdapter routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.
ms.assetid: 8642d0b8-ebc8-4053-b35e-3a81108a2f7f
keywords:
- HwStorFindAdapter routine Storage Devices
- HW_FIND_ADAPTER
topic_type:
- apiref
api_name:
- HwStorFindAdapter
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

# HW\_FIND\_ADAPTER routine

The **HwStorFindAdapter** routine uses the supplied configuration to determine whether a specific HBA is supported and, if it is, to return configuration information about that adapter.

## Syntax


```C++
HW_FIND_ADAPTER HwStorFindAdapter;

ULONG HwStorFindAdapter(
          IN PVOID                        DeviceExtension,
  _In_    PVOID                           HwContext,
  _In_    PVOID                           BusInformation,
  _In_    IN PVOID                        ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION ConfigInfo,
  _In_    PBOOLEAN                        Reserved3
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* 
</dt> <dd>

Supplies a per adapter storage area.

</dd> <dt>

*HwContext* \[in\]
</dt> <dd>

Set to NULL.

</dd> <dt>

*BusInformation* \[in\]
</dt> <dd>

Set to NULL.

</dd> <dt>

*ArgumentString* \[in\]
</dt> <dd>

Supplies a **NULL**-terminated string with context information about the driver.

</dd> <dt>

*ConfigInfo* \[in, out\]
</dt> <dd>

Supplies an initialized [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure that the miniport driver uses during initialization.

</dd> <dt>

*Reserved3* \[in\]
</dt> <dd>

Reserved for system use.

</dd> </dl>

## Return value

**HwStorFindAdapter** must return one of the following status values:



| Return code                                                                                            | Description                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**SP\_RETURN\_FOUND**</dt> </dl>       | Indicates that a supported HBA was found and that the HBA-relevant configuration information was successfully determined and set in the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure.<br/> |
| <dl> <dt>**SP\_RETURN\_ERROR**</dt> </dl>       | Indicates that an HBA was found but there was an error obtaining the configuration information. If possible, such an error should be logged with [**StorPortLogError**](storportlogerror.md).<br/>                                           |
| <dl> <dt>**SP\_RETURN\_BAD\_CONFIG**</dt> </dl> | Indicates that the supplied configuration information was invalid for the adapter.<br/>                                                                                                                                                       |
| <dl> <dt>**SP\_RETURN\_NOT\_FOUND**</dt> </dl>  | Indicates that no supported HBA was found for the supplied configuration information.<br/>                                                                                                                                                    |



 

## Remarks

Because the Storport driver supports only Plug and Play (PnP) devices, the *HwContext* and *BusInformation* parameters to **HwStorFindAdapter** are not supplied to non-virtual miniport drivers.

**HwStorFindAdapter** must set the **MaximumTransferLength** and **NumberOfPhysicalBreaks** fields in the *ConfigInfo* structure. Other than these fields, the [**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md) structure will always fully specify all adapter resources that are required to start the adapter.

The name **HwStorFindAdapter** is just a placeholder. The actual prototype of this routine is defined in *Storport.h* as follows:


```
typedef
ULONG
HW_FIND_ADAPTER (
  _In_ PVOID  DeviceExtension,
  _In_ PVOID  HwContext,
  _In_ PVOID  BusInformation,
  _In_z_ PCHAR  ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION  ConfigInfo,
  _In_ PBOOLEAN  Reserved3
  );
```



In most cases StorPort calls the **HwStorFindAdapter** routine at IRQL == PASSIVE\_LEVEL without acquiring any spin locks. The exception case is when the miniport does not support calling [**HwStorAdaptorControl**](hwstoradaptercontrol.md) with the **ScsiRestartAdapter** control type. In this situation, StorPort will instead reinitialize the adapter by calling both **HwStorFindAdapter** and [**HwStorInitialize**](hwstorinitialize.md). When this is the case, **HwStorFindAdapter** is called at IRQL == DISPATCH\_LEVEL. Also, when in dump mode, **HwStorFindAdapter** is called at IRQL == HIGH\_LEVEL.

## Examples

To define an **HwStorFindAdapter** callback function, you must first provide a function declaration that identifies the type of callback function you re defining. Windows provides a set of callback function types for drivers. Declaring a function using the callback function types helps [Code Analysis for Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454182), [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) (SDV), and other verification tools find errors, and it s a requirement for writing drivers for the Windows operating system.

For example, to define a **HwStorFindAdapter** callback routine that is named *MyHwFindAdapter*, use the **HW\_FIND\_ADAPTER** type as shown in this code example:


```
HW_FIND_ADAPTER MyHwFindAdapter;
```



Then, implement your callback routine as follows:


```
_Use_decl_annotations_
ULONG
MyHwFindAdapter (
  _In_ PVOID  DeviceExtension,
  _In_ PVOID  HwContext,
  _In_ PVOID  BusInformation,
  _In_z_ PCHAR  ArgumentString,
  _Inout_ PPORT_CONFIGURATION_INFORMATION  ConfigInfo,
  _In_ PBOOLEAN  Reserved3
  );
  {
      ...
  }
```



The **HW\_FIND\_ADAPTER** function type is defined in the Storport.h header file. To more accurately identify errors when you run the code analysis tools, be sure to add the \_Use\_decl\_annotations\_ annotation to your function definition. The \_Use\_decl\_annotations\_ annotation ensures that the annotations that are applied to the **HW\_FIND\_ADAPTER** function type in the header file are used. For more information about the requirements for function declarations, see [Declaring Functions Using Function Role Types for Storport Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454209). For information about \_Use\_decl\_annotations\_, see [**Annotating Function Behavior**](c0aa268d-6fa3-4ced-a8c6-f7652b152e61).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | PASSIVE\_LEVEL (See Remarks section.)<br/>                                                                                        |



## See also

<dl> <dt>

[**PORT\_CONFIGURATION\_INFORMATION**](port-configuration-information--storport-.md)
</dt> <dt>

[**StorPortLogError**](storportlogerror.md)
</dt> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> <dt>

[**HwStorInitialize**](hwstorinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HW_FIND_ADAPTER%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







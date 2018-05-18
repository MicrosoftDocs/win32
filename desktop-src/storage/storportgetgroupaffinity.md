---
title: StorPortGetGroupAffinity routine
description: The StorPortGetGroupAffinity routine constructs a mask of the active processors in a requested group.
ms.assetid: 'eec0c985-fb59-4190-afb8-5eb62ac1edea'
keywords: ["StorPortGetGroupAffinity routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetGroupAffinity
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortGetGroupAffinity routine

The **StorPortGetGroupAffinity** routine constructs a mask of the active processors in a requested group.

## Syntax


```C++
ULONG StorPortGetGroupAffinity(
  _In_  PVOID      HwDeviceExtension,
  _In_  USHORT     GroupNumber,
  _Out_ PKAFFINITY GroupAffinityMask
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*GroupNumber* \[in\]
</dt> <dd>

The group from which to return the processor mask.

</dd> <dt>

*GroupAffinityMask* \[out\]
</dt> <dd>

A pointer to a variable that holds the affinity mask of the given group.

</dd> </dl>

## Return value

The **StorPortGetGroupAffinity** routine returns one of the following status codes:



| Return code                                                                                                     | Description                                                                                                                                                                              |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>                                                                                                              |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The operation was successful.<br/>                                                                                                                                                 |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The operation fails with this return value if one or more of the parameters are invalid, for example, if *GroupAffinityMask* is set to **NULL**.<br/>                              |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>       | The operation fails with this return value if one or more of the parameters are invalid, for example, if *GroupNumber* is set to a value greater than the active group count.<br/> |



 

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>              | Available in Windows 7 and later versions of the Windows operating systems.<br/>                                                  |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | &lt;=DISPATCH\_LEVEL<br/>                                                                                                         |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetGroupAffinity%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






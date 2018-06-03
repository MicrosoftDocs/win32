---
title: StorPortGetLogicalProcessorRelationship routine
description: The StorPortGetLogicalProcessorRelationship routine returns relationship information for one or more specified types.
ms.assetid: 32b92771-7f23-492c-a3b0-b10032c9f80a
keywords:
- StorPortGetLogicalProcessorRelationship routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetLogicalProcessorRelationship
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortGetLogicalProcessorRelationship routine

The **StorPortGetLogicalProcessorRelationship** routine returns relationship information for one or more specified types. These types include groups, physical packages, and nodes in the host system. The information that is returned includes processor affinity masks that are composed of the logical processors in the host system. These logical processors share the specified relationship types.

## Syntax


```C++
ULONG StorPortGetLogicalProcessorRelationship(
  _In_     PVOID                                    HwDeviceExtension,
  _In_opt_ PPROCESSOR_NUMBER                        ProcessorNumber,
  _In_     LOGICAL_PROCESSOR_RELATIONSHIP           RelationshipType,
  _Out_    PSYSTEM_LOGICAL_PROCESSOR_INFORMATION_EX Information,
  _Inout_  PULONG                                   Length
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*ProcessorNumber* \[in, optional\]
</dt> <dd>

An optional pointer to a processor number for which relationships are to be returned. If this parameter is not provided, information about all processors is returned.

</dd> <dt>

*RelationshipType* \[in\]
</dt> <dd>

The type of relationship to be returned.

</dd> <dt>

*Information* \[out\]
</dt> <dd>

A pointer to a buffer that receives the specified information.

</dd> <dt>

*Length* \[in, out\]
</dt> <dd>

A pointer to the length of the information buffer, in bytes. Upon return, this value receives the number of bytes that are populated with relationship information.

</dd> </dl>

## Return value

The **StorPortGetLogicalProcessorRelationship**routine returns one of the following status codes:



| Return code                                                                                                     | Description                                                                                                                                                                                    |
|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>                                                                                                                    |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The operation was successful.<br/>                                                                                                                                                       |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The operation fails with this return value if one or more of the parameters are invalid, for example, if *Information* is set to **NULL**.<br/>                                          |
| <dl> <dt>**STOR\_STATUS\_BUFFER\_TOO\_SMALL**</dt> </dl> | The operation fails with this return value if one or more of the parameters are invalid, for example, if the supplied buffer is not large enough to hold the requested information.<br/> |



 

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>              | Available in Windows 7 and later versions of the Windows operating systems.<br/>                                                  |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>                 | &lt;=DISPATCH\_LEVEL<br/>                                                                                                         |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetLogicalProcessorRelationship%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






---
title: StorPortGetMSIInfo routine
description: The StorPortGetMSIInfo routine retrieves the message signaled interrupt (MSI) information for the specified message.
ms.assetid: '3c98c04c-246a-42a0-bb40-f7771f7ae968'
keywords: ["StorPortGetMSIInfo routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetMSIInfo
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortGetMSIInfo routine

The **StorPortGetMSIInfo** routine retrieves the message signaled interrupt (MSI) information for the specified message.

## Syntax


```C++
ULONG StorPortGetMSIInfo(
  _In_  PVOID                          HwDeviceExtension,
  _In_  ULONG                          MessageId,
  _Out_ PMESSAGE_INTERRUPT_INFORMATION InterruptInfo
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*MessageId* \[in\]
</dt> <dd>

The identifier of the message for which the information is retrieved.

</dd> <dt>

*InterruptInfo* \[out\]
</dt> <dd>

A pointer to a miniport driver-provided [**MESSAGE\_INTERRUPT\_INFORMATION**](message-interrupt-information.md) structure that receives the information for the message specified by the *MessageId* parameter.

</dd> </dl>

## Return value

**StorPortGetMSIInfo** returns one of the status codes:



| Return code                                                                                                           | Description                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>         | This function is not implemented on the active operating system.<br/>                                                                                                                                                                         |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                  | Indicates that the MSI information was successfully received for the specified message.<br/>                                                                                                                                                  |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>       | *HwDeviceExtension* passed was **NULL**.<br/> -or-<br/> The pointer in *InterruptInfo* for the structure to receive the information is **NULL**.<br/> -or-<br/> *MessageId* passed to the function is incorrect.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_DEVICE\_REQUEST**</dt> </dl> | The HBA does not support MSI.<br/>                                                                                                                                                                                                            |



 

## Remarks

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | This routine is available starting with Windows Vista.<br/>                                                                       |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any level.<br/>                                                                                                                   |



## See also

<dl> <dt>

[**MESSAGE\_INTERRUPT\_INFORMATION**](message-interrupt-information.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetMSIInfo%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







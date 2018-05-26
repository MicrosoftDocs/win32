---
title: StorPortInitializeListHead routine
description: The StorPortInitializeListHead routine initializes a STOR\_LIST\_ENTRY structure that represents the head of a doubly linked list.
ms.assetid: E37C54C1-209F-4944-940B-2247E86C8130
keywords:
- StorPortInitializeListHead routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializeListHead
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortInitializeListHead routine

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **StorPortInitializeListHead** routine initializes a [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structure that represents the head of a doubly linked list.

## Syntax


```C++
VOID StorPortInitializeListHead(
  _In_  PVOID            HwDeviceExtension,
  _Out_ PSTOR_LIST_ENTRY ListHead
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*ListHead* \[out\]
</dt> <dd>

Pointer to the [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structure that represents the head of the list.

</dd> </dl>

## Return value

This routine does not return a value.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**InitializeListHead**](https://msdn.microsoft.com/library/windows/hardware/ff547799)
</dt> <dt>

[**StorPortInterlockedInsertHeadList**](storportinterlockedinsertheadlist.md)
</dt> <dt>

[**StorPortInterlockedInsertTailList**](storportinterlockedinserttaillist.md)
</dt> <dt>

[**StorPortInterlockedRemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/mt790430)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializeListHead%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







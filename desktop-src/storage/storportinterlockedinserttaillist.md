---
title: StorPortInterlockedInsertTailList routine
description: The StorPortInterlockedInsertTailList routine atomically inserts an entry at the end of a doubly linked list of STOR\_LIST\_ENTRY structures.
ms.assetid: 56147D28-B832-4C5D-BFB7-60C4020CA299
keywords:
- StorPortInterlockedInsertTailList routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInterlockedInsertTailList
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

# StorPortInterlockedInsertTailList routine

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **StorPortInterlockedInsertTailList** routine atomically inserts an entry at the end of a doubly linked list of [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structures.

## Syntax


```C++
ULONG StorPortInterlockedInsertTailList(
  _In_    PVOID            HwDeviceExtension,
  _Inout_ PSTOR_LIST_ENTRY ListHead,
  _Inout_ PSTOR_LIST_ENTRY ListEntry,
  _Inout_ PSTOR_LIST_ENTRY *Result,
  _Inout_ PSTOR_KSPIN_LOCK Lock
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*ListHead* \[in, out\]
</dt> <dd>

Pointer to the [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structure that represents the head of the list.

</dd> <dt>

*ListEntry* \[in, out\]
</dt> <dd>

Pointer to a [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structure that represents the entry to be inserted into the list.

</dd> <dt>

*\*Result* \[in, out\]
</dt> <dd>

Pointer to a [**STOR\_LIST\_ENTRY**](https://msdn.microsoft.com/library/windows/hardware/mt790432) structure that represents the first entry of the list before the new entry was inserted.

</dd> <dt>

*Lock* \[in, out\]
</dt> <dd>

A pointer to a **STOR\_KSPIN\_LOCK** structure that serves as the spin lock used to synchronize access to the list. The storage for the spin lock must be resident and must have been initialized by calling [**StorPortInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/mt790427).

You must use this spin lock only with the **StorPortInterlocked*Xxx*List** routines.

</dd> </dl>

## Return value

**StorPortInterlockedInsertHeadList** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                       |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>       |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The list items were removed successfully or the list is already empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | A pointer in *ListHead* or *Result* is **NULL**.<br/>                       |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**InitializeListHead**](https://msdn.microsoft.com/library/windows/hardware/ff547799)
</dt> <dt>

[**InsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff547820)
</dt> <dt>

[**StorPortInitializeSpinLock**](https://msdn.microsoft.com/library/windows/hardware/mt790427)
</dt> <dt>

[**StorPortInterlockedInsertTailList**](https://msdn.microsoft.com/library/windows/hardware/mt790429)
</dt> <dt>

[**StorPortInterlockedRemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/mt790430)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInterlockedInsertTailList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: StorPortInterlockedPushEntrySList routine
description: Inserts an item at the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system.
ms.assetid: 74C32E55-79C6-449A-AFA3-27858CF4EA6B
keywords:
- StorPortInterlockedPushEntrySList routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortInterlockedPushEntrySList
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

# StorPortInterlockedPushEntrySList routine

Inserts an item at the front of a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system.

## Syntax


```C++
ULONG StorPortInterlockedPushEntrySList(
  _In_    PVOID               HwDeviceExtension,
  _Inout_ PSTOR_SLIST_HEADER  SListHead,
  _Inout_ PSTOR_SLIST_ENTRY   SListEntry,
  _Out_   PSTOR_SLIST_ENTRY * Result
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*SListHead* \[in, out\]
</dt> <dd>

A pointer to an **STOR\_SLIST\_HEADER** structure that represents the head of a singly linked list. This structure is considered opaque and is for use by the Storport driver only.

</dd> <dt>

*SListEntry* \[in, out\]
</dt> <dd>

A pointer to an **STOR\_SLIST\_ENTRY** structure that represents the item to insert into the singly linked list.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

A pointer to a list entry pointer. The value returned is a pointer to the previous item that existed at the front of the list. This pervious item remains in the list behind the item new item added from *SListEntry*. If the list is empty, then **NULL** is returned in value pointed to by *Result*.

</dd> </dl>

## Return value

**StorPortInterlockedPushEntrySList** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                           |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>           |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The list item was successfully inserted into the list or is already empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | A pointer in *SListHead*, *SListEntry*, or *Result* is **NULL**.<br/>           |



 

## Remarks

When allocated by the caller, the **STOR\_SLIST\_ENTRY** structure pointed to by *SListEntry* must be aligned at a **MEMORY\_ALLOCATION\_ALIGNMENT** boundary. **MEMORY\_ALLOCATION\_ALIGNMENT** is defined in *miniport.h*.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**StorPortInitializeSListHead**](storportinitializeslisthead.md)
</dt> <dt>

[**StorPortInterlockedFlushSList**](storportinterlockedflushslist.md)
</dt> <dt>

[**StorPortInterlockedPopEntrySList**](storportinterlockedpopentryslist.md)
</dt> <dt>

[**StorPortQueryDepthSList**](storportquerydepthslist.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInterlockedPushEntrySList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







---
title: StorPortInterlockedFlushSList routine
description: Removes all items from a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system.
ms.assetid: 'C686ABA7-BC44-45CE-A35B-63E76961A032'
keywords: ["StorPortInterlockedFlushSList routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortInterlockedFlushSList
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortInterlockedFlushSList routine

Removes all items from a Storport managed singly linked list. Access to the list is synchronized on a multiprocessor system

## Syntax


```C++
ULONG StorPortInterlockedFlushSList(
  _In_    PVOID               HwDeviceExtension,
  _Inout_ PSTOR_SLIST_HEADER  SListHead,
  _Out_   PSTOR_SLIST_ENTRY * Result
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

*Result* \[out\]
</dt> <dd>

A pointer to a list entry pointer. The value returned is a pointer to the items removed from the list. If the list is empty, then **NULL** is returned in value pointed to by *Result*.

</dd> </dl>

## Return value

**StorPortInterlockedFlushSList** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                       |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>       |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The list items were removed successfully or the list is already empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | A pointer in *SListHead* or *Result* is **NULL**.<br/>                      |



 

## Remarks

The **StorPortInterlockedFlushSList** will also return **STATUS\_SUCCESS** when no entries are in the list. The pointer value referenced by *Result* must be evaluated for **NULL** to verify that no entries were returned.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in starting with Windows 8.<br/>                                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | &lt;= DISPATCH\_LEVEL<br/>                                                                                                        |



## See also

<dl> <dt>

[**StorPortInitializeSListHead**](storportinitializeslisthead.md)
</dt> <dt>

[**StorPortInterlockedPopEntrySList**](storportinterlockedpopentryslist.md)
</dt> <dt>

[**StorPortInterlockedPushEntrySList**](storportinterlockedpushentryslist.md)
</dt> <dt>

[**StorPortQueryDepthSList**](storportquerydepthslist.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInterlockedFlushSList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







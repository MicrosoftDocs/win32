---
title: STOR\_LIST\_ENTRY structure
description: A STOR\_LIST\_ENTRY structure describes an entry in a doubly linked list or serves as the header for such a list.
ms.assetid: 41E713D9-9499-40EB-8B21-DDB73362BAE3
keywords:
- STOR_LIST_ENTRY structure Storage Devices
- PSTOR_LIST_ENTRY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STOR_LIST_ENTRY
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# STOR\_LIST\_ENTRY structure

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

A **STOR\_LIST\_ENTRY** structure describes an entry in a doubly linked list or serves as the header for such a list.

## Syntax


```C++
typedef struct _STOR_LIST_ENTRY {
  struct _STOR_LIST_ENTRY  *Flink;
  struct _STOR_LIST_ENTRY  *Blink;
} STOR_LIST_ENTRY, *PSTOR_LIST_ENTRY;
```



## Members

<dl> <dt>

**Flink**
</dt> <dd>

For a **LIST\_ENTRY** structure that serves as a list entry, the **Flink** member points to the next entry in the list or to the list header if there is no next entry in the list.

For a **LIST\_ENTRY** structure that serves as the list header, the **Flink** member points to the first entry in the list or to the LIST\_ENTRY structure itself if the list is empty.

</dd> <dt>

**Blink**
</dt> <dd>

For a **LIST\_ENTRY** structure that serves as a list entry, the **Blink** member points to the previous entry in the list or to the list header if there is no previous entry in the list.

For a **LIST\_ENTRY** structure that serves as the list header, the **Blink** member points to the last entry in the list or to the **LIST\_ENTRY** structure itself if the list is empty.

</dd> </dl>

## Remarks

A **STOR\_LIST\_ENTRY** structure that describes the list head must have been initialized by calling [**StorPortInitializeListHead**](https://msdn.microsoft.com/library/windows/hardware/mt790426).

A driver can access the **Flink** or **Blink** members of a **STOR\_LIST\_ENTRY**, but the members must only be updated by the system routines supplied for this purpose.

For more information about how to use **STOR\_LIST\_ENTRY** structures to implement a doubly linked list, see [Singly and Doubly Linked Lists](https://msdn.microsoft.com/library/windows/hardware/ff563802).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortInterlockedInsertHeadList**](storportinterlockedinsertheadlist.md)
</dt> <dt>

[**StorPortInterlockedInsertTailList**](storportinterlockedinserttaillist.md)
</dt> <dt>

[**StorPortInterlockedRemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/mt790430)
</dt> <dt>

[**InitializeListHead**](https://msdn.microsoft.com/library/windows/hardware/ff547799)
</dt> <dt>

[**InsertHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff547820)
</dt> <dt>

[**InsertTailList**](https://msdn.microsoft.com/library/windows/hardware/ff547823)
</dt> <dt>

[**IsListEmpty**](https://msdn.microsoft.com/library/windows/hardware/ff551789)
</dt> <dt>

[**RemoveEntryList**](https://msdn.microsoft.com/library/windows/hardware/ff561029)
</dt> <dt>

[**RemoveHeadList**](https://msdn.microsoft.com/library/windows/hardware/ff561032)
</dt> <dt>

[**RemoveTailList**](https://msdn.microsoft.com/library/windows/hardware/ff561036)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_LIST_ENTRY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







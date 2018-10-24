---
Description: Describes an array of wide area network (WWAN) interfaces.
ms.assetid: F8104B2E-304D-4DC4-9F2B-6FA29CD5DEA5
title: WWAN_INTERFACE_INFO_LIST structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WWAN_INTERFACE_INFO_LIST
api_type: 
- NA
---

# WWAN\_INTERFACE\_INFO\_LIST structure

Describes an array of wide area network (WWAN) interfaces.

## Syntax


```C++
typedef struct {
  DWORD               dwNumberOfItems;
  WWAN_INTERFACE_INFO pInterfaceInfo[*];
} WWAN_INTERFACE_INFO_LIST;
```



## Members

<dl> <dt>

**dwNumberOfItems**
</dt> <dd>

The number of interfaces in the array that **pInterfaceInfo** specifies.

</dd> <dt>

**pInterfaceInfo**
</dt> <dd>

An array of [**WWAN\_INTERFACE\_INFO**](wwan-interface-info.md) structures that describe each WWAN interface.

</dd> </dl>

## See also

<dl> <dt>

[**WwanEnumerateInterfaces**](wwanenumerateinterfaces.md)
</dt> </dl>

 

 




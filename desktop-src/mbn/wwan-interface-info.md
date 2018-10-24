---
Description: Describes a wide area network (WWAN) interface.
ms.assetid: CA85DE48-50AE-47D7-9F4F-5F7B574C67B3
title: WWAN_INTERFACE_INFO structure
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WWAN_INTERFACE_INFO
api_type: 
- NA
---

# WWAN\_INTERFACE\_INFO structure

Describes a wide area network (WWAN) interface.

## Syntax


```C++
typedef struct {
  GUID                  InterfaceGuid;
  WCHAR                 strInterfaceDescription[WWAN_STR_DESC_LENGTH];
  WWAN_INTERFACE_STATUS InterfaceStatus;
  GUID                  ParentInterfaceGuid;
  BOOL                  fIsAdditionalPdpContextInterface;
} WWAN_INTERFACE_INFO;
```



## Members

<dl> <dt>

**InterfaceGuid**
</dt> <dd>

The value that identifies the interface.

</dd> <dt>

**strInterfaceDescription**
</dt> <dd>

A string that describes the interface. The dimension of the string is **WWAN\_STR\_DESC\_LENGTH**, which is defined as 256.

</dd> <dt>

**InterfaceStatus**
</dt> <dd>

A [**WWAN\_INTERFACE\_STATUS**](wwan-interface-status.md) structure that describes status for the WWAN interface.

</dd> <dt>

**ParentInterfaceGuid**
</dt> <dd>

The value that identifies the parent interface of this interface.

</dd> <dt>

**fIsAdditionalPdpContextInterface**
</dt> <dd>

A Boolean value that indicates whether the interface includes an additional PDP context. **TRUE** indicates the interface includes an additional PDP context; otherwise, **FALSE**.

</dd> </dl>

## See also

<dl> <dt>

[**WWAN\_INTERFACE\_INFO\_LIST**](wwan-interface-info-list.md)
</dt> </dl>

 

 




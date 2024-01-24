---
title: BITS_FILE_PROPERTY_VALUE structure (Deliveryoptimization.h)
description: The BITS_FILE_PROPERTY_VALUE union provides the property value of the Delivery Optimization file based on a value from the BITS_FILE_PROPERTY_ID enumeration.
ms.assetid: 56A634F9-FB30-49D5-BD03-DD59AEF702C1
keywords:
- BITS_FILE_PROPERTY_VALUE structure
topic_type:
- apiref
api_name:
- BITS_FILE_PROPERTY_VALUE
api_location:
- deliveryoptimization.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# BITS_FILE_PROPERTY_VALUE structure

The **BITS_FILE_PROPERTY_VALUE** union provides the property value of the Delivery Optimization file based on a value from the [**BITS_FILE_PROPERTY_ID**](bits-file-property-id-.md) enumeration.

## Syntax


```C++
typedef struct {
  LPWSTR String;
} BITS_FILE_PROPERTY_VALUE;
```



## Members

<dl> <dt>

**String**
</dt> <dd>

This value is used when using the property ID enum value **BITS_FILE_PROPERTY_ID_HTTP_RESPONSE_HEADERS**.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl> |



## See also

<dl> <dt>

[**BITS_FILE_PROPERTY_ID**](bits-file-property-id-.md)
</dt> <dt>

[**IBackgroundCopyFile5.GetProperty**](ibackgroundcopyfile5-getproperty.md)
</dt> <dt>

[**IBackgroundCopyFile5.SetProperty**](ibackgroundcopyfile5-setproperty.md)
</dt> </dl>

 

 






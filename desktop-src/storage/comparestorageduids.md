---
title: CompareStorageDuids routine
description: The CompareStorageDuids routine compares two device unique identifiers (DUIDs) and reports whether they match or not.
ms.assetid: bf66a04d-0892-4813-9615-845054526125
keywords:
- CompareStorageDuids routine Storage Devices
topic_type:
- apiref
api_name:
- CompareStorageDuids
api_location:
- storduid.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CompareStorageDuids routine

The **CompareStorageDuids** routine compares two device unique identifiers (DUIDs) and reports whether they match or not.

## Syntax


```C++
__inline DUID_MATCH_STATUS CompareStorageDuids(
  _In_ PSTORAGE_DEVICE_UNIQUE_IDENTIFIER Duid1,
  _In_ PSTORAGE_DEVICE_UNIQUE_IDENTIFIER Duid2
);
```



## Parameters

<dl> <dt>

*Duid1* \[in\]
</dt> <dd>

A pointer to a DUID to compare with the DUID that *Duid2* points to.

</dd> <dt>

*Duid2* \[in\]
</dt> <dd>

A pointer to a DUID to compare with the DUID that *Duid1* points to.

</dd> </dl>

## Return value

**CompareStorageDuids** returns a [**DUID\_MATCH\_STATUS**](duid-match-status.md) value that indicates whether the two DUIDs matched or not, if the operation succeeds. Otherwise, this routine returns a DUID\_MATCH\_STATUS value that indicates the error status.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Storduid.h (include Storduid.h)</dt> </dl> |



## See also

<dl> <dt>

[**DUID\_MATCH\_STATUS**](duid-match-status.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20CompareStorageDuids%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")







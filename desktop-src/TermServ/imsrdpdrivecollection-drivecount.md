---
title: IMsRdpDriveCollection DriveCount property
description: Retrieves the count of objects in the collection. | IMsRdpDriveCollection DriveCount property
ms.assetid: 33b39657-2cc1-4f1e-b23a-809a9737ed8d
ms.tgt_platform: multiple
keywords:
- DriveCount property Remote Desktop Services
- DriveCount property Remote Desktop Services , IMsRdpDriveCollection interface
- IMsRdpDriveCollection interface Remote Desktop Services , DriveCount property
topic_type:
- apiref
api_name:
- IMsRdpDriveCollection.DriveCount
- IMsRdpDriveCollection.get_DriveCount
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDriveCollection::DriveCount property

Retrieves the count of objects in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_DriveCount(
  [out] ULONG *pDriveCount
);
```



## Property value

The object count.

## Error codes

If the method succeeds, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| IID<br/>                      | IID\_IMsRdpDriveCollection is defined as 7ff17599-da2c-4677-ad35-f60c04fe1585<br/> |



## See also

<dl> <dt>

[**IMsRdpDriveCollection**](imsrdpdrivecollection.md)
</dt> </dl>

 

 






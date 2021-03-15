---
title: IMsRdpDriveCollection RescanDrives method
description: Refreshes the list of objects in the collection. | IMsRdpDriveCollection RescanDrives method
ms.assetid: 5997b76c-d130-4375-b6ff-5ea871f059cc
ms.tgt_platform: multiple
keywords:
- RescanDrives method Remote Desktop Services
- RescanDrives method Remote Desktop Services , IMsRdpDriveCollection interface
- IMsRdpDriveCollection interface Remote Desktop Services , RescanDrives method
topic_type:
- apiref
api_name:
- IMsRdpDriveCollection.RescanDrives
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDriveCollection::RescanDrives method

Refreshes the list of objects in the collection.

## Syntax


```C++
HRESULT RescanDrives(
  [in] VARIANT_BOOL vboolDynRedir
);
```



## Parameters

<dl> <dt>

*vboolDynRedir* \[in\]
</dt> <dd>

The default redirection state that will be applied to any newly discovered devices or drives.

</dd> </dl>

## Return value

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

 

 






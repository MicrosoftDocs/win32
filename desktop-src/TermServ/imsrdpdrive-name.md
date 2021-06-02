---
title: IMsRdpDrive Name property
description: Retrieves the name of the drive.
ms.assetid: 5aabb7df-fd46-48aa-ad1d-51da45495782
ms.tgt_platform: multiple
keywords:
- Name property Remote Desktop Services
- Name property Remote Desktop Services , IMsRdpDrive interface
- IMsRdpDrive interface Remote Desktop Services , Name property
topic_type:
- apiref
api_name:
- IMsRdpDrive.Name
- IMsRdpDrive.get_Name
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDrive::Name property

Retrieves the name of the drive.

This property is read-only.

## Syntax


```C++
HRESULT get_Name(
  [out] BSTR *pName
);
```



## Property value

The drive name.

## Error codes

If the method succeeds, **S\_OK** is returned. Any other **HRESULT** value indicates that the call failed.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDrive is defined as d28b5458-f694-47a8-8e61-40356a767e46<br/>         |



## See also

<dl> <dt>

[**IMsRdpDrive**](imsrdpdrive.md)
</dt> </dl>

 

 






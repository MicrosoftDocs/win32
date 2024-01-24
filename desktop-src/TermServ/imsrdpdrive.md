---
title: IMsRdpDrive interface
description: Contains information about a drive object.
ms.assetid: 25e76657-a898-4581-a866-d66008540f50
ms.tgt_platform: multiple
keywords:
- IMsRdpDrive interface Remote Desktop Services
- IMsRdpDrive interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpDrive
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDrive interface

Contains information about a drive object.

## Members

The **IMsRdpDrive** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMsRdpDrive** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpDrive** interface has these properties.



| Property                                                            | Access type           | Description                                              |
|:--------------------------------------------------------------------|:----------------------|:---------------------------------------------------------|
| [**Name**](imsrdpdrive-name.md)<br/>                         | Read-only<br/>  | Retrieves the name of the drive.<br/>              |
| [**RedirectionState**](imsrdpdrive-redirectionstate.md)<br/> | Read/write<br/> | Indicates the redirection state of the drive.<br/> |



 

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

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> <dt>

[**IMsRdpDriveCollection**](imsrdpdrivecollection.md)
</dt> </dl>

 


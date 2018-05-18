---
title: PS\_RemoteAccessRadius class
description: Represents the configuration of the accounting and authentication RADIUS servers.
audience: developer
ms.assetid: '70c9b6cb-29ac-4c94-9637-114a078e7aaa'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessRadius class", "PS_RemoteAccessRadius class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessRadius
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessRadius class

Represents the configuration of the accounting and authentication RADIUS servers

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessRadius
{
};
```

## Members

The **PS\_RemoteAccessRadius** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessRadius** class has these methods.



| Method                                         | Description                                                                                                                                                                                                          |
|:-----------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-remoteaccessradius.md)       | This cmdlet adds a new external RADIUS server for one of the following purposes1. VPN authentication2. Accounting for DirectAccess and VPN3. OTP authentication for DirectAccess<br/>                          |
| [**Get**](get-ps-remoteaccessradius.md)       | This cmdlet displays the list of the following types of RADIUS servers 1. Radius for VPN authentication 2. Radius for DirectAccess and VPN Accounting3. Radius for OTP authentication for DirectAccess<br/>    |
| [**Remove**](remove-ps-remoteaccessradius.md) | This cmdlet removes an external RADIUS server from being used for one of the following purposes1. VPN authentication2. Accounting for both DirectAccess and VPN3. OTP authentication for DirectAccess<br/>     |
| [**Set**](set-ps-remoteaccessradius.md)       | This cmdlet edits the properties associated with an external RADIUS server being used for the following1. VPN authentication2. Accounting for DirectAccess and VPN 3. OTP authentication for DirectAccess<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






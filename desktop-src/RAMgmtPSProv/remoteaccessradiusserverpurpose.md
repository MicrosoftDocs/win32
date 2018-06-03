---
title: RemoteAccessRadiusServerPurpose class
description: Contains the Name and Purpose of a Radius Server.
audience: developer
ms.assetid: a48fdc7a-66a7-480d-bbf2-ae070525f02c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessRadiusServerPurpose class
- RemoteAccessRadiusServerPurpose class, described
topic_type:
- apiref
api_name:
- RemoteAccessRadiusServerPurpose
- RemoteAccessRadiusServerPurpose.ServerName
- RemoteAccessRadiusServerPurpose.Purpose
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessRadiusServerPurpose class

Contains the Name and Purpose of a Radius Server

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessRadiusServerPurpose
{
  string ServerName;
  string Purpose;
};
```

## Members

The **RemoteAccessRadiusServerPurpose** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessRadiusServerPurpose** class has these properties.

<dl> <dt>

**Purpose**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The purpose of this Radius Server

The possible values are.

<dt>

<span id="Authentication"></span><span id="authentication"></span><span id="AUTHENTICATION"></span>

**Authentication** ("Authentication")


</dt> <dd></dd> <dt>

<span id="Accounting"></span><span id="accounting"></span><span id="ACCOUNTING"></span>

**Accounting** ("Accounting")


</dt> <dd></dd> <dt>

<span id="Otp"></span><span id="otp"></span><span id="OTP"></span>

**Otp** ("Otp")


</dt> <dd></dd> </dl>

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name of the Radius Server

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 






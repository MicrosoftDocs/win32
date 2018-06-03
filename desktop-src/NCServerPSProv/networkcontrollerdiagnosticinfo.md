---
title: NetworkControllerDiagnosticInfo class
description: Contains network controller diagnostic information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1dd77ee2-2a4e-4a9b-9b8e-9e84044eeb21
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- NetworkControllerDiagnosticInfo class
- NetworkControllerDiagnosticInfo class, described
topic_type:
- apiref
api_name:
- NetworkControllerDiagnosticInfo
- NetworkControllerDiagnosticInfo.DiagnosticLogLocation
- NetworkControllerDiagnosticInfo.ShareAccessUserInfo
- NetworkControllerDiagnosticInfo.LogLevel
- NetworkControllerDiagnosticInfo.LogTimeLimit
- NetworkControllerDiagnosticInfo.LogSizeLimit
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# NetworkControllerDiagnosticInfo class

Contains network controller diagnostic information.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerDiagnosticInfo
{
  string                      DiagnosticLogLocation;
  NetworkControllerCredential ShareAccessUserInfo;
  sint8                       LogLevel;
  uint32                      LogTimeLimit;
  uint32                      LogSizeLimit;
};
```

## Members

The **NetworkControllerDiagnosticInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerDiagnosticInfo** class has these properties.

<dl> <dt>

**DiagnosticLogLocation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the log location.

</dd> <dt>

**LogLevel**
</dt> <dd> <dl> <dt>

Data type: **sint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the level of logging.

The possible values are.

<dt>

<span id="Error"></span><span id="error"></span><span id="ERROR"></span>

**Error** (2)


</dt> <dd></dd> <dt>

<span id="Warning"></span><span id="warning"></span><span id="WARNING"></span>

**Warning** (3)


</dt> <dd></dd> <dt>

<span id="Informational"></span><span id="informational"></span><span id="INFORMATIONAL"></span>

**Informational** (4)


</dt> <dd></dd> <dt>

<span id="Verbose"></span><span id="verbose"></span><span id="VERBOSE"></span>

**Verbose** (5)


</dt> <dd></dd> </dl>

</dd> <dt>

**LogSizeLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the size limit for logs.

</dd> <dt>

**LogTimeLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Retrieves the aging limit for logs.

</dd> <dt>

**ShareAccessUserInfo**
</dt> <dd> <dl> <dt>

Data type: **NetworkControllerCredential**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**NetworkControllerCredential**](networkcontrollercredential.md)")
</dt> </dl>

Gets an embedded [**NetworkControllerCredential**](networkcontrollercredential.md) instance containing the credentials for the log location access user.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 






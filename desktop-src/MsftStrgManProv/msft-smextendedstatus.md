---
title: MSFT\_SMExtendedStatus class
description: Used to report detailed status and error information.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4626E587-62D2-48D3-8B56-C5323BD27968
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- MSFT_SMExtendedStatus class
- MSFT_SMExtendedStatus class, described
topic_type:
- apiref
api_name:
- MSFT_SMExtendedStatus
- MSFT_SMExtendedStatus.Description
- MSFT_SMExtendedStatus.Operation
- MSFT_SMExtendedStatus.ParameterInfo
- MSFT_SMExtendedStatus.ProviderName
- MSFT_SMExtendedStatus.StatusCode
- MSFT_SMExtendedStatus.SMErrorSource
- MSFT_SMExtendedStatus.SMErrorCode
- MSFT_SMExtendedStatus.SMMessage
- MSFT_SMExtendedStatus.SMDetails
api_location:
- StorageService.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MSFT\_SMExtendedStatus class

Used to report detailed status and error information.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[AMENDMENT]
class MSFT_SMExtendedStatus : __ExtendedStatus
{
  string Description;
  string Operation;
  string ParameterInfo;
  string ProviderName;
  uint32 StatusCode;
  Uint16 SMErrorSource;
  Uint32 SMErrorCode;
  string SMMessage;
  string SMDetails;
};
```

## Members

The **MSFT\_SMExtendedStatus** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_SMExtendedStatus** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Any user-defined string that describes an error or operational status.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**Operation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Operation that takes place at the time of a failure or anomaly. Typically, Windows Management Instrumentation (WMI) sets this property to the name of a COM API for WMI method such as the following: [**IWbemServices::CreateInstanceEnum**](https://msdn.microsoft.com/library/aa392097).

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ParameterInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Parameters involved in an error or status change. For example, if an application attempts to retrieve a class that does not exist, this property is set to the offending class name.

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**ProviderName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the provider that causes or reports an error or status change. If a provider is not involved, this string is set to "Windows Management".

This property is inherited from [**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645).

</dd> <dt>

**SMDetails**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Optional additional information or request/response details.

</dd> <dt>

**SMErrorCode**
</dt> <dd> <dl> <dt>

Data type: **Uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The specific error code returned by the source.

</dd> <dt>

**SMErrorSource**
</dt> <dd> <dl> <dt>

Data type: **Uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The source of the error code or extended status.

The possible values are.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Microsoft_StorageService"></span><span id="microsoft_storageservice"></span><span id="MICROSOFT_STORAGESERVICE"></span>

**Microsoft StorageService** (1)


</dt> <dd></dd> <dt>

<span id="SMI-S_Provider"></span><span id="smi-s_provider"></span><span id="SMI-S_PROVIDER"></span>

**SMI-S Provider** (2)


</dt> <dd></dd> </dl>

</dd> <dt>

**SMMessage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error message or extended status message.

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Contains an error or information code for an operation. This can be any value defined by the provider, but the value 0 (zero) is usually reserved to indicate success. This property is inherited from [**\_\_NotifyStatus**](https://msdn.microsoft.com/library/aa394662).

</dd> </dl>

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**\_\_ExtendedStatus**](https://msdn.microsoft.com/library/aa394645)
</dt> <dt>

[Windows Storage Management WMI Provider](windows-storage-management-wmi-provider-portal.md)
</dt> </dl>

 

 






---
title: GetFailureInfo method of the MSFT\_FSRMAdr class
description: Retrieves information from the server when a client fails to access a file describing why the failure occurred.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f08eb303-82ae-400f-b386-63403d6e5bab
ms.prod: windows-server-dev
ms.technology: file-server-resource-manager
ms.tgt_platform: multiple
keywords:
- GetFailureInfo method File Server Resource Manager
- GetFailureInfo method File Server Resource Manager , MSFT_FSRMAdr class
- MSFT_FSRMAdr class File Server Resource Manager , GetFailureInfo method
topic_type:
- apiref
api_name:
- MSFT_FSRMAdr.GetFailureInfo
api_location:
- SrmSvc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetFailureInfo method of the MSFT\_FSRMAdr class

Retrieves information from the server when a client fails to access a file describing why the failure occurred.

## Syntax


```mof
uint64 GetFailureInfo(
  [in]  string Path,
  [in]  string ServerPath,
  [in]  uint32 Event,
  [in]  uint32 LocaleId,
  [out] uint32 DisplayFlag[],
  [out] string ErrorMessage,
  [out] string DeviceClaim[]
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

The path value. Must not exceed the value of **MAX\_PATH** (260).

</dd> <dt>

*ServerPath* \[in\]
</dt> <dd>

A valid path on the server. Must not exceed the value of **MAX\_PATH** (260).

</dd> <dt>

*Event* \[in\]
</dt> <dd>

Describes the type of failure handled by ADR.

<dt>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>

<span id="AccessDenied"></span><span id="accessdenied"></span><span id="ACCESSDENIED"></span>**AccessDenied** (1)


</dt> <dd>

The failure was an access denied error.

</dd> <dt>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>

<span id="FileNotFound"></span><span id="filenotfound"></span><span id="FILENOTFOUND"></span>**FileNotFound** (2)


</dt> <dd>

The failure was a file not found error.

</dd> </dl> </dd> <dt>

*LocaleId* \[in\]
</dt> <dd>

Reserved for future use. Set to 0.

</dd> <dt>

*DisplayFlag* \[out\]
</dt> <dd>

<dt>

<span id="AllowEmailRequests"></span><span id="allowemailrequests"></span><span id="ALLOWEMAILREQUESTS"></span>

**AllowEmailRequests** (1)


</dt> <dd></dd> <dt>

<span id="ShowDeviceTroubleShooting"></span><span id="showdevicetroubleshooting"></span><span id="SHOWDEVICETROUBLESHOOTING"></span>

**ShowDeviceTroubleShooting** (2)


</dt> <dd></dd> </dl>

Returns an array of flags describing how the failure information is presented.

</dd> <dt>

*ErrorMessage* \[out\]
</dt> <dd>

Returns the error message in a string value up to 4 KB in length.

</dd> <dt>

*DeviceClaim* \[out\]
</dt> <dd>

Returns the names of device claims that dictate the access to the requested file.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\FSRM<br/>                                                 |
| MOF<br/>                      | <dl> <dt>MSFT\_FSRM.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SrmSvc.dll</dt> </dl>     |



## See also

<dl> <dt>

[**MSFT\_FSRMAdr**](msft-fsrmadr.md)
</dt> </dl>

 

 






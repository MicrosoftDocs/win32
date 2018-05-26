---
title: GetCorpPrefix method of the PS\_RemoteAccessLocal class
description: This method gets the Corp Prefix configuration.
audience: developer
ms.assetid: 3e04752f-04b1-493d-bf69-236a71d1ff0e
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetCorpPrefix method
- GetCorpPrefix method, PS_RemoteAccessLocal class
- PS_RemoteAccessLocal class, GetCorpPrefix method
topic_type:
- apiref
api_name:
- PS_RemoteAccessLocal.GetCorpPrefix
api_location:
- RAServerPSProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetCorpPrefix method of the PS\_RemoteAccessLocal class

This method gets the Corp Prefix configuration.

## Syntax


```mof
uint32 GetCorpPrefix(
  [in]  string                    IntranetInterface,
  [in]  string                    InternetInterface,
  [out] DACorpPrefixConfiguration Result
);
```



## Parameters

<dl> <dt>

*IntranetInterface* \[in\]
</dt> <dd>

Intranet Interface chosen for deployment.

</dd> <dt>

*InternetInterface* \[in\]
</dt> <dd>

Internet Interface chosen for deployment.

</dd> <dt>

*Result* \[out\]
</dt> <dd>

On success, returns [**DACorpPrefixConfiguration**](dacorpprefixconfiguration.md) that contains the Corp Prefix, IPv6 deployment type and basePrefix.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_RemoteAccessLocal**](ps-remoteaccesslocal.md)
</dt> </dl>

 

 






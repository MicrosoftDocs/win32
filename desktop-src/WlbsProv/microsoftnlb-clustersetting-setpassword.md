---
title: SetPassword method of the MicrosoftNLB\_ClusterSetting class
description: Changes the remote control password for the cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '5d695518-add6-4a7c-be9c-77434b0daf19'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetPassword method", "SetPassword method, MicrosoftNLB_ClusterSetting class", "MicrosoftNLB_ClusterSetting class, SetPassword method"]
topic_type:
- apiref
api_name:
- MicrosoftNLB_ClusterSetting.SetPassword
api_location:
- WlbsProv.dll
api_type:
- COM
---

# SetPassword method of the MicrosoftNLB\_ClusterSetting class

\[This method is available for use in the operating systems specified in the Requirements section. Support for this method was removed in Windows Server 2008.\]

Changes the remote control password for the [*cluster*](https://msdn.microsoft.com/library/aa367183#mscs-a---e-5-gly).

## Syntax


```mof
void SetPassword(
  [in] string Password
);
```



## Parameters

<dl> <dt>

*Password* \[in\]
</dt> <dd>

The remote control password.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Use caution when changing the remote control password and be sure to commit the change by using the [**LoadAllSettings**](microsoftnlb-clustersetting-loadallsettings.md) method.

> [!Note]  
> Before calling this method, it is highly recommended that the authentication level for the call to the [**CoSetProxyBlanket**](_com_cosetproxyblanket) function or the [**CoInitializeSecurity**](_com_coinitializesecurity) function be set to **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. This setting reduces the threat of disclosure by ensuring that the password string is encrypted during its transfer from the client computer to the server computer.

 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | None supported<br/>                                                               |
| End of server support<br/>    | None supported<br/>                                                               |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**LoadAllSettings Method of the MicrosoftNLB\_ClusterSetting Class**](microsoftnlb-clustersetting-loadallsettings.md)
</dt> <dt>

[**MicrosoftNLB\_ClusterSetting**](microsoftnlb-clustersetting.md)
</dt> </dl>

 

 






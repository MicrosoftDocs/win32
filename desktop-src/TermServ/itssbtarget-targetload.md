---
title: ITsSbTarget TargetLoad property
description: Retrieves the relative load on a target.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 56618dcf-1319-4310-80ba-7ed71b8b02e8
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- TargetLoad property Remote Desktop Services
- TargetLoad property Remote Desktop Services , ITsSbTarget interface
- ITsSbTarget interface Remote Desktop Services , TargetLoad property
- TargetLoad property Remote Desktop Services , ITsSbTargetEx interface
- ITsSbTargetEx interface Remote Desktop Services , TargetLoad property
topic_type:
- apiref
api_name:
- ITsSbTarget.TargetLoad
- ITsSbTarget.get_TargetLoad
- ITsSbTargetEx.TargetLoad
- ITsSbTargetEx.get_TargetLoad
api_location:
- Sbtsv.idl
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ITsSbTarget::TargetLoad property

Retrieves the relative load on a target. This value is based on the number of existing and pending sessions. By default a pending session has the same value as an existing session.

This property is read-only.

## Syntax


```C++
HRESULT get_TargetLoad(
  [out, retval] DWORD *pTargetLoad
);
```



## Property value

A number representing the relative load on a target.

## Remarks

The weight of a pending session relative to an active session can be changed by setting the value of the *LB\_ConnectionEstablishmentPenalty* parameter for the Connection Broker. This parameter is located under the**HKLM\\System\\CurrentControlSet\\Services\\Tssdis\\Parameters** registry key. The default value of 1 specifies that pending sessions have the same weight as active sessions.

This property is available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed in the [**ITsSbTargetEx**](itssbtargetex.md) interface.

## Requirements



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Minimum supported client<br/></td>
<td>None supported<br/></td>
</tr>
<tr class="even">
<td>Minimum supported server<br/></td>
<td>Windows Server 2016<br/></td>
</tr>
<tr class="odd">
<td>IDL<br/></td>
<td><dl> <dt>Sbtsv.idl</dt> </dl></td>
</tr>
<tr class="even">
<td>IID<br/></td>
<td>IID_ITsSbTarget is defined as:
<ul>
<li>16616ECC-272D-411D-B324-126893033856</li>
<li>e85e10ea-db0b-4752-b456-5fd5840901c0 on Windows Server 2008 R2</li>
</ul></td>
</tr>
</tbody>
</table>



## See also

<dl> <dt>

[**ITsSbTargetEx**](itssbtargetex.md)
</dt> <dt>

[**ITsSbTarget**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbtarget)
</dt> </dl>

 

 






---
title: Add method of the MSFT\_MpPreference class
description: TBD.
ms.assetid: 3b3b6dfa-2387-44eb-9241-fe6cd3bd3062
keywords:
- Add method
- Add method, MSFT_MpPreference class
- MSFT_MpPreference class, Add method
topic_type:
- apiref
api_name:
- MSFT_MpPreference.Add
api_location:
- ProtectionManagement.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the MSFT\_MpPreference class

TBD

## Syntax


```mof
uint32 Add(
  [in] string  ExclusionPath[],
  [in] string  ExclusionExtension[],
  [in] string  ExclusionProcess[],
  [in] sint64  ThreatIDDefaultAction_Ids[],
  [in] uint8   ThreatIDDefaultAction_Actions[],
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ExclusionPath* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the paths listed.

</dd> <dt>

*ExclusionExtension* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the extensions listed.

</dd> <dt>

*ExclusionProcess* \[in\]
</dt> <dd>

Allows an administrator to explicitly disable a scan from checking any of the processes listed.

</dd> <dt>

*ThreatIDDefaultAction\_Ids* \[in\]
</dt> <dd>

The Ids of threats upon which default action should not be taken when detected. The actions in ThreatIDDefaultAction\_Actions need to be specified in the same order as the Ids in ThreatIDDefaultAction\_Ids

</dd> <dt>

*ThreatIDDefaultAction\_Actions* \[in\]
</dt> <dd>

Default actions for threats upon which default action should not be taken when detected. The actions need to be in the same order as their respective Ids specified in the ThreatIDDefaultAction\_Ids property.

<dl> <dt>

<span id="Clean"></span><span id="clean"></span><span id="CLEAN"></span>**Clean** (1)
</dt> <dt>

<span id="Quarantine"></span><span id="quarantine"></span><span id="QUARANTINE"></span>**Quarantine** (2)
</dt> <dt>

<span id="Remove"></span><span id="remove"></span><span id="REMOVE"></span>**Remove** (3)
</dt> <dt>

<span id="Allow"></span><span id="allow"></span><span id="ALLOW"></span>**Allow** (6)
</dt> <dt>

<span id="UserDefined"></span><span id="userdefined"></span><span id="USERDEFINED"></span>**UserDefined** (8)
</dt> <dt>

<span id="NoAction"></span><span id="noaction"></span><span id="NOACTION"></span>**NoAction** (9)
</dt> <dt>

<span id="Block_"></span><span id="block_"></span><span id="BLOCK_"></span>**Block** (10)
</dt> </dl> </dd> <dt>

*Force* \[in\]
</dt> <dd>

A user confirmation is sought by default by this cmdlet. If -Force is specified, the default confirmation is not sought from the user.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                        |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                             |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Defender<br/>                                                       |
| MOF<br/>                      | <dl> <dt>ProtectionManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ProtectionManagement.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_MpPreference**](msft-mppreference.md)
</dt> </dl>

 

 






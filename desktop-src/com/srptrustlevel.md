---
title: SRPTrustLevel
description: Sets the software restriction policy (SRP) trust level for applications.
ms.assetid: 2ec10eb5-f83a-4ce7-8e03-36cdafadf169
keywords:
- SRPTrustLevel registry value COM
ms.topic: article
ms.date: 05/31/2018
---

# SRPTrustLevel

Sets the software restriction policy (SRP) trust level for applications.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\AppID
   {AppID_GUID}
      SRPTrustLevel = value
```

## Remarks

This is a **REG\_DWORD** value that is available starting with Windows XP.



| Value                                 | Description                                                                          |
|---------------------------------------|--------------------------------------------------------------------------------------|
| 0x0 (SAFER\_LEVELID\_DISALLOWED)      | The application is disallowed from accessing and security-sensitive user privileges. |
| 0x40000 (SAFE\_LEVELID\_FULLYTRUSTED) | The application has unrestricted access to the user's privileges.                    |



 

If the **SRPTrustLevel** value does not exist, the default value of SAFER\_LEVELID\_DISALLOWED is used. If **SRPTrustLevel** is of the wrong type or out of range, COM returns the error COMADMIN\_E\_SAFERINVALID. If an activation of any sort fails because of SRP trust checks, COM returns the error CO\_E\_ACTIVATIONFAILED.

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> <dt>

[**SRPActivateAsActivatorChecks**](srpactivateasactivatorchecks.md)
</dt> <dt>

[**SRPRunningObjectChecks**](srprunningobjectchecks.md)
</dt> </dl>

 

 





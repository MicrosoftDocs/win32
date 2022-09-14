---
title: EnrollMethod method of the MDM_ClientCertificateInstall_Install03 class
description: Triggers the device to start the certificate enrollment.
ms.assetid: 21a31574-0b19-44bf-90db-4bb9e2611364
keywords:
- EnrollMethod method
- EnrollMethod method, MDM_ClientCertificateInstall_Install03 class
- MDM_ClientCertificateInstall_Install03 class, EnrollMethod method
topic_type:
- apiref
api_name:
- MDM_ClientCertificateInstall_Install03.EnrollMethod
api_location:
- DMWmiBridgeProv.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnrollMethod method of the MDM\_ClientCertificateInstall\_Install03 class

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

Triggers the device to start the certificate enrollment. The device will not notify MDM server after certificate enrollment is done. The MDM server could later query the device to find out whether new certificate is added. See also, [**Enroll**](/windows/client-management/mdm/clientcertificateinstall-csp).

## Syntax


```mof
uint32 EnrollMethod();
```



## Parameters

This method has no parameters.

## Return value

Required. Triggers the device to start the certificate enrollment. The device will not notify MDM server after certificate enrollment is done. The MDM server could later query the device to find out whether new certificate is added.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                      |
| Namespace<br/>                | Root\\cimv2\\mdm\\dmmap<br/>                                                             |
| MOF<br/>                      | <dl> <dt>DMWmiBridgeProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DMWmiBridgeProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_ClientCertificateInstall\_Install03**](mdm-clientcertificateinstall-install03.md)
</dt> <dt>

[Using PowerShell scripting with the WMI Bridge Provider](/windows/client-management/mdm/using-powershell-scripting-with-the-wmi-bridge-provider)
</dt> </dl>

 


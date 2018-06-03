---
Description: The WMI Policy provider provides extensions to group policy, permitting refinements in the application of policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f0016ae4-8ddd-4d93-9d43-630e016a0e86
ms.prod: windows-server-dev
ms.technology:
- group-policy
- windows-management-instrumentation
ms.tgt_platform: multiple
title: Policy Provider
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Policy Provider

The WMI policy provider provides extensions to group policy, permitting refinements in the application of policy. Policy is set using the WMI Query Language (WQL) and resides in the Active Directory for easy deployment. The policy provider and its classes reside in the \\root\\policy namespace. The provider has two [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688) instances named "PolicSOM" and "PolicStatus".

As an instance and method provider, the policy provider implements the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface and the following [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) methods:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The policy provider supports the following classes:

-   [**SomFilterPutStatus**](somfilterputstatus.md)
-   [**MSFT\_Rule**](msft-rule.md)
-   [**MSFT\_SomFilter**](msft-somfilter.md)
-   [**MSFT\_SomFilterStatus**](msft-somfilterstatus.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 




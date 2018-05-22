---
title: Handling WhatIf and Confirm in cmdlets
description: This topic covers some of the design considerations regarding handling WhatIf and Confirm in cmdlets.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'C9A74D0A-EC50-482E-903F-71467DC01CDA'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# Handling WhatIf and Confirm in cmdlets

This topic covers some of the design considerations regarding handling WhatIf and Confirm in cmdlets.

A PowerShell cmdlet that changes the system state must support WhatIf and Confirm parameters. A cmdlet run with WhatIf will tell the user what changes this cmdlet will make. Similarly, a cmdlet run with the Confirm parameter will display a confirmation prompt for the user before making the change.

A key concern for implementing WMI class WhatIf or Confirm semantics in PowerShell is whether the target WMI provider natively supports this behavior. A provider written using the new MI provider API may call MI\_ShouldProcess to prompt the user before making changes. If this is the case, the cmdlet defined in CDXML needs to declare that it supports WhatIf or Confirm. For WMI providers that do not support MI\_ShouldProcess natively - such as legacy providers under the root\\cimv2 namespace - CDXML will also declare that WhatIf or Confirm should be handled locally in the cmdlet without relying on the WMI provider.

## Related topics

<dl> <dt>

[Requesting Confirmation from Cmdlets](http://go.microsoft.com/fwlink/p/?linkid=257881)
</dt> </dl>

 

 





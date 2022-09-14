---
description: The WMI scripting reference contains definitions for the WMI Scripting API.
ms.assetid: 83fc78fc-929d-4d32-940e-9147543a6324
ms.tgt_platform: multiple
title: Scripting API for WMI
ms.topic: article
ms.date: 05/31/2018
---

# Scripting API for WMI

The WMI scripting reference contains definitions for the WMI Scripting API. Use this API if writing applications with Microsoft Visual Basic, Visual Basic for Applications, Visual Basic Scripting Edition (VBScript), or any other scripting language that supports active scripting technologies.

> [!Note]  
> PowerShell is also available for scripting with WMI. The Get-WMI cmdlet and the three type accelerators (\[wmi\], \[wmiclass\], and \[wmisearcher\]) enable basic administrative access to WMI.

 

WMI scripting objects, except for [**SWbemDateTime**](swbemdatetime.md) are not marked safe for scripting for scripts running on HTML pages in Internet Explorer. Therefore, unless the security level within Internet Explorer is lowered, the script will fail. **SWbemDateTime** is marked safe for initialization and scripting. However, use all WMI scripting objects in **GetObject** and **CreateObject** calls on server-side code in Active Server Pages (ASP).

-   [Scripting API Object Model](scripting-api-object-model.md)
-   [Document Conventions for the Scripting API](document-conventions-for-the-scripting-api.md)
-   [Scripting API Objects](scripting-api-objects.md)
-   [Scripting API Constants](scripting-api-constants.md)

## Related topics

<dl> <dt>

[WMI Reference](wmi-reference.md)
</dt> <dt>

[WMI Return Codes](wmi-return-codes.md)
</dt> </dl>

 

 




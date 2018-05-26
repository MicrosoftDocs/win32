---
title: Active Directory Provider
description: The Active Directory provider, also known as the Directory Services (DS) provider, maps Active Directory objects to WMI.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 655d7e24-9464-439a-a75f-076e4942603e
ms.prod: windows-server-dev
ms.technology:
- active-directory-domain-services
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- providers Windows Management Instrumentation , Active Directory
- Active Directory provider Windows Management Instrumentation
- __PUT_EXT_PROPERTIES
- __PUT_EXTENSIONS
- __PUT_EXT_CLIENT_REQUEST
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Active Directory Provider

The Active Directory provider, also known as the Directory Services (DS) provider, maps Active Directory objects to WMI. By accessing the LDAP namespace in WMI, you can reference or alias any object in the Active Directory.

As a dynamic instance and class provider, the Active Directory provider supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, as well as the following methods of the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) interface:

-   [**CreateClassEnumAsync**](https://msdn.microsoft.com/library/aa392096)
-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**DeleteInstanceAsync**](https://msdn.microsoft.com/library/aa392102)
-   [**ExecQueryAsync**](https://msdn.microsoft.com/library/aa392108)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

The Active Directory provider supports limited querying for association objects. For more information, see [Accessing Active Directory](https://msdn.microsoft.com/library/aa384689).

-   [**DS\_LDAP\_Class\_Containment**](ds-ldap-class-containment.md)
-   [**DS\_LDAP\_Instance\_Containment**](ds-ldap-instance-containment.md)
-   [**RootDSE**](rootdse.md)

To update the properties of a Directory Services provider instance, you must provide an [**IWbemContext**](https://msdn.microsoft.com/library/aa391465) object or a [**SWbemNamedValueSet**](https://msdn.microsoft.com/library/aa393732) object (for scripting) with these values defined:

-   "\_\_PUT\_EXT\_PROPERTIES"

    A string array that contains the name of the properties you want to update.

-   "\_\_PUT\_EXTENSIONS"

    A boolean value set to true.

-   "\_\_PUT\_EXT\_CLIENT\_REQUEST"

    A boolean value set to true.

The following VBScript code gives an example of how to provide a [**SWbemNamedValueSet**](https://msdn.microsoft.com/library/aa393732) object with the correct values defined to update the properties of a Directory Services provider.


```VB
set svc = GetObject("Winmgmts:root\directory\ldap")
set octx = createobject("wbemscripting.swbemnamedvalueset")

octx.add "__PUT_EXT_PROPERTIES", array("ds_displayname")
octx.add "__PUT_EXTENSIONS", true
octx.add "__PUT_EXT_CLIENT_REQUEST", true

set objEnum = svc.execQuery("select * from ds_computer", "WQL", 32)

for each obj in objEnum
 obj.put_ 1, octx
next
```



## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> <dt>

[**IWbemContext**](https://msdn.microsoft.com/library/aa391465)
</dt> <dt>

[**IWbemContext::SetValue method**](https://msdn.microsoft.com/library/aa391474)
</dt> <dt>

[**SWbemNamedValueSet**](https://msdn.microsoft.com/library/aa393732)
</dt> <dt>

[**SWbemNamedValueSet.Add method**](https://msdn.microsoft.com/library/aa393733)
</dt> </dl>

 

 





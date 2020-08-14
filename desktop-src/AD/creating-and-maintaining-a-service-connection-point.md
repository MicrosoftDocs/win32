---
title: Creating and Maintaining a Service Connection Point
description: When publishing with an SCP, remember that it must contain current data about the service instance.
ms.assetid: 2350cb65-3439-4a5f-adc5-b71476793247
ms.tgt_platform: multiple
keywords:
- Creating and Maintaining a Service Connection Point AD
- service connection point AD , creating and maintaining
ms.topic: article
ms.date: 05/31/2018
---

# Creating and Maintaining a Service Connection Point

When publishing with an SCP, remember that it must contain current data about the service instance. Otherwise, clients that bind to the SCP retrieve outdated data. Your service installer, that creates an SCP, specifies the initial values for the SCPs attributes. Then, when the service instance starts, it must locate the SCP and update the attribute values, if necessary. In this way, clients are assured the most current data.

After creating the SCP, your service installer performs two additional steps that enable your service to update the SCP:

-   Set ACEs in the security descriptor of the SCP object to enable the service to modify SCP attributes at run time. For more information and a code example, see [Enabling Service Account to Access SCP Properties](enabling-service-account-to-access-scp-properties.md).
-   Cache the **objectGUID** of the SCP in the registry on the service host computer. The service retrieves the cached GUID to bind to the SCP to verify and update its attributes.

The service installer caches the SCP's **objectGUID** rather than its DN. The **objectGUID** never changes, regardless of whether the SCP is moved or renamed. The DN can change if an administrator moves or renames the SCP. For example, if you create an SCP as a child of a computer object, the distinguished name of the SCP changes if the computer is renamed or moved to a different domain or organizational unit.

When a service installer creates an SCP, it must read the **objectGUID** of the newly created object and cache it in the registry of the service host computer. Use the [**IADs::get\_GUID**](/windows/desktop/ADSI/iads-property-methods) method to get the **objectGUID** value in string format suitable for binding. Cache the GUID string as a value under the following registry key.

```
HKEY_LOCAL_MACHINE
   vendor name
      product name
```

Where "vendor name" and "product name" identify the vendor and product.

When the service starts, it retrieves the cached GUID string from the registry and uses it to bind to the SCP. The service reads the important SCP attributes and compares them to current values. If the SCP values are outdated, the service updates them. Values that the service might require to update include **keywords**, **serviceBindingInformation**, **serviceDNSName**, and **serviceDNSNameType**.

## Examples

-   [Script samples](script-samples-for-managing-service-connection-points.md)
-   [Code (C/C++) samples](code-samples-for-managing-service-connection-points.md)

 

 
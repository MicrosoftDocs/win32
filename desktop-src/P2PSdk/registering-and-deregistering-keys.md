---
description: Registering and Deregistering Keys
ms.assetid: 90fd8df0-e2a8-4183-a50c-e6f8ea5041cc
title: Registering and Deregistering Keys
ms.topic: article
ms.date: 05/31/2018
---

# Registering and Deregistering Keys

## Registering Keys

A node can register keys with [**DrtRegisterKey**](/windows/desktop/api/drt/nf-drt-drtregisterkey) at anytime while in the **DRT\_ACTIVE**, **DRT\_ALONE**, and **DRT\_NO\_NETWORK** states. Keys registered in **DRT\_ALONE** and **DRT\_NO\_NETWORK** states can only be recognized by other DRTs after the local node has transitioned to **DRT\_ACTIVE**.

Identical keys cannot be registered within the same DRT instance when using [**DrtCreateDerivedKeySecurityProvider**](/windows/desktop/api/drt/nf-drt-drtcreatederivedkeysecurityprovider). If the registration of identical keys is attempted, the registration of the second key will fail. The use of identical keys should also be avoided between different DRT instances. Searches against the unique key designation these identical keys share could return any one of the keys, regardless of what data is associated to the key.

> [!Note]  
> If different behavior is required for implementation, a security provider can be created in place of [**DrtCreateDerivedKeySecurityProvider**](/windows/desktop/api/drt/nf-drt-drtcreatederivedkeysecurityprovider) to accommodate.

 

## Deregistering Keys

A node can deregister a key anytime after it has been registered. However, only the application that registered the key can deregister it. An application can deregister a key from the local node using the [**DrtUnregisterKey**](/windows/desktop/api/drt/nf-drt-drtunregisterkey) function. Upon completion the function triggers a **DRT\_EVENT\_LEAFSET\_KEY\_CHANGE** event; informing the application as well as other nodes participating in the DRT mesh.

While in the **DRT\_FAULTED** state, the required call of [**DrtClose**](/windows/desktop/api/drt/nf-drt-drtclose) will result in the DRT infrastructure deregistering all keys.

## Related topics

<dl> <dt>

[Searching a Distributed Routing Table](searching-a-distributed-routing-table.md)
</dt> <dt>

[About Distributed Routing Tables](about-distributed-routing-tables.md)
</dt> <dt>

[Distributed Routing Table API Reference](distributed-routing-table-api-reference.md)
</dt> </dl>

 

 




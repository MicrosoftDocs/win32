---
description: Resource Dispenser Resource Allocation Process
ms.assetid: 695d08f4-ba5c-4a5f-a2ad-481a8ede49ab
title: Resource Dispenser Resource Allocation Process
ms.topic: article
ms.date: 05/31/2018
---

# Resource Dispenser Resource Allocation Process

Each time a resource dispenser allocates a resource from its holder, the following occurs:

1.  The resource dispenser declares a resource type identifier (**RESTYPID**), which describes the type of resource required.

2.  The resource dispenser calls the holder's [**IHolder::AllocResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-allocresource) method, passing this **RESTYPID**.

3.  The holder generates a candidate list from the available resources. Candidates are resources that are either not enlisted in a transaction or already enlisted in the calling object's transaction.

4.  These candidates are individually passed to the [**IDispenserDriver::RateResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-rateresource) method where they are rated (on a scale of 0 to 100) by how well the candidate resource matches the desired **RESTYPID**.

5.  The holder chooses the resource that the resource dispenser rates as highest.

6.  The resource dispenser can terminate the rating loop early by assigning the candidate a resource rating of 100 (a perfect fit). A rating of 100 would normally be reserved for candidate resources that are already properly enlisted, unless the resource dispenser concludes that enlistment is an inexpensive operation. If all candidate resources (if any) are rated 0 (unusable), a new resource is created by calling [**IDispenserDriver::CreateResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-createresource).

7.  If the resource chosen previously is not already enlisted in the calling object's transaction, the resource dispenser's [**IDispenserDriver::EnlistResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-enlistresource) method is called.

8.  The [**AllocResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-allocresource) method call returns to the resource dispenser with the enlisted resource.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[Enlisting a Resource in a Transaction](enlisting-a-resource-in-a-transaction.md)
</dt> <dt>

[Tracking Non-Allocated Resources](tracking-non-allocated-resources.md)
</dt> </dl>

 

 




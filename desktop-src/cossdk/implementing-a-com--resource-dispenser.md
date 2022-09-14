---
description: Implementing a COM+ Resource Dispenser
ms.assetid: 083c5962-f55a-435a-964e-fdc868f9bd3d
title: Implementing a COM+ Resource Dispenser
ms.topic: article
ms.date: 05/31/2018
---

# Implementing a COM+ Resource Dispenser

The following steps outline a general procedure for implementing a COM+ resource dispenser:

1.  Decide on **RESTYPID** format that categorizes how your resources differ from each other.

2.  Use the Mtxdm.h and Mtxdm.lib header file and library, respectively.

3.  Build a DLL that implements the [**IDispenserDriver**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispenserdriver) interface and the API you want to expose to applications.

4.  In the startup ([*DllMain*](/windows/desktop/Dlls/dllmain) or first call to the dispenser API), call the [**GetDispenserManager**](/windows/desktop/api/MtxDM/nf-mtxdm-getdispensermanager) function. This returns a pointer to the dispenser manager's [**IDispenserManager**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispensermanager) interface.

5.  Call [**IDispenserManager::RegisterDispenser**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispensermanager-registerdispenser), passing a pointer to your implementation of [**IDispenserDriver**](/windows/desktop/api/ComSvcs/nn-comsvcs-idispenserdriver). This causes the dispenser manager to create a holder (pooling manager) for your resource dispenser and then return the pointer to your [**IHolder**](/windows/desktop/api/ComSvcs/nn-comsvcs-iholder) interface.

6.  Store this pointer so that you can call [**IHolder::AllocResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-allocresource) and [**IHolder::FreeResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-freeresource).

7.  You can now (in response to calls to your API) make calls to [**AllocResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-allocresource) and [**FreeResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-iholder-freeresource). **AllocResource** initially responds by calling back to your [**CreateResource**](/windows/desktop/api/ComSvcs/nf-comsvcs-idispenserdriver-createresource) method, but later **AllocResource** calls are serviced from the growing pool of resources.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[COM+ Resource Dispenser Interfaces](com--resource-dispenser-interfaces.md)
</dt> </dl>

 

 

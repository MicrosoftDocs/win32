---
Description: Implementing a COM+ Resource Dispenser
ms.assetid: '083c5962-f55a-435a-964e-fdc868f9bd3d'
title: Implementing a COM+ Resource Dispenser
---

# Implementing a COM+ Resource Dispenser

The following steps outline a general procedure for implementing a COM+ resource dispenser:

1.  Decide on **RESTYPID** format that categorizes how your resources differ from each other.

2.  Use the Mtxdm.h and Mtxdm.lib header file and library, respectively.

3.  Build a DLL that implements the [**IDispenserDriver**](idispenserdriver.md) interface and the API you want to expose to applications.

4.  In the startup ([*DllMain*](https://msdn.microsoft.com/library/windows/desktop/ms682583) or first call to the dispenser API), call the [**GetDispenserManager**](getdispensermanager.md) function. This returns a pointer to the dispenser manager's [**IDispenserManager**](idispensermanager.md) interface.

5.  Call [**IDispenserManager::RegisterDispenser**](idispensermanager-registerdispenser.md), passing a pointer to your implementation of [**IDispenserDriver**](idispenserdriver.md). This causes the dispenser manager to create a holder (pooling manager) for your resource dispenser and then return the pointer to your [**IHolder**](iholder.md) interface.

6.  Store this pointer so that you can call [**IHolder::AllocResource**](iholder-allocresource.md) and [**IHolder::FreeResource**](iholder-freeresource.md).

7.  You can now (in response to calls to your API) make calls to [**AllocResource**](iholder-allocresource.md) and [**FreeResource**](iholder-freeresource.md). **AllocResource** initially responds by calling back to your [**CreateResource**](idispenserdriver-createresource.md) method, but later **AllocResource** calls are serviced from the growing pool of resources.

## Related topics

<dl> <dt>

[COM+ Resource Dispenser Concepts](com--resource-dispenser-concepts.md)
</dt> <dt>

[COM+ Resource Dispenser Interfaces](com--resource-dispenser-interfaces.md)
</dt> </dl>

 

 




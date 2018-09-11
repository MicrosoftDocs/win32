---
Description: Describes status for a wide area network (WWAN) interface.
ms.assetid: C4BFF2BA-BFBB-46C8-AF94-F7BF5FC6A8C5
title: WWAN_INTERFACE_STATUS structure
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WWAN_INTERFACE_STATUS
api_type: 
- NA
---

# WWAN\_INTERFACE\_STATUS structure

Describes status for a wide area network (WWAN) interface.

## Syntax


```C++
typedef struct {
  BOOL                 fInitialized;
  WWAN_INTERFACE_STATE InterfaceState;
} WWAN_INTERFACE_STATUS;
```



## Members

<dl> <dt>

**fInitialized**
</dt> <dd>

A Boolean value that indicates whether the status is initialized. **TRUE** indicates the status is initialized; otherwise, **FALSE**.

</dd> <dt>

**InterfaceState**
</dt> <dd>

A **WWAN\_INTERFACE\_STATE**-typed value that indicates the state of the interface. Here are possible values:

<dl> <dt>

<span id="WwanInterfaceStateNotReady"></span><span id="wwaninterfacestatenotready"></span><span id="WWANINTERFACESTATENOTREADY"></span>**WwanInterfaceStateNotReady** (0)
</dt> <dt>

<span id="WwanInterfaceStateDeviceLocked"></span><span id="wwaninterfacestatedevicelocked"></span><span id="WWANINTERFACESTATEDEVICELOCKED"></span>**WwanInterfaceStateDeviceLocked**
</dt> <dt>

<span id="WwanInterfaceStateUserAccountNotActivated"></span><span id="wwaninterfacestateuseraccountnotactivated"></span><span id="WWANINTERFACESTATEUSERACCOUNTNOTACTIVATED"></span>**WwanInterfaceStateUserAccountNotActivated**
</dt> <dt>

<span id="WwanInterfaceStateRegistered"></span><span id="wwaninterfacestateregistered"></span><span id="WWANINTERFACESTATEREGISTERED"></span>**WwanInterfaceStateRegistered**
</dt> <dt>

<span id="WwanInterfaceStateRegistering"></span><span id="wwaninterfacestateregistering"></span><span id="WWANINTERFACESTATEREGISTERING"></span>**WwanInterfaceStateRegistering**
</dt> <dt>

<span id="WwanInterfaceStateDeregistered"></span><span id="wwaninterfacestatederegistered"></span><span id="WWANINTERFACESTATEDEREGISTERED"></span>**WwanInterfaceStateDeregistered**
</dt> <dt>

<span id="WwanInterfaceStateAttached"></span><span id="wwaninterfacestateattached"></span><span id="WWANINTERFACESTATEATTACHED"></span>**WwanInterfaceStateAttached**
</dt> <dt>

<span id="WwanInterfaceStateAttaching"></span><span id="wwaninterfacestateattaching"></span><span id="WWANINTERFACESTATEATTACHING"></span>**WwanInterfaceStateAttaching**
</dt> <dt>

<span id="WwanInterfaceStateDetaching"></span><span id="wwaninterfacestatedetaching"></span><span id="WWANINTERFACESTATEDETACHING"></span>**WwanInterfaceStateDetaching**
</dt> <dt>

<span id="WwanInterfaceStateActivated"></span><span id="wwaninterfacestateactivated"></span><span id="WWANINTERFACESTATEACTIVATED"></span>**WwanInterfaceStateActivated**
</dt> <dt>

<span id="WwanInterfaceStateActivating"></span><span id="wwaninterfacestateactivating"></span><span id="WWANINTERFACESTATEACTIVATING"></span>**WwanInterfaceStateActivating**
</dt> <dt>

<span id="WwanInterfaceStateDeactivating"></span><span id="wwaninterfacestatedeactivating"></span><span id="WWANINTERFACESTATEDEACTIVATING"></span>**WwanInterfaceStateDeactivating**
</dt> </dl> </dd> </dl>

## See also

<dl> <dt>

[**WWAN\_INTERFACE\_INFO**](wwan-interface-info.md)
</dt> </dl>

 

 




---
description: To create a WMI event provider you must register the \_\_Win32Provider instance that represents your provider using an instance of \_\_EventProviderRegistration.
ms.assetid: 81f2ba3b-a1cb-42f5-b1a7-b1ca65963902
ms.tgt_platform: multiple
title: Registering an Event Provider
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Registering an Event Provider

To create a WMI [*event provider*](gloss-e.md) you must register the [**\_\_Win32Provider**](--win32provider.md) instance that represents your provider using an instance of [**\_\_EventProviderRegistration**](--eventproviderregistration.md). As a COM object, your provider must register with the operating system and WMI. The following procedure assumes that you have already implemented the registration process as described in [Registering a Provider](registering-a-provider.md).

The following procedure describes how to register an event provider.

**To register an event provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class that describes the provider.
2.  Create an instance of the [**\_\_EventProviderRegistration**](--eventproviderregistration.md) class that describes the feature set of the provider.

    The [**\_\_EventProviderRegistration**](--eventproviderregistration.md) class inherits many properties from the [**\_\_ObjectProviderRegistration**](--objectproviderregistration.md) parent class. The properties local to the **\_\_EventProviderRegistration** class are the object path to the provider and a list of queries that describe the events that the provider supports. For more information, see [Querying WMI](querying-wmi.md).

3.  Load your implementation of the [**\_\_Win32Provider**](--win32provider.md) and [**\_\_EventProviderRegistration**](--eventproviderregistration.md) classes into the WMI repository.

    WMI uses your class definition to register and access your event provider. For more information, see [Registering a Provider](registering-a-provider.md).

The following code example describes an implementation of a [**\_\_Win32Provider**](--win32provider.md) class and a [**\_\_EventProviderRegistration**](--eventproviderregistration.md) class.

``` syntax
instance of __Win32Provider as $P
{
    ClientLoadableCLSID = NULL;
    CLSID = "{AA7828C5-95F9-11d2-BB0D-00C042424242}";
    DefaultMachineName = NULL;
    ImpersonationLevel = 0;
    InitializationReentrancy = 0;
    InitializeAsAdminFirst = FALSE;
    Name = "FaxEventProvider";
    PerLocaleInitialization = FALSE;
    PerUserInitialization = FALSE;
    Pure = TRUE;
    UnloadTimeout = NULL;
};

instance of __EventProviderRegistration
{  
Provider = $P;
EventQueryList = {
         "SELECT * FROM FaxEvent",
         "SELECT * FROM __InstanceCreationEvent WHERE TargetInstance ISA \"Win32_LogicalDisk\""};
};
```

The first query indicates that the provider generates all event notifications for the extrinsic event class FaxEvent. Because it uses the ISA operator, the second query implies that the provider generates notifications for all instance creation events for the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class and all of its subclasses.

When a provider registers to provide an intrinsic event, the event must apply to all instances of a class. In other words, a query cannot be written to provide instance creation events for only some of the disk drives that belong to the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class.

 

 

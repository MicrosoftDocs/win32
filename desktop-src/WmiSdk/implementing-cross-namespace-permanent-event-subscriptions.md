---
description: It is recommended that all permanent subscriptions be compiled into the \\root\\subscription namespace.
ms.assetid: 6d4ccc86-f29f-4ca5-bea5-c77ee07d7789
ms.tgt_platform: multiple
title: Implementing Cross-Namespace Permanent Event Subscriptions
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Cross-Namespace Permanent Event Subscriptions

It is recommended that all permanent subscriptions be compiled into the \\root\\subscription namespace. This prevents the need to compile the permanent consumer into each namespace being used, which means that there is only one namespace to look for permanent subscriptions. Use the **EventNamespace** property of [**\_\_EventFilter**](--eventfilter.md) to implement a cross-namespace subscription.

When using the [**CommandLineEventConsumer**](commandlineeventconsumer.md), it is important to secure the executable you are launching. If the executable is not in a secure location, or secured with a strong access control list (ACL), anyone can replace your executable with one of their own. For more information about ACLs, see [Creating a Security Descriptor for a New Object in C++](/windows/desktop/SecAuthZ/creating-a-security-descriptor-for-a-new-object-in-c--).

The following Managed Object Format (MOF) code example shows a cross-namespace subscription.

``` syntax
#pragma namespace("\\root\\subscription")

instance of __EventFilter as $FLT
{
  Name = "Filter";
  Query = "SELECT * FROM __InstanceModificationEvent "
          "WHERE TargetInstance ISA \"Win32_LocalTime\" "
          "AND TargetInstance.Hour = 8 "
          "AND TargetInstance.Minute = 0 "
          "AND TargetInstance.Second = 0 "
          "AND TargetInstance.DayOfWeek = 6";
  QueryLanguage = "WQL";
  EventNamespace = "root\\cimv2";
};

instance of CommandLineEventConsumer as $CONS
{
  ExecutablePath = "cmd.exe";
  ShowWindowCommand = 7;
  RunInteractively = true;
};

instance of __FilterToConsumerBinding
{
  Consumer = $CONS;
  Filter = $FLT;
};
```

 

 

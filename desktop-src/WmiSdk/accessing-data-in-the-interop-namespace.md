---
Description: 'Association providers enable Windows Management Instrumentation (WMI) clients to traverse and retrieve profiles and associated class instances from different namespaces.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '00c654d1-a5de-40c5-a190-99382949486a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Accessing Data in the Interop Namespace
---

# Accessing Data in the Interop Namespace

Association providers enable Windows Management Instrumentation (WMI) clients to traverse and retrieve profiles and associated class instances from different namespaces.

Association providers and classes reside in the \\\\root\\interop namespace. For more information, see [Cross Namespace Association Traversal](cross-namespace-association-traversal.md) and [Writing an Association Provider](writing-an-association-provider-for-interop.md).

Association providers expose standard profiles, like a power profile. The following examples use the power profile to illustrate how to discover and access data through the interop namespace.

Windows PowerShell provides a simple mechanism to traverse through the appropriate association, retrieve a device profile, and call a method.

## Enumerating profiles in the root/interop namespace

The following Windows PowerShell command enumerates the Distributed Management Task Force ([DMTF](http://go.microsoft.com/fwlink/p/?linkid=67786))-supported profiles on a Windows 7 computer:


```PowerShell
Get-WmiObject CIM_RegisteredProfile  -namespace root\interop
```



## Retrieving instances of a specific device profile

The following Windows PowerShell command returns all instances of a specified profile through [**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375):


```PowerShell
Get-WmiObject -namespace root\interop -query "Associators of {CIM_RegisteredProfile.InstanceID='Power Supply'}"
```



## Assigning the power profile to a variable

The following Windows PowerShell command assigns the power profile instance to a variable:


```PowerShell
$pplan = Get-WmiObject -query "Select * from Win32_PowerPlan" -Namespace root\cimv2\power
```



## Enumerating the power plans on a computer

The following Windows PowerShell command enumerates the available power profile plans:


```PowerShell
$pplan
```



## Calling a method

The following Windows PowerShell command calls the [**Activate**](https://msdn.microsoft.com/library/dd904499) method for the power plan:


```PowerShell
$pplan[2].Activate()
```



## Related topics

<dl> <dt>

[Cross Namespace Association Traversal](cross-namespace-association-traversal.md)
</dt> <dt>

[Writing an Association Provider](writing-an-association-provider-for-interop.md)
</dt> <dt>

[**CIM\_RegisteredProfile**](https://msdn.microsoft.com/library/ee309375)
</dt> <dt>

[**Win32\_PowerPlan**](https://msdn.microsoft.com/library/dd904531)
</dt> </dl>

 

 




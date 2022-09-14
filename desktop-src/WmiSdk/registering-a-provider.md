---
description: Before implementing your provider, you should first register your provider with WMI. Registering the provider defines the type of the provider and the classes that the provider supports. WMI can only access registered providers.
ms.assetid: b0a1a11c-a8e8-4bc1-b286-fb9243667976
ms.tgt_platform: multiple
title: Registering a Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Provider

Before implementing your provider, you should first register your provider with WMI. Registering the provider defines the type of the provider and the classes that the provider supports. WMI can only access registered providers.

> [!Note]  
> For more information on registering an MI provider, see [How to: Register an MI Provider](/previous-versions/windows/desktop/wmi_v2/how-to-register-an-mi-provider).

 

You can write your provider code before you register the provider. However, it is very difficult to debug a provider that is not registered with WMI. Determining the interfaces for your provider also helps to outline the purpose and structure of a provider. Therefore, registering your provider helps you design your provider.

Only administrators can register or delete a provider.

A provider must be registered for all the different types of provider functions that it performs. Nearly all providers supply instances of classes they define, but they may also provide property data, methods, events, or classes. The provider may also be registered as an event consumer provider or a performance counter provider. It is recommended that you combine all provider functionality in one provider rather than having many separate providers for each type. An example is the [System Registry provider](/previous-versions/windows/desktop/regprov/system-registry-provider), which provides methods and instances, and the [Disk Quota provider](/previous-versions/windows/desktop/wmipdskq/disk-quota-provider), which supplies instances, methods, and events.

A provider must be registered for all the different types of provider functions that it performs. Nearly all providers supply instances of classes they define, but they may also provide property data, methods, events, or classes. The provider may also be registered as an event consumer provider or a performance counter provider.

The same instance of [**\_\_Win32Provider**](--win32provider.md) is used for each type of registration:

-   [Registering an Instance Provider](registering-an-instance-provider.md)
-   [Registering a Class Provider](registering-a-class-provider.md)
-   [Registering a Method Provider](registering-a-method-provider.md)
-   [Registering an Event Provider](registering-an-event-provider.md)
-   [Registering an Event Consumer Provider](registering-an-event-consumer-provider.md)
-   [Making an Instance Provider into a High-Performance Provider](making-an-instance-provider-into-a-high-performance-provider.md)

## Example: Creating and Registering an Instance of a Provider

The following example shows a MOF file that creates and registers an instance of the [System Registry provider](/previous-versions/windows/desktop/regprov/system-registry-provider) in the root\\cimv2 namespace. It assigns the alias $Reg to the provider to avoid the long pathname required in the instance and method registrations. For more information, see [Creating an Alias](creating-an-alias.md).

``` syntax
// Place the Registry provider in the root\cimv2 namespace
#pragma namespace("\\\\.\\ROOT\\cimv2")

// Create an instance of __Win32Provider
instance of __Win32Provider as $Reg
{
Name = "RegProv";        
CLSID = "{fe9af5c0-d3b6-11ce-a5b6-00aa00680c3f}";
HostingModel = "NetworkServiceHost:LocalServiceHost";
};

// Register as an instance provider by
// creating an instance
// of __InstanceProviderRegistration
instance of __InstanceProviderRegistration
{
 provider = $Reg;
 SupportsDelete = FALSE;
 SupportsEnumeration = TRUE;
 SupportsGet = TRUE;
 SupportsPut = TRUE;
};

// Register as a method provider by
// creating an instance
// of __MethodProviderRegistration
instance of __MethodProviderRegistration
{
 provider = $Reg;
};

// Define the StdRegProv class
[dynamic: ToInstance, provider("RegProv")]
class StdRegProv
{
[implemented, static] uint32 CreateKey(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName);
[implemented, static] uint32 DeleteKey(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName);
[implemented, static] uint32 EnumKey(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [OUT] string sNames[]);
[implemented, static] uint32 EnumValues(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [OUT] string sNames[], 
 [OUT] sint32 Types[]);
[implemented, static] uint32 DeleteValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName);
 [implemented, static] uint32 SetDWORDValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [IN] uint32 uValue = 3);
[implemented, static] uint32 GetDWORDValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [OUT] uint32 uValue);
[implemented, static] uint32 SetStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [IN] string sValue = "hello");
[implemented, static] uint32 GetStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [in] string sValueName, 
 [OUT] string sValue);
[implemented, static] uint32 SetMultiStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [IN] string sValue[] = {"hello", "there"});
[implemented, static] uint32 GetMultiStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [OUT] string sValue[]);
[implemented, static] uint32 SetExpandedStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [IN] string sValue = "%path%");
[implemented, static] uint32 GetExpandedStringValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [OUT] string sValue);
[implemented, static] uint32 SetBinaryValue(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [in] string sValueName, 
 [in] uint8 uValue[] = {1, 2});
[implemented, static] uint32 GetBinaryValue(
 {IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] string sValueName, 
 [OUT] uint8 uValue[]);
[implemented, static] uint32 CheckAccess(
 [IN] uint32 hDefKey = 2147483650, 
 [IN] string sSubKeyName, 
 [IN] uint32 uRequired = 3, 
 [OUT] boolean bGranted);
};
```

## Example: Registering a Provider

The following procedure describes how to register a provider.

**To register a provider**

1.  Register the provider as a COM server.

    If necessary, you may need to create registry entries. This process applies to all COM servers and is unrelated to WMI. For more information, see the COM section in the Microsoft Windows Software Development Kit (SDK) documentation.

2.  Create a MOF file that contains instances of [**\_\_Win32Provider**](--win32provider.md) and an instance of a class derived either directly or indirectly from [**\_\_ProviderRegistration**](--providerregistration.md), such as [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md). Only administrators can register or delete a provider by creating instances of classes derived from **\_\_Win32Provider** or [**\_\_ProviderRegistration**](--providerregistration.md).
3.  Set the [**HostingModel**](--win32provider.md) in the instance of **\_\_Win32Provider** according to the values in [Hosting models](provider-hosting-and-security.md).

    > [!Note]  
    > Unless the provider requires the high privileges of the LocalSystem account, the [**\_\_Win32Provider.HostingModel**](--win32provider.md) property should be set to "NetworkServiceHost". For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

     

    The following MOF example from the full example shows the code that creates an instance of [**\_\_Win32Provider**](--win32provider.md).

    ```mof
    instance of __Win32Provider as $Reg
    {
    Name = "RegProv";        
    CLSID = "{fe9af5c0-d3b6-11ce-a5b6-00aa00680c3f}";
    HostingModel = "NetworkServiceHost:LocalServiceHost";
    };
    ```

    

4.  An instance of a class derived either directly or indirectly from [**\_\_ProviderRegistration**](--providerregistration.md), to describe the logical implementation of the provider. A provider can be registered for several different types of functionality. The example above registers RegProv as an instance and method provider. But if RegProv supports the functionality, it could also be registered as a property or event provider. The following table lists the classes that register provider functionality.

    

    | Provider registration classes                                                        | Description                                                                         |
    |--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
    | [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md)           | Registers an [instance provider](registering-an-instance-provider.md).             |
    | [**\_\_EventProviderRegistration**](--eventproviderregistration.md)                 | Registers an [event provider](registering-an-event-provider.md).                   |
    | [**\_\_EventConsumerProviderRegistration**](--eventconsumerproviderregistration.md) | Registers an [event consumer provider](registering-an-event-consumer-provider.md). |
    | [**\_\_MethodProviderRegistration**](--methodproviderregistration.md)               | Registers a [method provider](registering-an-event-consumer-provider.md).          |
    | [**\_\_PropertyProviderRegistration**](--propertyproviderregistration.md)           | Registers a [property provider](registering-a-property-provider.md).               |

    

     

5.  Place the MOF file into a permanent directory.

    Typically, you should place the file in the installation directory of the provider.

6.  Compile the MOF file using [mofcomp](mofcomp.md) or the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface.

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

    **Windows 8 and Windows Server 2012:** When installing providers, both [**mofcomp**](mofcomp.md) and the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface treat the \[Key\] and \[Static\] qualifiers as true if they are present, regardless of their actual values. Other qualifiers are treated as false if they are present but not explicitly set to true.

## Related topics

<dl> <dt>

[Developing a WMI Provider](developing-a-wmi-provider.md)
</dt> <dt>

[Setting Namepace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> <dt>

[Securing Your Provider](securing-your-provider.md)
</dt> </dl>

 

 

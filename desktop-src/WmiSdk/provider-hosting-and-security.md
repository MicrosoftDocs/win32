---
description: Specifies the provider hosting model. Setting this property causes the provider to be loaded into a shared host process that has a specified level of privilege.
ms.assetid: 1e5c778d-cd29-449b-88e2-fe0c90d0edcd
ms.tgt_platform: multiple
title: Provider Hosting and Security
ms.topic: article
ms.date: 05/31/2018
---

# Provider Hosting and Security

The [**HostingModel**](--win32provider.md) property in the **\_\_Win32Provider** instance that represents your provider specifies the provider hosting model. Setting this property causes the provider to be loaded into a shared host process that has a specified level of privilege.

## Shared Provider Host Process

WMI resides in a shared service host with several other services. To avoid stopping all the services when a provider fails, providers are loaded into a separate host process named "Wmiprvse.exe". More than one process with this name can be running. Each can run under a different account with varying security. Be aware that, starting with Windows Vista, use the [**winmgmt**](winmgmt.md) command to run WMI in a separate process by itself using a fixed port. For more information, see [Connecting to WMI Remotely Starting with Vista](connecting-to-wmi-remotely-starting-with-vista.md).

The shared host can run under one of the following system accounts in a Wmiprvse.exe host process:

-   [LocalSystem](/windows/desktop/Services/localsystem-account)
-   [NetworkService](/windows/desktop/Services/networkservice-account)
-   [LocalService](/windows/desktop/Services/localservice-account)

A provider can also be a local COM server (.exe), or self-hosted, which does not require a WMI provider host.

## Setting the Hosting Model

Because LocalSystem is a privileged account, it is recommended that you set [**HostingModel**](--win32provider.md) to **NetworkServiceHost** when a provider is running in a Wmiprvse.exe process. NetworkServiceHost account is for services that do not require extensive privileges, but do need to communicate remotely with other systems.

If you do not set a value for the [**HostingModel**](--win32provider.md) property, WMI will set a default value of **NetworkServiceHostOrSelfHost**. If the **HostingModel** value is set to **LocalSystemHost**, WMI uses tracing to generate events 5603 and 5604 in the Windows Event Log. Because the local [LocalSystem](/windows/desktop/Services/localsystem-account) account is highly privileged, this setting is not recommended. You can view these events in the **Event Viewer**. For more information, see [Tracing WMI Activity](tracing-wmi-activity.md).

Set the [**HostingModel**](--win32provider.md) property for decoupled providers as "Decoupled:Com". Providers created by adding instrumentation classes from [**Microsoft.Management.Infrastructure**](/previous-versions//hh872326(v=vs.85)) in the .NET Framework are decoupled providers. (**System.Management.Instrumentation** is no longer supported.) For more information about creating a decoupled provider, see [Incorporating a Provider in an Application](incorporating-a-provider-in-an-application.md).

The hosting model is specified in the [**HostingModel**](--win32provider.md) property in the **\_\_Win32Provider** instance that represents your provider.

**To set the hosting model for a provider**

1.  In the MOF file that defines your provider, create an instance of [**\_\_Win32Provider**](--win32provider.md).
2.  Assign a name to the provider in the **Name** property and assign the class identifier (CLSID) of the provider COM object to the **Clsid** property.

    The following code example assigns a name to the **Name** property and the CSLID of the provider COM object to the **Clsid** property.

    ``` syntax
    Instance of __Win32Provider as $NewProvider
    {
        Name = "MyProvider";
        Clsid = "{.......}";
    }
    ```

3.  Assign the appropriate shared host value to the [**HostingModel**](--win32provider.md) property. Shared host values such as "NetworkServiceHost" are defined in the **HostingSpecification** property of [**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers) class.

    The following code example assigns a shared host value to the [**HostingModel**](--win32provider.md) property.

    ``` syntax
    HostingModel = "NetworkServiceHost";
    ```

The following code example shows how to register a provider in NetworkServiceHost.

``` syntax
Instance of __Win32Provider as $NewProvider
{
    Name = "MyProvider";
    Clsid = "{.......}";
    HostingModel = "NetworkServiceHost";
}
```

If you have multiple providers, you can group them into a specific service host by registering your provider so that it resides in the specific instance.

The following code example also registers a provider in NetworkServiceHost. The [**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers) class defines values for the two values that combine to create the [**\_\_Win32Provider**](--win32provider.md) **HostingModel** property. In the example, "NetworkServiceHost" value comes from the **HostingSpecification** property of **MSFT\_Providers** and "LocalServiceHost" comes from the **HostingGroup** property.

``` syntax
Instance of __Win32Provider as $NewProvider
{
    Name = "MyProvider";
    Clsid = "{.......}";
    HostingModel = "NetworkServiceHost:MySharedHost";
}
```

Special development issues exist for providers that are not decoupled and are hosted in the Wmiprvse process. For more information, see [Debugging Providers](debugging-providers.md).

If you are writing a provider that contains property or class provider registration, not all threading models work. For more information, see [Choosing Correct Registration](choosing-correct-registration.md).

## HostingModel Values for In-Process Providers

The following list lists the provider hosting model values to use in the [**\_\_Win32Provider**](--win32provider.md) instance for providers that run in a Wmiprvse.exe process.



| Value in [**\_\_Win32Provider.HostingModel**](--win32provider.md) | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **SelfHost**                                                       | The provider starts using the local server implementation instead of in-process. The security context of the process in which the provider runs determines the provider security context.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **LocalSystemHost**                                                | The provider, if implemented as in-process, is loaded into a shared provider host running under [LocalSystem](/windows/desktop/Services/localsystem-account) context. Starting with Windows Vista, **LocalSystemHost** is no longer the default hosting model if the [**HostingModel**](--win32provider.md) of a WMI provider (**\_\_Win32Provider**.**HostingModel** property) is unspecified. For more information, see [Security of Hosting Models](#provider-hosting-and-security).                                                                                                                                                                                                                                                                               |
| **LocalSystemHostOrSelfHost**                                      | The provider is self-hosted or loaded into the Wmiprvse.exe process running under the [LocalSystem](/windows/desktop/Services/localsystem-account) account. Because LocalSystem is a highly privileged account, an entry is generated in the Security NT Event Log to notify administrators of a provider running in this trusted status.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **NetworkServiceHost**                                             | The provider, if implemented as in-process, is loaded into the Wmiprvse.exe process running under [NetworkService](/windows/desktop/Services/networkservice-account) account. Starting with Windows Vista, this is the default hosting model if the [**HostingModel**](--win32provider.md) of a WMI provider (**\_\_Win32Provider**.**HostingModel** property) is unspecified. For more information, see [Security of Hosting Models](#provider-hosting-and-security).<br/> **NetworkServiceHost** has limited privileges and therefore reduces the possibility of an elevation of privilege attack. If the provider only operates within the local computer, then set the [**HostingModel**](--win32provider.md) property to **LocalServiceHost**.<br/> |
| **NetworkServiceHostOrSelfHost**                                   | The provider is self-hosted or loaded into the WmiPrvse.exe process running under the [NetworkService](/windows/desktop/Services/networkservice-account) account. **NetworkServiceHostOrSelfHost** is the default configuration when the [**HostingModel**](--win32provider.md) property in **\_\_Win32Provider** is **NULL**. Because **NetworkServiceHostOrSelfHost** is the default, providers from earlier operating systems can continue to work in Windows Vista, Windows Server 2008, and later operating systems.                                                                                                                                                                                                                                             |
| **LocalServiceHost**                                               | The provider, if implemented as in-process, is loaded into the Wmiprvse.exe process running under the [LocalService](/windows/desktop/Services/localservice-account) account. This is the recommended hosting model for services because LocalService has limited privileges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |



 

## HostingModel Values for Decoupled Providers

The following list lists the provider hosting model values for decoupled providers.

<dl> <dt>

<span id="Decoupled_Com"></span><span id="decoupled_com"></span><span id="DECOUPLED_COM"></span>**Decoupled:Com**
</dt> <dd>

The provider is a decoupled provider hosted in a separate process that is a client to WMI.

The following example shows the FoldIdentity specifier for the [**HostingModel**](--win32provider.md) property set to **FALSE**, which allows the provider to impersonate the client.

``` syntax
Decoupled:Com:FoldIdentity(FALSE)
```

If FoldIdentity is not specified, the FoldIdentity value is set to **TRUE** by default. For security reasons, it is recommended that you not specify FoldIdentity(FALSE) since a rogue application with impersonation of Delegate can affect an entire domain.

The following example shows the [**HostingModel**](--win32provider.md) property set in the recommended manner that is equivalent to setting FoldIdentity(TRUE).

``` syntax
Decoupled:Com
```

</dd> <dt>

<span id="Decoupled_Noncom"></span><span id="decoupled_noncom"></span><span id="DECOUPLED_NONCOM"></span>**Decoupled:Noncom**
</dt> <dd>

For internal use only. Not supported.

</dd> </dl>

## Security of Hosting Models

For most situations, **LocalSystem** is unnecessary and the **NetworkServiceHost** context is more appropriate. Most WMI Providers must impersonate the client security context to perform requested operations on behalf of the WMI client. Starting with Windows Vista, a WMI provider that lacks a hosting model definition and executes as if it is running under **LocalSystem** will not run properly. To correct this situation, change the expected hosting model and ensure that the WMI provider code performs the operations in the client security context by impersonating the WMI client. LocalSystem is rarely an requirement. If your provider must have that level of privilege, specify the hosting model with the following statement in the MOF file.

``` syntax
HostingModel=LocalSystemHost
```

## Related topics

<dl> <dt>

[Choosing Correct Registration](choosing-correct-registration.md)
</dt> <dt>

[Access to WMI Namespaces](access-to-wmi-namespaces.md)
</dt> <dt>

[Securing WMI Namespaces](securing-wmi-namespaces.md)
</dt> <dt>

[Provider Configuration and Troubleshooting Classes](provider-configuration-and-troubleshooting-classes.md)
</dt> <dt>

[**MSFT\_Providers**](/previous-versions/windows/desktop/wmisystemprov/msft-providers)
</dt> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> </dl>

 


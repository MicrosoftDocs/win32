---
description: An association provider provides a mechanism to register profiles and associate them with profiles that are implemented in different namespaces.
ms.assetid: e6aab944-4ed8-4678-ad35-426f7b4f9a35
ms.tgt_platform: multiple
title: Writing an Association Provider for Interop
ms.topic: article
ms.date: 05/31/2018
---

# Writing an Association Provider for Interop

An association provider provides a mechanism to register profiles and associate them with profiles that are implemented in different namespaces.

Association providers are used to expose standard profiles, like a power profile. This is accomplished by writing an association provider in the root/interop namespace that exposes association instances by implementing a class, which is derived from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)). The provider must be registered in both the root/interop and the root/<implemented> namespace to support cross namespace traversal.

Windows Management Instrumentation (WMI) loads the association provider whenever an association query is run in the root/interop namespace.

**To implement an association provider for interop**

1.  Derive a class from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) and create a static instance of this derived class in the root\\interop namespace. At a minimum, the following properties must be propagated with valid values:

    -   [**InstanceID**](/previous-versions//ee309375(v=vs.85))
    -   [**RegisteredName**](/previous-versions//ee309375(v=vs.85))
    -   [**RegisteredOrganization**](/previous-versions//ee309375(v=vs.85))
    -   [**RegisteredVersion**](/previous-versions//ee309375(v=vs.85))

    Even though [**InstanceID**](/previous-versions//ee309375(v=vs.85)) uniquely defines the instance of the **CIM\_RegisteredProfile**, the combination of **RegisteredName**, **RegisteredOrganization**, and **RegisteredVersion** must uniquely identify the registered profile within the scope of the organization. For more information about the individual properties, see [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)).

    The following code example describes the syntax for deriving the **ProcessProfile** class from [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) and populating the static instance.

    ```syntax
    class ProcessProfile : CIM_RegisteredProfile
    {
    };

    instance of ProcessProfile as $PP
    {
         InstanceID = "Process";
         RegisteredName = "Process";
         RegisteredOrganization = "1"; // Set to "Other"
         OtherRegisteredOrganization = "Microsoft";
         RegisteredVersion = "1.0";
    };
    ```

    > [!Note]  
    > For Windows clients, the **RegisteredOrganization** property must be set to 1 and the **OtherRegisteredOrganization** property set to "Microsoft".

     

2.  Create a provider that returns association instances of [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile). This is a two-step process.

    1.  Create a class that is derived from [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile) in both the interop and implementation namespaces. Because the same profile can be implemented by different vendors, the name of the class should be unique. The recommended naming convention is "<Organization>\_<ProductName>\_<ClassName>\_<Version>". Either the **ConformantStandard** or the **ManagedElement** property must specify the **MSFT\_TargetNamespace** qualifier that contains the namespace to which this class belongs.

        The following code example describes the syntax for deriving the Microsoft\_Process\_ElementConformsToProfile\_v1 class from [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile) in the root\\interop namespace. In this example, the Win32\_Process managed element references the root\\cimv2 namespace by using the **MSFT\_TargetNamespace** qualifier.

        ```syntax
        #pragma namespace("\\\\.\\root\\interop")
        [Provider("ProcessAssociation"),Dynamic]
        Class Microsoft_Process_ElementConformsToProfile_v1: CIM_ElementConformsToProfile
        {
             CIM_RegisteredProfile ref ConformantStandard = $PP;
             [MSFT_TargetNamespace("root\\cimv2")]Win32_process ref ManagedElement = null;
        };
        ```

        The following code example describes the syntax for deriving the Microsoft\_Process\_ElementConformsToProfile\_v1 class from [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile) in the root\\cimv2 namespace. In this example, the [**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85)) conformant standard references the root\\interop namespace by using the **MSFT\_TargetNamespace** qualifier.

        ```syntax
        #pragma namespace("\\\\.\\root\\cimv2")
        [Provider("ProcessAssociation"),Dynamic]
        Class Microsoft_Process_ElementConformsToProfile_v1: CIM_ElementConformsToProfile
        {
             [MSFT_TargetNamespace("root\\interop")] CIM_RegisteredProfile ref ConformantStandard = $PP;
             Win32_process ref ManagedElement = null;
        };
        ```

        If the **MSFT\_TargetNamespace** qualifier is not specified on the property that is referencing the implemented namespace, the **ResultClass** filter of "Associators of" statement will not work. For example, if the **MSFT\_TargetNamespace** qualifier is not specified, the following Windows PowerShell command-line will not return an object: **get-wmiobject -query "associators of {ProcessProfile.InstanceID='Process'} where resultclass='Win32\_Process'"**.

        The **MSFT\_TargetNamespace** qualifier cannot point to a namespace on a remote computer. For example, the following namespace is not supported: MSFT\_TargetNamespace(\\\\\\\\<RemoteMachine>\\\\root\\\\interop).

    2.  Write a provider that returns instances of the created derived class. For more information, see [Writing an Instance Provider](writing-an-instance-provider.md). When you access cross-namespace instances, you might have to access the security levels for the client. For more information, see [Impersonating a Client](impersonating-a-client.md).

        The association provider should implement both the [**IWbemServices.CreateInstanceEnumAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenumasync) and [**IWbemServices.GetObjectAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-getobjectasync) methods. Implementing the [**IWbemServices.ExecQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execqueryasync) method is optional. Because this provider can be accessed from both the root\\interop and the root\\<implemented> namespaces, there should not be an explicit dependency on a namespace inside the provider.

3.  Register the association provider in both the root\\interop and the root\\<implemented> namespaces. For more information, see [Registering an Instance Provider](registering-an-instance-provider.md).

    The following code example describes the syntax to register the association provider in the root\\interop namespace.

    ```syntax
    #pragma namespace("\\\\.\\root\\interop")
    instance of __Win32Provider as $P
    {
        Name    = "ProcessAssociation" ;
        ClsId   = "{DA13393B-A2D5-4BAC-9BD2-30B092E9EBB8}";
    } ;

    instance of __InstanceProviderRegistration
    {
        Provider = $P;
        SupportsPut = false;
        SupportsGet = TRUE;
        SupportsDelete = false;
        SupportsEnumeration = TRUE;
    };
    ```

    The following code example describes the syntax to register the association provider in the root\\cimv2 namespace.

    ```syntax
    #pragma namespace("\\\\.\\root\\cimv2")
    instance of __Win32Provider as $R
    {
        Name    = "ProcessAssociation" ;
        ClsId   = "{DA13393B-A2D5-4BAC-9BD2-30B092E9EBB8}";
    } ;

    instance of __InstanceProviderRegistration
    {
        Provider = $R;
        SupportsPut = false;
        SupportsGet = TRUE;
        SupportsDelete = false;
        SupportsEnumeration = TRUE;
    };
    ```

4.  Place the schema for the [**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile) into the implemented namespace. For Windows clients this is the interop.mof file that is located in the %systemroot%\\system32\\wbem folder.
5.  Implement the [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) interface for your provider.

    WMI uses [**IWbemProviderInit**](/windows/desktop/api/Wbemprov/nn-wbemprov-iwbemproviderinit) to load and initialize a provider. The [**IWbemProviderInit.Initialize**](/windows/desktop/api/Wbemprov/nf-wbemprov-iwbemproviderinit-initialize) method should be implemented in a way that allows it to be called for two different namespaces. For more information, see [Initializing a Provider](initializing-a-provider.md).

## Related topics

<dl> <dt>

[**CIM\_ElementConformsToProfile**](/previous-versions/windows/desktop/iscsitarg/cim-elementconformstoprofile)
</dt> <dt>

[**CIM\_RegisteredProfile**](/previous-versions//ee309375(v=vs.85))
</dt> <dt>

[Writing an Instance Provider](writing-an-instance-provider.md)
</dt> <dt>

[Registering an Instance Provider](registering-an-instance-provider.md)
</dt> </dl>

 

 

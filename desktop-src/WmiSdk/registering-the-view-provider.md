---
description: WMI automatically registers the View Provider DLL during the WMI installation process. However, you still need to register the View Provider with WMI for each namespace that will contain view classes.
ms.assetid: 62db8cdc-0bbf-4784-bfc4-6fd5cb53368a
ms.tgt_platform: multiple
title: Registering the View Provider
ms.topic: article
ms.date: 05/31/2018
---

# Registering the View Provider

WMI automatically registers the View Provider DLL during the WMI installation process. However, you still need to register the View Provider with WMI for each namespace that will contain view classes.

The following procedure describes how to register the View Provider.

**To register the View Provider**

1.  Create an instance of the [**\_\_Win32Provider**](--win32provider.md) class to describe the implementation of the View Provider.

    The [**\_\_Win32Provider**](--win32provider.md) instance describes the name of the provider and its class identifier (CLSID), as well as the default security settings.

    The following code example describes an implementation of [**\_\_Win32Provider**](--win32provider.md).

    ``` syntax
    instance of __Win32Provider as $DataProv
    {
        Name = "MS_VIEW_INSTANCE_PROVIDER";
        ClsId = "{AA70DDF4-E11C-11D1-ABB0-00C04FD9159E}";
        ImpersonationLevel = 1;
        PerUserInitialization = "True";
        
    };
    ```

2.  Create an instance of the [**\_\_InstanceProviderRegistration**](--instanceproviderregistration.md) class.

    The following code example shows how to create an instance of the **\_\_InstanceProviderRegistration** class.

    ``` syntax
    instance of __InstanceProviderRegistration
    {
        Provider = $DataProv;
        SupportsPut = True;
        SupportsGet = True;
        SupportsDelete = True;
        SupportsEnumeration = True;
        QuerySupportLevels = {"WQL:UnarySelect"};
    };
    ```

3.  Create an instance of the [**\_\_MethodProviderRegistration**](--methodproviderregistration.md) class if you want to have your union view class support methods.

    The following code example shows how to create an instance of the **\_\_MethodProviderRegistration** class.

    ``` syntax
    instance of __MethodProviderRegistration
    {
        Provider = $DataProv;
    };
    ```

4.  Compile your MOF code using the MOF compiler ([mofcomp](mofcomp.md)) or the [**IMofCompiler**](/windows/desktop/api/Wbemcli/nn-wbemcli-imofcompiler) interface.

    If you save the previously listed MOF code example into a file named Viewtest.mof, use the Mofcomp command to load the MOF code into the target namespace. *NamespacePath* is the namespace in which you wish to create the view class instance.

    Type the following command at a command prompt to load the MOF code into the target namespace.

    ``` syntax
    Mofcomp /N:<NamespacePath> Viewtest.mof
    ```

    For more information, see [Compiling MOF Files](compiling-mof-files.md).

For more information, see [Registering a Provider](registering-a-provider.md).

 

 




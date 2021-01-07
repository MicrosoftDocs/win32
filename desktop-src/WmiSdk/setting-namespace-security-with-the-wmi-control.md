---
description: The WMI Control is an MMC snap-in located in the Control Panel and is used to set WMI namespace security manually on a local computer. You can also set the default namespace for scripting.
ms.assetid: 87c23919-c482-4278-b005-894a8ac21da4
ms.tgt_platform: multiple
title: Setting Namespace Security with the WMI Control
ms.topic: article
ms.date: 05/31/2018
---

# Setting Namespace Security with the WMI Control

The WMI Control is an MMC snap-in located in the **Control Panel** and is used to set WMI namespace security manually on a local computer. You can also set the default namespace for scripting.


The following procedure describes how to locate the WMI Control.

**To locate the WMI control**

1.  In the **Control Panel**, double-click **Administrative Tools**.
2.  In the **Administrative Tools** window, double-click **Computer Management**.
3.  In the **Computer Management** window, expand the **Services and Applications** tree and double-click the **WMI Control**.
4.  Right-click the **WMI Control** icon and select **Properties**.

The following procedure describes how to use the WMI control to set up the security for a namespace as a template, then programmatically obtain the security settings to set security for other namespaces.

**To set namespace security with the WMI control**

1.  Create a new namespace by using Managed Object Format (MOF) code.
2.  Run the WMI Control to set the security on the new namespace. On the **Start** menu, click **Run** and type **wmimgmt.msc** or see [Locating the WMI Control](#).
3.  In the **WMI Control** pane, right-click **WMI Control**, choose **Properties**, and then select the **Security** tab.
4.  Navigate to the new namespace, click **Security**, and then configure groups and permissions for the namespace.

You can also use Windows Management Instrumentation Command-Line ([WMIC](/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc754534(v=ws.11))) to set namespace security. For more information, see [**wmic**](wmic.md).

## Setting the Default Namespace for Scripts

If a script does not connect explicitly to a namespace when connecting to WMI, then WMI uses the default namespace specified in this control. The default is also found in the registry entry as follows:

```
HKEY_LOCAL_MACHINE
   SOFTWARE
      Microsoft
         WBEM
            Scripting
               Default
                  Namespace
```

Because the default namespace is easy to change, either with this control or programmatically by calling methods of [**StdRegProv**](/previous-versions/windows/desktop/regprov/stdregprov), specify the namespace when connecting to WMI either through the [moniker](constructing-a-moniker-string.md) or calls to [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md). For more information, see [Creating a WMI Script](creating-a-wmi-script.md)

**To set the default namespace for scripts**

1.  In the **WMI Control Properties** window, choose the **Advanced** tab.
2.  Click the **Change** button and select the namespace to make the default.

## Related topics

<dl> <dt>

[Setting Namespace Security Descriptors](setting-namespace-security-descriptors.md)
</dt> </dl>

 

 

---
description: Windows Installer can repair, replace, and verify files contained in an application. A partial or complete application reinstallation might be required if any files or registry entries associated with any feature are missing or corrupt.
ms.assetid: fab23ab9-f1ab-4743-b883-cffc29b0124b
title: Reinstalling a Feature or Application
ms.topic: article
ms.date: 05/31/2018
---

# Reinstalling a Feature or Application

Windows Installer can repair, replace, and verify files contained in an application. A partial or complete application reinstallation might be required if any files or registry entries associated with any feature are missing or corrupt.

When a feature or application is reinstalled, all the services, environment variables, and custom actions belonging to the feature or application are reinstalled as well. Note that this means that any changes made to environment variables between the original installation and the reinstallation are lost.

The following list contains methods of reinstalling a feature or product. The first two methods have been automated by the installer:

-   Repair, replace, or verify files by calling the [**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea) function.
-   Reinstall the entire product by calling the [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta) function.
-   Reinstall, replace, or verify files with an installer UI control button through the [Reinstall ControlEvent](reinstall-controlevent.md).
-   Reinstall, replace, or verify files from a command line by setting the [**REINSTALL**](reinstall.md) property and the [**REINSTALLMODE**](reinstallmode.md) property.

For more information on reinstalling a feature or application, see [Resiliency](resiliency.md).

**To reinstall a product using the installer**

-   Call [**MsiReinstallProduct**](/windows/desktop/api/Msi/nf-msi-msireinstallproducta).

**To reinstall a feature using the installer**

-   Call [**MsiReinstallFeature**](/windows/desktop/api/Msi/nf-msi-msireinstallfeaturea).

**To reinstall a product or feature with an installer user interface**

1.  Add a button to the specified dialog box by adding an entry to the [Control table](control-table.md).
2.  Add a [ReinstallMode ControlEvent](reinstallmode-controlevent.md) to the ControlEvent table, with the Dialog\_ and Control\_ fields referencing the button control created in step 1. In the Argument field, enter a string containing the letters corresponding to the reinstall modes you want (the acceptable values for this field are identical to those accepted for the [**REINSTALLMODE**](reinstallmode.md) property). The value in the Ordering column for this event should be 1.
3.  Add a [Reinstall ControlEvent](reinstall-controlevent.md) event to the [ControlEvent table](controlevent-table.md), again referencing the same button control. The Argument field for this event will normally be ALL, to force reinstallation of all features, but you can place the name of a specific feature here. The value in the Ordering column for this event should be 2.
4.  Add one more event tied to the same button control, to actually initiate the reinstallation. This can be an EndDialog event (with an argument of Return). More typically, however, a NewDialog event would be used here to jump to an **Are you sure you want to reinstall?** confirmation dialog box. The value in the Ordering column for this event should be 3.

    If desired, several [**REINSTALL**](reinstall.md) buttons can be created for a single dialog box, allowing the user to select the type of reinstallation performed. In this case, each button is authored as outlined in the preceding procedure, with a different [ReinstallMode ControlEvent](reinstallmode-controlevent.md) parameter for each button.

Once a particular product has been installed (with some or all of the product's features), a reinstallation can be performed at the command line:

**To reinstall a product or feature from a command line**

1.  From the command prompt, specify the [**REINSTALL**](reinstall.md) property.
2.  From the command prompt, specify the [**REINSTALLMODE**](reinstallmode.md) property.

    Specifying these properties allows the user to reinstall any or all of the product's features. The type of reinstallation can also be specified. For example, you can specify that only those files that are completely missing should be reinstalled, or that only corrupt files (for example, any executable file whose checksum does not match the actual file contents) be replaced.

 

 




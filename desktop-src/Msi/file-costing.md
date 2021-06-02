---
description: Costing is the process of determining the total disk space requirements for an installation.
ms.assetid: 53ebb532-9eb3-46b7-9dcc-f593bfd25c60
title: File Costing
ms.topic: article
ms.date: 05/31/2018
---

# File Costing

Costing is the process of determining the total disk space requirements for an installation. The elements calculated in the file costing process include the amount of disk space in which files are installed or removed, as well as the amount of disk space taken up by registry entries, shortcuts, and other miscellaneous files. Existing files scheduled to be overwritten are also calculated in the disk cost totals.

Total costs are accumulated on a per-[component](components-and-features.md) basis and consist of three separate parts: local costs, source costs, and removal costs. These parts correspond to the disk cost that is incurred if the component is installed locally, installed to run from the source media, or removed.

All calculations involving the cost of installing files depend upon the disk volume to which the file is to be installed or removed. Each time the directory associated with a component changes, the costs of the installation files controlled by that component must be recalculated. For example, because a directory change might also imply a volume change, the clustered file sizes must be recalculated. In addition, the new directory must be checked to determine whether any existing files that may be overwritten must be taken into account.

After the [CostInitialize](costinitialize-action.md) action is called, the [FileCost](filecost-action.md) action must be called. The CostInitialize action initializes the installer's internal routines that dynamically calculate the disk costs involved with the standard installation actions. No other dynamic cost calculations are done at this point.

Next, the [CostFinalize](costfinalize-action.md) action must be called. This action finalizes all cost calculations and makes the costing data available through the [Component](component-table.md) table.

After the [CostFinalize](costfinalize-action.md) action completes execution, the [Component](component-table.md) table is fully initialized and a user interface dialog box sequence containing a [SelectionTree](selectiontree-control.md) control can be initiated if needed. The user interface dialog boxes may offer the option to change the selection state or destination directory of any feature in the [Feature](feature-table.md) table to the user. The process is similar when the selection state of a component changes; however, in this case, the dynamic cost of the changed component only is recalculated.

Once the user has completed selecting features in the user interface, the [InstallValidate](installvalidate-action.md) action should be called. This action verifies that all volumes to which cost has been attributed have sufficient space for the installation.

 

 




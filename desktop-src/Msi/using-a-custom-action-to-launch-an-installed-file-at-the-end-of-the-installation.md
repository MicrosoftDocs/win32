---
description: The following example illustrates how to launch an HTML file at the end of an installation.
ms.assetid: 6b082559-bcfa-4098-b072-27ee78092833
title: Using a Custom Action to Launch an Installed File at the End of the Installation
ms.topic: article
ms.date: 05/31/2018
---

# Using a Custom Action to Launch an Installed File at the End of the Installation

The following example illustrates how to launch an HTML file at the end of an installation. The Installer installs the component that contains the file, and then publishes a control event at the end of the installation to run a custom action that opens the file. This approach may be used to launch a help tutorial at the end of the first installation of an application.

The sample must meet the following specifications.

-   The Installer executes the custom action only if the [*full UI*](f-gly.md) level is used to install an application.
-   The Installer executes the custom action only if the component that contains the HTML file is installed to run locally on the computer.
-   The custom action only runs on the first installation of the application.
-   The installation does not fail if the custom action fails.

The sample includes a hypothetical component named Tutorial that controls at least one resource, a file named tutorial.htm. The identifier for this file in the File column of the File table is Tutorial. The following discussion assumes that you have already created the resources required by Tutorial, and have made all the necessary entries in the [Feature](feature-table.md), [Component](component-table.md), [File](file-table.md), [Directory](directory-table.md), and [FeatureComponents](featurecomponents-table.md) tables to install this component. For more information, see [An Installation Example](an-installation-example.md).

The following topics contain information about how to create required custom actions and add them to an installation package.

-   [Authoring the Launch Custom Action](authoring-the-launch-custom-action.md)
-   [Adding Launch to the CustomAction and Binary Tables](adding-launch-to-the-customaction-and-binary-tables.md)
-   [Adding a Control Event at the End of the Installation to Run Launch](adding-a-control-event-at-the-end-of-the-installation-to-run-launch.md)

 

 



